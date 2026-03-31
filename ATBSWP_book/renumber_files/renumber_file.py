
import re
from pathlib import Path
import sys
#tested, and succeeded, made spam001.txt and bumped everything

"""
Write a program that finds all files with a given prefix, such as spam001.txt, spam002.txt, and so on, in a single folder and locates any gaps in the numbering (such as if there is a spam001.txt and a spam003.txt but no spam002 .txt)
As an added challenge, write another program that can insert gaps into
numbered files (and bump up the numbers in the filenames after the gap) so that a new file can be inserted.
"""
#json stuff made by ChatGPT

# this file stores which insertion operations have already been applied,
# so running the script again with the same exact request does not repeat
# the same renaming chain a second time.


def find_files(path=Path.cwd()) -> list:
    # dev errors
    if not isinstance(path, Path):
        raise ValueError("expected Path obj")
    elif not path.is_dir():
        raise ValueError("expected directory.")

    pattern = re.compile(r"""
    ([a-zA-Z]+)
    (\d+)\.
    ([a-zA-Z]+)
    """, re.VERBOSE)

    file_info = []

    for filepath in path.iterdir():
        match = re.fullmatch(pattern, filepath.name)
        if match:
            file_info.append(
                (
                    match.group(1),          # prefix
                    int(match.group(2)),     # number
                    len(match.group(2)),     # padding width
                    match.group(3),          # extension
                    filepath,                # actual Path object
                )
            )
    return file_info


# newer update
# i got the list of tuples working.
# breakdown before i go, it returns (prefix, number, padding width, extension, Path obj to file)

# older update
# todo: organize all files with a common prefix and filename extension
# then be able to identify which stuff is missing using the function below.


def find_ordering(files: tuple):
    # everything should be in a dictionary.
    # no need to do any dev checks or stuff. this is just for the user, if it breaks, its not my fault.
    file_collection = {}
    for file in files:
        key = (file[0], file[3])  # (prefix, extension)
        if key not in file_collection:
            file_collection[key] = {"numbers": [], "width": file[2]}
        file_collection[key]["numbers"].append(file[1])

    return file_collection


def find_gaps(collection: dict):
    gaps = {}

    for entry, data in collection.items():
        imperfect_set = set(data["numbers"])
        perfect_set = set(range(1, max(imperfect_set) + 1))
        gaps[entry] = {
            "missing": sorted(perfect_set - imperfect_set),
            "width": data["width"],
        }

    return gaps


# the values within entry
# a list of files found within a folder.



# missing files:


# cool, stored padding as a key value pair


print("Finding files...")
files = find_files()
# prefix   # number  # padding width  # extension # actual Path object
if not files:
    print("no files found, maybe check your current folder?")
    sys.exit()
for file in files:
    print(f"found {file[4].name}..")
info = find_gaps(find_ordering(files))
total_missing = 0

for filegroup in info:
    total_missing += len(info[filegroup]["missing"])

print(f"\n\n{total_missing} missing files found!\n")
if total_missing:
    print("namely:\n")

for filegroup in info:
    prefix, ext = filegroup
    width = info[filegroup]["width"]

    for num in info[filegroup]["missing"]:
        print(f"{prefix}{num:0{width}}.{ext}")
#width in find_gaps is redundant :/

#this section shall be where i bump up files and stuff


print("\nDo you want to automatically create empty files for all missing numbers in this group? (y/n)")
while True:
    user_fill = input(">").lower().strip()
    if user_fill == "y":
        pass
    elif user_fill == "n":
        print("Skipping auto-fill.")
        break
    else:
        print("invalid response")
        continue
    if not info:
        print("you typed 'y' knowing full well that there are no missing files\nexiting..")
        sys.exit()
    for filegroup in info:
        prefix, ext = filegroup
        width = info[filegroup]["width"]
        
       
        for num in info[filegroup]["missing"]:
            new_path = Path(f"{prefix}{num:0{width}}.{ext}")
            if not new_path.exists():   # avoid overwriting just in case
                new_path.touch()
                print(f"created {new_path.name}")
    print("\nAuto-fill complete.\n\nexiting...")
    sys.exit()
        
        
                

    
 
    
print("\nwould you like to insert a file?(y/n)")
#validation block
while True:
    user_input = input(">").lower().strip()
    if user_input == "y":
        break
    elif user_input == "n":
        print("exiting..")
        sys.exit()
    else:
        print("invalid response")
        continue
