#
# License: BSD
#    https://raw.githubusercontent.com/stonier/vcs_extras/devel/LICENSE
#
##############################################################################
# Documentation
##############################################################################

"""
Find and fetch the contents of an indexed .repo file.
"""

##############################################################################
# Imports
##############################################################################

import argparse

##############################################################################
# Methods
##############################################################################


def parse_args(args):
    """
    Execute the command given the incoming args.
    """
    print("Execute find")


def add_subparser(subparsers):
    """
    Add our own argparser to the parent.

    :param subparsers: the subparsers factory from the parent argparser.
    """
    subparser = subparsers.add_parser(
        "find",
        description="""Find and fetch the contents of a .repos file in the version control index yaml.""",
        help="search and retrieve from the version control index",  # this shows in the parent parser
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
        )
    subparser.set_defaults(func=parse_args)
    # add = subparser.add_argument
