"""
    The main script file to launch the pysines application
"""
import sys
import argparse

def create_parser():
    """
    Create the Argument Parser for this script
    :return:  An argparse.ArgumentParser instance
    """
    parser = argparse.ArgumentParser('pysines', description="")
    return parser

def parse_args(args):
    """
    Perform the actual argument parsing, useful for testing the parser
    :return: An argparse.Options namespace
    """
    parser = create_parser()
    return parser.parse_args(args)

def run(options):
    """
    Run the actual script
    :param options: Parsed options namespace
    :return:
    """

    pass


if __name__ == '__main__':
    # Script has been launched

    options = parse_args(sys.argv)
    run(options)