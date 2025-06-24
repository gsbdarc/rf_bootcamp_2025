---
title: Day 1
layout: page
nav_order: 1
has_children: true
updateDate: 2025-06-17
---

# {{ page.title }}


Welcome to the first day of our journey! Today, we will cover the basics of our computing system the Yens. We'll start with logging in, understanding the file system, and learning how to navigate through it. We'll end with a hands on exercise which will help solidify your understanding and get you comfortable with the system.


## The Yens 

The computing cluster is called the Yens. Its a powerful system with 5 interactive nodes,  and 10 slurm nodes(7 CPU and 3 GPU). The Yens has a petabyte of storage and is more powerful than your laptop. Its designed to handle large computing tasks doing work in groups and helping you and your professors publish papers and do research.

Today we are going to focus on the interactive nodes.


### Exercises 1: Logging into the Yens

To log into the Yens, you will need to use SSH (Secure Shell). Open your terminal and type the following command:

```bash
ssh <SUNetID>@yens.stanford.edu
```
 
-- Need to test this command with a real SUNetID and ensure it works as expected.

If you are using a Mac or Linux, you can use the terminal. If you are on Windows, you can use an SSH client like PuTTY or the built-in SSH client in Windows 10 and later.


You will need to Duo authenticate. You WILL NEED to Duo authenticate to log in



challenge
log into a specific node
    [Check out our website](https://rcpedia-dev.stanford.edu/_getting_started/how_access_yens/)

### Navigating the File System

The Yens uses a Unix-like file system. Here are some basic commands to help you navigate:
```bash
# List files in the current directory
ls  

# Linux commands usually have a lot of options. You can see the options by typing the command with --help
ls --help
# To see all files  

ls -a
# Change directory
cd <directory_name>
# Go up one directory
cd ..
# Print the current working directory
pwd
# Create a new directory
mkdir <directory_name>

```

#### Exercise 3: Move and Organize Files

Download the zip file from the link below:
(File link)[https://drive.google.com/file/d/1yLJQunPAksSLPkbWhWZCSIk31DF68g_y/view?usp=drive_link]


Lets unzip the file in your local machine first: 

```bash
unzip file.zip
```

Now these may be familiar files to some of you and others not so much. They do have a common file structure 

name_type1_type2_evolution

How do we organize these files into some manageable structure, without dragging and dropping them? Without opening an IDE? 

So we can all be on the same page, lets upload the zip file into the Yens using te `scp` command.
The `scp` command allows you to securely copy files between your local machine and the Yens.

```bash
scp /path/to/local/file.zip <SUNetID>@yens.stanford.edu:/
```

Log back into the Yens and the file should be in your home directory.

Important point: You should be able to ssh into any one of the interactive nodes and the file should be there.
that because the file system is **shared across all the the nodes on the yens**



Now lets unzip the files on the Yens and complete some challenges:

## 🔰 Task 1: Move all Rock-type Pokémon to a folder (Easy)
🧠 Focus: Use of wildcards (*) and the mv command.

💪 Challenge:

Move all files that include _Rock_ as one of their types into a new folder called rock/.
```bash
mkdir rock
mv *_Rock_* rock/
```

## 🔰 Task 2: Move all Pokémon with secondary type “Flying”

🧠 Focus: Wildcards matching specific position (second type in slot 3).

💪 Challenge:

Move all files where the second type is “Flying” into a folder named flying/.

✅ Solution:
```bash
mkdir flying
mv *_*_Flying_* flying/
```

## 🔰 Task 3: Move all Pokémon with only one type

🧠 Focus: Identify files where type2 is none.

💪 Challenge:

Move all Pokémon with only one type (i.e., type2 == none) into a folder called singletype/.

✅ Solution:
```bash
mkdir singletype
mv *_none_* singletype/
```

## 🔰 Task 4: Separate evolved and unevolved Pokémon

🧠 Focus: Matching patterns in the evolution field.

💪 Challenge:

Move all Pokémon that evolve into another (i.e., the last field is not none) into a folder called evolving/.

```bash

# Better:
mkdir evolving
for file in *_*_*_*.png; do
    if [[ "$file" != *_*_none.png ]]; then
        mv "$file" evolving/
    fi
done
```

## 🔰 Task 5: Group by primary type (dynamic folder creation)(Hard)

🧠 Focus: Bash parameter expansion and scripting

💪 Challenge:

Write a loop that scans all files and moves each one into a folder matching its primary type.
```bash
for file in *.png; do
    type1=$(echo "$file" | cut -d'_' -f2)
    mkdir -p "$type1"
    mv "$file" "$type1/"
done
```

## 🔰 Task 6: Handle special forms (like aegislash-blade or pumpkaboo-average)

🧠 Focus: Handling dashes in names

💪 Challenge:

Move all Pokémon with a dash (-) in their name into a folder called variants/.
```bash
mkdir variants
mv *-* variants/
```     
