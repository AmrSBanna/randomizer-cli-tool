"""
########################################################################################################################
##                                                                                                                    ##
##                           Copyright (C) 2021 Adjust GmbH.  All rights reserved.                                    ##
##                           Created on 06.07.2021 by @author: amr.banna@gmail.com                                    ##
##                                                                                                                    ##
########################################################################################################################
"""
import argparse
import sys
from randomize.randomizer import Randomizer
from .colors import Colors 


class CliException(Exception):
    pass


class Cli:
    def __init__(self):

        self.numbersList = []
        self.cliToolDesc = f'Randomizer is a cli-tool that used to print randomized a numbers from a range of numbers.'\
                           f' This range could be also provided as arguments in the CLI (Default range is 1..10). It ' \
                           f'prints the list of numbers randomized or not based on the argument of (-r) ' \
                           f'\n\n' \
                           f'{Colors.UNDERLINE}{Colors.OKCYAN}Example-1:{Colors.ENDC} $ randomize --randomize true ' \
                           f'--startValue 3 --endValue 20' \
                           f'\n' \
                           f'Displaying randomized list: [ startValue=3  -- endValue=20 ]' \
                           f'\n' \
                           f'[16, 12, 9, 13, 8, 5, 14, 17, 7, 19, 18, 20, 11, 15, 3, 6, 10, 4]' \
                           f'\n' \
                           f'{Colors.UNDERLINE}{Colors.OKCYAN}Example-2:{Colors.ENDC} $ randomize -r false -s 15 -e 20'\
                           f'\n' \
                           f'Displaying sorted ' \
                           f'list: [ startValue=15  -- endValue=20 ]' \
                           f'\n' \
                           f'[15, 16, 17, 18, 19, 20]' \
                           f'\n'

        print(self.validate_arguments(self.parse_arguments()).numbersList)

    def parse_arguments(self):
        """
        This method parses values of the command line arguments

        :param: none
        :return: Parser object
        """
        # Parse arguments from CLI
        parser = argparse.ArgumentParser(self.cliToolDesc)
        parser.add_argument("-r", "--randomize", help="[true | false] randomize if true (default=true)")
        parser.add_argument("-s", "--startValue", help="Start value Integer format (default=1)")
        parser.add_argument("-e", "--endValue", help="End value Integer format (default=10)")

        return parser

    @staticmethod
    def validate_arguments(parser):
        """
        This method...
         1. validates the values of the command line arguments
         2. sets default values start=1, end=10, randomize=True

        :param: none
        :return: Randomizer object
        """
        # Set defaults
        start, end = 1, 10
        args = parser.parse_args()

        # Print help msg if no argument used
        if len(sys.argv) == 1:
            parser.print_help(sys.stderr)
            sys.exit(1)

        # validate passed argument randomize
        if args.randomize.lower() == "true" or args.randomize.lower() is None:
            randomize = True
        elif args.randomize.lower() == "false":
            randomize = False
        else:
            parser.print_help(sys.stderr)
            print(f'{Colors.FAIL}{Colors.UNDERLINE}EXECUTION FAILED:{Colors.ENDC} Wrong value for (-r) has been used')
            sys.exit(1)
            # We could have used raise ArgumentTypeError but it looks inconvenient to user
            # raise argparse.ArgumentTypeError("Wrong value for '-r' has been used")

        # Convert passed arguments startValue & endValue to int otherwise set to default
        if args.startValue:
            start = int(args.startValue)
        if args.endValue:
            end = int(args.endValue)

        # validate end > start
        if start > end:
            print(f'{Colors.FAIL}{Colors.UNDERLINE}EXECUTION FAILED:{Colors.ENDC} startValue={start} (>=) is greater '
                  f'than or equal to endValue={end}. Please use valid startValue > endValue')
            sys.exit(1)

        return Randomizer(randomize, start, end)


def main():
    Cli()