from plistParser.plist import PList
import sys

plist = PList(sys.argv[1])
print(plist.getParsed())
