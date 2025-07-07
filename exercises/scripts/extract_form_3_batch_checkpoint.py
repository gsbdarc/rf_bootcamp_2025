import os
import json
import pandas as pd
from openai import OpenAI
from pydantic import BaseModel
from typing import List
from dotenv import load_dotenv

# Load environment variables (your API key)
load_dotenv("/zfs/projects/darc/rf_bootcamp_2025/.env")
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

PROJ_DIR = "/zfs/projects/darc/rf_bootcamp_2025/exercises"
os.makedirs(f"{PROJ_DIR}/results", exist_ok=True)

# Output file path (single master file)
master_json_path = f"{PROJ_DIR}/results/parsed_form3.json"

# Load existing checkpoint if exists
if os.path.exists(master_json_path):
    with open(master_json_path, "r") as f:
        master_data = json.load(f)
else:
    master_data = {}

# Pydantic model for parsing
class Form3Filing(BaseModel):
    insider_name: str
    insider_role: List[str]
    company_name: str
    company_cik: str
    filing_date: str

# The system prompt for GPT extraction
system_prompt = """
You are a data extraction agent for SEC Form 3 filings.

Extract the following fields:

- insider_name: The name of the insider (from reportingOwner or anywhere in the document).
- insider_role: A list of roles the insider holds (Director, Officer, 10% Owner, Other).
- company_name: The issuer's company name.
- company_cik: The CIK number of the issuer (from issuerCik or COMPANY DATA).
- filing_date: The filing date (prefer signatureDate or FILED AS OF DATE).

Return valid JSON matching the provided Pydantic model.
"""

# Load CSV with paths
csv_path = f"{PROJ_DIR}/data/form_3_10.csv"
df = pd.read_csv(csv_path)

total_files = len(df)
print(f"Starting extraction for {total_files} filings...")

# Iterate through each filepath
for idx, row in df.iterrows():
    filing_path = row["filepath"]

    # Use full filing_path as key
    filing_key = filing_path

    if filing_key in master_data:
        print(f"[{idx+1}/{len(df)}] Skipping already processed: {filing_key}")
        continue

    print(f"[{idx+1}/{total_files}] Processing: {filing_path}")

    with open(filing_path, "r") as f:
        filing_text = f.read()

    # Run GPT extraction
    response = client.responses.parse(
            model="o4-mini",
            input=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": filing_text}
            ],
            text_format=Form3Filing,
        )

    filing = response.output_parsed

    # Store result
    master_data[filing_key] = filing.model_dump()

    print(f"Processed {filing_key}")
    with open(master_json_path, "w") as f:
        json.dump(master_data, f, indent=2)
print(f"Saved result to {master_json_path}.")
