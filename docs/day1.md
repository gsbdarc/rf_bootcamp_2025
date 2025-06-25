---
title: Day 1
layout: page
nav_order: 1
has_children: true
updateDate: 2025-06-17
---

# {{ page.title }}



## Objectives

- **Log into the Yens computing cluster** using SSH from your local machine.

- **Understand the file system structure** used in Unix-based environments.

- **Navigate the system** with basic command-line tools (ls, cd, pwd, etc.).

- **Practice hands-on exercises to:**
  - Move, organize, and manipulate files.
  - Understand shared file systems across nodes.
  - Use commands like `scp`, `mv`, and pattern matching with wildcards.

- **Build comfort and fluency** using the command line interface (CLI) on a shared computing cluster.


## The Yens and DARC

The computing cluster is called the Yens. Its a powerful system with 5 interactive nodes, and 10 slurm nodes(7 CPU and 3 GPU). The Yens has a petabyte of storage and is more powerful than your laptop. Its designed to handle large computing tasks doing work in groups and helping you and your professors publish papers and do research.

Today we are going to focus on the interactive nodes.

The Yens is managed by the [Data Analytics and Research Computing (DARC)](https://darc.stanford.edu/) team. They provide support and resources for researchers at Stanford to perform data analysis and computational tasks efficiently.

Our Website is [Rcpedia](https://rcpedia.stanford.edu/), where you can find more information and resources about the Yens and other computing resources at Stanford.

We also have a [Slack channel](https://app.slack.com/client/E7SAV7LAD/C01JXJ6U4E5) where you can ask questions and get help from the community.

## Introduction into the CLI

### 🧠 Why Use It?

- 🚀 Speed: Do things faster than clicking

- 📁 Navigate: Move around folders and files

- 🧹 Organize: Clean and sort data

- ⚙️ Power: Run complex scripts and jobs


### Navigating the File System

The Yens uses a Unix-like file system. Here are some basic commands to help you navigate:
```bash
ls          # List files
cd folder/  # Change directory
pwd         # Where am I?
mkdir test  # Make a folder
cat file.txt # View file content
rm file.txt # Remove a file
```

#### Investigation 

- Find your current working directory and list the files in it.
```bash
pwd          # Print working directory
ls          # List files
- Determine if there are any hidden files in your current directory.

```bash
pwd          # Print working directory
ls -a       # List all files, including hidden ones (those starting with a dot)
``` 

-a is a flag that tells the `ls` command to show all files, including hidden ones (those starting with a dot). Many CLI commands have flags that modify their behavior. You can find more about these flags by checking the manual pages for each command. For example, you can type `man ls` to see the manual for the `ls` command. (hint: type `q` to exit the manual page)


#### Movement

- Change directories to your Desktop or Documents folder.
- Head back to your home directory. 

```bash
cd ~/Desktop    # Once you type D try pressing tab to autocomplete or tab twice to see all options
cd .. # This goes up one level 
```

#### Creation

- Create a new folder in your Desktop or documents called `test_folder`.

```bash
mkdir ~/Desktop/test_folder
```


#### Deletion

- Remove the folder you just created

```bash
rm -r ~/Desktop/test_folder
```



# Exercise 1: Move and Organize Files

Download the zip file from the link below:
[File link](https://drive.google.com/file/d/1yLJQunPAksSLPkbWhWZCSIk31DF68g_y/view?usp=drive_link)


## Step 1: Download, Store, and Unzip the File

- Put the file in a directory on your local machine, for example, in your Desktop folder. 

```bash
mv ~/Downloads/file.zip ~/Desktop/
```

Lets unzip the file in your local machine first: 
```bash
cd ~/Desktop
unzip ~/Desktop/file.zip -d ~/Desktop/  
```

This should create a folder called `images/` on your Desktop with all the Pokémon images.

Take a moment to look at the files in the `images/` folder. You should see files named like this:
```plaintext
bulbasaur_Grass_Poison_ivysaur.png
charmander_Fire_none_charmeleon.png
squirtle_Water_none_wartortle.png
``` 
Now these may be familiar files to some of you and others not so much. They do have a common file structure 

`name_type1_type2_evolution`

Example : `bulbasaur_Grass_Poison_ivysaur.png` where:
- `bulbasaur` is the name of the Pokémon
- `Grass` is the primary type
- `Poison` is the secondary type (if applicable)
- `ivysaur` is the evolution stage (if applicable)


# Challenge: How do we organize these files?
You have a folder full of Pokémon images, but they are all mixed together.
You want to organize them by type, evolution, and other characteristics.  

How do we organize these files into some manageable structure, without dragging and dropping them? Without opening an IDE? 

## 🔰 Task 1: Move all Rock-type Pokémon to a folder
🧠 Focus: Use of wildcards (*) and the mv command.

💪 Challenge:

Move all files that include _Rock_ as one of their types into a new folder called rock/.

hint- the wildcard `*` can be used to match any characters in the file name.
Example: `c*` will match any file that starts with c regardless of what comes after it.

```bash
ls c*
``` 

## 🔰 Task 2: Move all Pokémon with secondary type “Flying”

🧠 Focus: Wildcards matching specific position (second type in slot 3).

💪 Challenge:

**Copy** all files where the **second type** is “Flying” into a folder named flying/.


## 🔰 Task 3: Report the pokemon image with the largest file size

🧠 Focus: Understanding different flags you can use

💪 Challenge: find the file which has the largest size, smallest size
Bonus: craft a command that will only report the largest file size and name of the fole

Hint: This has to do with flags you can use with the 'ls' command 

Bonus Hint: The `head` command can be used to limit the output to the first line the `|` pipe operator can be used to pass the output of one command to another command.


## 🔰 Task 4: Make a file with all the water type Pokemon names
🧠 Focus: Using grep to filter files based on content
💪 Challenge: Create a **file** that contains the file names of all Water-type Pokémon.

Hint: The `grep` command can be used to search for specific patterns in files. For example ls | grep "Dragon" will list all files that contain the word "Dragon" in their name. The  `>` operator can be used to redirect the output of a command to a file. `ls > all_files.txt` will save the output of the `ls` command to a file called `all_files.txt`.


## 🔰 Task 5: Challenge Task

#### 🧪 Challenge
Find the least common primary type among all Pokémon in the image set.

Your job:

1. Extract the type from file names

`abomasnow_Grass_Ice_none.png` is the file name, and the type is `Grass_Ice`.

2. Count the frequency of the type combos

```plaintext
14 Grass_Poison
15 Ground_none
16 Fairy_none
  ```
3. Output the type(s) with the smallest count

hint: You can use the `cut` command to extract the type from the file name, and then use the `sort` and `uniq` commands to count the frequency of each type. Then smartly search the output for those with only 1 type.


# The Yens

## Logging into the Yens 

Use SSH in your terminal (replace <SUNetID>):

```bash
ssh <SUNetID>@yen.stanford.edu
```

Duo authentication is required.

## Yens Task 1: Explore your home folder
 Explore the Yens file systems. What are some different files and directories you see?

Here are some Yens specific commands to help you understand your home directory

```bash
gsbquota # Find out how much space you have left on your home or in a project directory
```

```bash
ml avail # List all available modules on the Yens
```

## Yens Task 2:
 Open another terminal window and upload the zip file you downloaded earlier to the Yens.

The `scp` command allows you to securely copy files between your local machine and the Yens.

```bash
scp /path/to/local/file.zip <SUNetID>@yens.stanford.edu:/
```

Switch back to the Yens and the file should be in your home directory.

Try running `gsbbrowser` to understand this news files effect on your system.

```bash
gsbbrowser
```

[!NOTE]
**Important point**: You should be able to ssh into any one of the interactive nodes and the file should be there.
that because the file system is **shared across all the the nodes on the yens**

## Yens Challenge:

log into a specific node
    [Check out our website](https://rcpedia-dev.stanford.edu/_getting_started/how_access_yens/)

## Yens Task 3: Clone the repository:

We won't be using git for the rest of the course, but we will use it to get the files for the next day.


```bash
git clone https://github.com/gsbdarc/rf_bootcamp_2025.git
```

This will create a folder called `rf_bootcamp_2025` in your home directory with all the files for the course.
