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

    # Request the filing
    response = requests.get(filing_url)

    # Get the text from the filing request response
    filing_text = response.text

    print(f"[{idx+1}/{total_files}] Processing: {filing_url}")

    # If the filing is relevant to the pharmaceuticals industry, proceed
    if "pharma" in filing_text.lower():

        # Use full filing_url as key
        filing_key = filing_url

        # Save url corresponding to pharma-relevant filing
        master_data[filing_key] = filing_url

print("All filings processed. Writing output...")
with open(master_json_path, "w") as f:
    json.dump(master_data, f, indent=2)
print(f"Saved result to {master_json_path}.")
