#py -m pip install --upgrade pip
#pip install --upgrade setuptools --user
#pip install --upgrade build

import sys
#import ver
#sys.path.append("D:\\PythonDev\\E-Learning-Python\\Python Intermedio\\Unidad 2")
"""import os
BASE_DIR = os.path.dirname((os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(BASE_DIR)
sys.path.append(BASE_DIR)
print(">>>>>>", BASE_DIR)"""

from NicolasPack import ver

#print(sys.path)
ver.imprimir("".join(sys.argv[1:]))