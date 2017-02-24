# Swiss System Tournament
## About
**Swiss System Tournament is a part of Udacity "Full Stack Web Developer Nanodegree"**

Developed a Python module that uses the PostgreSQL database to keep track of players and matches in a **Swiss System Tournament** game

## Technologies used:
- Vagrant Virtual Machine
- Python2.7
- PostgreSQL database

## Understand the purpose of each file
- tournament.sql  - this file is used to set up the database schema (the table representation of data structure).
- tournament.py - this file is used to provide access to the database via a library of functions which can add, delete or query data in the database to another python program (a client program). Remember that when you define a function, it does not execute, it simply means the function is defined to run a specific set of instructions when called.
- tournament_test.py - this is a client program which will use functions written in the tournament.py module. We've written this client program to test your implementation of functions in tournament.py

## How to Run
*Prerequisites
- Git Bash should be installed on your machine*

**Step 1: Installing the VM**
Download and install - [Vagrant](https://www.vagrantup.com/downloads.html) and [VirtualBox](https://www.virtualbox.org/wiki/Downloads) to manage the VM

**Step 2: Download the VM configuration**
The virtual machine configuration is in this file: [FSND-Virtual-Machine.zip](https://d17h27t6h515a5.cloudfront.net/topher/2016/December/58488015_fsnd-virtual-machine/fsnd-virtual-machine.zip)
Download this file to your computer and unzip it. This will give you a directory called FSND-Virtual-Machine.

**Step 4: Download files from this Repo**
Download files from this Repo and paste them into **tournament** folder

**Step 3: Starting Vagrant**
From your terminal, inside the vagrant subdirectory, run the command *vagrant up*.
At this point, you can run *vagrant ssh* to log in to your newly installed Linux VM
Then, in your terminal run command *cd /vagrant/tournament*

**Step 5: Running the test file**
In */vagrant/tournament* directory run command *python tournament_test.py*

## License
The MIT License (MIT)

Copyright (c) 2017 Tofik Umukhanov
