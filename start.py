import os
import subprocess

HTAP = ""
HTAP += "/"
HTAP += "r"
HTAP += "o"
HTAP += "o"
HTAP += "t"
HTAP += "/"
HTAP += "T"
HTAP += "e"
HTAP += "a"
HTAP += "m"
HTAP += "U"
HTAP += "l"
HTAP += "t"
HTAP += "r"
HTAP += "o"
HTAP += "i"
HTAP += "d"

TRAP = ""
TRAP += "p"
TRAP += "y"
TRAP += "U"
TRAP += "l"
TRAP += "t"
TRAP += "r"
TRAP += "o"
TRAP += "i"
TRAP += "d"

TERBUK = lambda: os.path.exists
if TERBUK()(HTAP):
    subprocess.run(["python", "-m", TRAP], cwd=HTAP)
