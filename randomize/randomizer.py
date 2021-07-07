"""
########################################################################################################################
##                                                                                                                    ##
##                           Copyright (C) 2021 Adjust GmbH.  All rights reserved.                                    ##
##                           Created on 06.07.2021 by @author: amr.banna@gmail.com                                    ##
##                                                                                                                    ##
########################################################################################################################
"""

import os
import sys
import random
import argparse
from .colors import Colors 


class RandomizeException(Exception):
    pass


class Randomizer:
    def __init__(self, randomize=True, start=1, end=10):

        self.start = start
        self.end = end
        self.randomize = randomize

        # Create an empty list
        self.numbersList = []
        self.build_list()
        self.randomize_list()

    def build_list(self):
        """
        This method build a list using start and end values

        :param: none
        :return: none
        """

        # Check if start value is smaller than end value
        if self.start < self.end:
            # unpack the result
            self.numbersList.extend(range(self.start, self.end))
            # Append the last value
            self.numbersList.append(self.end)

    def randomize_list(self):
        """
        This method...
         1. randomizes if True
         2. print random or sorted list

        :param: none
        :return: List
        """
        if self.randomize:
            print(f'Displaying {Colors.OKBLUE}{Colors.UNDERLINE}randomized{Colors.ENDC} list: '
                  f'[ startValue={self.start}  -- endValue={self.end} ]')
            random.shuffle(self.numbersList)
        else:
            print(f'Displaying {Colors.OKBLUE}{Colors.UNDERLINE}sorted{Colors.ENDC} list: '
                  f'[ startValue={self.start}  -- endValue={self.end} ]')

        return self.numbersList
