from plistParser.plist import PList
import sys

plist = None

if len(sys.argv) is 3:
    if sys.argv[2] == 'true':
        plist = PList(sys.argv[1], True)
    elif sys.argv[2] == 'false':
        plist = PList(sys.argv[1], False)
elif len(sys.argv) is 2:
    plist = PList(sys.argv[1])

print(plist.getParsed())
