#!/usr/bin/env python
import sys
import helloworld.main
import os

if __name__ == '__main__':
    print "hello1"
    print os.environ["AW_PASSWORD"]
    sys.exit(helloworld.main.main())
