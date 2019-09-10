__header = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<!DOCTYPE plist PUBLIC \"-//Apple//DTD PLIST 1.0//EN\" \"http://www.apple.com/DTDs/PropertyList-1.0.dtd\">\n"

class PList:
    def __init__(self, plistFile: str, debug: bool = False):
        self.file = plistFile
        self.rawText = ""
        self.parsed = None
        self.debug = debug
        with open(plistFile, 'r') as file:
            self.rawText = file.read()

    def __debug(self, message):
        if self.debug:
            print(f"[PListParser//Debug] {str(message)}")

    def getParsed(self):
        if (self.parsed is not None):
            return self.parsed
        else:
            print(f"[PListParser] Parsing {self.file}...")

            # TODO: Parsing Logic [Start]
            dataLines = self.rawText.split("\n")

            root = {}

            previousRoot = root

            currentRoot = root

            key = ""
            value = ""
            nextIsValue = False

            for line in dataLines:
                if (line.startswith("<?") or line.startswith("<!") or line is ""):
                    continue

                line = line.strip()

                lineData = line.split("<")

                for i in range(len(lineData)):
                    content = lineData[i]

                    if content is '':
                        continue
                    tagContent = content.split(">")[0]

                    self.__debug(root)

                    if tagContent[0] is "/":
                        self.__debug(f"End tag <{tagContent}>")
                        if tagContent == '/dict':
                            self.__debug(f"/!\ This tag was a supported data holder. Restoring the root...")
                            temp = previousRoot
                            previousRoot = currentRoot
                            currentRoot = temp

                    elif tagContent[len(tagContent)-1] is "/":
                        self.__debug(f"One use tag <{tagContent}>")

                        if nextIsValue:
                            self.__debug(f"/!\ This tag is a value!")
                            if tagContent == 'true/':
                                value = True
                            elif tagContent == 'false/':
                                value = False
                            nextIsValue = False

                    else:
                        self.__debug(f"Start tag <{tagContent}>")
                        tagData = content.split(">")[1]
                        if tagData != '':
                            self.__debug(f"Tag's data (inline): {tagData}")
                        elif tagContent == 'dict':
                            tagData = {}

                        if nextIsValue:
                            self.__debug(f"/!\ This tag is a value!")
                            value = tagData
                            currentRoot.update({key: value})
                            self.__debug(f"Added new Key-Value: {str(key)}: {str(value)}")
                            if tagContent == 'dict':
                                nextIsValue = True
                            nextIsValue = False

                        if tagContent == 'dict' and nextIsValue:
                            self.__debug(f"/!\ This tag is a supported data holder. Switching the root...")
                            previousRoot = currentRoot
                            currentRoot = tagData
                            nextIsValue = False

                        if tagContent == 'key':
                            key = tagData
                            self.__debug(f"Next tag is a value.")
                            nextIsValue = True
            return root
            # TODO: Parsing Logic [End]

            print(f"[PListParser] Parsed {self.file}!")
