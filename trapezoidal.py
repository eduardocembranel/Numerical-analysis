from __future__ import division, print_function
from math import *

__all__ = ["trapezoidal"]

def trapezoidal(func, a, b, n=1):
   """
   Calcula a integral definida usando regra do trapezio

   Integra a funcao de 'a' para 'b' usando regra do trapezio
   obtendo a estimativa de erro

   Parametros
   ----------
   func: funcao
      Uma funcao a ser integrada
   a: float
      Limite inferior da integracao
   b: float
      Limite superior da integracao
   n: int, opcional
      Quantidade de subintervalos

   Retornos
   --------
   val: float
      Integral definida aproximada pela regra do trapezio
   err: float
      Erro

   """
   if n < 1 or n != int(n):
      raise ValueError("'n' deve ser um inteiro > 0") 
   if a != float(a) or b != float(b):
      raise ValueError("intervalo[a,b] deve ser composto por numeros reais")

   h = (b - a) / n
   val_functions = [func(a), func(b)]
   val = sum(val_functions)

   x = a + h
   for i in range(n - 1):
      val_functions.append(func(x))
      val += val_functions[-1] * 2
      x += h

   val *= h / 2
   max_function = max(map(abs, val_functions))
   err = (b - a) * h ** 2 * max_function / 12

   return val, err