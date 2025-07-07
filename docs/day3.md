---
title: Day 3 - Running Your First Cluster Jobs
layout: page
nav_order: 1
updateDate: 2025-06-20
---


# {{ page.title }}

## Objectives

- Monitor resources while running interactively

- Submit your first job to the cluster using Slurm

- Connect your code, environment, and input data into a runnable job

- Build mental models of how cluster resources are shared

Today we take your interactive work and transition it into Slurm cluster jobs. We'll also pause at several points to discuss how resources are allocated on a shared research cluster. 

### Conceptualizing Resources on a Shared Cluster

We'll whiteboard these concepts to build intuition:

- CPUs (Cores): How many cores are available? How many does your job actually use?

- RAM (Memory): How much memory does your job need?

- GPU (if applicable): Specialized resource for certain tasks.

- Time: How long will your job run? What happens if it runs too long?

- Quota (Storage Space Limits): How much disk space do you have for your files, and where?

- Notebook Limits / Interactive Yen Limits: Interactive sessions have lower resource caps compared to batch jobs.

### Recap: Running Code Interactively

- You already have a Python script that calls an API and processes one file.

- You've tested it interactively using your virtual environment.

Exercise:

- Run your script again interactively while monitoring CPU and RAM usage with `top` or `htop` and `userload`.

- How much RAM and CPU does your job actually need?

- Discuss: What would happen if you ran 100 of these in parallel?

### Submitting Your First Slurm Job
Submitting Your First Slurm Job:
Exercise:

- Write and submit your own Slurm job.

- Check job status with `squeue`.

- View logs in your `logs/` directory.

- Verify results are generated correctly.


### Debugging and Iterating on Cluster Jobs

- What happens if your job crashes?

- What information is in the Slurm log files?

- How do you rerun failed jobs?

Exercise:

- Intentionally break your job (e.g., wrong file name) and review logs.

- Fix and resubmit.


### Organizing Your Research Project
Project structure best practices:

```
project-name/
│
├── data/         # Input data files
├── results/      # Output files
├── scripts/      # Code/scripts
├── slurm/        # Slurm job submission scripts
├── venv/         # Virtual environment 
├── requirements.txt  # Dependencies
└── README.md     # Project documentation
```

