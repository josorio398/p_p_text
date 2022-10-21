# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 23:06:27 2022

@author: ejemp
"""
# importando la librería de esta forma no se generan errores
import p_p_text.clean_text as ct

text = ct.CleanText("Esto es 1 ejemplo de l'limpieza de6 TEXTO  https://t.co/rnHPgyhx4Z @cienciadedatos #textmining")

T1 = text.c_numbers()
T2 = text.c_mentios()
T3 = text.c_emojis()
T4 = text.c_hasgtags()
T5 = text.c_url()

print(T1)
print(T2)
print(T3)
print(T4)
print(T5)
