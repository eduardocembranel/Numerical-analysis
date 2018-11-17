from __future__ import division, print_function
from integrate import quadrature as qd
from integrate import trapezoidal as tz
from integrate import simpson as simps
from differential import *
from decimal import Decimal
from numpy import *
import os
import re

__all__ = ["call_quadrature", "call_gauss1", "call_gauss2", "call_trapz", 
         "call_trapzRep", "call_simps", "call_simpsRep", "call_euler",
         "call_euler_iter", "call_heun_iter", "call_heun", "call_midpoint",
         "call_ralston", "call_rk", "call_help", "clear", "press_return"]

def clear():
   os.system('cls')

def press_return():
   input('\nPressione ENTER para retornar...')

def format_input(string):
   rep = {"seno":     "sin",
         "sen":       "sin",
         "cosseno":   "cos",
         "tangente":  "tan",
         "tang":      "tan",
         "ln":        "log",
         "^":         "**"
         }

   float_elem = re.findall("\d+\.\d+", string)
   for key in float_elem:
      value    = 'Decimal(' + str(key) + ')'
      rep[key] = value

   rep = dict((re.escape(k), v) for k, v in rep.items())
   pattern = re.compile("|".join(rep.keys()))
   string = pattern.sub(lambda m: rep[re.escape(m.group(0))], string)

   return string

def call_help():
   clear()
   print('blablablal')
   press_return()

def call_quadrature():
   clear()
   print('[Quadratura Gaussiana]\n')
   
   f = input('Funcao: ')
   a = Decimal(input('a: '))
   b = Decimal(input('b: '))
   n = int(input('n: '))
   f = format_input(f)
   
   try:
      x = 0
      eval(f)
   except (NameError, SyntaxError) as e:
      print('Erro, funcao invalida!')
   else:
      fx = lambda x: eval(f)
      print('\nS =', qd(fx, a, b, n), '\n')

   press_return()
   

def call_gauss1():
   clear()
   print('[Gauss - primeira ordem]\n')
   
   f = input('Funcao: ')
   f = format_input(f)
   
   try:
      x = 0
      eval(f)
   except (NameError, SyntaxError) as e:
      print('Erro, funcao invalida!')
   else:
      fx = lambda x: eval(f)
      print('\nS =', qd(fx, Decimal(-1), Decimal(1), 1), '\n')

   press_return()

def call_gauss2():
   clear()
   print('[Gauss - segunda ordem]\n')
   
   f = input('Funcao: ')
   f = format_input(f)
   
   try:
      x = 0
      eval(f)
   except (NameError, SyntaxError) as e:
      print('Erro, funcao invalida!')
   else:
      fx = lambda x: eval(f)
      print('\nS =', qd(fx, Decimal(-1), Decimal(1), 2), '\n')

   press_return()
   
def call_trapz():
   clear()
   print('[Regra do Trapezio]\n')
   
   f = input('Funcao: ')
   a = Decimal(input('a: '))
   b = Decimal(input('b: '))
   f = format_input(f)
   
   try:
      x = 0
      eval(f)
   except (NameError, SyntaxError) as e:
      print('Erro, funcao invalida!')
   else:
      fx = lambda x: eval(f)
      val = tz(fx, a, b)
      print('\nS = {}\n'.format(val))

   press_return()
   
def call_trapzRep():
   clear()
   print('[Regra do Trapezio repetido]\n')
   
   f = input('Funcao: ')
   a = Decimal(input('a: '))
   b = Decimal(input('b: '))
   n = int(input('n: '))
   f = format_input(f)
   
   try:
      x = 0
      eval(f)
   except (NameError, SyntaxError) as e:
      print('Erro, funcao invalida!')
   else:
      fx = lambda x: eval(f)
      val = tz(fx, a, b, n)
      print('\nS = {}\n'.format(val))
      
   press_return()

def call_simps():
   clear()
   print('[1/3 de Simpson]\n')
   
   f = input('Funcao: ')
   a = Decimal(input('a: '))
   b = Decimal(input('b: '))
   f = format_input(f)
   
   try:
      x = 0
      eval(f)
   except (NameError, SyntaxError) as e:
      print('Erro, funcao invalida!')
   else:
      fx = lambda x: eval(f)
      val = simps(fx, a, b)
      print('\nS = {}\n'.format(val))

   press_return()


