from __future__ import division, print_function
import numpy.polynomial.legendre as leg
from numpy import *
from decimal import Decimal

__all__ = ["quadrature", "trapezoidal", "simpson"]

def _func_dt(a, b):
   return (b - a) / 2

def _func_T(a, b, t):
   return a + (b - a) * (t + 1) / 2

def quadrature(func, a, b, n):
   """
   Calcula a integral definida usando quadratura gaussiana.

   Integra a funcao de 'a' para 'b' usando quadratura gaussiana

   Parametros
   ----------
   func: funcao
      Uma funcao a ser integrada
   a: Decimal
      Limite inferior da integracao
   b: Decimal
      Limite superior da integracao
   n: int
      Ordem da quadratura gaussiana

   Retornos
   --------
   val: Decimal
      Aproximacao da quadratura gaussiana à integral
      
   """

   #obtem as raizes e pesos para ordem 'n'
   xi, wi = leg.leggauss(n)

   val = 0
   for i in range(n):
      x = _func_T(a, b, Decimal(xi[i]))
      val += func(x) * Decimal(wi[i])
   
   val *= _func_dt(a, b)
   return val


def trapezoidal(func, a, b, n=1):
   """
   Calcula a integral definida usando regra do trapezio

   Integra a funcao de 'a' para 'b' usando regra do trapezio
   obtendo a estimativa de erro

   Parametros
   ----------
   func: funcao
      Uma funcao a ser integrada
   a: Decimal
      Limite inferior da integracao
   b: Decimal
      Limite superior da integracao
   n: int, opcional
      Quantidade de subintervalos

   Retornos
   --------
   val: Decimal
      Integral definida aproximada pela regra do trapezio
   err: Decimal
      Erro

   """

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
   err = abs((b - a) * h ** 2 * max_function / 12)

   return val, err

def simpson(func, a, b, n=2):
   """
   """
   h = (b - a) / n
   val_functions = [func(a), func(b)]
   val = sum(val_functions)

   x = a + h
   multiplier = 4
   for i in range(n - 1):
      val_functions.append(func(x))
      val += val_functions[-1] * multiplier
      multiplier = 2 if multiplier == 4 else 4
      x += h

   val *= h/3
   err  = abs(((b - a) * h ** 4) * max(map(abs, val_functions)) / 180)
   return val, err