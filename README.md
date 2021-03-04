A Python script to clean up your downloads folder. All files will be sorted into categorized folders.

## How to set up and run

The script uses `C:/Users/<Your-Username>/Downloads` as a standard path. If you want to change that, open `config.json` and replace `Your-Path-Here` with the path of your downloads folder. Then just run the `clean.py` file.

## Customization

All settings can be found in `config.json`. You can:

- rename, add and remove folders
- add, remove or reorganize the filetypes
- All folders found in downloads will be moved. You can rename the folder at `unpacked_folder` and/or disable that function by setting `sort_unpacked` to "false"
- All files that can not be categorized will be moved to a misc folder. You can rename the folder at `misc_folder` and/or disable that function by setting `sort_misc` to "false"
