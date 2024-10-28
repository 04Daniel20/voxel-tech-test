import os
import re
import xml.etree.ElementTree as ET
from PyPDF2 import PdfReader


class FileExtractor:
    def __init__(self, folder_path):
        self.folder_path = folder_path

    def extract_pdf_ids(self):
        
        ids = []
        print(self.folder_path)
        for pdf_file in os.listdir(self.folder_path):
            if pdf_file.endswith(".pdf"):
                pdf_path = os.path.join(self.folder_path, pdf_file)
                try:
                    reader = PdfReader(pdf_path)
                    text = ""

                    
                    for page in reader.pages:
                        if page.extract_text():
                            text += page.extract_text()
                    
                    cleaned_text = re.sub(
                        r"\s+", " ", text
                    )  
                    pattern = r"Número Referencia:\s*(\d+)"
                    match = re.search(pattern, cleaned_text)
                    if match:
                        ids.append(match.group(1))

                except Exception as e:
                    print(f"Error al procesar {pdf_file}: {e}")

        return ids

    def extract_xml_invoices(self):
    
        invoice_data = []

        for filename in os.listdir(self.folder_path):
            if filename.endswith(".xml"):
                file_path = os.path.join(self.folder_path, filename)
                try:
                    tree = ET.parse(file_path)
                    root = tree.getroot()

                    general_data = root.find("GeneralData")
                    supplier_data = root.find("Supplier")

                    if general_data is not None and supplier_data is not None:
                        invoice_info = {
                            "Ref": general_data.get("Ref"),
                            "Type": general_data.get("Type"),
                            "Date": general_data.get("Date"),
                            "Currency": general_data.get("Currency"),
                            "Supplier": supplier_data.get("Company"),
                            "CIF": supplier_data.get("CIF"),
                            "Email": supplier_data.get("Email"),
                        }

                        invoice_data.append(invoice_info)
                    else:
                        print(f"Archivo {filename} no tiene los datos esperados.")

                except ET.ParseError as e:
                    print(f"Error analizando el archivo {filename}: {e}")

        return invoice_data