---
title: Running and Scaling Cluster Jobs
layout: page
nav_order: 1
parent: Day 4
updateDate: 2025-06-18
---


# {{ page.title }}

## Day 4 Objectives

- How do you structure and document reproducible, scalable work on a cluster?

- How do you rerun your pipeline when new data arrives without repeating completed work?

- How do you document your process and retrieve results back to your local machine?

On Day 4, we'll build up from a simple data extraction task to more scalable cluster workflows. This is also a perfect moment to reinforce good project organization practices you should follow in your research projects.

### Example Project Directory

Here is a directory structure for this project:

```
project_root/
│
├── data/
│   └── input/
│       └── form_3_10.csv        # Input file to process
│
├── results/                      # Processed outputs go here
│   └── (generated output files)
│
├── scripts/
│   ├── extract_form_3_one_file.py
│   ├── extract_form_3_batch.py
│   ├── extract_form_3_batch_checkpoint.py
│   ├── extract_form_3_onefile_array.py
│   └── utils.py          # (shared functions if needed)
│
├── slurm/
│   ├── extract_form_3_one_file.slurm
│   ├── extract_form_3_batch.slurm
│   ├── extract_form_3_batch_checkpoint.slurm
│   └── extract_form_3_array.slurm
│
├── logs/
│   ├── extract-one-file-758543.out
│   ├── extract-batch-checkpoint-758547.out
│   ├── extract-form-3-758549_0.out
│   └── ...
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
