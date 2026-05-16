import csv
from pathlib import Path
import time

def main():
    user_dir = Path("CSV_noHeader")
    print("This script assumes your files have a header line\nCheck output carefully!")
    time.sleep(1.8)

    filenames = []

    for file in Path.cwd().iterdir():
        if file.suffix == ".csv" and file.parent != user_dir:
            print(f"\n\nFound {file.name}\n")
            filenames.append(file)

            with open(file, "r", newline="") as f:
                dict_read = csv.DictReader(f)
                headers = dict_read.fieldnames

                if headers:
                    print("Assumed Headers:")
                    for h in headers:
                        print(h)
                else:
                    print("No Headers Found")
                
                    

    print("remove headers? (y/n)")
    while True:
        user = input(">").lower().strip()
        if user not in ["y", "n"]:
            print("invalid command")
            continue
        elif user == "y":
            break
        else:
            return

    user_dir.mkdir(exist_ok=True)

    for i, file in enumerate(filenames):
        print(f"\n[{i+1}/{len(filenames)}] cleaning {file.name}...")

        new_path = user_dir / f"{file.stem}_new{file.suffix}"

        with open(file, "r", newline="") as src, open(new_path, "w", newline="") as dst:
            #discovered that you can call open more than once
            reader = csv.reader(src)
            writer = csv.writer(dst)

            next(reader, None)  # skip iterator once to 
            #avoid the header

            for row in reader:
                writer.writerow(row)

        print(f"Saved to file: {new_path.name}")

    print(f"Cleaning done.\nCheck the Folder named {user_dir} for output")

if __name__ == "__main__":
    main()