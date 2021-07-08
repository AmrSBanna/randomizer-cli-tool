# Randomizer CLI-TOOL README 
Randomizer cli-tool is a simple tool that's used to print a list of numbers randomized or sorted. The list of numbers 
is range that starts with startValue (default=1) and ends with endValue (default=10). Nonetheless, the tool provides 
the possibility to select any range based the values of the arguments. In addition to that it prints the list 
randomized or ordered based on the (--randomize) argument value

The tool written python and packaged as a python package that can be installed on MacOS or Linux like any other popular 
python packages using pip3. 

## Installation Pre-requisites: 
* This tool has been developed using Python 3.6.9 on Ubuntu	18.04 (bionic). Please find the appropriate package manager 
  if you other Linux distro.

* **_Linux:_** 
  - Install python3 virtualenv if not installed
  
    ```
    $ apt install python3-venv
    ```
  - Install pip in not installed
    ```
    $ sudo apt install python3-pip
    $ pip3 --version
    $ pip 9.0.1 from /usr/lib/python3/dist-packages (python 3.6)
    ```
* **_MacOS:_** 
  - Install python3. _Pip3 is installed with Python3_
    ```
    $ brew install python3
    ```
  - To install virtualenv via pip run:
    ```
    $ pip3 install virtualenv
    ```
* Perform these step on **_MacOS_** & **_Linux_**. They are identical
  * It's always highly recommended to use python virtualenv to install the package as the tool will install other
    dependencies.
    ```
    $ python3 -m venv venv
    $ source venv/bin/activate
    ```
## Install Randomizer cli-tool
* clone repo from GitHub to your favorite directory.
  ```
  $ git clone git@github.com:AmrSBanna/randomizer-cli-tool.git
  ```
* Install Randomizer python package
  ```
  pip3 install -e .
  ```
* Now you're to enjoy the randomization   
* How to use the tool by example?

  ```  
  Example-1: 
  $ randomize --randomize true --startValue 3 --endValue 22
  Displaying randomized list: [ startValue=3  -- endValue=20 ]
  [16, 12, 9, 13, 8, 5, 14, 17, 7, 19, 18, 20, 11, 15, 3, 6, 10, 4]

  Example-2: 
  $ randomize -r false -s 15 -e 20
  Displaying sorted list: [ startValue=15  -- endValue=20 ]
  [15, 16, 17, 18, 19, 20]
  ```

## Uninstall & Cleanup
* Execute the steps below to uninstall the tool and clean-up the virtualenv
  ```
  $ pip3 uninstall randomize 
  $ deactivate 
  $ rm -rf venv
  ```  

### Tasks Checklist

- [x] Develop CLI tool
- [x] Run on Linux
- [x] Run on MacOS
- [x] Uploaded to GitHub

