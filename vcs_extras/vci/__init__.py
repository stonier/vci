#
# License: BSD
#    https://raw.githubusercontent.com/stonier/vcs_extras/devel/LICENSE
#
##############################################################################
# Documentation
##############################################################################

"""
Version control index handling from a yaml file on the internet (e.g. github)
"""
##############################################################################
# Imports
##############################################################################

from . import argument_parsing
from . import common
from . import config
from . import index_contents

##############################################################################
# Entry Point
##############################################################################


def main(args=None):
    """
    Main entry point to the command line vci tool.
    """
    try:
        # Create a top level parser
        parser = argument_parsing.get_parser()
        options, unused_unknown_args = parser.parse_known_args(args)
        options.func(options)  # relay arg parsing to the subparser configured `set_defaults` function callback

    except KeyboardInterrupt:
        print('Interrupted by user!')
