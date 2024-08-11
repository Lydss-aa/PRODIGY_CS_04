# Keylogger Project

## Overview

The Keylogger Project is a Python script designed to capture and log keystrokes. This script is an educational tool to demonstrate basic keylogging functionality using the `pynput` library. It serves as a learning exercise to understand how keystroke monitoring can be implemented and used in Python.

## Features

- **Captures Keystrokes**: Records every keystroke typed on the keyboard.
- **Log File**: Saves all captured keystrokes to a file named `log.txt`.
- **Graceful Exit**: Stops the logging process when the `Esc` key is pressed, ensuring that no more keystrokes are captured after stopping.

## Requirements

- **Python 3.x**: The script requires Python 3 to run. It should be installed on your system.
- **pynput Library**: A Python library used to monitor and control input devices.

## Installation

1. **Clone the Repository:**
   - To get a copy of this project, clone it from GitHub:
     ```bash
     git clone https://github.com/yourusername/keylogger_project.git
     ```

2. **Navigate to the Project Directory:**
   - Change to the directory where the project is located:
     ```bash
     cd keylogger_project
     ```

3. **Create a Virtual Environment (optional but recommended):**
   - Setting up a virtual environment ensures that dependencies are isolated from the system-wide Python installation:
     ```bash
     python -m venv venv
     ```

4. **Activate the Virtual Environment:**
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

5. **Install Dependencies:**
   - Install the `pynput` library, which is required for the keylogger to function:
     ```bash
     pip install pynput
     ```

## Usage

1. **Run the Keylogger Script:**
   - Start the keylogger by executing the script:
     ```bash
     python keylogger.py
     ```

2. **Type in Any Application:**
   - Open any application that accepts text input, such as Notepad, a web browser, or any other text field. The keylogger will record all keystrokes made in these applications.

3. **Stop the Keylogger:**
   - To stop logging keystrokes, press the `Esc` key. The script will terminate, and no further keystrokes will be logged.

4. **Check the Log File:**
   - After stopping the script, open `log.txt` in the project directory to view the recorded keystrokes.

## Notes

- **Ethical Use**: This script is intended solely for educational purposes to learn about keylogging and keystroke capture. It should not be used for unauthorized monitoring or malicious activities. Always obtain proper consent before using such tools.
- **Privacy**: Be mindful of privacy concerns. Avoid capturing sensitive or personal information with this script.


