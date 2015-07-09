"""
    The main script file to launch the pysines application
"""
import sys
import os
import argparse
from matplotlib import pyplot as plt
import numpy as np

def check_options(options):
    """
    Check that the options are sane and restricted to the project specs
    :param options: An `argparse.Namespace` object
    :return:
    """
    plot_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, 'plots'))

    n_options = len(options)
    if n_options == 0:
        file_option = 'None'
        num_option = 1
        save_option = 0;
    elif n_options == 1:
        file_option = options[0]
        num_option = 1
        save_option = 1;
    else:
        file_option = options[0]
        num_option = options[1]
        save_option = 1;
    
   

    if save_option != 0:
        time = np.linspace(0, 6 * np.pi)
        data = 2 * np.sin(time) + 3 * np.cos(time)
        if num_option == 1:
            plt.plot(time, data, '-b')
        elif num_option == 2:
            plt.plot(time, data, '-b', time*2, data, '-r')
        else:
            plt.plot(time, data, '-b', time*2, data, '-r',time*3, data, '-g')
        plt.title('A title')
        plt.xlabel('Time')
        plt.ylabel('Data')
        plot_name = os.path.join(plot_dir, "{}.png".format(file_option))
        plt.savefig(plot_name)
    
    print save_option

def create_parser():
    """
    Create the Argument Parser for this script
    :return:  An `argparse.ArgumentParser` instance
    """
    parser = argparse.ArgumentParser('pysines', description="")
    return parser

def parse_args(args):
    """
    Perform the actual argument parsing, useful for testing the parser
    :param args: The list of arguments to parse, something like `sys.argv`
    :return: An `argparse.Namespace` object
    """
    parser = create_parser()
    return parser.parse_args(args)

def run(options):
    """
    Run the actual script
    :param options: An `argparse.Namespace` object
    :return:
    """

    # Do some additional check on the options
    check_options(options)

    pass


if __name__ == '__main__':
    # Script has been launched
    options=['file1',2]
    check_options(options)    
    
    options = parse_args(sys.argv)
    
    run(options)