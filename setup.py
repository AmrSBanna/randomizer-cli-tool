"""
########################################################################################################################
##                                                                                                                    ##
##                           Copyright (C) 2021 Adjust GmbH.  All rights reserved.                                    ##
##                           Created on 06.07.2021 by @author: amr.banna@gmail.com                                    ##
##                                                                                                                    ##
########################################################################################################################
"""

#!/usr/bin/env python

import setuptools

setuptools.setup(
  name="randomize",
  version="0.0.1",
  author="Amr Banna",
  author_email="amr.banna@gmail.com",
  description="Randomizer is a cli-tool that used to print randomized a numbers from a range of numbers. This range "
              "could be also provided as arguments in the CLI (Default range is 1..10). It prints the list of "
              "numbers randomized or not based on the argument of '-r' (default=true to randomize)",
  packages=setuptools.find_packages(include=['randomize', 'randomize.*']),
  install_requires=["wheel"],
  zip_safe=False,
  entry_points={"console_scripts": ["randomize = randomize.cli:main"]}
)
