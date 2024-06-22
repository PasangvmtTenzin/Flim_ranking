import pandas as pd 
import os
import numpy as np 

akas_path = 'data/movie/title.akas.tsv'


def split_file_large(file_path, num_parts=4, chunk_size=1024*1024):
    file_base = os.path.splitext(file_path)[0]
    file_extension = ".csv"  # Change the extension to .csv

    file_size = os.path.getsize(file_path)
    part_size = file_size // num_parts
    read_size = min(part_size, chunk_size)

    with open(file_path, 'rb') as file:
        for i in range(num_parts):
            with open(f"{file_base}_part{i+1}{file_extension}", 'w', encoding='utf-8') as part_file:
                bytes_written = 0
                remainder = b''

                while bytes_written < part_size:
                    file_chunk = file.read(read_size)
                    if not file_chunk:
                        break

                    # Add the remainder from the previous read
                    file_chunk = remainder + file_chunk

                    # Attempt to decode the chunk
                    try:
                        csv_chunk = file_chunk.decode('utf-8')
                        remainder = b''  # Reset remainder if decoding is successful
                    except UnicodeDecodeError as e:
                        # Find the start position of the problematic character
                        problem_pos = e.start
                        csv_chunk = file_chunk[:problem_pos].decode('utf-8')
                        remainder = file_chunk[problem_pos:]  # Save the remainder for the next chunk

                    # Replace tabs with commas
                    csv_chunk = csv_chunk.replace('\t', ',')
                    part_file.write(csv_chunk)

                    bytes_written += len(file_chunk) - len(remainder)

                # Ensure the last part includes any remaining bytes
                if i == num_parts - 1:
                    while True:
                        file_chunk = file.read(read_size)
                        if not file_chunk:
                            break

                        file_chunk = remainder + file_chunk
                        try:
                            csv_chunk = file_chunk.decode('utf-8')
                            remainder = b''
                        except UnicodeDecodeError as e:
                            problem_pos = e.start
                            csv_chunk = file_chunk[:problem_pos].decode('utf-8')
                            remainder = file_chunk[problem_pos:]

                        csv_chunk = csv_chunk.replace('\t', ',')
                        part_file.write(csv_chunk)

# Path to the file
akas_path = 'data/movie/title.akas.tsv'
# split_file_large(akas_path, num_parts=4)

part1_path = 'data/movie/akas/akas_part1.csv'

part2_path = 'data/movie/akas/akas_part2.csv'

part3_path = 'data/movie/akas/akas_part3.csv'

part4_path = 'data/movie/akas/akas_part4.csv'


def load_akas_part1(part1_path):
    part1_data = pd.read_csv(part1_path, on_bad_lines='skip', low_memory=False) 
    # data = part1_data.drop(columns=['ordering', 'title', 'types', 'attributes', 'isOriginalTitle'])
    data1 = part1_data.rename(columns={'titleId': 'tconst', 'region': 'Country_Code'})
    data1.replace('\\N', np.nan, inplace=True)
    data1.dropna(inplace=True)

    grouped_data = data1.groupby('tconst').agg({
        'title': list,
        'Country_Code': list,
        'attributes': list
    }).reset_index()

    # Extracting the first element from each list
    grouped_data['title'] = grouped_data['title'].apply(lambda x: x[0])
    grouped_data['Country_Code'] = grouped_data['Country_Code'].apply(lambda x: x[0])
    grouped_data['attributes'] = grouped_data['attributes'].apply(lambda x: x[0])

    return grouped_data
   

# akas = load_akas_part1(part1_path)
# print(akas.head(50))
# print(akas.isnull().sum())
# print(akas.info())


def load_akas_part2(part2_path):
    part2_data = pd.read_csv(part2_path, on_bad_lines='skip', low_memory=False) 
    data2 = part2_data.rename(columns={'titleId': 'tconst', 'region': 'Country_Code'})
    data2.replace('\\N', np.nan, inplace=True)
    data2.dropna(inplace=True)

    grouped_data = data2.groupby('tconst').agg({
        'title': list,
        'Country_Code': list,
        'attributes': list
    }).reset_index()

    # Extracting the first element from each list
    grouped_data['title'] = grouped_data['title'].apply(lambda x: x[0])
    grouped_data['Country_Code'] = grouped_data['Country_Code'].apply(lambda x: x[0])
    grouped_data['attributes'] = grouped_data['attributes'].apply(lambda x: x[0])

    return grouped_data
   

# akas = load_akas_part2(part2_path)
# print(akas.head(50))
# print(akas.isnull().sum())
# print(akas.info())

def load_akas_part3(part3_path):
    part3_data = pd.read_csv(part3_path, on_bad_lines='skip', low_memory=False) 
    data3 = part3_data.rename(columns={'titleId': 'tconst', 'region': 'Country_Code'})
    data3.replace('\\N', np.nan, inplace=True)
    data3.dropna(inplace=True)

    grouped_data = data3.groupby('tconst').agg({
        'title': list,
        'Country_Code': list,
        'attributes': list
    }).reset_index()

    # Extracting the first element from each list
    grouped_data['title'] = grouped_data['title'].apply(lambda x: x[0])
    grouped_data['Country_Code'] = grouped_data['Country_Code'].apply(lambda x: x[0])
    grouped_data['attributes'] = grouped_data['attributes'].apply(lambda x: x[0])

    return grouped_data
   

# akas = load_akas_part3(part3_path)
# print(akas.head(50))
# print(akas.isnull().sum())
# print(akas.info())

def load_akas_part4(part4_path):
    part4_data = pd.read_csv(part4_path, on_bad_lines='skip', low_memory=False) 
    data4 = part4_data.rename(columns={'titleId': 'tconst', 'region': 'Country_Code'})
    data4.replace('\\N', np.nan, inplace=True)
    data4.dropna(inplace=True)

    grouped_data = data4.groupby('tconst').agg({
        'title': list,
        'Country_Code': list,
        'attributes': list
    }).reset_index()

    # Extracting the first element from each list
    grouped_data['title'] = grouped_data['title'].apply(lambda x: x[0])
    grouped_data['Country_Code'] = grouped_data['Country_Code'].apply(lambda x: x[0])
    grouped_data['attributes'] = grouped_data['attributes'].apply(lambda x: x[0])

    return grouped_data
   

# akas = load_akas_part4(part4_path)
# print(akas.head(50))
# print(akas.isnull().sum())
# print(akas.info())


