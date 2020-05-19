#-*- couding:utf-8 -*-


#from cx_Freeze import setup, Executable
from cx_Freeze import setup, Executable
import sys

setup(
    name = "Tux",
    version = "1.0",
    description = "Open Source Teslimat",
    executables = [Executable("tux.py", base = "Win32GUI", icon = "tux.ico")])