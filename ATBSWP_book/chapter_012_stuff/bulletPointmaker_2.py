import sys
import argparse
from pathlib import Path


def parse_args() -> tuple:
    parser = argparse.ArgumentParser(description="A tool to add bulletpoints to text")
    parser.add_argument("source", type=str, help="your text or filepath.")
    parser.add_argument(
        "-f", "--is_file",
        action="store_true",
        help="treat source as a filepath"
    )
    args = parser.parse_args()
    return args.source, args.is_file


def main():
    # --- dependency check ---
    try:
        import nltk
        from nltk.tokenize import sent_tokenize
    except ModuleNotFoundError:
        print("Missing dependency: nltk\nInstall with: pip install nltk")
        sys.exit(1)

    content, is_file = parse_args()
    text = ""

    PLAINTEXT_EXTENSIONS = {
        "txt", "csv", "log", "md", "markdown", "rst", "json", "yaml", "yml",
        "toml", "ini", "conf", "cfg", "xml", "html", "htm", "css", "scss",
        "js", "ts", "py", "pyi", "c", "cpp", "h", "hpp", "cs", "java", "go",
        "rs", "rb", "php", "pl", "sh", "bat", "ps1", "sql", "r", "swift",
        "env", "gitignore", "dockerignore", "editorconfig", "makefile"
    }

    # --- input handling ---
    if not is_file:
        text = content   
    else:
        file = Path(content)
        if not file.suffix:
            print("file has no extension, cannot determine type.")
            sys.exit(1)

        if not file.exists():
            print("file doesnt exist.")
            sys.exit(1)

        if file.is_dir():
            print("filepath is a directory.")
            sys.exit(1)

        if file.suffix[1:] not in PLAINTEXT_EXTENSIONS:
            print("file is not readable.")
            sys.exit(1)

        text = file.read_text(encoding="utf-8", errors="ignore")

    if not text.strip():
        print("no input detected. nice try.\nexiting")
        sys.exit(1)

    print("\nwant bulleted text? i gotchu\n\n")

    # data stuff
    nltk.download("punkt", quiet=True)
    nltk.download("punkt_tab", quiet=True)
    sentences = sent_tokenize(text)

    for sentence in sentences:
        print(f"* {sentence}")


if __name__ == "__main__":
    main()