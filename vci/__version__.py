#
# License: BSD
#    https://raw.githubusercontent.com/stonier/vci/devel/LICENSE
#
##############################################################################
# Imports
##############################################################################

import pkg_resources

##############################################################################
# Version
##############################################################################

# When changing, also update setup.py
__version__ = pkg_resources.require('vci')[0].version
