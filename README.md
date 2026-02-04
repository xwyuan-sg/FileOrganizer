## FileOrganizer
FileOrganizer is a fast, cross-platform command-line tool that organizes files in any folder by type. It groups files into predefined categories such as Videos, Music, Images, Documents, Archives, Executables, and Scripts.  

It handles all file extensions, resolves name conflicts automatically, and provides a color-coded summary at the end of the process.

---

## ✨ Features

- Recursive folder scanning  
- Organizes files by type (Videos, Music, Images, Documents, Archives, Executables, Scripts, Others)  
- Handles all extensions and unknown file types  
- Automatically resolves name collisions  
- Color-coded output:  
  - 🟢 Green: organization complete  
  - 🔵 Blue: donation message  
- Human-readable summary of files organized  
- Cross-platform: Windows, Linux, macOS  
- No ads, no tracking, no data sent anywhere  

---

## 🛠️ Technology

- **Language:** Python 3  
- **Libraries:** Python Standard Library only: `os`, `shutil`, `argparse`, `pathlib`, `sys`  
- No external dependencies required  

---

## 🚀 How to use

### Requirements

- Python 3.8 or newer

### Basic command

```bash
python FileOrganizer.py group "C:\\Path\\To\\Folder"
```

This command will scan the folder and move all files into their respective categories, creating folders if they do not exist.

## 🔒 Why this tool is safe
FileOrganizer only reads and moves files locally on your system. It does not send any data to external servers.
All operations are performed in-place, and name collisions are handled automatically to prevent overwriting.

## ❤️ Support the project
If you enjoy this project and want to support development, you can make a donation here: https://www.paypal.com/paypalme/EnricoArama
