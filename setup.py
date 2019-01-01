import sys
from cx_Freeze import setup, Executable


base = None
if sys.platform == "win64":
    base = "Win64GUI"

executables = [
        Executable("Calculadora.py", base=base)
]

buildOptions = dict(
        packages = [],
        includes = [],
        include_files = [],
        excludes = []
)




setup(
    name = "Calculadora",
    version = "1.0",
    description = "Calculadora simples",
    options = dict(build_exe = buildOptions),
    executables = executables
 )
