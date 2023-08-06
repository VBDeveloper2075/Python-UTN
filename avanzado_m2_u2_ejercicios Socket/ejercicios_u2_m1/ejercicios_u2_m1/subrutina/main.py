import sys
import os
from pathlib import Path
import subprocess


global elproceso
elproceso=""
raiz=Path(__file__).resolve().parent
ruta=os.path.join(raiz, "prueba.py")

the_path=ruta
elproceso=subprocess.Popen([sys.executable, the_path])
elproceso.communicate()