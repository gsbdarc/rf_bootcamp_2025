#!/bin/bash

#SBATCH --job-name=extract-form-3-array
#SBATCH --output=extract-form-3-%A_%a.out
#SBATCH --array=0-9
#SBATCH --time=02:00:00
#SBATCH --mem=8G
#SBATCH --cpus-per-task=1

# Activate virtual environment
source ../venv/bin/activate

# Run the python script
python extract_form_3_onefile_array.py ${SLURM_ARRAY_TASK_ID}
