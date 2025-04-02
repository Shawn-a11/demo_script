# File to PDF Merger

A Python script that combines various file formats (images, Word documents, and PDFs) into a single PDF file.

## Features

- Supports multiple file formats:
  - Images: JPG, JPEG, PNG, GIF, BMP
  - Documents: DOC, DOCX
  - PDF files
- Automatically converts images and Word documents to PDF
- Merges all converted files into a single PDF
- Handles temporary files cleanup
- Supports both Windows and WSL paths

## Prerequisites

### Python Packages
```bash
pip install Pillow python-docx docx2pdf reportlab PyPDF2
```

### System Dependencies (for Linux/WSL)
```bash
sudo apt-get update
sudo apt-get install -y \
    libtiff5 \
    libtiff5-dev \
    libjpeg-dev \
    zlib1g-dev \
    libfreetype6-dev \
    liblcms2-dev \
    libwebp-dev \
    tcl8.6-dev \
    tk8.6-dev \
    python3-tk
```

## Usage

### Basic Usage
1. Place the script in the directory containing your files
2. Run the script:
```bash
python combine_pdf.py
```

### Command Line Arguments
```bash
python combine_pdf.py [input_files/directories] [-o output_file]
```

#### Examples:

1. Process single file:
```bash
python combine_pdf.py document.docx
```

2. Process multiple files:
```bash
python combine_pdf.py image1.jpg document.docx file.pdf
```

3. Process entire directory:
```bash
python combine_pdf.py /path/to/directory
```

4. Specify output file:
```bash
python combine_pdf.py file1.jpg folder1 -o result.pdf
```

### Windows/WSL Path Support

The script supports both Windows and WSL path formats:

Windows format:
```bash
python combine_pdf.py "D:\Documents\file.jpg"
```

WSL format:
```bash
python combine_pdf.py "/mnt/d/Documents/file.jpg"
```

## Output

- Converted files are saved in the `output` directory by default
- Default output filename is `merged_output.pdf`
- Custom output path can be specified using the `-o` option

## Error Handling

The script includes error handling for:
- File conversion failures
- Unsupported file formats
- PDF merging issues
- File access permissions
- Path conversion errors

## Limitations

- Word document conversion requires Microsoft Word or LibreOffice installed
- Large files may require additional processing time
- Maximum file size depends on available system memory

## Troubleshooting

1. If images fail to convert:
   - Ensure all required system libraries are installed
   - Check file permissions
   - Verify image file integrity

2. If Word documents fail to convert:
   - Ensure Microsoft Word or LibreOffice is installed
   - Check if the document is password protected
   - Verify file permissions

3. Path issues in WSL:
   - Use correct path format for your environment
   - Ensure files are accessible from WSL
   - Check file permissions in both Windows and WSL

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Uses PyPDF2 for PDF manipulation
- Uses python-docx for Word document processing
- Uses Pillow for image processing