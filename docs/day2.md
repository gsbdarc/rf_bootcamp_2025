---
title: Day 2
layout: page
nav_order: 2
has_children: true
updateDate: 2025-06-17
---

# {{ page.title }}

Welcome to the second day of our journey! Today, we will dive deeper into the Yens computing cluster. We’ll explore the Yens-provided IDE, **JupyterHub**. You'll learn about Python virtual environments, how to use Jupyter notebooks, and how to run Python code on the Yens. We'll wrap up with a hands-on exercise to solidify your understanding and get you comfortable with the system.

---

## JupyterHub on the Yens

JupyterHub is a web-based interactive development environment (IDE) available on the Yens. It allows you to create and share documents that contain live code, equations, visualizations, and narrative text. It’s a powerful tool for data analysis, machine learning, and scientific computing.

However, it does have limitations, especially with long-running jobs. For those, we’ll use the **Slurm job scheduler** — covered on a later day.

---

### Exercise 1: Accessing JupyterHub

To access JupyterHub, open your web browser and visit one of the following links:

- [Yen1](https://yen1.stanford.edu/jupyter/hub/home)
- [Yen2](https://yen2.stanford.edu/jupyter/hub/home)
- [Yen3](https://yen3.stanford.edu/jupyter/hub/home)
- [Yen4](https://yen4.stanford.edu/jupyter/hub/home)
- [Yen5](https://yen5.stanford.edu/jupyter/hub/home)

You should see the folders you created on the previous day, including your exercise notebooks.

- Click the blue plus button to create a new notebook.
- Also, create a new terminal by clicking the terminal icon.

In your notebook, run the following code (in separate cells):

```python
# Print "Hello, World!"
print("Hello, World!")  
# Import the math module and print the value of pi

import math
print(math.pi)

# Create a list of numbers and print the sum
numbers = [1, 2, 3, 4, 5]
print(sum(numbers))


Load a pokemon image


Make a grid, plot all fire type
```

Protip: You can run a cell by clicking the Run button or by pressing Shift + Enter.


### Exercise 2: Creating a Python Virtual Environment

A Python virtual environment is a self-contained directory that includes its own Python installation and packages. It allows you to manage dependencies separately for different projects.

More detailed directions can be found on our [website](https://rcpedia-dev.stanford.edu/_user_guide/python_envs/).

Let’s walk through the steps:

1. Open a terminal in JupyterHub.

2. Run the following:   

```bash
mkdir day2
cd day2

/usr/bin/python3  -m venv venv

source venv/bin/activate

# You should see (venv) at the beginning of your terminal prompt
```

Lets install some packages in our virtual environment. 

You can install packages using pip, the Python package installer. In your terminal, run the following command:


```bash
pip install numpy, pandas, matplotlib, seaborn 
```


Now lets go back to our Jupyter notebook and create and run a cell with the following commands

```python
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
```
You’ll likely get an **ImportError**, that's expected. This is because your JupyterHub kernel isn't connected to your virtual environment.

To fix this, we need to install the ipykernel package in our virtual environment and create a new kernel for JupyterHub to use. Go back to our terminal and run the following commands:


### Fixing the Kernel Connection
To connect your virtual environment to JupyterHub, install `ipykernel` and create a new kernel:

note: Make sure you are still in your virtual environment (you should see `(venv)` at the beginning of your terminal prompt).

```bash
pip install ipykernel
python -m ipykernel install --user --name=<kernel_name>
```

Replace <kernel_name> with a name like day2-venv.

Now go to your notebook, open the Kernel menu → Change kernel, and select the new kernel you just created. Restart the notebook.


### Final Hands-On Exercise

1. Copy the notebook code from ____________ to your day2 directory.

2. Open it in JupyterHub and activate your new kernel.

3. Run the first cell with code and observe any errors (likely due to missing packages).

4. Return to the terminal and install the required packages.

Once successful, create a `requirements.txt` file:

```bash
pip list --format=freeze | cut -d= -f1 > requirements.txt
```
This lists only package names without versions.

Now let’s replicate this setup elsewhere:

```bash
mkdir day2_venv
cd day2_venv
/usr/bin/python3 -m venv venv
source venv/bin/activate
pip install -r ../day2/requirements.txt #or wherever you saved your requirements.txt file
```

Return to your notebook and change the kernel to the one in day2_venv. You should now be able to run the imports and remaining code without errors.





