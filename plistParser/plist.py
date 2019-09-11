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

    def __update(self, object, key, value):
        if type(object) is dict:
            object.update({key: value})
        elif type(object) is list:
            object.append(value)

    def getParsed(self):
        if (self.parsed is not None):
            return self.parsed
        else:
            print(f"[PListParser] Parsing {self.file}...")

            # TODO: Parsing Logic [Start]
            dataLines = self.rawText.split("\n")

            root = {}

            previousRoots = [root]
            previousRoot = 0
            currentRoot = root

            key = ""
            value = ""
            nextIsValue = False

            firstValue = False

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

                    #self.__debug(root)

                    if tagContent[0] is "/":
                        self.__debug(f"End tag <{tagContent}>")
                        if tagContent == '/dict' or tagContent == '/array':
                            self.__debug(f"/!\\ This tag was a supported data holder. Exiting the chroot...")
                            previousRoot-=1
                            currentRoot = previousRoots[previousRoot]

                    elif tagContent[len(tagContent)-1] is "/":
                        self.__debug(f"One use tag <{tagContent}>")

                        if nextIsValue:
                            firstValue = True
                            self.__debug(f"/!\\ This tag is a value!")
                            if tagContent == 'true/':
                                value = True
                            elif tagContent == 'false/':
                                value = False
                            self.__update(currentRoot, key, value)
                            self.__debug(f"Added new data: {str(key)}: {str(value)}")
                            nextIsValue = False

                    else:
                        self.__debug(f"Start tag <{tagContent}>")
                        tagData = content.split(">")[1]
                        if tagData != '':
                            self.__debug(f"Tag's data (inline): {tagData}")
                        elif tagContent == 'dict':
                            tagData = {}
                        elif tagContent == 'array':
                            tagData = []

                        if nextIsValue or type(currentRoot) is list:
                            firstValue = True
                            self.__debug(f"/!\\ This tag is a value!")
                            value = tagData
                            if tagContent == 'integer':
                                value = int(value)
                            elif tagContent == 'data':
                                value = 'DATA-'+value
                            self.__update(currentRoot, key, value)
                            self.__debug(f"Added new data: {str(key)}: {str(value)}")
                            nextIsValue = False

                        if tagContent == 'dict' or tagContent == 'array':
                            if firstValue is not False:
                                self.__debug(f"/!\\ This tag is a supported data holder. CHRooting...")
                                previousRoot+=1
                                self.__update(previousRoots, '', currentRoot)
                                currentRoot = tagData

                        if tagContent == 'key':
                            key = tagData
                            self.__debug(f"Next tag is a value.")
                            nextIsValue = True
            return root
            # TODO: Parsing Logic [End]

            print(f"[PListParser] Parsed {self.file}!")

    def encodeDict(self, data: dict):
        root = data

        previousRoots = []
        rootCount = 0
        currentRoot = root

        print(f"[PListParser] Encoding dict into plist...")

        encoded = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<!DOCTYPE plist PUBLIC \"-//Apple//DTD PLIST 1.0//EN\" \"http://www.apple.com/DTDs/PropertyList-1.0.dtd\">\n"
        encoded += "<plist version=\"1.0\">\n"
        def parse(root):
            for object in root:
                print(object)
                if type(root[object]) == dict:
                    previousRoots.append(root)
                    rootCount+=1
                    currentRoot = object
                    self.__debug("/!\\ Found a supported data holder. CHRooting into it.")
