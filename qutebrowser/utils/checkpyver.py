# This file is part of qutebrowser.
#
# qutebrowser is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# qutebrowser is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with qutebrowser.  If not, see <http://www.gnu.org/licenses/>.

"""Check if qutebrowser is run with the correct python version.

This should import and run fine with both python2 and python3.
"""

import sys


# First we check the version of Python. This code should run fine with python2
# and python3. We don't have Qt available here yet, so we just print an error
# to stderr.
def check_python_version():
    """Check if correct python version is run."""
    if sys.hexversion < 0x03030000:
        # We don't use .format() and print_function here just in case someone
        # still has < 2.6 installed.
        version_str = '.'.join(map(str, sys.version_info[:3]))
        sys.stderr.write("Fatal error: At least Python 3.3 is required to run "
                         "qutebrowser, but " + version_str + " is "
                         "installed!\n")
        sys.stderr.flush()
        sys.exit(1)