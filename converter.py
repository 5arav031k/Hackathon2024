import pandas as pd
import chardet
import os

def convert_file_to_json(file_path) -> str:
    try:
        file_extension = os.path.splitext(file_path)[1].lower()

        if file_extension == '.csv':
             with open(file_path, 'rb') as file:
                encoding_type = chardet.detect(file.read())
                data = pd.read_csv(file_path, encoding=encoding_type['encoding'])
        elif file_extension in ['.xls', '.xlsx']:
            data = pd.read_excel(file_path)
        elif file_extension == '.parquet':
            data = pd.read_parquet(file_path)
        elif file_extension in ['.h5', '.hdf5']:
            data = pd.read_hdf(file_path)
        else:
            raise ValueError("Unsupported file format.")

        data_json = data.to_json(orient="records", indent=4)
        return data_json
    except FileNotFoundError:
        print(f"File {file_path} not found. Turn the file over and try again.")
    except Exception as e:
        print(f"An error occurred: {e}")