from __future__ import division, print_function
import sys
import quadrature as qd
import trapezoidal as tz
from math import *
import re

if __name__ == '__main__':
   rep = {"sen":      "sin",
         "seno":      "sin",
         "cosseno":   "cos",
         "tangente":  "tan",
         "tang":      "tan",
         "ln":        "log",
         "^":         "**"
         }

   f = input('insira a funcao: ')
   a = float(input('insira a: '))
   b = float(input('insira b: '))
   n = int(input('insira n: '))

   rep = dict((re.escape(k), v) for k, v in rep.items())
   pattern = re.compile("|".join(rep.keys()))
   f = pattern.sub(lambda m: rep[re.escape(m.group(0))], f)

   fx = lambda x: eval(f)

   print(tz.trapezoidal(fx, a, b, n))