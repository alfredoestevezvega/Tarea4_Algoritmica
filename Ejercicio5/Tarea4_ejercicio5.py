"""Modifica la función imprimirExpresion para que no incluya un par de paréntesis ‘extra’ alrededor de
cada número.
"""

from recorridos import *
arbol = ArbolBinario("+")
arbol.insertarDerecho("2")
arbol.insertarIzquierdo("*")
arbol.hijoIzquierdo.insertarIzquierdo("3")
arbol.hijoIzquierdo.insertarDerecho("3")

print(imprimirExpresion(arbol))