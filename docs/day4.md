---
title: Day 4 -- Running and Scaling Cluster Jobs
layout: page
nav_order: 4
updateDate: 2025-06-18
---


# {{ page.title }}

## Recap: Day 3

Yesterday, we learned about: 
* Creating and _sharing_ reproducible Python environments;
* How resources are shared on the Yens cluster;
* How to submit jobs to the Yens scheduler (via SLURM); 

<!-- Take a quick poll: was yesterday too fast, too slow? -->

## Day 4 Learning Goals: 

We want to close the loop on what we've learned and finish laying the foundations for you to become power users of Stanford GSB's computing resources. 
So far, we've learned: 
* How to use the command line;
* What "paths" are;
* How to use Jupyter notebooks and write Python scripts;
* How to interact with APIs; and 
* How to submit simple jobs to the Yens cluster.

Today, we're going to cover: 
* Best practices for organizing your code;
* How to handle jobs ending unexpectedly, _without losing all of your work_; 
* Scaling up jobs on the Yens and running things in parallel; and
* How to document your work and retrieve results from the Yens onto your laptop.

> [!IMPORTANT]  
> Before we continue, let's take the pulse of the class. With a show of hands, was yesterday's class a) too fast, b) too slow, or c) about right?

## Review: Submitting Batch Jobs on the Yens

We noticed that some people got stuck on the last part of yesterday's class, so we're going to review this before moving on to newer topics. 

Remember, we wanted to write a `.slurm` script that runs our Python script on the Yens and saves its output to an output file (ending in `.out`).
Let's walk through together: 
1. First, `ssh` onto the Yens.
2. Navigate to the `exercises` subdirectory of the repository you "cloned" (i.e. downloaded) yesterday. You should be able to get there by running the following in your home directory:
```bash
cd rf_bootcamp_2025/exercises
```

<!-- 3. **If you didn't do so yesterday**, create a directory from `rf_bootcamp_2025/exercises` called `slurm`: 
```bash
mkdir slurm
``` -->

3. **Inside** the `slurm` directory, create a SLURM script called `my_first_slurm_script.slurm` that we'll use to run code **non-interactively** on the Yens. If you're in Jupyter, you can do this by creating a file using the graphical user interface. Alternately, you can run the following from within the `slurm` directory you just created.
```bash
touch my_first_slurm_script.slurm
```


> [!IMPORTANT]  
> Who can tell me the difference between the interactive and non-interactive nodes on the Yens?

4. Populate your `.slurm` script with the following content (remember to update the line with `--mail-user` with your Stanford email address): 

<!-- TODO: Figure out the correct file structure here -->
```bash
#!/bin/bash
#SBATCH --job-name=my-first-job
#SBATCH --output=logs/my-first-job-%j.out
#SBATCH --time=00:10:00
#SBATCH --mem=4GB
#SBATCH --cpus-per-task=1
#SBATCH --mail-type=ALL
#SBATCH --mail-user=<insert-your-email>@stanford.edu

# Navigate to your project
cd $HOME/rf_bootcamp_2025/exercises

# Activate your virtual environment 
source venv/bin/activate

# Call the main Python script we want to run 
python scripts/extract_form_3_one_file.py
```

> [!IMPORTANT]  
> Can someone explain to me what each section here does?

5. Create a `logs` subdirectory **within** your `slurm` directory. We'll save the outputs from our SLURM jobs to this `logs` subdirectory so we can verify the job's outputs if it ran successfully (or else see where it went wrong).
6. We're now ready to submit our job to the Yens via SLURM. To do so, run 
```bash
sbatch my_first_slurm_script.slurm
```
Navigate to the `logs` subdirectory and inspect the output file (either in Jupyter, or in the command line using `cat <insert-name-of-output-file>.out`). Once you've verified that the job ran successfully, please put a green sticky note (🟩) on the back of your laptop.

<!-- **If you need to clone the repository again**, run the snippet below _in your home directory_:
```bash
git clone https://github.com/gsbdarc/rf_bootcamp_2025.git
```
3. Activate the virtual environment you created yesterday:
```bash
source venv/bin/activate
```
**If you need to create your virtual environment again**, run: 
```bash
/usr/bin/python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
``` -->

### Common Pitfalls We Saw

What's wrong with the following SLURM script? There are at least four issues; let's find them together.

```bash
#!/bin/bash
#SBATCH --job-name=my-first-job
#SBATCH --output=logs/my-first-job.out/%j
#SBATCH --time=00:10:00
#SBATCH --mem=4GB
#SBATCH --cpus-per-task=1
#SBATCH --mail-type=ALL
#SBATCH --mail-user=<insert-your-email>@stanford.edu

# Navigate to your project
cd rf_bootcamp_2025/

# Activate your virtual environment 
source venv/bin/activate

# Call the main Python script we want to run 
python extract_form_3_one_file.py
```

