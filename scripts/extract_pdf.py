from pypdf import PdfReader
import sys

pdf_path = sys.argv[1]
output_path = sys.argv[2]

reader = PdfReader(pdf_path)
full_text = ""

for i, page in enumerate(reader.pages):
    text = page.extract_text()
    full_text += f"\n--- PAGE {i+1} ---\n{text}\n"

with open(output_path, "w", encoding="utf-8") as f:
    f.write(full_text)

print(f"Extracted {len(reader.pages)} pages to {output_path}")
