---
title: Day 2 — Working on the Yens Cluster with JupyterHub
layout: page
nav_order: 2
updateDate: 2025-06-17
---

# {{ page.title }}

## Learning Goals
By the end of today you will be able to

- understand what a "path" is and why it matters

- create and activate **Python virtual environments** on Yens;

- understand how a virtual environment can assist with reproducible code

- open and run **Jupyter notebooks** in JupyterHub;

- understand how to manage passwords and other "secrets" in your code

- Run API calls to OpenAI from JupyterHub.



---

### Exercise 0: Log in using `ssh`

Open a local terminal and use `ssh` to connect to the Yens.

- What server are you on?
- What directory are you in?
- What files are in your current directory?
- Do you see the files from yesterday?

### Exercise 1: Accessing JupyterHub

##### 1: Open the Hub

Choose any of the following links to access JupyterHub on the Yens cluster:

- [Yen1](https://yen1.stanford.edu/jupyter/hub/home)
- [Yen2](https://yen2.stanford.edu/jupyter/hub/home)
- [Yen3](https://yen3.stanford.edu/jupyter/hub/home)
- [Yen4](https://yen4.stanford.edu/jupyter/hub/home)
- [Yen5](https://yen5.stanford.edu/jupyter/hub/home)

You should see the folders you created on the previous day, including your exercise notebooks.

##### 2: Start a New Notebook and Terminal
- Click the **blue “+”** to open a **Python 3 notebook**.

- Click the **Terminal** icon to launch a shell (we’ll use it for environment commands).


#### Exercise 1.1 -First Notebook Cells

Copy each of the following into separate cells in your notebook, then run them using `Shift + Enter.`

```python
# Print "Hello, World!"
print("Hello, World!")  
# Import the math module and print the value of pi
```

```python
# Use the math module
import math
print(math.pi)
```

```python
numbers = [1, 2, 3, 4, 5]
print(sum(numbers))
```



#### Exercise 1.2 — Jupyter Terminal Basics

Open the terminal tab you started above and try:

```bash
# List files in your home directory
ls

# navigate into your pokemon_images directory
cd technical_data_important

# List files in the pokemon_images directory
ls

# Find out which python version you are using
which python3
```

#### Exercise 1.3: — Display a Pokémon Image

1. Locate any PNG in your images folder (use the file browser or ls). 

{: .tip}
>You can double click on it to view it natively in JupyterHub.

2. Replace /path/to/your/pokemon_image.png below with that full path.

```python
from PIL import Image
from IPython.display import display      
# Load and display a Pokémon image
img_path = '/path/to/your/pokemon_image.png'  # Replace with your image
img = Image.open(img_path)
display(img)
```

#### Exercise 1.4: — Manipulate an image on the terminal

1. Let's manipulate an image on the terminal using a tool called `imagemagick`.

Go to your terminal and type:

```bash
module load imagemagick
```

Pick the Pokemon you displayed above and flip it upside down like this:

```bash
magick /path/to/your/pokemon_image.png -flip /path/to/your/output_image.png
```

2. Did it work? Go check in your notebook.

3. Type the following command in your terminal:

```bash
which magick
```

Does it look the same as when you did `which python3`? 

<!-- 
Note: If you get an error about the library not being installed, you can install it in your terminal with:

```bash
pip install matplotlib
``` -->

<!-- ### Exercise 1.4 - Counts by Primary Type

In this exercise, we'll create a **bar chart** showing the count of Pokémon by their **primary type**, and then prompt you to think about how to visualize Pokémon images based on their **secondary type.**

#### Install libraries (one-time)

```bash
# In your terminal window, run:
pip install pandas seaborn matplotlib   
```
#### Notebook Code

```python

import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

type_colors = {
    'Water':    '#6890F0', 'Normal':  '#A8A878', 'Grass':   '#78C850',
    'Bug':      '#A8B820', 'Psychic': '#F85888', 'Fire':    '#F08030',
    'Electric': '#F8D030', 'Poison':  '#A040A0', 'Ground':  '#E0C068',
    'Dark':     '#705848', 'Fighting':'#C03028', 'Dragon':  '#7038F8',
    'Ghost':    '#705898', 'Steel':   '#B8B8D0', 'Ice':     '#98D8D8',
    'Fairy':    '#EE99AC', 'Flying':  '#A890F0', 'none':    '#CCCCCC'
}

oslist = os.listdir('/path/to/your/pokemon_images')  # Replace with your image directory

type_list = []
for filename in oslist:
    if filename.endswith('.png'):
        file_parts = filename.split('_')
        name, primary_type, secondary_type, evolution = file_parts
        type_list.append((name, primary_type, secondary_type, evolution))
# Create a DataFrame from the list
df = pd.DataFrame(type_list, columns=['name', 'primary_type', 'secondary_type', 'evolution'])


type_counts = df['primary_type'].value_counts().reset_index()
type_counts.columns = ['primary_type', 'count']

# Match colors to each type
colors = type_counts['primary_type'].map(type_colors)

# Plot
plt.figure(figsize=(12, 6))
sns.barplot(
    data=type_counts,
    x='primary_type',
    y='count',
    hue='primary_type',
    palette=type_colors,
    legend=False  # optional
)
plt.title('Pokémon Counts by Primary Type')
plt.xlabel('Primary Type')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
```


### Challenge — Visualizing by Secondary Type

How would you create a grid of Pokémon images grouped by their `secondary_type`?
 -->

### Whiteboarding

I'll do my best to build some intuition for paths for you on the whiteboard!

### Exercise 2: Understand Paths

Let's explore your own path, and see how it can change. Earlier, you ran, `module load imagemagick`, and typed `which magick`.

#### Exercise 2.1

In your (Jupyter) terminal, type:

```bash
which python
which magick
echo $PATH
```

The `$PATH` (anything with a `$` in front, actually) is a *variable*. Find the python and magick programs in your `$PATH`. The command `echo` is just like print.

#### Exercise 2.2

We used `module load` to load the imagemagick module. Let's explore the module command more. Try the following:

```bash
module list
```

What is listed? Does it make sense?

Now try this:

```bash
module unload imagemagick
```

Is `magick` there for you to use? Verify by trying the following:

* running the command to flip your Pokemon image
* using `which` to see if the command is available

Take a look at your `$PATH` -- what changed?

Run `module avail` -- what do you see? Try and load a specific version of R, and verify that it works as you expect. Why would you care about versions?

#### Exercise 2.3

Let's think a little bit more about Python in particular. 

* Go to the terminal within Jupyter. Which `python3` do you see? How do you know?
* Go to the terminal you get from logging in with `ssh`. Which `python3` do you see? How do you know?



<!-- #### Optional Bonus Confusion

Go back to your Jupyter Notebook, and run the following:

```python
import site
print(site.getsitepackages())
print(site.getusersitepackages())
```

This shows all the places Python looks for things that get installed. Compare this with Python on your terminal. -->

### Whiteboarding

All this path and version stuff is important for reproducibility. Let's take a beat to think through what reproducibility means in research.


### Exercise 3: Creating a Python Virtual Environment

A Python virtual environment is a self-contained directory that includes its own Python installation and packages. It allows you to manage dependencies separately for different projects.

More detailed directions can be found on our [website](https://rcpedia.stanford.edu/_user_guide/python_envs/).

First, we will create a dedicated directory for our work and set up our environment inside it.

1. Open a new Terminal from the JupyterHub Launcher.

2. Run the following commands in your terminal to create a new directory and navigate into it:

```bash
mkdir day2
cd day2
```

3. Next, create the virtual environment. We'll name it `venv`:
```bash
/usr/bin/python3  -m venv venv
# This should make a new folder called venv in your day2 directory
```

Find the path to `python3`, and echo the entire `$PATH`. Where is `python3`?

4. Activate the environment:

```bash
source venv/bin/activate
```

This runs a script that's located in the ./venv/bin directory called `activate`. The `bin` directory doesn't mean like, a literal bin.  It's short for `bin`ary, things that can be executed as programs, as opposed to data or configuration files.

{: .tip}
>**Tip:** You will know the activation was successful when you see (venv) at the beginning of your terminal prompt. This indicates that the virtual environment is active.

5. Check which Python version is being used in your virtual environment:

```bash 
which python3
```
The output should point to the Python executable inside your day2/venv directory.

What is in your path now? What changed?

Run `deactivate` to exit the virtual environment, and then check `which python3` and your path again.

Now, reactivate the environment.


#### Step 2: Installing Packages

Your environment is activated, so now you can install  packages using `pip`. Let's try it.

```bash
pip install dotenv
```

This library is now installed in *this* environment. You can load it while the environment is activated, but it's not installed for anyone else. Test it out! Try importing `numpy` and `dotenv` in the Jupyter terminal with your virtual environment activated and deactivated.

#### Step 3: Integrating Jupyter Notebooks

Now, let's install the `ipykernel` package, which provides the tools to connect your environment to Jupyter:

```bash
pip install ipykernel
```

Now, create a new Jupyter **kernel** linked to your virtual environment. Replace `<kernel_name>` with `day2-venv`. Make sure you're in your active venv when you run this command!

```bash
python -m ipykernel install --user --name=<kernel_name>
```

In the Jupyter interface, go to your `day2` folder, and start a new notebook. Name it `Interactive.ipynb`. Change the *kernel* to `day2-env`.

You should be able to run:

```python
import dotenv
```

If you can't, let's get help!

### Whiteboarding

Let's whiteboard out a real task, where we use an external large language model to process a SEC filing.

----------

### Exercise 4: Calling OpenAI API

Go ahead and install the `openai` package in your day2 venv. Once you're done, we're ready to call the OpenAI API.

Here's how we initialize calls to the OpenAI API:

```python
from openai import OpenAI
client = OpenAI(api_key=<your api key>)
```

**DO NOT** put your API key in here. Instead, we're going to use an API key stored in a 'hidden' file, and load it in as an environment variable.

#### 4.1 Try out the `dotenv` library

We can use `os.getenv` to retrieve an *environment variable*. This a variable (like `$PATH`) that exists on the shell, and you can also read it from Python.

```python
import os
os.getenv("PATH")
```

We can use the `dotenv` library to put things into our environment variables, which is a good practice for storing things like API keys.

We prepared a hidden file for you -- take a look at it in the terminal.

```bash
cat /scratch/shared/rf_bootcamp_2025/.env
```

Now we're going to use it in Jupyter.

```python
from dotenv import load_dotenv
load_dotenv('/scratch/shared/rf_bootcamp_2025/.env')
```

This should load the environment variable -- test by seeing if `OPENAI_API_KEY` is there in your environment.

Look at the code below -- we can publish this on the internet no problem, because our API key isn't in there!

```python
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
```

#### 4.2 OpenAI: "Hello, World!"

We can try this simple example to confirm it works!


```python
completion = client.chat.completions.create(
    model="gpt-4.1-nano",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Say hello world!"}
    ]
)

# Print the model's response
print(completion.choices[0].message.content)
```

#### 4.3 OpenAI with a SEC Document

We have a mirror of the SEC filings on the Yen servers. Here's one example:

    /zfs/data/NODR/EDGAR_HTTPS/edgar/data/1656998/0000950103-24-000077.txt

Go ahead and load in your notebook at take a look.

One neat thing about Jupyter is that if the document is HTML, you can render the HTML in the document itself:

```python
from IPython.display import display, HTML

sec_doc = open(filing_path).read()
display(HTML(sec_doc))
```

Now, you pass the document and use the LLM to extract a useful piece of information.

#### 4.4 OpenAI with Structured Outputs

We're not out of time yet? Amazing!

We're going to extract key information from a Form 3 filing, including the insider’s name, their role(s), the company name, CIK, and filing date — and return it in a structured, standardized format (e.g., JSON or dictionary).

This will make the data easy to validate, analyze, and store for downstream use (like building a dataset or running queries).

* Write a system prompt that's going to extract the information listed above.
* Try running it.

Now, we're going to using **structured outputs** to ensure that OpenAI returns a consistent format. We'll use a library called `pydantic` to define what that format is.

* Install `pydantic` in your virtual environment
* Build a model that contains the information in your filing
* Send that model to the OpenAI API and confirm you get a structured output back

Here's an example pydantic model:

```python
from pydantic import BaseModel, Field

class MenuItem(BaseModel):
    name: str = Field(..., description="Name of the menu item")
    price: float = Field(..., description="Price of the menu item in dollars")

response = client.responses.parse(
    model="gpt-4.1-nano",
    input=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ],
    text_format=Form3Filing,
)
```

<!-- TODOOOOOO: finish structured outputs part -->



<!-- 
### Step 2: Install Required Packages

Let's look into our `openai_tutorial.ipynb` notebook, which contains code that uses various Python packages.

Lets install some packages in our virtual environment so we can run the code in the notebook.

You can install packages using pip, the Python package installer. In your terminal, run the following command:

```bash
pip install numpy pandas matplotlib seaborn openai python-dotenv
```

### Step 3: Connect Your Environment to Jupyter

Now, let's see what happens when we try to use these packages in a notebook.

1. Navigate back to the JupyterLab file browser and open the openai_tutorial.ipynb notebook located in your day2 directory.

2. Run the first cell that contains the import statements.

[!CAUTION]
You will likely encounter an `ImportError`. This is expected! It happens because your Jupyter notebook is running on a "kernel" that is separate from the virtual environment you just created.

To fix this, we need to make Jupyter aware of your new environment.

1. Go back to your terminal window where the (venv) environment is still active.

2. Install the `ipykernel` package, which provides the tools to connect your environment to Jupyter:
```bash
pip install ipykernel
```

3. Now, create a new Jupyter kernel linked to your virtual environment. Replace `<kernel_name>` with a name like `day2-venv`.
```bash
python -m ipykernel install --user --name=<kernel_name>
```


### Step 4. Switch the Notebook Kernel

Finally, tell your notebook to use the new kernel.

1. Go back to your openai_tutorial.ipynb notebook.

2. In the menu at the top, click Kernel → Change kernel.

3. Select the new kernel you just created (e.g., day2-venv) from the list.

4. Restart the kernel by clicking the restart icon (a circular arrow) or by selecting Kernel → Restart Kernel.

Once the kernel has restarted, try running the import cell again. The ImportError should now be gone!


### Step 5:  Documenting and Replicating Your Environment

In this final step, you will learn the most important workflow for creating reproducible Python projects: documenting your dependencies and using that document to recreate your environment anywhere.


#### Part A: Create a requirements.txt File
A `requirements.txt` file is the standard way to create a "parts list" for your project. It records all the external packages and their specific versions needed to run your code.



1. Ensure your `day2` environment is active. Go to your terminal and check that the prompt begins with `(venv)`. If it isn't, navigate to your `day2` directory and run `source venv/bin/activate`.

2. Generate the requirements file. While inside the `day2` directory, run the following command:

```bash
pip freeze > requirements.txt
```
3. Inspect the file (optional). Use the `cat` command to see what you created:

```bash
cat requirements.txt
```


#### Part B: Recreate the Environment from the File

### Exercise: 

1. Create an additional directory called `day2_replicated`
2. Create a new virtual environment in this directory called `venv_replicated`
3. Install all packages from the `requirements.txt` file you created earlier.
    - Hint: `pip install -r requirements.txt` 
4. Create a new Jupyter kernel for the replicated environment.
5. Verify `openai_tutorial.ipynb` runs without errors in the new environment.
 -->
