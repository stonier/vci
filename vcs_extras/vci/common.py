#
# License: BSD
#    https://raw.githubusercontent.com/stonier/vcs_extras/devel/LICENSE
#
##############################################################################
# Documentation
##############################################################################

"""
Common helpers for the vci commands.
"""
##############################################################################
# Imports
##############################################################################

import os
import urlparse

##############################################################################
# Methods
##############################################################################


def home():
    """
    Get directory location of '.vcs_extras' where configuration is stored.

    @return: path to the home directory
    @rtype: str
    """
    home_dir = os.path.join(os.path.expanduser('~'), '.vcs_extras', 'vci')
    if not os.path.exists(home_dir):
        os.makedirs(home_dir)
    return home_dir


def is_url(source_uri):
    """
    Uses heuristics to check whether uri is a url (as opposed to a file path).

    File paths always have empty scheme (e.g. http, file, https) AND
    netloc (e.g. github.com).

    :param str source_uri: string representing web uri or file path
    :returns: bool
    """
    if source_uri is None or source_uri == '':
        return False
    parsed_uri = urlparse.urlparse(source_uri)
    if (parsed_uri.scheme == '' and
        parsed_uri.netloc == '' and
        '@' not in parsed_uri.path.split('/')[0]
        ):
        return False
    return True


def add_index_argument(subparser):
    """

    add = subparser.add_argument
    common.add_index_argument(subparser)
    """
    add = subparser.add_argument
    add('-i', '--index', action='store', default=None, help="override the currently stored index for this call only")




