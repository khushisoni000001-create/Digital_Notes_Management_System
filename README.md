# Digital Notes Management System

**PS No.:** 60  
**Project:** Digital Notes Management System  
**Language:** Python 3

## Description
A console-based application to add, view, search, edit and delete text notes. Notes are stored permanently in `notes.txt`, so they are available when the program is started again.

## Files
- `one.py` — main Python program
- `notes.txt` — saved notes (one note per line)
- `Test_cases_passed.pdf` — test-case report and execution results
- `Project_Details/PS_No_60.png` — project allocation details

## Requirements
- Python 3
- No external Python packages are required.

## How to run
1. Download or clone this repository.
2. Open a terminal in the project folder.
3. Run:

   ```bash
   python one.py
   ```

4. Choose an option from the menu:
   - `1` Add a note
   - `2` View all notes
   - `3` Search notes
   - `4` Edit a note
   - `5` Delete a note
   - `6` Exit

## Storage format
Each line in `notes.txt` follows this format:

`ID|Title|Content`

Example:

`N1|Python|Learn loops`

Search checks both title and content and ignores uppercase/lowercase differences. The application creates `notes.txt` automatically when a note is first saved.
