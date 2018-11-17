from __future__ import division, print_function
from invoke import *

def show_menu():
   clear()
   print('[Analise Numerica]')
   print('\nIntegral:')
   print(' [1]Quadratura Gaussiana')
   print(' [2]Gauss - primeira ordem')
   print(' [3]Gauss - segunda ordem')
   print(' [4]Trapezio')
   print(' [5]Trapezio repetido')
   print(' [6]1/3 de Simpson')
   print(' [7]1/3 de Simpson repetido')
   print('\nEDO:')
   print(' [8]Euler simples')
   print(' [9]Euler iterativo')
   print(' [10]Heun iterativo')
   print(' [11]RK-2 de Heun')
   print(' [12]RK-2 de ponto medio')
   print(' [13]RK-2 de Ralston')
   print(' [14]Runge-Kutta 4')
   print(' [15]Sair')
   print('\nEscolha uma opcao (-h para ajuda): ')

if __name__ == '__main__':
   menu = {'1':  call_quadrature,
           '2':  call_gauss1,
           '3':  call_gauss2,
           '4':  call_trapz,
           '5':  call_trapzRep,
           '6':  call_simps,
           '7':  call_simpsRep,
           '8':  call_euler,
           '9':  call_euler_iter,
           '10': call_heun_iter,
           '11': call_heun,
           '12': call_midpoint,
           '13': call_ralston,
           '14': call_rk,
           '-h': call_help
           }
      
   choice = '0'
   while choice != '15': #exit
      show_menu()
      choice = input('>> ')
      if choice in menu:
         menu[choice]()
      elif choice != '15':
         print('\nOpcao invalida!')
         press_return()
   #!while
#!if