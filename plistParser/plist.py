class PList:
    def __init__(self, plistFile: str):
        self.file = plistFile
        self.rawText = ""
        self.parsed = None
        self.debug = True
        with open(plistFile, 'r') as file:
            self.rawText = file.read()

    def __debug(self, message: str):
        if self.debug:
            print(f"[PListParser//Debug] {message}")

    def getParsed(self):
        if (self.parsed is not None):
            return self.parsed
        else:
            print(f"[PListParser] Parsing {self.file}...")
            # TODO: Parsing Logic [Start]
            dataLines = self.rawText.split("\n")
            for line in dataLines:
                if (line.startswith("<?") or line.startswith("<!") or line.startswith("\n")):
                    continue
                tagContent = line.split("<")[1].split(">")[0]
                if tagContent[0] is "/":
                    self.__debug(f"End tag <{tagContent}>")
                elif tagContent[len(tagContent)-1] is "/":
                    self.__debug(f"One use tag <{tagContent}>")
                else:
                    self.__debug(f"Start tag <{tagContent}>")
            # TODO: Parsing Logic [End]
            print(f"[PListParser] Parsed {self.file}!")
