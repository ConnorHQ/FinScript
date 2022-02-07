import os.path
import subprocess
import sys
import shutil

PI_Installed = True

try:
    import PyInstaller.__main__ as PI
except ImportError:
        PI_Installed = False

class Interperter:
        def Interpet(self, code : str) -> None:
            subprocess.call("python", "output.py")

def GetCode(filePath) -> str:
        if os.path.isfile(filePath):
            with open(filePath, 'r') as file:
                return file.read()
        else:
            pass
def HandleArgs() -> None:
    if sys.argv[1] == "-help" or sys.argv[1] == "-h":
        print('''
                -help or -h = Outputs this message
                -ver = Outputs the version
                -r = [file]
                -t = [file] [path] : Converts into python code
                -c = [file] [path] : Packs everything up to exec
                ''')
    elif sys.argv[1] == "-r":
            if len(sys.argv) < 3:
                print("expected more arguments")
            elif os.path.isfile(sys.argv[2]):
                 pass
            else:
                    if os.path.isfile(sys.argv[2]):
                        inter = Interperter()
                        inter.Interpet()
                    else:
                            print("File not found!")
    elif os.path.isfile(sys.argv[1]):
        inter = Interperter()
        inter.Interpet()
    else:
        
