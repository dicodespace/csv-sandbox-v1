import csv

def main(filepath):
    total_revenue=0
    transaction_count=0
    with open(filepath,'r') as csv_file:
        spam_reader=csv.reader(csv_file)
        header=next(spam_reader)

        for row in spam_reader:            
            print(row[1])
        total_revenue += float(row[3]) + float(row[2])
        avg_transaction = total_revenue / float(row[4])

    print(f"Total Revenue: {total_revenue}")
    print(f"Avg Transaction across all centers: {avg_transaction}")   

main("sample_center_data_v1.csv")