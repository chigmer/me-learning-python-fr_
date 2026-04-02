from pathlib import Path
import re

def find_files(path: Path = Path.cwd(), ext: str = 'txt') -> list[Path]:
    if not isinstance(path, Path):
        raise ValueError("expected Path on arg 1")
    elif not isinstance(ext, str):
        raise ValueError("expected str on arg 2")
    elif not path.exists():
        return []

    if ext == "*":
        files = [f for f in path.rglob("*") if f.is_file()]
    else:
        files = list(path.rglob(f"*.{ext}"))
    return files


def create_dir(text: Path) -> None:
    if text.exists():
        print("Directory exists.")
        return
    try:
        text.mkdir(exist_ok=True, parents=True)
        print("Done")
    except PermissionError:
        print("no permission")
    except Exception as e:
        print(f"error making directory: {e}")


if __name__ == "__main__":
    import shutil

    files = find_files(Path.cwd(), "*")
    matches = {}
    current_script = Path(__file__).resolve()
    excluded = set()

    print("files:\n")

    # first pass: collect extension folders that will be created
    for file in files:
        if file.resolve() == current_script:
            continue

        match = re.fullmatch(r"(.+)\.([a-zA-Z0-9]+)$", file.name)
        if match:
            ext = match.group(2)
            matches.setdefault(ext, []).append(file)
            excluded.add(Path(f"{ext} files"))

    # second pass: create directories and move files
    for group in matches:
        current_dir = Path(f"{group} files")
        print(f"creating directory.. ({current_dir})")
        create_dir(current_dir)

        if not current_dir.exists():
            print(f"there was trouble in making directory {current_dir}.. skipping")
            continue

        for file in matches[group]:
            destination = current_dir / file.name

            # skip files already inside ANY organizer folder
            if any(folder in file.parents for folder in excluded):
                print(f"{file.name} is already inside an organized folder, skipping")
                continue

            if destination.exists():
                print(f"{destination.name} already exists in {current_dir}, skipping")
                continue

            shutil.move(file, destination)
            print(f"moving {file.name} to {current_dir}")