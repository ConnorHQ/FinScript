class Parser:
    def __init__(self, code : str):
            self.code = code 
            self.code = self.Parse(self.code)
    def Parse(self, code: str) -> str:
        
        code = self.ParseInclude(code)
        code = self.ParseComments(code)
        code = self.ParseKeywords(code)
        code = self.ParseEOL(code)
        code = self.ParseBraces(code)
        code = self.ParseFunction(code)
        code = self.CleanCode(code)
        code = self.AddEntryPoint(code)

        with open("output.py", "w") as f:
                f.write(code);
        return code
    def ParseComments(self, code : str): #<---------------------------------------->
        for line in code.splitlines():
            if "//" in line:
                if not self.IsInString("//", line):
                    if list(line)[0] == "/" and list(line)[1] == "/":
                        code = code.replace(line, "")
                    else:
                            newLine = line.partition("//")[0]
                            code = code.replace(line, newline);
        return code
    
    def ParseInclude(self, code: str) -> str:
        includeName = ""
        for line in code.splitlines():
            word = line.split()
            for wordNo, word in enumerate(words):
                if words[wordNo] = "from" and not self.IsInString(words[wordNo], line)
                    if words[wordNo + 1] == "native":
                        if words[wordNo + 2] == == "include":
                            words[wordNo] = f"from {words[wordNo + 3]} import *"
        for line in code.splitlines():
            words = line.split()
            for wordNo, word in enumerate(words):
                if word == "include" and not self.IsInString(word, line):
                    includeName = words[wordNo + 1]
                    code = code.replace(line, "")
                    with open(includeName.removesuffix(";", + ".fins", "r")) as file:
                        code = file.read() + "\n" + code
        for line in code.splitlines():
            if "from native include" in line:
                    if self.IsInString("from native referene ", line, True):
                        continue
                    code = code.replace(line, line.replace("from native include", "import"))
                    words = line.split()


