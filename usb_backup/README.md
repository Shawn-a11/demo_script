# USB File Auto Backup Tool

This is an automatic monitoring and backup tool for educational files on USB drives that can:
1. Automatically detect newly inserted USB drives
2. Scan for educational files (PPT, PDF, DOC, etc.)
3. Automatically backup to the local C:\course_ppt folder

## Features

- Automatic USB device monitoring
- Support for multiple file formats (PPT, PPTX, PDF, DOC, DOCX, TXT)
- Automatic filename conflict resolution
- Real-time file monitoring
- Automatic backup directory creation

## Requirements

1. Python 3.7 or higher
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Install pywin32 (Windows system):
   ```bash
   pip install pywin32
   ```

## Usage

1. Run the script:
   ```bash
   python usb_backup.py
   ```

2. Insert a USB drive, the script will automatically:
   - Scan for educational files on the USB drive
   - Copy to C:\course_ppt directory
   - Add random string if filename conflicts occur

## Supported File Types

- PowerPoint files (.ppt, .pptx)
- PDF files (.pdf)
- Word documents (.doc, .docx)
- Text files (.txt)

## Notes

- Script requires administrator privileges to access C: drive
- Close other programs that might be using the USB drive before running the script
- Run the script as administrator if you encounter file access permission issues

## Stop Monitoring

Press Ctrl+C to stop monitoring and exit the program 