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
* How to document your work and retrieve code outputs from the Yens onto your laptop.

## Review: Submitting Batch Jobs on the Yens

We noticed that some people got stuck on this step yesterday, so we're going to review the last part of yesterday's class before moving on to newer topics. 
Let's walk through together: 
1. Something 
2. Something else 
3. TBD.












## Day 4 Learning Goals

Today is our last day! Hopefully you'll agree that we've already learned a lot: how to use the command line, what paths are, how to use Jupyter notebooks, interact with APIs, and submit simple jobs to the Yens computing cluster. 

We want to end by getting you another step closer to being a Stanford GSB computing power user. To do this, we're going to talk about the following:

- How to structure and document reproducible, scalable work on a cluster;

- How to re-run your data pipeline when new data arrives, without repeating completed work;

- How to document your work and retrieve results back to your local machine.

We'll build up from a simple data extraction task to more scalable cluster workflows. This is also a good moment to reinforce good project organization practices you should follow in your research projects.

### Example Project Directory

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
```


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
