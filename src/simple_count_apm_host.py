import csv

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
    csv_filename = "pods.csv"  # Update with the actual CSV file path if needed
    unique_host_count = count_unique_hosts(csv_filename)
    print(f"Number of unique hosts: {unique_host_count}")

