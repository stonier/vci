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
