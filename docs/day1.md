---
title: Day 1
layout: page
nav_order: 1
updateDate: 2025-06-17
---

# {{ page.title }}



## Objectives

- **Log into the Yens computing cluster** using SSH from your local machine.

- **Understand the file system structure** used in Unix-based environments.

- **Navigate the system** with basic command-line tools (`ls`, `cd`, `pwd`, etc.).
  - Don't worry if these commands don't mean anything to you yet!
- **Practice hands-on exercises to:**
  - Move, organize, and manipulate files.
  - Understand shared file systems across "nodes".
  - Use commands like `scp`, `mv`, and pattern matching with wildcards.

- **Build comfort and fluency** using the command line interface (CLI) on a shared computing cluster.


## The Yens and DARC

The computing cluster is called the Yens. It's a powerful system with (as of July 2025) 5 interactive nodes, and 10 SLURM nodes (7 CPU and 3 GPU). The Yens has a petabyte of storage and is more powerful than your laptop. It's designed to handle large computing tasks doing work in groups, and to help you and your professors publish papers and do research.

Today we are going to focus on the interactive nodes.

The Yens is managed by the [Data Analytics and Research Computing (DARC)](https://darc.stanford.edu/) team. They provide support and resources for researchers at Stanford to perform data analysis and computational tasks efficiently.

Our website is [Rcpedia](https://rcpedia.stanford.edu/), where you can find more information and resources about the Yens and other computing resources at Stanford.

We also have a [Slack channel](https://app.slack.com/client/E7SAV7LAD/C01JXJ6U4E5) where you can ask questions and get help from the community.

## Introduction To The Command Line Interface (CLI)

### 🧠 Why Use It?

- 🚀 Speed: Do things faster than clicking

- 📁 Navigate: Move around folders and files

- 🧹 Organize: Clean and sort data

- ⚙️ Power: Run complex scripts and jobs to automate your work


{: .important}
If you are a **Mac** or **Linux** user, you can use the native terminal for these exercises.

{: .important}
If you are a **Windows** user, you can use [Git Bash](https://git-scm.com/downloads) to run these commands.


#### **Investigation**

- Find your current working directory and list the files in it.
  
``` bash
pwd          # Print working directory
ls           # List files
```  
- Determine if there are any hidden files in your current directory.
  
```bash
ls -lah       # - l long file -a all files -h human readable
``` 

`-lah` is a flag that tells the `ls` command to show all files long format with human readable sizes, including hidden ones (those starting with a dot). In general, a flag modifies the behavior of a CLI command. You can find out more about these flags by googling the command.

#### **Movement**

- Change directories to your Desktop or Documents folder.
- You can use the `cd` command to change directories. The `~` symbol represents your home directory, and you can use `..` to go up one level in the directory structure.

```bash
cd ~/Desktop    # Once you type D try pressing tab to autocomplete or tab twice to see all options
cd .. # This goes up one level 
```

#### **Creation**

- Create a new folder in your Desktop or documents called `test_folder`.

```bash
mkdir ~/Desktop/test_folder # Create a new folder

cd ~/Desktop/test_folder # Change into the new folder

touch test_file.txt # Create a new file

cp test_file.txt test_file_copy.txt # Create a copy of that new file
```



#### **Deletion**

- Remove the folder and files  you just created

{: .warning}
These `rm` actions are **permanent**, so make sure you double check what you are removing!

```bash
rm test_file.txt # Remove the file
rm test_file_copy.txt # Remove the copy of the file
rm -r ~/Desktop/test_folder # Remove the directory and its contents recursively
```


# Exercise 1: Move and Organize Files

Your professor has asked you to grab some research data and organize it for a project. The data is in a zip file that you need to download, unzip, and organize.

## Download the technical_data_important.zip file from this link: **[data](https://drive.google.com/file/d/1lxJTH1wrDhOH7k6gEndRPOTA57sA-vbp/view?usp=sharing)**


## Store, and Unzip the File

- Put the file in a directory on your local machine, for example, in your Desktop folder. 

```bash
mv ~/Downloads/technical_data_important.zip ~/Desktop/
```

- Examine the contents of the zip file without unzipping it. 

```bash
unzip -l ~/Desktop/technical_data_important.zip
``` 

- Unzip the file to your Desktop

```bash
cd ~/Desktop
unzip ~/Desktop/technical_data_important.zip -d ~/Desktop/technical_data_important/
```

{: .note}
Take a moment to look at the files in the `technical_data_important/` folder. You should see files named like this:

```plaintext
bulbasaur_Grass_Poison_ivysaur.png
charmander_Fire_none_charmeleon.png
squirtle_Water_none_wartortle.png
``` 

Now these may be familiar files to some of you and to others not so much. They do have a common file structure:

`name_type1_type2_evolution`

Example : `bulbasaur_Grass_Poison_ivysaur.png` where:
- `bulbasaur` is the name of the Pokémon
- `Grass` is the primary type
- `Poison` is the secondary type (if applicable)
- `ivysaur` is the evolution stage (if applicable)


# Challenge: How do we organize these files?

You have a folder full of Pokémon images, but they are all mixed together.
You want to organize them by type, evolution, and other characteristics.  


🧠 How can you wrangle this wild folder into order?


## 🔰 Task 1: Rock On!

> ## 📁 Copy all Rock-type Pokémon into a folder called rock/

### 🧠 Focus: Use of wildcards (*) and the cp command.

{: .note}
> The `cp` command is used to copy files from one location to another. We copy here so we don't lose the original files.


{: .tip}
>The wildcard `*` can be used to match any characters in the file name. Example: `c*` will match any file that starts with c regardless of what comes after it, try the command `ls c*`


## 🔰 Task 2: Freebird

> ## 🪶 Copy all Pokémon with secondary type “Flying” into flying/

### 🧠 Focus: Wildcards matching specific position (second type in slot 3).

Example: `altaria_Dragon_Flying_none.png` is the file name, and the secondary type is `Flying`.


## 🔰 Task 3: Stone cold 

> ## 🪨 Move all Pokémon with “rock” in their name, not type, to rock_names/
Also, report the largest and smallest file in that folder.

### 🧠 Focus: moving, piping, data flags



{: .tip}
>This has to do with flags you can use with the `ls` command 

{: .tip}
>The `grep` command can be used to list files based on their names.  The `|` operator can be used to pipe the output of one command into another. 

## 🔰 Task 4: Keeping Track

> ## 💧 Create a file listing the names of all Water-type Pokémon called `water_types.txt`

🧠 Focus: `grep`, redirecting (`>`), file viewing

{: .tip}
>The `grep` command can be used to search for specific patterns in files. For example `ls | grep "Dragon"` will list all files that contain the word "Dragon" in their name. The  `>` operator can be used to redirect the output of a command to a file. `ls > all_files.txt` will save the output of the `ls` command to a file called `all_files.txt`.

{: .tip}
The `cat` command can be used to display the contents of a file. For example, `cat water_pokemon.txt` will display the contents of the `water_pokemon.txt` file.



## 🔰 Task 5: Gotta Catch them All -- BONUS

>## 🧪 Find the least common primary+secondary type combination

🧠 Focus: `cut`, `sort`, `uniq`, `awk` (or other ways to get frequency counts)

1. Extract the type from file names

 -  `abomasnow_Grass_Ice_none.png` is the file name, and the type is `Grass_Ice`.

2. Count the frequency of the type combos
  ```plaintext
  14 Grass_Poison
  15 Ground_none
  16 Fairy_none
  ```
3. Output the type(s) with the smallest count

{: .tip}
>You can use the `cut` command to extract the type from the file name, and then use the `sort` and `uniq` commands to count the frequency of each type. Then smartly search the output for those with only 1 type.


# The Yens

The Yens are Stanford GSB's high-powered computing clusters. You’ll use them to organize your data, run code, and collaborate with others in a shared computational ecosystem.

Let’s get you connected and operational.

🔗 Helpful Reference: [Rcpedia](https://rcpedia.stanford.edu/)


## Logging into the Yens 

Use SSH in your terminal (replace `<SUNetID>`):

```bash
ssh <SUNetID>@yen.stanford.edu
```

{: .note}
Duo authentication is required.

- What do you see when you first log in?
- What commands are shown?
- Which node are you connected to?

{: .tip}
> You can connect to specific nodes by using `ssh <SUNetID>@yen3.stanford.edu` for `yen3`

## Yens Task 1: Explore your home folder

 Explore the Yens file systems. 
 
 - What are some different files and directories you see?
 
 - What are some of the hidden files you see?

Here are some Yens specific commands to help you understand your home directory

```bash
gsbquota # Find out how much space you have left on your home or in a project directory
```

```bash
gsbbrowser # is a disk usage analyzer with an interactive interface
```

```bash
module avail # List all available modules on the Yens
```

## Yens Task 2:

- Open another terminal window and upload the zip file you downloaded earlier to the Yens.

{: .tip}
> You want to be doing this on your local machine (i.e., run the commands below in your _local_ terminal and not in your Yens terminal).

The `scp` command allows you to securely copy files between your local machine and the Yens.

```bash
scp /path/to/local/technical_data_important.zip <SUNetID>@yen.stanford.edu:/
```

- Also copy the unzipped folder `technical_data_important/` to the Yens.

```bash
scp -r ~/Desktop/technical_data_important <SUNetID>@yen.stanford.edu:~/technical_data_important
``` 

Now switch back to the Yens and the file should be in your home directory.

- Try running `gsbbrowser` to understand this new file's effect on your system.


{: .important}
> **Important point**: You should be able to ssh into any one of the interactive nodes and the file should be there.
That is because the file system is **shared across all the the nodes on the yens**

## Yens Task 3: Find the Python Version
Find which python version is installed on the Yens. You can do this by running the following command:

```bash
which python3
```

## Yens Challenge Task

1. Unzip and/or move into the directory you uploaded to the Yens 
2. Copy your favorite Pokémon image to to the shared folder zfs/scratch/shared/pokedex
3. Find my favorite Pokemon image

