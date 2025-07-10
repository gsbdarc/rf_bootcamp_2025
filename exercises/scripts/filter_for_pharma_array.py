import os
import sys
import json
import requests
import pandas as pd

# Specify which directory we're working from
PROJ_DIR = f"{os.getenv('HOME')}/rf_bootcamp_2025/exercises"
# Specify where to save our results
os.makedirs(f"{PROJ_DIR}/results/array", exist_ok=True)

# Load CSV with paths
csv_path = f"{PROJ_DIR}/data/aws_links.csv"
df = pd.read_csv(csv_path)

# Task ID is from Slurm
task_id = int(sys.argv[1])

# Write one output file per task
output_path = f"{PROJ_DIR}/results/array/pharma_relevant_filings_{task_id}.json"

# Select the row in df corresponding to `task_id`
row = df.iloc[task_id]
# Get the filing URL
filing_url = row["urls"]

# Request the filing
response = requests.get(filing_url)

# Get the text from the filing request response
filing_text = response.text

# Determine whether the filing is relevant to the pharmaceuticals industry
is_pharma_relevant = "pharma" in filing_text.lower()

# Use full filing_url as key
filing_key = filing_url

result = {filing_key: {"is_pharma_relevant": is_pharma_relevant}}

with open(output_path, "w") as f:
    json.dump(result, f, indent=2)

print(f"Saved result to {output_path}")
