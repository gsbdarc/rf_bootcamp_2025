#!/bin/bash

#SBATCH --job-name=extract-form-3-checkpoint
#SBATCH --output=extract-batch-checkpoint-%j.out
#SBATCH --time=02:00:00
#SBATCH --mem=8G
#SBATCH --cpus-per-task=1

# Activate virtual environment
source ../venv/bin/activate

# Run the python script
python extract_form_3_batch_checkpoint.py