#TODO: make a system where the user specifies where they want to insert a file, or alternatively, create a file for the missing files earlier

print(f"which filegroup do you want to insert to?\nrecognized {len(info)} group/s")

i = 1
data = {}
for filegroup in info:
    prefix, ext = filegroup
    width = info[filegroup]["width"]
    print(f"{i}.  {prefix}{'X' * width}.{ext}")
    data[i] = filegroup
    i += 1
#multiple foolproof user input collecting incoming!
while True:
    try:
        user_filegroup = int(input(">"))

    except Exception:
        print("invalid response.")
        continue
    if user_filegroup in data:
        break
    else:
        print("invalid choice, please type one of the numbers listed above")




print("type a number in which to insert your file. (press enter to exit)")
chosen_files = []
for file in files:
    if file[0] == data[user_filegroup][0] and file[3] == data[user_filegroup][1]:
        chosen_files.append(list(file))
max_number_in_group = max(file[1] for file in chosen_files)

while True:
    try:
        user_number = input(">")
        if user_number == "":
            sys.exit()
        user_number = int(user_number)
        if user_number <= 0:
            print("ensure that your input is a positive integer")
            continue
        if user_number > max_number_in_group + 8:
            print(f"Error: insertion number {user_number} is too high. Max number is roughly {max_number_in_group + 8} for safety purposes.")
            continue
    except Exception:
        print("ensure that your input is a positive integer")
        continue
    break



#files



# prefix  0 # number 1 # padding width 2 # extension 3 # actual Path object 4
sorted_files = sorted(chosen_files, key=lambda x: x[1], reverse=True)  # got this neat line from ChatGPT
new_files = []
for file in sorted_files:
    if file[1] >= user_number:        # include the insertion point
        old_path = file[4]            # original file
        file[1] += 1                  # bump the number
        new_path = old_path.parent / f"{file[0]}{file[1]:0{file[2]}}.{file[3]}"  # keep it in cwd
        old_path.rename(new_path)     # actually rename the file
        new_files.append(new_path)    # track new files


#TODO: one more, make a blank file on that one specific gap that was made after all the bumping, since its 1am and im tired, I'll have AI write it (assume that i know what the code does even when not done by me)
prefix, ext = data[user_filegroup]
width = info[(prefix, ext)]["width"]
new_gap_file = Path(f"{prefix}{user_number:0{width}}.{ext}")

if not new_gap_file.exists():
    new_gap_file.touch()
    print(f"Created: {new_gap_file.name}")



print("it is done.\ninsertion successful. yay")


    # --- INSERTION LOGIC STEP-BY-STEP ---

# 1. Ask the user which group they want to insert into.
#    - A group is defined by (prefix, extension), e.g., ('spam', 'txt')
#    - You can list all available groups from your find_ordering(files) output.
#    - Prompt the user to input the prefix and extension, scrap that, I have a way better idea

# 2. Ask the user for the number where they want to insert the new file.
#    - Ensure it’s a positive integer.
#    - This number will be the "insertion point."

# 3. Identify all files in that group.
#    - Loop through your 'files' list returned from find_files()
#    - Only keep files where (file_prefix, file_ext) == chosen group.

# 4. Sort the files in descending order of their numbers.
#    - Sorting descending avoids overwriting files when you rename them.
#    - For example: spam003.txt, spam002.txt, spam001.txt

# 5. Loop through the sorted files.
#    For each file:
#    a) If its number >= insertion number:
#       - Compute new number: current number + 1
#       - Format the new filename with zero-padding:
#           e.g., f"{prefix}{new_number:0{width}}.{ext}"
#       - Rename the file using file_path.rename(new_path)
#    b) If its number < insertion number:
#       - Leave it alone

# 6. After bumping all relevant files, create the new file at the insertion number.
#    - Use Path().touch() to create an empty file:
#       Path(f"{prefix}{insert_number:0{width}}.{ext}").touch()

# 7. Optionally, print a confirmation to the user:
#       e.g., "Inserted spam002.txt and bumped subsequent files."

# 8. Optional extra safety measures:
#    - Validate that the group exists before trying to insert.
#    - Validate that the insertion number is within a reasonable range:
#      >=1 and <= max(current numbers)+1
#    - Handle any filesystem errors with try/except when renaming or touching files.

# --- END ---


# info = (spam,txt): {'missing': [42, 86, 103], 'width': 3}}



