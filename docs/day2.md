---
title: Day 2
layout: page
nav_order: 2
has_children: true
updateDate: 2025-06-17
---

# {{ page.title }}

# Day 2 — Working on the Yens Cluster with JupyterHub
## Learning Goals
By the end of today you will be able to

- create and activate **Python virtual environments** on Yens;

- open and run **Jupyter notebooks** in JupyterHub;

- execute **Python code** directly on the cluster;

- make simple visualizations with `pandas`, `seaborn`, and `matplotlib`.

- Run API calls to OpenAI from JupyterHub.

We finish with a hands‑on exercise to reinforce each skill.

---

### Exercise 1: Accessing JupyterHub

#### 1: Open the Hub

Choose any of the following links to access JupyterHub on the Yens cluster:

- [Yen1](https://yen1.stanford.edu/jupyter/hub/home)
- [Yen2](https://yen2.stanford.edu/jupyter/hub/home)
- [Yen3](https://yen3.stanford.edu/jupyter/hub/home)
- [Yen4](https://yen4.stanford.edu/jupyter/hub/home)
- [Yen5](https://yen5.stanford.edu/jupyter/hub/home)

You should see the folders you created on the previous day, including your exercise notebooks.

#### 2: Start a New Notebook and Terminal
- Click the **blue “+”** to open a **Python 3 notebook**.

- Click the **Terminal** icon to launch a shell (we’ll use it for environment commands).


### Exercise 1.1 -First Notebook Cells

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



### Exercise 1.2 — Jupyter Terminal Basics

Open the terminal tab you started above and try:

```bash
# List files in your home directory
ls

# navigate into your pokemon_images directory
cd images

# List files in the pokemon_images directory
ls

# Find out which python version you are using
which python3
```

### Exercise 1.3: — Display a Pokémon Image

1. Locate any PNG in your images folder (use the file browser or ls).

2. Replace /path/to/your/pokemon_image.png below with that full path.

```python
import matplotlib.pyplot as plt
import matplotlib.image as mpimg        
# Load and display a Pokémon image
img_path = '/path/to/your/pokemon_image.png'  # Replace with your image
img = mpimg.imread(img_path)
plt.imshow(img)
plt.axis('off')  # Hide axes
plt.show()
```

Note: If you get an error about the libary not being installed, you can install it in your terminal with:

```bash
pip install matplotlib
```

### Exercise 1.4 - Counts by Primary Type

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



### Exercise 2: Creating a Python Virtual Environment

A Python virtual environment is a self-contained directory that includes its own Python installation and packages. It allows you to manage dependencies separately for different projects.

More detailed directions can be found on our [website](https://rcpedia.stanford.edu/_user_guide/python_envs/).

### Step 1 Create and Activate a Virtual Environment

First, we will create a dedicated directory for our work and set up our environment inside it.

1. Open a new Terminal from the JupyterHub Launcher.

2. Run the following commands in your terminal to create a new directory and navigate into it:

```bash
mkdir day2
cd day2
```

3. Next, create the virtual environment. We'll name is `venv`:
```bash
/usr/bin/python3  -m venv venv
# This should make a new folder called venv in your day2 directory
```

4. Activate the environment:

```bash
source venv/bin/activate
```

[!TIP]
**Tip:** You will know the activation was successful when you see (venv) at the beginning of your terminal prompt. This indicates that the virtual environment is active.

L5. Check which Python version is being used in your virtual environment:

```bash 
which python3
```
The output should point to the Python executable inside your day2/venv directory.


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

