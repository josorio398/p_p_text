#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 20:08:55 2022

@author: oscar
"""

import re


class CleanText():
    '''
    Esta clase hace la limpieza de texto
    '''



    def __init__(self, input_text: str) -> None:

        # inicializo las variables
        self.input_text = input_text


    def c_numbers(self, not_clear: bool = True) -> str:
        """_summary_

        Args:
            not_clear (bool, optional): _description_. Defaults to True.

        Returns:
            str: _description_
        """




        if not_clear:
            c_numbers_pattern = re.compile(r"[0-9]+")
            out_put_txt = re.sub(c_numbers_pattern, "", self.input_text)
        else:
            out_put_txt = self.input_text

        return out_put_txt


    def c_mentios(self, not_clear: bool = True) -> str:

        '''
        Esta función elimina las menciones en los textos

        Parameters
        ----------
        not_clear : bool, optional si no quiero eliminar las menciones
            DESCRIPTION. The default is True.

        Returns
        -------
        str
            DESCRIPTION. texto sin menciones

        '''

        if not_clear:
            rt_patter = re.compile(r"\@[a-zA-Z0-9\-\_]+\b")
            out_put_text = re.sub(rt_patter," ", self.input_text)
        else:
            out_put_text = self.input_text

        return out_put_text
        # este metodo borra las @ Valentina

    def c_emojis(self, not_clear: bool = True) -> str:
        '''
        Esta función elimina los emojis de una cadena de texto

        Parameters
        ----------
        not_clear : bool:opcional si no quiero eliminar los emojis
            DESCRIPTION.

        Returns
        -------
        str
            DESCRIPTION. texto sin emojis

        '''

        if not_clear:
            c_emojis_pattern = re.compile(r"[^a-zA-Z\u00C0-\u00FF ]")
            out_put_txt = re.sub(c_emojis_pattern, ' ', self.input_text)

        else:
            out_put_txt = self.input_text

        return out_put_txt


    def c_hasgtags(self, not_clear: bool = True) -> str:
        '''
        Este metodo elimina los hastags del texto.

       Parameters
        ----------
        not_clear : bool, optional
            DESCRIPTION. The default is True.

        Returns
        -------
        str
            DESCRIPTION. El texto sin los hastags.


        '''


        if not_clear:
            c_hast_pattern = re.compile(r"\#[a-zA-Z0-9\-\_]+\b")
            out_put_txt = re.sub(c_hast_pattern, " ", self.input_text)

        else:
            out_put_txt = self.input_text

        return out_put_txt

    def c_url(self, not_clear: bool = True) -> str:
        '''
        Este metodo borra las url

        Parameters
        ----------
        not_clear : bool, optional
            DESCRIPTION. The default is True.

        Returns
        -------
        str
            DESCRIPTION. Eliminación de signos de puntuación

        '''

        if not_clear:

            c_url_pattern =  re.compile(r"http\S+")
            out_put_txt   =   re.sub(c_url_pattern,"", self.input_text)

        else:
            out_put_txt = self.input_text

        return out_put_txt




