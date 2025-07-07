#!/bin/bash

#SBATCH --job-name=extract-form-3-batch
#SBATCH --output=logs/extract-batch-%j.out
#SBATCH --time=01:00:00
#SBATCH --mem=4G
#SBATCH --cpus-per-task=1
#SBATCH --mail-type=ALL
#SBATCH --mail-user=your_email@stanford.edu

# Navigate to your project
cd /zfs/projects/darc/rf_bootcamp_2025/exercises

# Activate virtual environment
source venv/bin/activate

# Run the python script
python scripts/extract_form_3_batch.py
