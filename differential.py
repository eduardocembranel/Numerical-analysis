from __future__ import division, print_function
from numpy import *
from decimal import Decimal

__all__ = ["euler", "euler_iter", "heun_iter", "rk2_heun", "rk2_midpoint",
           "rk2_ralston", "rk4"]

def euler(func, x, y, x_max, h):
   """
   """
   n = 0
   print('\nn = 0\n  x0 = {}\n  y0 = {}'.format(x, y))
   while x < x_max:
      n += 1
      y  = y + h * func(x, y)
      x += h
      print('\nn = {}\n  x{} = {}\n  y{} = {}'.format(n, n, x, n, y))

#erro absoluto
def euler_iter(func, x, y, x_max, h, err):
   """
   """
   n = 0
   print('\nn = 0 x0 = {}\n  y0 = {}'.format(x, y))
   while x < x_max:
      n += 1
      y0 = y
      y = y + h * func(x, y)
      y_prev = y
      x += h
      print('\nn = {} x{} = {}'.format(n, n, x))
      while True:
         y_pos = y0 + h * func(x, y_prev)
         print('  y{} = {}\n  y{} = {}\n  Erro = {}\n'.format(
            n, y_prev, n, y_pos, abs(y_pos - y_prev)))
         if abs(y_pos - y_prev) < err: break
         y_prev = y_pos

def heun_iter(func, x, y, x_max, h, err):
   """
   """
   n = 0
   print('\nn = 0 x0 = {}\n  y0 = {}'.format(x, y))
   while x < x_max:
      n        += 1
      y0        = y
      slope     = func(x, y)
      y         = y + h * slope
      x        += h
      slope_end = func(x, y)
      y         = y0 + (h/2) * (slope + slope_end)
      y_prev    = y
      print('\nn = {} x{} = {}'.format(n, n, x))
      it = 0
      while True:
         y_pos = y0 + (h/2) * (slope + func(x, y_prev))
         print('  y{} = {}\n  y{} = {}\n  Erro = {}\n'.format(
            n, y_prev, n, y_pos, abs(y_pos - y_prev)/y_pos))
         if abs(y_pos - y_prev)/y_Pos < err: break
         y_prev = y_pos
         it += 1
         if it == 15: break
    #  y = y_pos #se deixar isso funciona, porem o primeiro valor de y das 
                #tabelas n bate
                #se tirar isso o ultimo valor da tabela n bate, porem o
                #primeiro sim
                #......


def rk2_heun(func, x, y, x_max, h):
   n = 0
   print('\nn = 0\n  x0 = {}\n  y0 = {}'.format(x, y))
   while x < x_max:
      n       += 1
      k1       = func(x, y)
      k2       = func(x + h, y + h * k1)
      y        = y + (h/2) * (k1 + k2)
      x       += h
      print('\nn = {}\n  x{} = {}\n  y{} = {}'.format(n, n, x, n, y))

def rk2_midpoint(func, x, y, x_max, h):
   n = 0
   print('\nn = 0\n  x0 = {}\n  y0 = {}'.format(x, y))
   while x < x_max:
      n       += 1
      k1       = func(x, y)
      k2       = func(x + Decimal(0.5) * h, y + Decimal(0.5) * k1 * h)
      y        = y + k2 * h
      x       += h
      print('\nn = {}\n  x{} = {}\n  y{} = {}'.format(n, n, x, n, y))
        
def rk2_ralston(func, x, y, x_max, h):
   n = 0
   print('\nn = 0\n  x0 = {}\n  y0 = {}'.format(x, y))
   while x < x_max:
      n       += 1
      k1       = func(x, y)
      k2       = func(x + Decimal(3/4) * h, y + Decimal(3/4) * k1 * h)
      y        = y + h * (Decimal(1/3) * k1 + Decimal(2/3) * k2)
      x       += h
      print('\nn = {}\n  x{} = {}\n  y{} = {}'.format(n, n, x, n, y))

def rk4(func, x, y, x_max, h):
   n = 0
   print('\nn = 0\n  x0 = {}\n  y0 = {}'.format(x, y))
   while x < x_max:
      n       += 1
      k1       = func(x, y)
      k2       = func(x + (h/2), y + (h/2) * k1)
      k3       = func(x + (h/2), y + (h/2) * k2)
      k4       = func(x + h, y + h * k3)
      y        = y + Decimal(h/6) * (k1 + 2 * k2 + 2 * k3 + k4)
      x       += h
      print('\nn = {}\n  x{} = {}\n  y{} = {}'.format(n, n, x, n, y))