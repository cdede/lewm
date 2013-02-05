#!/usr/bin/python
import os
try:
    from lib_lewm.main import main1
except ImportError:
    os.sys.path.append(os.curdir)
    from lib_lewm.main import main

if __name__ == "__main__":
    main('~/lewm/config')