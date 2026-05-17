import csv
import os
from datetime import datetime

def generate_and_clean_report():
    """
    Simulates a production data pipeline.
    Reads raw data, filters out anomalies, and exports a clean CSV report.
    """
    raw_data = [
        {"item": "Laptop", "price": 1200, "status": "available"},
        {"item": "Smartphone", "price": 800, "status": "available"},
        {"item": "Broken Monitor", "price": 0, "status": "out_of_stock"},
        {"item": "Tablet", "price": 450, "status": "available"},
        {"item": "Headphones", "price": -10, "status": "error_rate"}  # Anomaly
    ]
    
    clean_data = []
    filename = "cleaned_business_report.csv"
    
    print(f"[{datetime.now()}] Starting data cleaning process...")
    
    # Simulating data transformation and cleaning logic
    for entry in raw_data:
        if entry["price"] > 0 and entry["status"] == "available":
            # Adding a 10% tax column programmatically
            entry["price_with_tax"] = round(entry["price"] * 1.1, 2)
            clean_data.append(entry)
        else:
            print(f"--> Filtered out invalid entry: {entry['item']}")

    # Exporting to CSV
    try:
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=["item", "price", "status", "price_with_tax"])
            writer.writeheader()
            writer.writerows(clean_data)
            
        print(f"\n[Success] Cleaned report saved to '{os.path.abspath(filename)}'")
        print(f"Total processed items: {len(clean_data)}")
        
    except IOError as e:
        print(f"[Error] Failed to write file: {e}")

if __name__ == "__main__":
    generate_and_clean_report()
