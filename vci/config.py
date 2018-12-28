#
# License: BSD
#    https://raw.githubusercontent.com/stonier/vci/devel/LICENSE
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
import os
import sys
import urllib.parse

from . import common
from . import console

##############################################################################
# Constants
##############################################################################

DEFAULT_INDEX_URL = 'https://raw.githubusercontent.com/stonier/vci/repos/kinetic.yaml'

##############################################################################
# Library
##############################################################################


def get_index_url():
    filename = os.path.join(common.home(), "settings")
    try:
        f = open(filename, 'r')
    except IOError:
        return set_index_url(DEFAULT_INDEX_URL)
    index_url = f.read()
    f.close()
    return index_url


def set_index_url(index_url):
    '''
      Set a uri for the vcs index to use for retrieval.
    '''
    # could actually check that it is a valid uri though.
    filename = os.path.join(common.home(), "settings")
    f = open(filename, 'w+', encoding='utf-8')
    try:
        f.write(index_url)
    finally:
        f.close()
    return index_url

##############################################################################
# Command Parser
##############################################################################


def examples_string():
    examples = console.bold + "Examples\n\n" + console.reset  \
        + "  1) Display the current index url\n\n" \
        + console.cyan + "      vci config\n\n" + console.reset \
        + "  2) Set the index to a local file\n\n" \
        + console.cyan + "      vci config " + console.yellow + "file:///home/stonier/kinetic.yaml\n\n" + console.reset \
        + "  3) Set the index to a public github file\n\n" \
        + console.cyan + "      vci config " + console.yellow + "{0}\n\n".format(DEFAULT_INDEX_URL) + console.reset \
        + "  4) Reset the index to the default\n\n" \
        + console.cyan + "      vci config " + console.yellow + "--set-default\n\n" + console.reset
    return examples


def parse_args(args):
    """
    Execute the command given the incoming args.
    """
    if args.set_default:
        set_index_url(DEFAULT_INDEX_URL)
    elif args.url:
        # very simple validation (note netloc is empty for file://)
        result = urllib.parse.urlparse(args.url)
        if not result.scheme:
            console.logerror("invalid url ['{0}']".format(args.url))
            sys.exit(1)
        set_index_url(args.url)
    index_url = get_index_url()
    if args.no_colour:
        print(index_url)
    else:
        print("\n" + console.cyan + "URL " + console.reset + ": " + console.yellow + index_url + console.reset + "\n")


def add_subparser(subparsers):
    """
    Add our own argparser to the parent.

    :param subparsers: the subparsers factory from the parent argparser.
    """
    subparser = subparsers.add_parser(
        "config",
        description="""Manage the list of version control index url's and their keys.""",
        help="manage the version control index list",  # this shows in the parent parser
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    subparser.epilog = examples_string()
    subparser.set_defaults(func=parse_args)
    common.add_nocolour_argument(subparser)
    add = subparser.add_argument
    add('-d', '--set-default', action='store_true', default=False, help='Reset to the default url ({0})'.format(DEFAULT_INDEX_URL))
    add('url', type=str, nargs='?', default="", help='set the url for the index to use for retrieval')
