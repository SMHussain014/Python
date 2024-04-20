# Introduction

Python is a programming language. 
Program is the set of instructions, written in the shape of a code or a commands.

# How to install "Python"

You can download python from "python.org". Install python version 3.12.0 or later.
Always check box, read as "Add python.exe to Path" and install.
To check, Python is installed on your system, go to Command Prompt (using cmd).
Type python --version, the display will show version details.

# Where to write Python's code

To write python's code, an IDE is required.
Download "Visual Studio Code" from Google and install.
Please also install Python's extensions 'Pylance (server)' and 'Pylance (IntelliSense)'.

# How to set Environment for Python

To set Python's environment, we have to download and install "Anaconda" from google.
To check, Anaconda is installed on your system, go to search bar and type 'Anaconda Prompt' and
press enter. Open that and see if world 'base' appears onto screen or not, if so, task is done.
In 'Anaconda Prompt' type 'conda create -n env_name python==3.12 -y' and press enter.
After that activate this environment by using 'conda activate env_name' and press enter.
Now, make a txt file in your project and type the names of desired packages.
To install these packages, type 'pip install -r txt-file_name' and press enter in 'Anaconda Prompt'.

# How to get started

First Method:
First create a Folder, like "Python-Course".
Open VSC, go to "File Menu" and click "Open Folder".
In that folder, open "New File", like "name.py". (.py is the extension of python code)
After naming, create file and just start writing code(s) in that file.

Second Method:
Open 'Command Prompt' ( by using cmd), create a directory (by using mkdir dir_name & press enter).
In that directory, type 'code .' and press enter.  The project will be opened in VSC. 

Third Method:
If you have not installed 'Python' on your system, go to "Golab" and just start enjoying Python.

# How to run file containing Python's code

First Method:
In VSC, go to "Terminal Menu", click "New Terminal".
In lower part of VSC's Interface, a small window will appear.
Type python, press Space, type current File's Name with extension and press Enter.
The coded file will execute the desired codes.
To clear Terminal's Interface, type "clear" or "cls" and press Enter.
To exist Terminal's Interface, type ctrl+z.
Alternatively, press 'Run Python File' button, present at top-right corner of VSC. 

Second Method:
In Anaconda Prompt, type python press Space, type current File's Name with extension 
and press Enter.

# Useful packages
jupyter
Its file extension is 'ipynb'. Make sure to install its extensions in VSC before its usage.

mypy
It is a program to check run-time error of python's file. Make sure to install its extension, namely 'mypy (Matan Gover) in VSC before its usage.

pandas
Its extension, i.e. lxml, is required to be installed before its usage.
To install that type '!pip install lxml' and run the App.
Any PDF file can be import by using 'Pandas' in 'Jupyter Note Book'. Go to Code Bar and type 'import panda as pd', then type the address, like 'table = pd.read_html('https://www.w3schools.com/python/python_operators.asp') table[0]' and run the App.

numpy