import fitz  # PyMuPDF
import os
import json
from tqdm import tqdm

def pdf_to_md(pdf_path: str, output_dir: str):
    """Convert a PDF to markdown, extract images, and save metadata."""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    doc = fitz.open(pdf_path)
    md_filename = os.path.join(output_dir, f"{os.path.splitext(os.path.basename(pdf_path))[0]}.md")
    images_dir = os.path.join(output_dir, "images")
    os.makedirs(images_dir, exist_ok=True)
    
    metadata = {
        "filename": os.path.basename(pdf_path),
        "page_count": len(doc),
        "pages": []
    }

    with open(md_filename, 'w', encoding='utf-8') as md_file:
        md_file.write(f"# {os.path.basename(pdf_path)}\n\n")
        
        for page_num in tqdm(range(len(doc)), desc="Processing pages"):
            page = doc.load_page(page_num)
            text = page.get_text("text")
            
            page_data = {"page": page_num + 1, "images": []}
            md_file.write(f"## Page {page_num + 1}\n\n")
            md_file.write(text.strip() + "\n\n")
            
            image_list = page.get_images(full=True)
            for img_idx, img in enumerate(image_list):
                xref = img[0]
                pix = fitz.Pixmap(doc, xref)
                img_name = f"page{page_num + 1}_img{img_idx + 1}.png"
                img_path = os.path.join("images", img_name)
                pix.save(os.path.join(output_dir, img_path))
                md_file.write(f"![Image {img_idx + 1}]({img_path})\n\n")
                page_data["images"].append(img_name)
            
            metadata["pages"].append(page_data)

    with open(os.path.join(output_dir, "metadata.json"), 'w', encoding='utf-8') as f:
        json.dump(metadata, f, indent=4)
        
    print(f"[OK] Conversion complete. Files saved in: {output_dir}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Convert PDF to Markdown with images and metadata.")
    parser.add_argument("pdf_path", help="Path to the source PDF file")
    parser.add_argument("output_dir", nargs='?', default="output", help="Directory to save output files")
    args = parser.parse_args()
    pdf_to_md(args.pdf_path, args.output_dir)