## Organizing Projects

We saw in the previous example that paths are really important, and that they can be easy to get wrong. But note that the previous example was just small-scale! In practice, many of you will be interfacing with much larger codebases in your research, making this problem potentially more severe.

What are some ways we can make projects easy to navigate, understand, and keep tidy? 

> [!IMPORTANT]  
> Remember: Understanding your past self's work can be as difficult as understanding someone else's work.

Consider the following set of files (taking from our `rf_bootcamp_2025/exercises` subdirectory): 
```bash 
extract_form_3_one_file.py
form_3_10.csv
extract_form_3_one_file_broken.slurm
fix_me_2.slurm
requirements.txt 
fix_me_3.slurm
README.md
fix_me.slurm
extract_form_3_one_file_broken.py
mystery_script.py
my-first-job-20425.out
```
How would you organize them? 

> [!NOTE]
> Note that there is no one "correct" way to organize a project. But there _are_ good conventions.
<!-- 
Here is a directory structure for this project:

```
exercises/
│
├── data/
│   └── form_3_10.csv        # Input file to process
│
├── results/                 # Processed outputs go here
│   └── parsed_form3.json
│
├── scripts/
│   ├── extract_form_3_one_file.py
│   ├── extract_form_3_batch.py
│   ├── extract_form_3_batch_checkpoint.py
│   └── extract_form_3_onefile_array.py
│
├── slurm/
│   ├── extract_form_3_one_file.slurm
│   ├── extract_form_3_batch.slurm
│   ├── extract_form_3_batch_checkpoint.slurm
│   ├── extract_form_3_array.slurm
│   │
│   └── logs/                      # Slurm logs directory
│       ├── extract-one-file-758543.out
│       ├── extract-batch-checkpoint-758547.out
│       └── extract-form-3-758549_0.out 
│
├── venv/                  # Virtual environment
├── requirements.txt       # Python dependencies
└── README.md              # Short project documentation
``` -->

## Scaling Up Our Workloads 
So far, we've asked you to write code to extract information from a single SEC file. But what if constructing a dataset for your advisor requires extracting information from 100s, or 1000s?

Let's go back to a variant of the task we gave you on Day 2. 
We're given the URL to an SEC Form 3 filing, and we want to determine if the filing has anything to do with the pharmaceuticals industry. 

```python
import os
import requests
import pandas as pd

# URL to your filing
filing_url = "https://rf-bootcamp-2025.s3.us-west-2.amazonaws.com/Form3_files/0000003570-22-000041.txt"

# Request the filing from the URL
response = requests.get(filing_url)

# Get the text from the filing request response
filing_text = response.text

# Check if the filing is relevant to the pharmaceuticals industry
if "pharma" in filing_text.lower():
    print(f"Filing at {filing_url} relates to the pharma industry.")
```

**Questions for you:**
1. How is this script useful, even if it doesn't let us extract information from more than one SEC filing?
2. How do we need to change it to process multiple files?
3. Imagine you want to submit our modified Python script to run non-interactively on the Yens? Do we need to change our SLURM script, and how?
4. What might go wrong with our modified Python script? Are we using all the computing resources available to us?

Run the modified script. What happens?


### Single File Processing for Testing and Debugging

- Script: `extract_form_3_one_file.py`
- Slurm job: `extract_form_3_one_file.slurm`
- Processes one file.
- Great for testing your code and debugging errors.

Excercise: 

- Discuss what happens if you need to process 1,000 files.

### Sequential Processing: One Job Handles Many Files

- Script: `extract_form_3_batch.py`
- Slurm job: `extract_form_3_batch.slurm`
- Loop over multiple files inside one Python job.

Exercise: 

- Discuss what happens if the job fails partway through.

### Checkpointing for Fault Tolerance

- Script: `extract_form_3_batch_checkpoint.py`
- Slurm job: `extract_form_3_batch_checkpoint.slurm`
- Adds checkpointing logic: tracks completed files and resumes on failure.
- A common pattern for long-running research jobs.

Exercise:

- Simulate a failure by forcing the job to stop after a few files.
- Restart the job and verify it skips already completed files.


### Parallel Processing with Slurm Job Arrays
- Script: `extract_form_3_onefile_array.py`
- Slurm job: `extract_form_3_array.slurm`
- Uses Slurm job arrays to process files independently and in parallel.
- Highly efficient for large datasets.

Exercise:

- Discuss how to aggregate results.
- Discuss the limitations of job arrays on Yen-Slurm.
- Discuss the limitations of file system on the Yens.

### Copy Results and Document Your Work
Exercise:
 
- Use `scp` to copy your `results` directory back to your laptop.
- Write a short `README.md` describing:

  - What the pipeline does
  - How it runs (Slurm + Python)
  - Where the results go
  - How to rerun it with new data
