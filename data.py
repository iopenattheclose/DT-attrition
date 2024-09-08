import dill
import pandas as pd
import os

def store_data(input_file_path, output_file_path):
    try:
        if input_file_path.endswith(".csv"):
            df = pd.read_csv(input_file_path)
            with open(output_file_path, 'wb') as f:
                dill.dump(df, f)
        print("Data stored successfully as dill file.")
    except Exception as e:
        print("Error reading or storing data:", e)



if __name__ == "__main__":
    store_data("data/employee-attrition.csv", "data/employee-attrition.dill")