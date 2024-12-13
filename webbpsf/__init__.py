# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""
WebbPSF: Simulated Point Spread Functions for the James Webb Space Telescope
----------------------------------------------------------------------------

WebbPSF produces simulated PSFs for the James Webb Space Telescope, NASA's next
flagship infrared space telescope. WebbPSF can simulate images for any of the
four science instruments plus the fine guidance sensor, including both direct
imaging and coronagraphic modes.

Developed by Marshall Perrin and collaborators at STScI, 2010-2018.

Documentation can be found online at https://webbpsf.readthedocs.io/
"""


import os
import stpsf
import sys
import warnings

warnings.warn(
    """"

    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    THIS LIBRARY HAS BEEN DEPRECATED
    All existing WebbPSF code has been migrated to the STPSF package.
    Please update your code to use STPSF instead of WebbPSF.
    WebbPSF is an alias of STPSF and is running code from the STPSF library.

    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    """,
    DeprecationWarning,
    stacklevel=2,  # Shows the webbpsf import code
)

sys.modules["webbpsf"]=stpsf

os.environ["STPSF_PATH"] = os.environ.get("WEBBPSF_PATH", "")