import glob
import csv 

def merge_csv_files(file_list, output_file):
    unique_rows = set()
    
    for file in file_list:
        with open(file, mode='r', newline='') as f:
            reader = csv.reader(f)
            next(reader)  # Skip header row
            for row in reader:
                if len(row) >= 2:  # Ensure row has at least 2 columns (POD, NODE)
                    unique_rows.add(tuple(row))
    
    with open(output_file, mode='w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["POD", "NODE"])  # Write header
        writer.writerows(unique_rows)

def count_unique_hosts(csv_file):
    unique_hosts = set()
    
    with open(csv_file, mode='r', newline='') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        
        for row in reader:
            if len(row) >= 2:  # Ensure row has at least 2 columns (POD, NODE)
                node = row[1].strip()
                if node:
                    unique_hosts.add(node)
    
    return len(unique_hosts)

if __name__ == "__main__":
    csv_files = glob.glob("*.csv")  # Adjust to target specific CSV files if needed
    merged_csv_filename = "merged_pods.csv"
    merge_csv_files(csv_files, merged_csv_filename)
    
    unique_host_count = count_unique_hosts(merged_csv_filename)
    print(f"Number of unique hosts: {unique_host_count}")

