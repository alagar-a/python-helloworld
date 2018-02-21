#!/usr/bin/env python
import sys
import helloworld.main
import os

if __name__ == '__main__':
    print "hello1"
    print os.environ
    sys.exit(helloworld.main.main())
