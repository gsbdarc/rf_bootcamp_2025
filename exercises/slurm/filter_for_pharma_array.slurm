#!/bin/bash

# Example of running python script as a job array

#SBATCH --job-name=parallelized-pharma
#SBATCH --array=0-9
#SBATCH --cpus-per-task=1
#SBATCH --time=00:10:00
#SBATCH --output=logs/parallelized-pharma-%A-%a.out
#SBATCH --mail-type=ALL
#SBATCH --mail-user=<insert-your-email>@stanford.edu

# Navigate to your project
cd $HOME/rf_bootcamp_2025/exercises

# Activate your virtual environment 
source venv/bin/activate

# Call the main Python script we want to run 
python scripts/filter_for_pharma_array.py $SLURM_ARRAY_TASK_ID