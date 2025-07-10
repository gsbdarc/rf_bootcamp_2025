---
title: Day 4 — Running and Scaling Cluster Jobs
layout: page
nav_order: 4
updateDate: 2025-06-18
---


# {{ page.title }}

## Recap: Day 3

Yesterday, we learned about: 
* Creating and _sharing_ reproducible Python environments;
* How resources are shared on the Yens cluster;
* How to submit jobs to the Yens scheduler.

{: .note }
> Who can tell me about each of these?

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
* How to handle jobs ending unexpectedly; 
* Scaling up jobs on the Yens; and
* How to document your work and retrieve results from the Yens onto your laptop.

{: .note }
> Before we continue, let's take the pulse of the class. With a show of hands, was yesterday's class a) too fast, b) too slow, or c) about right?

**One other thing for you to note: we'd love to get your feedback on this mini-course. We'll be circulating a survey at the end; if you stay and fill it out, you'll be entered into a raffle for a $50 Coupa coffee gift card.**

## Review: Submitting Batch Jobs on the Yens

We noticed that some people got stuck on the last part of yesterday's class, so we're going to review this before moving on to newer topics. 

Remember, we wanted to write a `.slurm` script that runs our Python script on the Yens and saves its output to an output file (ending in `.out`).
Let's walk through together: 
* First, `ssh` onto the Yens.
* Navigate to the `exercises/slurm` subdirectory of the repository you "cloned" (i.e. downloaded) yesterday. You should be able to get there by running the following in your home directory:
```bash
cd rf_bootcamp_2025/exercises/slurm
```

* **Inside** the `slurm` directory, create a SLURM script called `my_first_slurm_script.slurm` that we'll use to run code **non-interactively** on the Yens. If you're in Jupyter, you can do this by creating a file using the graphical user interface. Alternately, you can run the following from within the `slurm` directory:
```bash
touch my_first_slurm_script.slurm
```


{: .note }
> Who can tell me the difference between the interactive and non-interactive nodes on the Yens?

* If you didn't yesterday, create a `log` directory in which we'll write output files from our SLURM scripts (we use these to see whether a job ran as expected):
```bash 
mkdir logs
```

* Populate your `.slurm` script with the following content (remember to update the line with `--mail-user` with your Stanford email address): 

```bash
#!/bin/bash
#SBATCH --job-name=my-first-job
#SBATCH --output=logs/my-first-job-%j.out
#SBATCH --time=00:10:00
#SBATCH --mem=4GB
#SBATCH --cpus-per-task=1
#SBATCH --mail-type=ALL
#SBATCH --mail-user=<insert-your-email>@stanford.edu

cd $HOME/rf_bootcamp_2025/exercises

source venv/bin/activate

python scripts/extract_form_3_one_file.py
```

{: .note }
> Can someone explain to me what each section here does?


* We're now ready to submit our job to the Yens via SLURM. To do so, run 
```bash
sbatch my_first_slurm_script.slurm
```
Navigate to the `logs` subdirectory and inspect the output file (either in Jupyter, or in the command line using `cat <insert-name-of-output-file>.out`). Once you've verified that the job ran successfully, please put a green sticky note 🟩 on the back of your laptop.

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

{: .important }
> Remember: Understanding your past self's work can be as difficult as understanding someone else's work. Make it easy for yourself and others.

Consider the following set of files (taken from our `rf_bootcamp_2025/exercises` subdirectory): 
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

{: .note }
> There is no one "correct" way to organize a project. But there _are_ good conventions.

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

filing_url = "https://rf-bootcamp-2025.s3.us-west-2.amazonaws.com/Form3_files/0000003570-22-000041.txt"

response = requests.get(filing_url)

filing_text = response.text

if "pharma" in filing_text.lower():
    print(f"Filing at {filing_url} relates to the pharma industry.")
```

{: .note }
> Can someone walk us through what this file is doing?

**Questions for you:**
* How is this script useful, even if it doesn't let us extract information from more than one SEC filing?
* What might be one way to change our script so that it processes multiple files? **Let's write out the modifications in pseudocode.**
* Imagine you want to submit our modified Python script to run non-interactively on the Yens? Do we need to change our SLURM script, and how?
<!-- 4. What might go wrong with our modified Python script? Are we using all the computing resources available to us? -->

{: .note }
> Let's talk about this together, live.

Let's run the modified script. What happens?

### Building In Fault Tolerance

In a script like the one we wrote above, if something fails, we lose all our progress.
That's OK in our toy example, but imagine you had a job that had been running for a week before failing. That's a lot of lost time and progress.

* How might we avoid that outcome? **There are three main things we can think about.**
* What happens when we run our modified script?

{: .note }
> Let's talk about this together, live.

What happens when we run our modified script?

### Moving On From Sequential Processing

Let's recap what we've done so far today:
* We started with a script that operates on a **single** SEC filing.
* We generalized that script to handle **multiple** SEC filings.
* We made the script more **robust** to unexpected errors.

<!-- TODO: Is Python capitalized? -->
However, our code and workflow can still be improved. What's less-than-optimal about our Python script? 
* Are we using the Yens' resources effectively?
* Does our problem have a common structure we can exploit?

{: .note }
> Let's talk about this together, live. We'll draw a graphic to illustrate what we can do differently.

Now let's look at an example script that addresses these points.
We'll need two components: an **adapted** Python script, and a corresponding SLURM script.

{: .important }
> Using arrays on the Yens has a lot of advantages:
> * We can maximally exploit the large number of cores on the Yens and finish our work faster;
> * Since each array job is entirely independent from the others, we still get the same result.
> 
> However, using arrays is **not** a silver bullet: 
> * In our example, we assumed we have one array job per filing URL. In practice, it may be more efficient to process several URLs together for one individual array job.
> * As we've written it, our code spits out one output file per array job. In practice, you still need to combine these into one single data output, ideally using an additional script you'll have to write.

## Sharing Your Work & Results

OK! We've now processed a bunch of SEC filings, and have determined for each one whether it relates to the pharmaceuticals industry. 

{: .note }
> What's left for us to do?

### Copying Results

To make things easy for you, we've put the results from processing our SEC filings on a shared folder on the Yens:
```bash
/scratch/shared/rf_bootcamp_2025/pharma_relevant_filings.json
```
You want to copy these results onto your local machine to share the results with your advisor. How do you do it?

{: .tip }
> Remember: Where do we run commands for copying from?

### Communicating Your Work

Finally, your advisor (who hasn't been keeping up with your progress, alas) wants to understand the code you've written, to make sure that everything makes sense.

We've already created a `README.md` document for you to edit in the repository you cloned yesterday.
Your job is to edit that document, and fill in the following details so it's easy for your advisor (or your future self) to understand your work:
* What does your SEC filing pipeline do?
* How can someone run it?
* Where are the results are saved?
* If we get new SEC filings data, how should someone update and re-run the pipeline?

When you're done, please put a green sticky note 🟩 on the back of your laptop so we know you're done. 

## Open-Ended Question Round

We've now walked through four days of material. Are there any lingering questions you still have? Please share — there's a good chance you're not the only one wondering.

## Feedback

We'd love your feedback: what was good, what could we have done better. Please fill out the survey [here](https://docs.google.com/forms/d/1rH-7m3rYdcZxp8QHTLXzgUwteQzvygLWd_MGYEO74xE/edit). 

If you complete it, we'll enter you into a raffle for a $50 Coupa coffee gift card.
