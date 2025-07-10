import os
import requests
import pandas as pd

# URL to your filing
filing_url = "https://rf-bootcamp-2025.s3.us-west-2.amazonaws.com/Form3_files/0000003570-22-000041.txt"

# Request the filing
response = requests.get(filing_url)

# Get the text from the filing request response
filing_text = response.text

# Check if the filing is relevant to the pharmaceuticals industry
if "pharma" in filing_text.lower():
    print(f"Filing at {filing_url} relates to the pharma industry.")
