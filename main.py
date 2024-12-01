#pip install pdf2docx

from pdf2docx import Converter
import os

def pdf_to_word(pdf_file, word_file):
    """
    Converts a PDF file to a Word document.
    
    :param pdf_file: Path to the input PDF file.
    :param word_file: Path to the output Word file.
    """
    try:
        # Create a Converter object
        converter = Converter(pdf_file)
        print("Converting PDF to Word...")
        # Perform the conversion
        converter.convert(word_file, start=0, end=None)  # Converts all pages
        converter.close()
        print(f"Conversion successful! Word document saved as: {word_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    print("PDF to Word Converter")
    print("======================")
    # Input PDF file
    pdf_file = input("Enter the path to the PDF file: ").strip()
    
    # Check if the file exists
    if not os.path.exists(pdf_file):
        print("Error: The specified PDF file does not exist.")
        return
    
    # Output Word file
    word_file = input("Enter the path to save the Word document (e.g., output.docx): ").strip()
    
    # Perform the conversion
    pdf_to_word(pdf_file, word_file)

if __name__ == "__main__":
    main()
