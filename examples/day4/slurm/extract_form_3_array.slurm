#!/bin/bash

#SBATCH --job-name=extract-form-3-array
#SBATCH --output=logs/extract-form-3-%A_%a.out
#SBATCH --array=0-9
#SBATCH --time=01:00:00
#SBATCH --mem=4G
#SBATCH --cpus-per-task=1
#SBATCH --mail-type=ALL
#SBATCH --mail-user=your_email@stanford.edu

# Navigate to your project
cd /zfs/projects/darc/rf_bootcamp_2025

# Activate virtual environment
source venv/bin/activate

# Run the python script
python scripts/extract_form_3_onefile_array.py ${SLURM_ARRAY_TASK_ID}
