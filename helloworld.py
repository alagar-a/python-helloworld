#!/usr/bin/env python
import sys
import helloworld.main
import os

if __name__ == '__main__':
    print "hello1"
    variables = os.environ
    for k in variables.keys():
      print k
      print variables[k]
    sys.exit(helloworld.main.main())
