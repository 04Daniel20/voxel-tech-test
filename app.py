import argparse
import os
from csv_exporter import export_to_csv
from extractor import FileExtractor
from tabulate import tabulate



def main():
    parser = argparse.ArgumentParser(description="File Extractor CLI")
    parser.add_argument(
        "-p", "--path", type=str, required=True, help="Directorio de archivos"
    )
    args = parser.parse_args()

    def print_invoice(data):
        headers = ["Field", "Value"]
        rows = [(key, value) for key, value in data.items()]
        print(tabulate(rows, headers, tablefmt="pretty"))

    while True:
        print("\n--- File Extractor CLI ---")
        print("1. Extraer IDs de PDFs")
        print("2. Extraer información de facturas XML")
        print("3. Exportar facturas a un archivo CSV")
        print("4. Salir")
        option = input("Seleccione una opción (1-4):")

        if option == "1":
            extractor = FileExtractor(args.path + "\pdf")
            pdf_ids = extractor.extract_pdf_ids()
            if pdf_ids:
                print("\nIDs extraídos de PDFs:")
                for pdf_id in pdf_ids:
                    print(f"- {pdf_id}")
            else:
                print("\nNo se encontraron IDs en los PDFs.")

        elif option == "2":
            extractor = FileExtractor(args.path + r"\xml")
            invoices = extractor.extract_xml_invoices()
            if invoices:
                print("\nFacturas procesadas:")
                for invoice in invoices:
                    print_invoice(invoice)
            else:
                print("\nNo se encontraron facturas en los archivos XML.")

        elif option == "3":
            extractor = FileExtractor(os.path.join(args.path, "xml"))
            invoices = extractor.extract_xml_invoices()
            if invoices:
                export_to_csv(invoices)
            else:
                print("\nNo se encontraron facturas en los archivos XML para exportar.")

        elif option == "4":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida, por favor intente nuevamente.")


if __name__ == "__main__":
    main()
