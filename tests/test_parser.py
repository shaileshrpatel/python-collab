"""
    We need to test the parser to ensure it handles our use cases correctly and fails when it is supposed to
"""
import sys
import unittest
import argparse

from pysines.main import parse_args

class ParserTest(unittest.TestCase):

    def setUp(self):
        # Redirect stderr to stdout for nose failures on argparsing
        self.stderr = sys.stderr
        sys.stderr = sys.stdout

    def tearDown(self):
        sys.stderr = self.stderr

    def format_args(self, *args):
        """
        Format the arguments to look like they came from sys.argv
        :param args: Optional list of command line arguments
        :return: A list resembling sys.argv
        """
        ret = []
        ret.extend(list(args))
        return ret

    def parse_args(self, *args, **kwargs):
        fail_on_exc = kwargs.get('fail_on_exc', True)
        try:
            return parse_args( self.format_args( *args ) )
        except SystemExit as e:
            if fail_on_exc:
                self.fail( "Parse Error" )
            else:
                raise

    def test_parser_simple(self):
        """
        Check the parser returns a sane type
        :return:
        """

        parser = parse_args( () )

        self.assertIsNotNone( parser )

        self.assertTrue( isinstance( parser, argparse.Namespace ) )

    def test_parser_option_num_long(self):
        """
        Test the --num option to plot a number of sines
        :return:
        """

        parser = self.parse_args('--num=4' )

        self.assertIsNotNone( getattr( parser, 'num', None ) )

        self.assertIsNotNone( parser.num )

        self.assertEqual( parser.num, 4)

    def test_parser_option_num_short(self):
        """
        Check short form, '-n'
        :return:
        """
        parser = self.parse_args( '-n', '4')

        self.assertIsNotNone( getattr( parser, 'num', None ) )

        self.assertIsNotNone( parser.num )

        self.assertEqual( parser.num, 4 )

    def test_parser_option_num_bad_input(self):
        """
        Assert that parser handles bad input correctly
        :return:
        """
        with self.assertRaises(SystemExit):
            parser = self.parse_args('-n', 'jeebus', fail_on_exc=False )

    def test_parser_option_file(self):
        """
        Test the --file option
        :return:
        """
        filename = 'myfile.svg'

        parser = self.parse_args('--file='+filename )

        self.assertIsNotNone( getattr( parser, 'file', None ) )

        self.assertIsNotNone( parser.file )

        self.assertEqual( parser.file, filename)

        # Check short form, '-f'
        parser = self.parse_args( '-f', filename )

        self.assertIsNotNone( getattr( parser, 'file', None ) )

        self.assertIsNotNone( parser.file )

        self.assertEqual( parser.file, filename )

    def test_parser_option_legend(self):
        """
        Test the legend boolean is parsed properly
        :return:
        """

        parser = self.parse_args('--legend')

        self.assertIsNotNone( getattr( parser, 'legend', None ) )

        self.assertIsNotNone( parser.legend )

        self.assertEqual( parser.legend, True)

        # Check short form, '-l'
        parser = self.parse_args( '-l' )

        self.assertIsNotNone( getattr( parser, 'legend', None ) )

        self.assertIsNotNone( parser.legend )

        self.assertEqual( parser.legend, True )


if __name__ == '__main__':
    unittest.main()
