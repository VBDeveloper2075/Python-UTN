"""
pip install -U setuptools --user

Consideraciones con relación a las versiones:

1) Para especificar bien la versión
2) Para saber de que versiones de otros proyectos depende nuestra versión

VERSIÓN
Una versión consiste en una serie alterna de números de publicación y etiquetas de publicación previa o posterior.
NÚMERO DE PUBLICACIÓN
Un número de publicación es una serie de dígitos separados  por puntos, cómo 2.4 o 0.5
NOTA: Los ceros iniciales dentro de una serie de dígitos se ignoran: 2.01 == 2.1 != 2.0.1
ETIQUETAS PREVIAS O POSTERIORES
Después de un número de versión, puede tener una etiqueta previa o posterior a la liberación.

***** previo ***********   versión  ******  posterior  ****** nueva versión
2.4a1    2.4b1     2.4c1     2.4    --->    2.4-1       --->   2.4.1

PRELANZAMIENTO
Una etiqueta de prelanzamiento es una serie de letras que están alfabéticamente antes de "final".
Ejemplos: alfa, beta, a, c, dev, etc.
2.4c1 == 2.4.c1
2.4rc1 == 2.4pre1 == 2.4preview1

POSTERIORES 
Se suele usar un guión --> Un parche o revisión en la versión
2.4-r1263     versión 2.4 revisón 1263

RECOMENDACIÓN
Para estar seguros del la correlatividad de versiones podemos usar: pkg_resources.parse_version ()

from pkg_resources import parse_version
parse_version('1.9.a.dev') == parse_version('1.9a0dev')
parse_version('2.1-rc2') < parse_version('2.1')




"""
from pkg_resources import parse_version
print(parse_version('1.9.a.dev') == parse_version('1.9a0dev'))
print(parse_version('2.4c1') < parse_version('2.4b1'))

  