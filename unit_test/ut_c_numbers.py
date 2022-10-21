#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 21:09:39 2022

@author: oscar
"""

import unittest
import p_p_text.clean_text as ct


class Test(unittest.TestCase):

    def setUp(self):
        '''

        Returns
        -------
        None.

        '''

        self.input_t = 'Un perro necesita salir a caminar 125'

    def testOutPut(self):
        '''
        Prueba la salida de la función

        Returns
        -------
        None.

        '''

        print('Test 1')

        output_t = 'Un perro necesita salir a caminar '

        text_f = ct.CleanText(input_text=self.input_t).c_numbers()

        self.assertEqual(text_f, output_t, msg='normal case OK')

    def testOutPutFalse(self):
        '''

        Returns
        -------
        None.

        '''
        print('Test 2')
        
        output_t = 'Un perro necesita salir a caminar 125'
        
        text_f = ct.CleanText(input_text=self.input_t).c_numbers(not_clear=False)

        self.assertEqual(text_f,output_t, msg='no clean case OK')


if __name__ == "__main__":
    unittest.main()

