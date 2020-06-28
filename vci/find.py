#
# License: BSD
#    https://raw.githubusercontent.com/stonier/vci/devel/LICENSE
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
import os
import sys
import urllib.error
import urllib.request
import yaml

from . import common
from . import config
from . import console
from . import index_contents

##############################################################################
# Library Methods
##############################################################################


def parse_index(search_names, index_contents):
    """
    Scan the index for the search names as keys.

    :param [str] search_names : list of keys to search for in the index contents
    :param dict index_contents : the index
    :returns: (names, sources) : names of the keys used and the url's they point to
    :rtype: ([str], [str])
    """
    names = []
    sources = []
    for name in search_names:
        if name in index_contents.keys():
            elements = index_contents[name]
            new_names = []
            new_sources = []
            if (type(elements) is list):
                for element in elements:
                    if element.endswith('.repos'):
                        new_sources.append(element)
                    else:
                        new_names.append(element)
            else:  # single entry
                if elements.endswith('.repos'):
                    new_sources.append(elements)
                else:
                    new_names.append(elements)
            names.extend(new_names)
            sources.extend(new_sources)
            if new_names:
                (new_names, new_sources) = parse_index(new_names, index_contents)
                names.extend(new_names)
                sources.extend(new_sources)
        else:
            raise RuntimeError("not found in the rosinstall database [%s]" % name)
#                    (new_names, new_sources) = parse_database([elements], index_url)
#                        (new_names, new_sources) = parse_database([element], index_url)
#                        names.extend(new_names)
#                        sources.extend(new_sources)
#                    sources.append(elements)
#                    names.extend(new_names)
#                    sources.extend(new_sources)
    return (names, sources)


def _create_yaml_from_key(key, index_url):
    """
    Debugging version of create_yaml_from_key that retuns extra variables for
    printing if required.

    :param str key: key to look up in the index
    :param str index_url: url of the index to look up

    @todo better exception handling than sys.exit now it's a library function

    :returns: tuple of (combined_yaml_contents, name_aliases, urls)
    """
    contents = index_contents.get(index_url)
    try:
        (name_aliases, locations) = parse_index(key, contents)
    except RuntimeError as e:
        console.logerror(str(e))
        sys.exit(1)
    # TODO move this off to a library method when needed
    combined_yaml_contents = {'repositories': {}}
    urls = []
    for l in locations:
        if common.is_url(l):
            urls.append(l)
        else:
            if os.path.isabs(l):
                urls.append("file://" + l)
            else:
                urls.append(os.path.dirname(index_url) + "/" + l)
    for url in urls:
        try:
            # Note : vcstools.common (underneath wstool) has some interesting
            # functions which let this fall back to handling via netrc
            response = urllib.request.urlopen(url)
            raw_text = response.read()
            yaml_contents = yaml.load(raw_text, Loader=yaml.FullLoader)
            combined_yaml_contents['repositories'].update(yaml_contents['repositories'])
        except urllib.error.URLError as unused_e:
            console.logwarn("url not found, skipping [{0}]".format(url))
    return (combined_yaml_contents, name_aliases, urls)


def create_yaml_from_key(key):
    """
    Lookup the specified key in the current index and return
    the list of all repository details combined in a single yaml dict.

    To convert this to a single string suitable for passing to 'vcs import',
    simply dump the yaml dict, for example:

    .. code-block::python

       yaml.dump(create_yaml_from_key(key)))

    """
    (combined_yaml_contents, unused_name_aliases, unused_urls) = _create_yaml_from_key(key, config.get_index_url())
    return combined_yaml_contents


##############################################################################
# Command Line Tool
##############################################################################


def examples_string():
    examples = console.bold + "Examples\n\n" + console.reset  \
        + "  1) Raw Yaml of the ECL repos\n\n" \
        + console.cyan + "      vci find " + console.yellow + "ecl\n\n" + console.reset \
        + "  2) Detailed Information\n\n" \
        + console.cyan + "      vci find " + console.yellow + "--verbose ecl\n\n" + console.reset \
        + "  3) Piping Into vcs\n\n" \
        + console.cyan + "      vci find " + console.yellow + "| vcs import\n\n" + console.reset
    return examples


def parse_args(args):
    """
    Execute the command given the incoming args.
    """
    args.index = config.get_index_url() if args.index is None else args.index
    (combined_yaml_contents, name_aliases, urls) = _create_yaml_from_key(args.key, args.index)
    if args.verbose:
        if name_aliases:
            print(console.bold + "Aliases" + console.reset)
            for name in name_aliases:
                print(console.cyan + "  name" + console.reset + " : " + console.yellow + name + console.reset)
        print(console.bold + "Urls" + console.reset)
        for url in urls:
            print(console.cyan + "  url" + console.reset + " : " + console.yellow + url + console.reset)
        print(console.bold + "Repos" + console.reset)
        for repo_name, repo_details in combined_yaml_contents['repositories'].iteritems():
            print(console.cyan + "  {0}".format(repo_name) + console.reset + " : " + console.yellow + str(repo_details) + console.reset)
    else:
        print(yaml.dump(combined_yaml_contents))


def add_subparser(subparsers):
    """
    Add our own argparser to the parent.

    :param subparsers: the subparsers factory from the parent argparser.
    """
    subparser = subparsers.add_parser(
        "find",
        description="""Find, fetch and print the contents of a .repos file in the version control index yaml.""",
        help="search and retrieve from the version control index",  # this shows in the parent parser
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    subparser.epilog = examples_string()
    subparser.set_defaults(func=parse_args)
    add = subparser.add_argument
    common.add_index_argument(subparser)
    add('--verbose', '-v', action='store_true', default=False, help='Print verbose information (i.e. more than raw yaml)')
    add('key', nargs=1, type=str, help="the key to lookup the index")
