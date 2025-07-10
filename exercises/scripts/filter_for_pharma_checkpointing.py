import os
import json
import requests
import pandas as pd

# Specify which directory we're working from
PROJ_DIR = f"{os.getenv('HOME')}/rf_bootcamp_2025/exercises"
# Specify where to save our results
os.makedirs(f"{PROJ_DIR}/results", exist_ok=True)

# Specify our output file path (single master file)
master_json_path = f"{PROJ_DIR}/results/pharma_relevant_filings.json"

# Keep track of results file-by-file
# If version of output already exists, load existing (intermediate) output
if os.path.exists(master_json_path):
    with open(master_json_path, "r") as f:
        master_data = json.load(f)
else:
    master_data = {}

# Load CSV with paths
csv_path = f"{PROJ_DIR}/data/aws_links.csv"
df = pd.read_csv(csv_path)

total_files = len(df)
print(
    f"Starting looking for pharma-relevant filings among {total_files} total filings..."
)

# Iterate through each filepath
for idx, row in df.iterrows():
    # Get the URL corresponding to the filing
    filing_url = row["urls"]

    # Use full filing_url as key
    filing_key = filing_url

    if filing_key in master_data:
        print(f"[{idx+1}/{len(df)}] Skipping already processed: {filing_key}")
        continue

    # Request the filing
    response = requests.get(filing_url)

    # Get the text from the filing request response
    filing_text = response.text

    print(f"[{idx+1}/{total_files}] Processing: {filing_url}")

    # Determine whether the filing is relevant to the pharmaceuticals industry
    is_pharma_relevant = "pharma" in filing_text.lower()

    # Save url corresponding to pharma-relevant filing
    master_data[filing_key] = {"is_pharma_relevant": is_pharma_relevant}

    print(f"Processed {filing_key}")
    with open(master_json_path, "w") as f:
        json.dump(master_data, f, indent=2)
print(f"Saved result to {master_json_path}.")
