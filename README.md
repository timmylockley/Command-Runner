# Autonomous Cross-Platform Background Task Runner

A powerful Python deployment system built to fetch, configure, and execute remote task lists from an online JSON repository entirely in stealth mode. Designed for easy portability via USB drives across multiple operating systems.

---

## Table of Contents
- [Features](#features)
- [Project Architecture](#project-architecture)
- [USB Setup & Auto-Deployment](#usb-setup--auto-deployment)
- [Configuration Guide](#configuration-guide)
- [JSON Schema Reference](#json-schema-reference)
- [Troubleshooting](#troubleshooting)

---

## Features

- **Stealth Background Execution:** Executes tasks without opening a visible command prompt or terminal shell window (`CREATE_NO_WINDOW` on Windows, silent background processing on Unix).
- **Universal Portability:** Compatible with Windows, macOS, and Linux out of the box.
- **Dynamic Payload Management:** Commands are hosted externally on a remote server or GitHub JSON file, allowing you to change tasks dynamically without modifying the files on the USB drive.
- **OS Filtering:** Selectively filter and execute commands specific to the target operating system.

---

## Project Architecture
USB_ROOT/
│
├── background_runner.py   # Main Python worker script
├── launch.bat             # Silent launcher for Windows machines
├── autorun.inf            # Windows configuration integration
└── run.command            # Shell launcher for macOS machines
---

## USB Setup & Auto-Deployment

1. **Format your USB Drive:** Format the drive to `FAT32` or `exFAT` to ensure cross-platform compatibility.
2. **Add Files:** Copy `background_runner.py`, `launch.bat`, and `run.command` to the root directory of the USB drive.
3. **Configure URL:** Open `background_runner.py` and replace `JSON_URL` with the raw web link pointing to your hosted `commands.json` file.
4. **Execution:**
   - **On Windows:** Double-click `launch.bat` (or set up the USB to prompt via `autorun.inf`). Python will fetch and execute your code frames silently.
   - **On macOS:** Double-click `run.command` in the mounted Finder window.

---

## Configuration Guide

The script relies on native system interpreters. Ensure target target systems have Python installed. 

- **Windows Requirement:** Uses `pythonw.exe` (bundled with standard Python installations on Windows) to bypass terminal rendering.
- **Network Dependency:** Requires an active internet connection on the target machine to successfully pull the command registry from your JSON URL.

---

## JSON Schema Reference

Host your configuration file online (e.g., via GitHub raw links, AWS S3, or a private web server):

```json
{
  "commands": [
    {
      "name": "Diagnostic Check Windows",
      "os": "Windows",
      "command": "systeminfo > C:\\temp_info.txt"
    },
    {
      "name": "Diagnostic Check Unix",
      "os": "Linux",
      "command": "uname -a > /tmp/sys_info.txt"
    }
  ]
}
