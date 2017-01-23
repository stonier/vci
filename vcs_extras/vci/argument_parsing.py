#
# License: BSD
#    https://raw.githubusercontent.com/stonier/vcs_extras/devel/LICENSE
#
##############################################################################
# Documentation
##############################################################################

"""
Arg parse construction.
"""
##############################################################################
# Imports
##############################################################################

import argparse

from . import find
from . import config
from . import index_contents

##############################################################################
# Methods
##############################################################################


def get_parser():
    # Create a top level parser
    parser = argparse.ArgumentParser(
        description="version control index handling", formatter_class=argparse.RawDescriptionHelpFormatter)
    subparsers = parser.add_subparsers(title='commands',
                                       help='valid commands for vci interactions')
    find.add_subparser(subparsers)
    config.add_subparser(subparsers)
    index_contents.add_subparser(subparsers)
    return parser
