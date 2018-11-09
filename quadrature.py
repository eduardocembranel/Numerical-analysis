from __future__ import division, print_function
import numpy.polynomial.legendre as legendre
from math import *

__all__ = ["quadrature"]

def _func_dt(a, b):
   return (b - a) / 2

def _func_T(a, b, t):
   return a + (b - a) * (t + 1) / 2

def quadrature(func, a, b, n):
   """
   Calcula a integral definida usando quadratura gaussiana.

   Integra a funcao de 'a' para 'b' usando quadratura gaussiana
   obtendo a estimativa de erro

   Parametros
   ----------
   func: funcao
      Uma funcao a ser integrada
   a: float
      Limite inferior da integracao
   b: float
      Limite superior da integracao
   n: int
      Ordem da quadratura gaussiana

   Retornos
   --------
   val: float
      Aproximacao da quadratura gaussiana à integral
   err: float
      Erro

   """
   if n < 1 or n != int(n):
      raise ValueError("'n' deve ser um inteiro > 0") 
   if a != float(a) or b != float(b):
      raise ValueError("intervalo[a,b] deve ser composto por numeros reais")

   #obtem as raizes e pesos para ordem 'n'
   xi, wi = legendre.leggauss(n) 

   a, b = min(a, b), max(a,b)

   val = 0
   for i in range(n):
      x = _func_T(a, b, float(xi[i]))
      val += func(x) * wi[i]

   val *= _func_dt(a, b)
   return val

   """
   falta implementar a parte do erro
   return val, err
   """