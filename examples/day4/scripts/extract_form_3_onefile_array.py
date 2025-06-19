import os
import sys
import json
import pandas as pd
from openai import OpenAI
from pydantic import BaseModel
from typing import List
from dotenv import load_dotenv

# Load environment variables
load_dotenv("/zfs/projects/darc/rf_bootcamp_2025/.env")
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

PROJ_DIR = "/zfs/projects/darc/rf_bootcamp_2025"
os.makedirs(f"{PROJ_DIR}/results/array", exist_ok=True)

# Model
class Form3Filing(BaseModel):
    insider_name: str
    insider_role: List[str]
    company_name: str
    company_cik: str
    filing_date: str

# System prompt
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

# Task ID is from Slurm 
task_id = int(sys.argv[1])

# Write one output file per task
output_file = f"{PROJ_DIR}/results/array/parsed_form3_{task_id}.json"

# Load CSV with paths
csv_path = f"{PROJ_DIR}/data/form_3_10.csv"
df = pd.read_csv(csv_path)

# Select the specific row
row = df.iloc[task_id]
filing_path = row["filepath"]
filing_key = filing_path

with open(filing_path, "r") as f:
    filing_text = f.read()

response = client.responses.parse(
    model="o4-mini",
    input=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": filing_text}
    ],
    text_format=Form3Filing,
)

filing = response.output_parsed
result = {filing_key: filing.model_dump()}

with open(output_file, "w") as f:
    json.dump(result, f, indent=2)

print(f"Saved result to {output_file}")

