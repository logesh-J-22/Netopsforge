# Copyright (c) 2025-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

from .five import pyMajor, pyMinor

if (pyMajor, pyMinor) < (3, 10):
    msg = "Python 3.10 or newer is required (found {0}.{1})".format(pyMajor, pyMinor)
    raise Exception(msg)