def call_simpsRep():
   clear()
   print('[1/3 de Simpson repetido]\n')
   
   f = input('Funcao: ')
   a = Decimal(input('a: '))
   b = Decimal(input('b: '))
   n = int(input('n: '))
   f = format_input(f)
   
   try:
      x = 0
      eval(f)
   except (NameError, SyntaxError) as e:
      print('Erro, funcao invalida!')
   else:
      fx = lambda x: eval(f)
      val = simps(fx, a, b, n)
      print('\nS = {}\n'.format(val))

   press_return()

def call_euler():
   clear()
   print('[Metodo de Euler]\n')
   
   f  = input('Funcao: ')
   xi = Decimal(input('xi: '))
   xf = Decimal(input('xf: '))
   yi = Decimal(input('yi: '))
   h  = Decimal(input('h:  '))
   f  = format_input(f)
   
   try:
      x = y = 0
      eval(f)
   except (NameError, SyntaxError) as e:
      print('Erro, funcao invalida!')
   else:
      fxy = lambda x, y: eval(f)
      euler(fxy, xi, yi, xf, h)

   press_return()

def call_euler_iter():
   clear()
   print('[Metodo de Euler iterativo]\n')
   
   f   = input('Funcao: ')
   xi  = Decimal(input('xi: '))
   xf  = Decimal(input('xf: '))
   yi  = Decimal(input('yi: '))
   h   = Decimal(input('h:  '))
   err = Decimal(input('Erro: '))
   f   = format_input(f)
   
   try:
      x = y = 0
      eval(f)
   except (NameError, SyntaxError) as e:
      print('Erro, funcao invalida!')
   else:
      fxy = lambda x, y: eval(f)
      euler_iter(fxy, xi, yi, xf, h, err)

   press_return()

def call_heun():
   clear()
   print('[Metodo RK-2 Heun]\n')
   
   f  = input('Funcao: ')
   xi = Decimal(input('xi: '))
   xf = Decimal(input('xf: '))
   yi = Decimal(input('yi: '))
   h  = Decimal(input('h:  '))
   f  = format_input(f)
   
   try:
      x = y = 0
      eval(f)
   except (NameError, SyntaxError) as e:
      print('Erro, funcao invalida!')
   else:
      fxy = lambda x, y: eval(f)
      rk2_heun(fxy, xi, yi, xf, h)
      
   press_return()

def call_heun_iter():
   clear()
   print('[Metodo de Heun iterativo]\n')
   
   f   = input('Funcao: ')
   xi  = Decimal(input('xi: '))
   xf  = Decimal(input('xf: '))
   yi  = Decimal(input('yi: '))
   h   = Decimal(input('h:  '))
   err = Decimal(input('Erro: '))
   f   = format_input(f)
   
   try:
      x = y = 0
      eval(f)
   except (NameError, SyntaxError) as e:
      print('Erro, funcao invalida!')
   else:
      fxy = lambda x, y: eval(f)
      heun_iter(fxy, xi, yi, xf, h, err)

   press_return()
   
def call_midpoint():
   clear()
   print('[Metodo RK-2 ponto medio]\n')
   
   f  = input('Funcao: ')
   xi = Decimal(input('xi: '))
   xf = Decimal(input('xf: '))
   yi = Decimal(input('yi: '))
   h  = Decimal(input('h:  '))
   f  = format_input(f)
   
   try:
      x = y = 0
      eval(f)
   except (NameError, SyntaxError) as e:
      print('Erro, funcao invalida!')
   else:
      fxy = lambda x, y: eval(f)
      rk2_midpoint(fxy, xi, yi, xf, h)
      
   press_return()

def call_ralston():
   clear()
   print('[Metodo RK-2 de Ralston]\n')
   
   f  = input('Funcao: ')
   xi = Decimal(input('xi: '))
   xf = Decimal(input('xf: '))
   yi = Decimal(input('yi: '))
   h  = Decimal(input('h:  '))
   f  = format_input(f)
   
   try:
      x = y = 0
      eval(f)
   except (NameError, SyntaxError) as e:
      print('Erro, funcao invalida!')
   else:
      fxy = lambda x, y: eval(f)
      rk2_ralston(fxy, xi, yi, xf, h)
      
   press_return()

def call_rk():
   clear()
   print('[Metodo RK-4 classico]\n')
   
   f  = input('Funcao: ')
   xi = Decimal(input('xi: '))
   xf = Decimal(input('xf: '))
   yi = Decimal(input('yi: '))
   h  = Decimal(input('h:  '))
   f  = format_input(f)
   
   try:
      x = y = 0
      eval(f)
   except (NameError, SyntaxError) as e:
      print('Erro, funcao invalida!')
   else:
      fxy = lambda x, y: eval(f)
      rk4(fxy, xi, yi, xf, h)
      
   press_return()