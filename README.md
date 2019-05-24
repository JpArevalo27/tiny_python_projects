# Playful Python

I believe you can learn serious things through silly games. 

I'd like to make this into a book or something, similar to the Python bioinformatics/data science (https://github.com/kyclark/practical_python_for_data_science) repo. I think you will learn best by *doing*, so I think I will write this as a loose collection of exercises that spell out the skills I aim to teach with each exercise. I will create descriptions for each exercise with examples of how the program should work along with a test suite. You will need to write the program that satisfies the test suite.

I think I'm going to present this differently from other material in that I won't necessarily show you beforehand what you need to write a program. I'll describe what the program should do and provide some discussion about how to write it. I'll also create an appendix with short example of how to do things like read/write from/to a file, process all the files in a directory, extract k-mers from a string, etc. I'll provide some building blocks, but I want you to figure out how to put the pieces together!

# new_py.py

I provide a program in the `bin` directory called `new_py.py` that will help you stub out new Python programs using the fabulous `argparse` module to parse the command line arguments and options for your programs. I highly recommend you start every new program with this. For example, if the `README` say "Write a Python program called `abc.py` that ...", then you should do this:

````
$ new_py.py abc
````

To create a new `abc.py` program that has example code for you to start writing your program.

# How to Use

Do a `git clone $URL` of this repository, then do `git add upstream master $URL` so that you can do `git pull upstream master` to get updates. When you create new files, `git add/commit/push` them to *your* repository. (Please do not create pull requests on *my* repository -- unless, of course, you have suggestions for improving my repo!).

This is a work in progress. If you see a directory contains a `README.md`, `solution.py`, `Makefile`, and `test.py`, then it's likely ready to be solved.

# Author

Ken Youens-Clark <kyclark@gmail.com>
