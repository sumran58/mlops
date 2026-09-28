import pandas as pd
import os

data = {
    'Name': ['alice', 'bob', 'charlie'],
    'age': [24, 25, 26],
    'city': ['ratnagiri', 'mumbai', 'pune']
}

df = pd.DataFrame(data)

# Get the folder where mycode.py is located
base_dir = os.path.dirname(os.path.abspath(__file__))

# Create data folder inside dvc_data_versioning
data_dir = os.path.join(base_dir, 'data')

os.makedirs(data_dir, exist_ok=True)

file_path = os.path.join(data_dir, 'sample_data.csv')

df.to_csv(file_path, index=False)

print(f"CSV file saved to the path: {file_path}")