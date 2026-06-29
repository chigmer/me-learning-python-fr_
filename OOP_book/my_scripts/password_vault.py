import sqlite3
from datetime import datetime

class MyVault:
    def __init__(self,vault_name:str):
        if not isinstance(vault_name,str):
            raise TypeError
        self.vault = vault_name
        with sqlite3.connect(vault_name) as conn:
            cur = conn.cursor()
            cur.execute("""
CREATE TABLE IF NOT EXISTS vault(
    ID INTEGER PRIMARY KEY,
    platform TEXT,
    username TEXT,
    password TEXT,
    last_updated TEXT
) STRICT
""")

    def _get_now_iso(self):
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def add(self, name, platform, password):
        if not isinstance(name, str):
            raise TypeError(f"name: expected str, got {type(name).__name__}")
        if not isinstance(platform, str):
            raise TypeError(f"platform: expected str, got {type(platform).__name__}")
        if not isinstance(password, str):
            raise TypeError(f"password: expected str, got {type(password).__name__}")

        data = (platform.lower(), name, password, self._get_now_iso())
        try:
            with sqlite3.connect(self.vault) as conn:
                cur = conn.cursor()
                cur.execute("INSERT INTO vault (platform, username, password, last_updated) VALUES (?,?,?,?)", data)
        except Exception as err:
            print(f"Couldn't complete transaction: {err}")

    def get(self, platform=None, username=None):
        if platform is not None and not isinstance(platform, str):
            raise TypeError(f"platform: expected str, got {type(platform).__name__}")
        if username is not None and not isinstance(username, str):
            raise TypeError(f"username: expected str, got {type(username).__name__}")

        try:
            with sqlite3.connect(self.vault) as conn:
                cur = conn.cursor()
                if platform and not username:
                    cur.execute("SELECT ID, platform, username, password, last_updated FROM vault WHERE platform = ?", (platform.lower(),))
                elif username and not platform:
                    cur.execute("SELECT ID, platform, username, password, last_updated FROM vault WHERE username = ?", (username,))
                elif platform and username:
                    cur.execute("SELECT ID, platform, username, password, last_updated FROM vault WHERE platform = ? AND username = ?", (platform.lower(), username))
                else:
                    return None
                data = cur.fetchall()
        except Exception as err:
            print(f"Couldn't complete transaction: {err}")
            return None

        if not data:
            return None
        return data[0] if len(data) == 1 else data

    def update(self, ID, name=None, platform=None, password=None):
        if not isinstance(ID, int):
            raise TypeError(f"ID: expected int, got {type(ID).__name__}")
        if name is not None and not isinstance(name, str):
            raise TypeError(f"name: expected str, got {type(name).__name__}")
        if platform is not None and not isinstance(platform, str):
            raise TypeError(f"platform: expected str, got {type(platform).__name__}")
        if password is not None and not isinstance(password, str):
            raise TypeError(f"password: expected str, got {type(password).__name__}")

        columns = []
        values = []

        if name is not None:
            columns.append("username = ?")
            values.append(name)
        if platform is not None:
            columns.append("platform = ?")
            values.append(platform.lower())
        if password is not None:
            columns.append("password = ?")
            values.append(password)

        if not columns:
            return

        values.append(ID)
        try:
            with sqlite3.connect(self.vault) as conn:
                cur = conn.cursor()
                cur.execute(f"UPDATE vault SET {', '.join(columns)} WHERE ID = ?", values)
        except Exception as err:
            print(f"Couldn't complete transaction: {err}")

    def delete(self, *args):
        for arg in args:
            if not isinstance(arg, int):
                raise TypeError(f"expected int, got {type(arg).__name__}")

        placeholders = ','.join(['?'] * len(args))
        try:
            with sqlite3.connect(self.vault) as conn:
                cur = conn.cursor()
                cur.execute(f"DELETE FROM vault WHERE ID IN ({placeholders}) RETURNING *", args)
                self.deleted = cur.fetchall()
        except Exception as err:
            print(f"Couldn't complete transaction: {err}")


if __name__ == "__main__":
    vault = MyVault("vault.db")

    #vault.add("john_doe", "github", "MyGithubPass123!")
    #vault.add("john_doe", "youtube", "YoutubePass456@")
    #vault.add("jane_smith", "netflix", "NetflixPass789#")
    #vault.add("john_doe", "spotify", "SpotifyPass321$")
    #vault.add("jimmy_dough", "github", "Githubpass100$")

    print("Get by platform (github):")
    print(vault.get(platform="github"))

    print("\nGet by username (john_doe):")
    print(vault.get(username="john_doe"))

    print("\nGet by platform + username:")
    print(vault.get(platform="youtube", username="john_doe"))

    vault.update(1, password="NewGithubPass999!")
    print("\nAfter update:")
    print(vault.get(platform="github"))

    vault.delete(4, 5)
    print("\nAfter deleting IDs 4 and 5:")
    print(vault.get(username="john_doe"))