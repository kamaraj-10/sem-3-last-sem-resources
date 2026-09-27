"""
PDF Data Extraction Script
Extracts text content from PDF files and organizes them for analysis
"""

import os
import sys
from pathlib import Path
from typing import List, Dict, Tuple

try:
    import PyPDF2
    print("✓ PyPDF2 is available")
except ImportError:
    print("Installing PyPDF2...")
    os.system("pip install PyPDF2")
    import PyPDF2


class PDFExtractor:
    """Extract and process data from PDF files"""
    
    def __init__(self, folder_path: str):
        """
        Initialize the PDF extractor
        
        Args:
            folder_path: Path to folder containing PDFs
        """
        self.folder_path = Path(folder_path)
        self.pdfs = []
        self.extracted_data = {}
        
    def find_pdfs(self) -> List[Path]:
        """Find all PDF files in the folder"""
        pdfs = list(self.folder_path.glob("*.pdf"))
        print(f"\n📄 Found {len(pdfs)} PDF files:")
        for pdf in pdfs:
            print(f"   - {pdf.name}")
        self.pdfs = pdfs
        return pdfs
    
    def extract_text_from_pdf(self, pdf_path: Path) -> Tuple[str, Dict]:
        """
        Extract text from a PDF file
        
        Args:
            pdf_path: Path to PDF file
            
        Returns:
            Tuple of (full_text, metadata_dict)
        """
        try:
            with open(pdf_path, 'rb') as pdf_file:
                pdf_reader = PyPDF2.PdfReader(pdf_file)
                
                # Get metadata
                num_pages = len(pdf_reader.pages)
                metadata = {
                    'filename': pdf_path.name,
                    'num_pages': num_pages,
                    'title': pdf_path.stem,
                }
                
                # Extract text from all pages
                text_content = []
                for page_num, page in enumerate(pdf_reader.pages):
                    text = page.extract_text()
                    if text:
                        text_content.append(f"--- Page {page_num + 1} ---\n{text}")
                
                full_text = "\n\n".join(text_content)
                return full_text, metadata
                
        except Exception as e:
            print(f"❌ Error reading {pdf_path.name}: {str(e)}")
            return "", {}
    
    def extract_all_pdfs(self) -> Dict:
        """Extract text from all PDFs"""
        self.find_pdfs()
        print("\n🔄 Extracting text from PDFs...\n")
        
        for pdf_path in self.pdfs:
            print(f"   Processing: {pdf_path.name}")
            text, metadata = self.extract_text_from_pdf(pdf_path)
            
            self.extracted_data[pdf_path.stem] = {
                'text': text,
                'metadata': metadata,
                'text_length': len(text),
            }
            
            if text:
                print(f"      ✓ Extracted {len(text)} characters")
            else:
                print(f"      ⚠ No text extracted")
        
        return self.extracted_data
    
    def get_summary(self) -> Dict:
        """Get summary of extracted data"""
        summary = {}
        for pdf_name, data in self.extracted_data.items():
            summary[pdf_name] = {
                'pages': data['metadata'].get('num_pages', 0),
                'text_length': data['text_length'],
                'has_content': len(data['text']) > 0,
            }
        return summary
    
    def save_extracted_data(self, output_folder: str = None):
        """Save extracted data to text files for reference"""
        if output_folder is None:
            output_folder = self.folder_path / "extracted_data"
        
        output_path = Path(output_folder)
        output_path.mkdir(exist_ok=True)
        
        print(f"\n💾 Saving extracted data to: {output_path}")
        for pdf_name, data in self.extracted_data.items():
            output_file = output_path / f"{pdf_name}_extracted.txt"
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(f"PDF: {pdf_name}\n")
                f.write(f"Pages: {data['metadata'].get('num_pages', 0)}\n")
                f.write("=" * 80 + "\n\n")
                f.write(data['text'])
            print(f"   ✓ Saved: {output_file.name}")


def main():
    """Main execution"""
    # Get the folder containing this script
    script_dir = Path(__file__).parent
    
    print("=" * 80)
    print("PDF DATA EXTRACTION TOOL")
    print("=" * 80)
    
    extractor = PDFExtractor(script_dir)
    extracted_data = extractor.extract_all_pdfs()
    
    # Print summary
    print("\n" + "=" * 80)
    print("EXTRACTION SUMMARY")
    print("=" * 80)
    summary = extractor.get_summary()
    for pdf_name, info in summary.items():
        status = "✓" if info['has_content'] else "⚠"
        print(f"{status} {pdf_name}")
        print(f"    Pages: {info['pages']}, Text Length: {info['text_length']} chars")
    
    # Save extracted data
    extractor.save_extracted_data()
    
    print("\n✅ Extraction complete!")
    return extracted_data


if __name__ == "__main__":
    extracted_data = main()
