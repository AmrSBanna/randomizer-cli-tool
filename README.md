# Randomizer CLI-TOOL README 
Randomizer cli-tool is a simple tool that's used to print a list of numbers randomized or sorted. The list of numbers 
is range that starts with startValue (default=1) and ends with endValue (default=10). Nonetheless, the tool provides 
the possibility to select any range based the values of the arguments. In addition to that it prints the list 
randomized or ordered based on the (--randomize) argument value

The tool written python and packaged as a python package that can be installed on MacOS or Linux like any other popular 
python packages using pip3. 

## Installation Pre-requisites: 
* This tool has been developed using Python 3.6.9.
* Install python3 virtualenv if not isntalled
  ```
  $ apt-get install python3-venv
  ```
* Install pip in not installed
  ```
  $ sudo apt install python3-pip
  $ pip3 --version
  $ pip 9.0.1 from /usr/lib/python3/dist-packages (python 3.6)
  ```
* It's recommended to python virtual environment to install the package as the tool will install other dependencies.
  ```
  $ python3 -m venv venv
  $ source venv/bin/activate
  ```

    - taqa --on-gitlab docker
    - deactivate
    - rm -rf venv
python3 -m venv venv ; source venv/bin/activate ; python3 -m pip install --upgrade pip ; pip3 install cli-tool/,

pip3 install -e .

## Install Randomizer cli-tool
* clone repo from GitHub to your favorite directory.
  ```
  $ git clone http://github/.../repoName.git 
  ```
* Install Randomizer python package
  ```
  pip3 install -e .
  ```
* python3 -m venv venv
* amr@probe:~/myWork$ source venv/bin/activate

```
Example-1: $ randomize --randomize true --startValue 3 --endValue 22
Displaying randomized list: [ startValue=3  -- endValue=20 ]
[16, 12, 9, 13, 8, 5, 14, 17, 7, 19, 18, 20, 11, 15, 3, 6, 10, 4]

Example-2: $ randomize -r false -s 15 -e 20
Displaying sorted list: [ startValue=15  -- endValue=20 ]
[15, 16, 17, 18, 19, 20]
```


## Uninstall
    - pip3 uninstall cli-tool 
    - deactivate 
    - rm -rf venv  

pip3 uninstall cli-tool ; deactivate ; rm -rf venv  ; python3 -m venv venv ; source venv/bin/activate ; python3 -m pip install --upgrade pip ; pip3 install cli-tool/,

 

### Tasks Checklist

- [x] CLI tool
- [x] Run on Linux
- [x] Run on MacOS
- [x] Uploaded to GitHub


# Email of task desc

My name is Dulcie and I am a Senior Hiring Coordinator here at Adjust. I will be taking over from Jemma in coordinating your next interview steps for the DevOps Engineer position.

Thanks for taking the time to chat with Aurelia. As anticipated in the call, the next step in the process is for you to take our home task (attached), which is an extract of what you will typically work on.

Please submit your finished solution (GitHub Link) through the Greenhouse link found at the bottom of this email. Kindly make your repo public so that the team can access it, but don't mention anywhere that it's a part of the Adjust recruiting process. ;)

Reminder: We understand that you might have other commitments on your side and give you therefore 3 working days to complete the task (so ideally by Fri 9 July). If you don’t have the opportunity to complete the task right now, please let us know. We will put your profile on hold and you can get in touch with us again once you are able to start the task. If you decide not to proceed with the task, please let us know as well.

We hope that the task intrigues you to learn more about the position and we’re looking forward to your submission!


Please write a simple CLI application in the language of your choice that does the
following:
+ Print the numbers from 1 to 10 in random order to the terminal.
+ Please provide a README that explains in detail how to run the program on
MacOS and Linux.

2. Imagine a server with the following specs:
+ 4 times Intel(R) Xeon(R) CPU E7-4830 v4 @ 2.00GHz
+ 64GB of ram
+ 2 TB HDD disk space
+ 2 x 10Gbit/s nics

The server is used for SSL offloading and proxies around 25000 requests per second.
Please let us know which metrics are interesting to monitor in that specific case and how
would you do that? What are the challenges of monitoring this?
Please send us your solution as a GitHub project.

