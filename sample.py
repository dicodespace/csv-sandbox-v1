import csv

def main(filepath):
    total_revenue=0
    transaction_count=0
    with open(filepath,'r') as csv_file:
        spam_reader=csv.DictReader(csv_file)
        header=next(spam_reader)

        for row in spam_reader:            
            center_name=row['center_name']
            total_received = float(row['total_received'])
            total_pending = float(row['total_pending'])
            total_transactions = float(row['total_transactions'])

            total_revenue += total_pending + total_received
            avg_transaction = total_revenue / total_transactions

            print(f"Center: {center_name}")
            print(f"Total Revenue: {total_revenue}")
            print(f"Avg Transaction : {avg_transaction}")   

main("sample_center_data_v1.csv")