#/usr/bin/python3

import sys, re

"""
VBS Script to One Line
'.* - Replace comments (lines that starts with ' )
_.*?\n - Replace continuation character that are represented as _ in VBS
\t - Replace tabs
\n - Replace with : (vbs command terminator)
"""


text = sys.stdin.read()
#x = re.findall(r"'(.*?)'", text)
#x = re.findall(r"", text)
p = re.compile("'.*")
t1 = p.sub('',text)

p = re.compile("_.*?\n")
t2 = p.sub('',t1)

p = re.compile("\t")
t3 = p.sub('',t2)

p = re.compile("\n")
t4 = p.sub(':',t3)

print(t4)
