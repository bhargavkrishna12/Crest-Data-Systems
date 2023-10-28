'''' Install required python software and do run the python file '''
import os
import csv

# Function to read and process data from input files
def process_input_files(input_files):
    data = []  # To store processed data
    for input_file in input_files:
        with open(input_file, 'r') as file:
            next(file)  # Skip the header row
            for line in file:
                fields = line.strip().split('\t')
                data.append({
                    'id': fields[0],
                    'first_name': fields[1],
                    'last_name': fields[2],
                    'email': fields[3],
                    'job_title': fields[4],
                    'basic_salary': float(fields[5]),
                    'allowances': float(fields[6])
                })
    return data

# Function to calculate 2nd highest salary and average salary
def calculate_statistics(data):
    unique_data = list({entry['id']: entry for entry in data}.values())  # Remove duplicates
    sorted_data = sorted(unique_data, key=lambda x: x['basic_salary'], reverse=True)
    second_highest = sorted_data[1]['basic_salary'] if len(sorted_data) > 1 else None
    average = sum(entry['basic_salary'] + entry['allowances'] for entry in unique_data) / len(unique_data) if unique_data else None
    return second_highest, average

# Function to create the output CSV file
def create_output_csv(output_folder, output_file, data, second_highest, average):
    with open(os.path.join(output_folder, output_file), 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        
        # Write the header
        writer.writerow(['id', 'first_name', 'last_name', 'email', 'job_title', 'basic_salary', 'allowances', 'Gross Salary'])

        # Write data
        for entry in data:
            gross_salary = entry['basic_salary'] + entry['allowances']
            writer.writerow([entry['id'], entry['first_name'], entry['last_name'], entry['email'], entry['job_title'], entry['basic_salary'], entry['allowances'], gross_salary])
        
        # Write second-highest and average salary
        writer.writerow([])  # Empty row for separation
        writer.writerow(['Second Highest Salary', second_highest])
        writer.writerow(['Average Salary', average])



# Main function
def main():
    input_files = ['data1.dat', 'data2.dat']  # List of input files
    output_folder = 'C:\\Users\\bharg\\Downloads\\assessment'  # Replace with your output folder path
    output_file = 'result.csv'

    # Process input files
    data = process_input_files(input_files)
    # print(data)

    # Calculate statistics
    second_highest, average = calculate_statistics(data)

    # Create the output CSV file
    # Use os.makedirs to create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)
    create_output_csv(output_folder, output_file, data, second_highest, average)

if __name__ == '__main__':
    main()

