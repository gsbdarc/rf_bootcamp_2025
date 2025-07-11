---
title: Day 3 — Running Your First Cluster Job
layout: page
nav_order: 3
updateDate: 2025-07-08
---


# {{ page.title }}

## Objectives

- Monitor Yen resources while running interactively

- Connect your code, environment, and input data into a runnable job

- Build mental models of how cluster resources are shared

- Submit your first job to the cluster using Slurm

Today we take your interactive work and transition it into Slurm cluster jobs. We'll also pause at several points to discuss how resources are allocated on a shared research cluster. 

## Day 2 Recap

What have we learned so far:

- Made a virtual environment that can be run on the Yens as a kernel or interactively 
- Made a python script that calls OpenAI API to extract key pieces of information from one Form 3 filing
- Talked about LLM structured outputs and how useful they are


Let's start by downloading some scripts to the Yens, making a new virtual env and running a python script to extract information from Form 3 using structured outputs.

---

A legend we will use:
- 💻: means "use terminal on the Yens"
- ✏️ : means "we will white board this"
- ❓: question for class
- 🟩/🟥: means "put up the colored sticky once you finish the exercise / ask for help"

### 💻 Exercise 0: Git Clone the Class Repo

- `ssh` to the yens

- Remove all kernels you made and folders you copied or made in Day 1 and Day 2

```
# activate old env that has jupyter installed
source <old-env>/bin/activate

# list kernels
jupyter kernelspec list

# uninstall kernel by name
jupyter kernelspec uninstall <kernel-name>

# deactivate venv 
deactivate

# cd to your home
cd

# clean up directories from Day 1 and Day 2
rm -r <folder-name>
```

- Copy a repo with exercises for Day 3:

```
git clone https://github.com/gsbdarc/rf_bootcamp_2025.git
```

- Navigate to the exercises directory and look at the `requirements.txt` file:

```
cd $HOME/rf_bootcamp_2025/exercises
cat requirements.txt
```

- 🟩/🟥

-❓ What is `requirements.txt` file? 

-❓ Why is it useful? 

### 💻 Exercise 1: Make a virtual environment (yes, again)

- Let's make a virtual environment from `requirements.txt`:

```
/usr/bin/python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

- 🟩/🟥

### 💻 Exercise 2: Run python script 

- Let's look at the script called `extract_form_3_one_file.py` inside `scripts` directory.

- ❓: What is the script doing?

- Run it using the virtual env you just made

- ❓: What do you see? 

- 🟩/🟥 

### ✏️  Conceptualizing Resources on a Shared Cluster
### Research Project

  - **What** am I doing?
  - **Where** am I doing it?
  - **How** am I doing it?  

### ✏️  Let us cook! 
Analogy: Research computing as a kitchen 

### ✏️  **Where** am I cooking?
- ❓: Pro's / con's
- Kitchen demo!

### ✏️  **How** am I cooking it? 

### 💻 Exercise 3: Run python script again 

- Run your script again interactively

- ❓: **Why** do you want to estimate the resources? 

- ❓: **How** do we estimate time it will take, cores and RAM we need for the script to run? 

### 💻 Exercise 4: Run a different python script
 
- Run `mystery_script.py` 

- While the script is running, on the same yen (in a second terminal), watch the script run while running `time`, `htop`, `htop -u $USER` `userload`

- Compare with your neighbor the time, cores and RAM usage 

- What do you see?

- 🟩/🟥

### ✏️  Interactive Yens

### ✏️  Yen-Slurm Cluster

### 💻  Exercise 5: Let's make a slurm script to run our research code to process one Form 3 file

- Make a new file in `slurm` directory called `extract_form_3_one_file.slurm`

- Make the first line to be:
  ```
  #!/bin/bash
  ```

- Add Slurm flags that request appropriate resources

  ```
  #SBATCH --job-name=<job-name>
  #SBATCH --output=<output-file.out>
  #SBATCH --time=<time>
  #SBATCH --mem=<RAM>
  #SBATCH --cpus-per-task=<cores>
  #SBATCH --mail-type=<alert-types>
  #SBATCH --mail-user=<your_email@stanford.edu>
  ```

- Activate venv we made
  ```
  # Navigate to your project
  cd $HOME/rf_bootcamp_2025/exercises

  # Activate virtual environment
  source venv/bin/activate
  ```

- Call python script
  ```
  python scripts/extract_form_3_one_file.py
  ```

- Save the file.

- 🟩/🟥

Discussion:

- `%j` in job name
- `log` directory for logs
- paths! (remember day 2?)

### 💻 Let's submit it:

```
sbatch slurm/extract_form_3_one_file.slurm
```

- Verify results are generated correctly

- Monitor the queue with `squeue` or `squeue -u $USER`

- Use `scancel <jobid>` if you need to cancel
 
- Verify results are generated correctly.

- 🟩/🟥

### 💻 Exercise 6: Debugging and Iterating on Cluster Jobs

- ❓ What happens if your job crashes?

- ❓ What information is in the Slurm log files?

- ❓ How do you rerun failed jobs?

- Submit `fix_me.slurm`, `fix_me_2.slurm`, or `fix_me_3.slurm`

- Look at logs

- Fix it and resubmit

- Bonus: debug `extract_form_3_one_file_broken.slurm` 

- 🟩/🟥

### Discussion

-❓ What will happen if you underestimate the time your script needs? 

-❓ What will happen if you overestimate the time your script needs? 

-❓ What will happen if you underestimate the CPU cores your script needs? 

-❓ What will happen if you overestimate the CPU cores your script needs? 

-❓ What will happen if you underestimate the RAM your script needs? 

-❓ What will happen if you overestimate the RAM your script needs? 
