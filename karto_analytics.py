""" This project 3 demonstates my ability to fetch, parse and write different file types with python"""

# Standard Library imports
import csv
import json
import pathlib
from collections import Counter, defaultdict
import pandas as pd

# External library imports (requires virtual environment)
import requests

# Data Acquisition
def fetch_and_write_txt_data(folder_name, filename, url):
    '''Retrieves data from specified URL and writes files in folder'''
    try:
        response = requests.get(url)
        response.raise_for_status()
        if response.status_code == 200:
            write_txt_file(folder_name, filename, response.text)
        else:
            print(f"Failed to fetch TXT data: {response.status_code}")
            
    except requests.exceptions.HTTPError as errh:
        print(f"Http Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"Oops: Something Else: {err}")
    except IOError as e:
        print(f"I/O error({e.errno}): {e.strerror}")

def fetch_and_write_csv_data(folder_name, filename, url):
    '''Retrieves CSV data from specified URL writes it to a file in folder'''
    try:
        response = requests.get(url)
        response.raise_for_status()
        if response.status_code == 200:
            write_csv_file(folder_name, filename, response.content)
        else:
            print(f"Failed to fetch CSV data: {response.status_code}")
            
    except requests.exceptions.HTTPError as errh:
        print(f"Http Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"Oops: Something Else: {err}")
    except IOError as e:
        print(f"I/O error({e.errno}): {e.strerror}")

def fetch_and_write_json_data(folder_name, filename, url):
    '''Retrieves JSON Data from specified URL writes it to a file in folder'''
    try:
        response = requests.get(url)
        response.raise_for_status()
        if response.status_code == 200:
            write_json_file(folder_name, filename, response.text)
        else:
            print(f"Failed to fetch JSON data: {response.status_code}")
        
    except requests.exceptions.HTTPError as errh:
        print(f"Http Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"Oops: Something Else: {err}")
    except IOError as e:
        print(f"I/O error({e.errno}): {e.strerror}")

def fetch_and_write_excel_data(folder_name, filename, url):
    '''Retrieves EXCEL Data from specified URL writes it to a file in folder'''
    try:
        response = requests.get(url)
        response.raise_for_status()
        if response.status_code == 200:
            write_excel_file(folder_name, filename, response.content)
        else:
            print(f"Failed to fetch Excel data: {response.status_code}")
            
    except requests.exceptions.HTTPError as errh:
        print(f"Http Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"Oops: Something Else: {err}")
    except IOError as e:
        print(f"I/O error({e.errno}): {e.strerror}")
        
# Write Data
def write_txt_file(folder_name, filename, data):
    '''Saves Text Data to a file'''
    file_path = pathlib.Path(folder_name) / filename
    file_path.write_text(data)
    print(f"Text data saved to {file_path}")

def write_csv_file(folder_name, filename, data):
    '''Saves CSV data to a file'''
    file_path = pathlib.Path(folder_name) / filename
    with open(file_path, 'wb') as file:
        file.write(data)
    print(f"CSV data saved to {file_path}")

def write_json_file(folder_name, filename, data):
    '''Saves JSON data to a file'''
    file_path = pathlib.Path(folder_name) / filename
    with open(file_path, 'w') as file:
        file.write(data)
    print(f"JSON data saved to {file_path}")

def write_excel_file(folder_name, filename, data):
    '''Saves Excel File Data'''
    file_path = pathlib.Path(folder_name) / filename
    with open(file_path, 'wb') as file:
        file.write(data)
    print(f"Excel data saved to {file_path}")
    
# Process and Generate Output

def process_txt_file(folder_name, filename, result_filename):
    file_path = pathlib.Path(folder_name) / filename
    result_path = pathlib.Path(folder_name) / result_filename
    '''Reads content of a text file, processes with lists and sets, and handles exceptions'''
    try:
        with open(file_path, 'r') as file:
            text = file.read()
        
        words = text.split()
        word_count = len(words)
        word_freq = Counter(words)
        unique_words = set(words)
        unique_word_count = len(unique_words)
        
        with open(result_path, 'w') as file:
            file.write(f"Total word count: {word_count}\n")
            file.write(f"Unique word count: {unique_word_count}\n")
            file.write("Word frequencies:\n")
            for word, freq in word_freq.most_common():
                file.write(f"{word}: {freq}\n")
        
        print(f"Processed text data saved to {result_path}")
    except Exception as e:
        print(f"Error processing text file: {e}")

def process_csv_file(folder_name, filename, result_filename):
    file_path = pathlib.Path(folder_name) / filename
    result_path = pathlib.Path(folder_name) / result_filename
    '''Reads content of a csv file, processes with tuples, and handles exceptions'''
    try:
        with open(file_path, 'rb') as file:
            data = file.read().decode('utf-8').splitlines()
        reader = csv.reader(data)
        headers = next(reader)
        rows = [row for row in reader]
        
        column_data = defaultdict(list)
        for row in rows:
            for header, value in zip(headers, row):
                column_data[header].append(value)
        
        with open(result_path, 'w') as file:
            for header, values in column_data.items():
                file.write(f"Column: {header}\n")
                file.write(f"Number of entries: {len(values)}\n")
                file.write(f"Sample values: {', '.join(values[:5])}\n")  
                file.write("\n")
        
        print(f"Processed CSV data saved to {result_path}")
    except Exception as e:
        print(f"Error processing CSV file: {e}")

def process_excel_file(folder_name, filename, result_filename):
    file_path = pathlib.Path(folder_name) / filename
    result_path = pathlib.Path(folder_name) / result_filename
    '''Reads content of an Excel file, processes with pandas, and handles exceptions'''
    try:
        data = pd.read_excel(file_path, sheet_name=None)
        with open(result_path, 'w') as file:
            for sheet_name, df in data.items():
                file.write(f"Sheet: {sheet_name}\n")
                file.write(df.describe(include='all').to_csv())
                file.write("\n")
        print(f"Processed Excel data saved to {result_path}")
    except Exception as e:
        print(f"Error processing Excel file: {e}")

def process_json_file(folder_name, filename, result_filename):
    file_path = pathlib.Path(folder_name) / filename
    result_path = pathlib.Path(folder_name) / result_filename
    '''Reads content of a JSON file, processes with dictionaries, and handles exceptions'''
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        
        insights = []
        def extract_info(d, indent=0):
            for key, value in d.items():
                if isinstance(value, dict):
                    insights.append(f"{' ' * indent}{key}:")
                    extract_info(value, indent + 2)
                elif isinstance(value, list):
                    insights.append(f"{' ' * indent}{key}:")
                    for item in value:
                        if isinstance(item, dict):
                            extract_info(item, indent + 2)
                        else:
                            insights.append(f"{' ' * (indent + 2)}- {item}")
                else:
                    insights.append(f"{' ' * indent}{key}: {value}")

        extract_info(data)
        
        with open(result_path, 'w') as file:
            file.write("\n".join(insights))
        
        print(f"Processed JSON data saved to {result_path}")
    except Exception as e:
        print(f"Error processing JSON file: {e}")

# Main Function
def main():
    ''' Main function to demonstrate module capabilities. '''

    # URL definitions
    txt_url = 'https://github.com/denisecase/datafun-03-spec/raw/main/data.txt'
    csv_url = 'https://github.com/denisecase/datafun-03-spec/raw/main/data.csv'
    excel_url = 'https://github.com/denisecase/datafun-03-spec/raw/main/data.xls'
    json_url = 'https://github.com/denisecase/datafun-03-spec/raw/main/data.json'

    # Folder and file names
    txt_folder_name = 'data-txt'
    csv_folder_name = 'data-csv'
    excel_folder_name = 'data-excel'
    json_folder_name = 'data-json'

    txt_filename = 'data.txt'
    csv_filename = 'data.csv'
    excel_filename = 'data.xls'
    json_filename = 'data.json'

    # Create directories if they don't exist
    pathlib.Path(txt_folder_name).mkdir(exist_ok=True)
    pathlib.Path(csv_folder_name).mkdir(exist_ok=True)
    pathlib.Path(json_folder_name).mkdir(exist_ok=True)
    pathlib.Path(excel_folder_name).mkdir(exist_ok=True)

    # Fetch and write data
    fetch_and_write_txt_data(txt_folder_name, txt_filename, txt_url)
    fetch_and_write_csv_data(csv_folder_name, csv_filename, csv_url)
    fetch_and_write_excel_data(excel_folder_name, excel_filename, excel_url)
    fetch_and_write_json_data(json_folder_name, json_filename, json_url)

    # Process data
    process_txt_file(txt_folder_name, txt_filename, 'results_txt.txt')
    process_csv_file(csv_folder_name, csv_filename, 'results_csv.txt')
    process_excel_file(excel_folder_name, excel_filename, 'results_excel.txt')
    process_json_file(json_folder_name, json_filename, 'results_json.txt')

if __name__ == '__main__':
    main()