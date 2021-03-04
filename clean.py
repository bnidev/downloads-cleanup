import json
import os
import collections

# load config
config = None
file = open("config.json",)
config = json.load(file)
file.close()

# get path from config
base_path = config["path"]
if not base_path or not os.path.isdir(base_path):
    username = os.getlogin()
    base_path = f"C:/Users/{username}/Downloads"

# get folders from config
folders = []
for folder in config["folders"]:
    folders.append(folder)

# add misc and unpacked to folder list
folders.append(config["misc_folder"])
folders.append(config["unpacked_folder"])

# create folders in Downloads
for folder in folders:
    dir_path = os.path.join(base_path, folder)
    if not os.path.isdir(dir_path):
        os.mkdir(dir_path)

# get file names from Downloads folder
files_dict = collections.defaultdict(list)
files_list = os.listdir(base_path)

# seperate folders from files
for name in files_list:
    name_dir = os.path.join(base_path, name)
    if os.path.isdir(name_dir) and name not in folders:        
        target_dir = os.path.join(base_path, config["unpacked_folder"], name)
        if config["sort_unpacked"]:
            os.rename(name_dir, target_dir)
    elif name not in folders:
        ext = name.split(".")[-1]
        files_dict[ext].append(name)

# copy files to associated directory
misc_files = []
for ext, files in files_dict.items():   
    for folder, filetypes in config["folders"].items():
        if ext in filetypes:
            for file in files:
                current_dir = os.path.join(base_path, file)
                target_dir = os.path.join(base_path, folder, file)
                os.rename(current_dir, target_dir)
        else:
            for file in files:
                misc_files.append(file)                


# copy files without specific directory to Misc
if misc_files and config["sort_misc"]:
    misc_f = list(dict.fromkeys(misc_files))
    misc_path = os.path.join(base_path, config["misc_folder"])
    if not os.path.isdir(misc_path):
        os.mkdir(misc_path)

    for file in misc_f:
        current_dir = os.path.join(base_path, file)
        target_dir = os.path.join(misc_path, file)
        os.rename(current_dir, target_dir)