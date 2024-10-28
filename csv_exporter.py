import csv

def export_to_csv(invoices, output_file="./data-storage/csv/facturas.csv"):
    if not invoices:
        print("\nNo hay facturas para exportar.")
        return

    headers = invoices[0].keys()
    try:
        with open(output_file, mode='w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=headers)
            writer.writeheader()
            writer.writerows(invoices)
        print(f"\nFacturas exportadas al PATH {output_file}")
    except Exception as e:
        print(f"\nOcurrió un error al exportar a CSV: {e}")