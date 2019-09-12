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

# print(plist.getParsed())
testData = {'Comment': 'This is a test PList used for testing the PList Parser. Internal use only.', 'Embed Dict': {'Embed Array': [0, 'Testing', True, {'Hello': 'There'}]}, 'Second Dict': {'Data': 'DATA-Aq0000='}}
print("// Parsing")
print(plist.getParsed())
print("\n// Encoding")
print(plist.encodeDict(testData))
# plist.encodeDict(testData)
