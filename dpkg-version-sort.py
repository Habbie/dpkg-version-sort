#!/usr/bin/python
import os, sys

def compare(a,b):
	if os.system("dpkg --compare-versions %s lt %s" % (a,b)): return 1 
	if os.system("dpkg --compare-versions %s gt %s" % (a,b)): return -1
	return 0;

versions = [s.strip() for s in sys.stdin]
versions.sort(cmp=compare)
print '\n'.join(versions)
