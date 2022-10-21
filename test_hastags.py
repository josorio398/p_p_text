# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 18:23:13 2022

@author: User
"""

import p_p_text.clean_text as CL

file = "hola soy #miguel_pinto y vengo a saludar"
file2 = "hola soy miguel"

classObj  = CL.CleanText(input_text=file)
classObj2 = CL.CleanText(input_text=file2)

text =  classObj.c_hasgtags()
text2 = classObj2.c_hasgtags()

print(f'El texto sin hastags es: {text}')
print(f'El texto no tiene hastags, y este es: {text2}')