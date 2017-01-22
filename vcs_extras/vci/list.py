#
# License: BSD
#    https://raw.githubusercontent.com/stonier/vcs_extras/devel/LICENSE
#
##############################################################################
# Documentation
##############################################################################

"""
Configure version control index settings.
"""

##############################################################################
# Imports
##############################################################################

import argparse
import urllib2
import yaml

import vcs_extras.console as console

from . import config

##############################################################################
# Methods
##############################################################################


def list_index_database(index_url):
    try:
        response = urllib2.urlopen(index_url)
    except urllib2.URLError as unused_e:
        raise urllib2.URLError("index not found [{0}]".format(index_url))
    contents = yaml.load(response.read())
    sorted_contents = contents.keys()
    sorted_contents.sort()
    print("\n" + console.green + index_url + console.reset + "\n")
    for r in sorted_contents:
        print(console.cyan + "  {0}: ".format(r) + console.yellow + "{0}".format(contents[r]) + console.reset)
    print("\n")


def parse_args(args):
    """
    Execute the command given the incoming args.
    """
    index_url = config.get_index()
    list_index_database(index_url)


def add_subparser(subparsers):
    """
    Add our own argparser to the parent.

    :param subparsers: the subparsers factory from the parent argparser.
    """
    subparser = subparsers.add_parser(
        "list",
        description="""List the contents of the index.""",
        help="display each key, url in the current index",  # this shows in the parent parser
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    subparser.set_defaults(func=parse_args)
