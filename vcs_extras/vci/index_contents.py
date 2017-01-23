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
import collections
import urllib2
import yaml

import vcs_extras.console as console

from . import config

##############################################################################
# Library Methods
##############################################################################


def get(index_url):
    try:
        response = urllib2.urlopen(index_url)
    except urllib2.URLError as unused_e:
        raise urllib2.URLError("index not found [{0}]".format(index_url))
    contents = yaml.load(response.read())
    sorted_contents = collections.OrderedDict(sorted(contents.items(), key=lambda x: x[0]))
    return sorted_contents


def display(index_url, contents=None):
    if contents is None:
        contents = get(index_url)
    print("\n" + console.green + index_url + console.reset + "\n")
    for k, v in contents.iteritems():
        print(console.cyan + "  {0}: ".format(k) + console.yellow + "{0}".format(v) + console.reset)
    print("\n")

##############################################################################
# Command Line Tool
##############################################################################


def parse_args(args):
    """
    Execute the command given the incoming args.
    """
    url = config.get_index_url()
    contents = get(url)
    display(url, contents)


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
