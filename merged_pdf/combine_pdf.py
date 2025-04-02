import os
from PIL import Image
from docx2pdf import convert
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import tempfile
import shutil

def create_directory(directory):
    """Create directory if it doesn't exist"""
    if not os.path.exists(directory):
        os.makedirs(directory)

def convert_image_to_pdf(image_path, output_path):
    """Convert image to PDF"""
    try:
        image = Image.open(image_path)
        # If image is in RGBA mode, convert to RGB
        if image.mode == 'RGBA':
            image = image.convert('RGB')
        image.save(output_path, 'PDF', resolution=100.0)
        return True
    except Exception as e:
        print(f"Error converting image {image_path}: {str(e)}")
        return False

def merge_pdfs(pdf_files, output_path):
    """Merge multiple PDF files"""
    from PyPDF2 import PdfMerger
    merger = PdfMerger()
    
    for pdf in pdf_files:
        try:
            merger.append(pdf)
        except Exception as e:
            print(f"Error merging PDF {pdf}: {str(e)}")
    
    merger.write(output_path)
    merger.close()

def main():
    # Create temporary and output directories
    temp_dir = tempfile.mkdtemp()
    output_dir = os.path.join("merged_pdf", "output")
    create_directory(output_dir)
    
    # Supported file formats
    image_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.bmp'}
    word_extensions = {'.doc', '.docx'}
    pdf_extension = '.pdf'
    
    # Store paths of all converted PDF files
    pdf_files = []
    
    # Process all files in current directory
    for filename in os.listdir('.'):
        file_extension = os.path.splitext(filename)[1].lower()
        
        if file_extension in image_extensions:
            # Process image files
            temp_pdf = os.path.join(temp_dir, f"{filename}{pdf_extension}")
            if convert_image_to_pdf(filename, temp_pdf):
                pdf_files.append(temp_pdf)
        
        elif file_extension in word_extensions:
            # Process Word documents
            try:
                temp_pdf = os.path.join(temp_dir, f"{filename}{pdf_extension}")
                convert(filename, temp_pdf)
                pdf_files.append(temp_pdf)
            except Exception as e:
                print(f"Error converting Word document {filename}: {str(e)}")
        
        elif file_extension == pdf_extension:
            # Directly add PDF files
            pdf_files.append(filename)
    
    if pdf_files:
        # Merge all PDF files
        output_path = os.path.join(output_dir, "merged_output.pdf")
        merge_pdfs(pdf_files, output_path)
        print(f"Files successfully merged to: {output_path}")
    else:
        print("No processable files found")
    
    # Clean up temporary files
    shutil.rmtree(temp_dir)

if __name__ == "__main__":
    main()