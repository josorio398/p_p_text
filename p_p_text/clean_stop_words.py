# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 20:55:51 2022

@author: User
"""
class stop_words():

    def __init__(self, input_text: str, folder: str = 'p_p_text/Stop_Words/') -> None:


        self.input_text = input_text

        self.stop_words =  [] #stop words español e ingles


        with open(f"{folder}English.txt", "r") as file:

            stop_words_e = file.read().splitlines()

            self.stop_words.extend(stop_words_e) # llamar stop words ingles



        with open(f"{folder}Spanish.txt","r") as file:

            stop_words_s = file.read().splitlines()

            self.stop_words.extend(stop_words_s) # llamar stop words español



            self.text1 = self.input_text.split() # volver a lista
            self.text1 = list(map(lambda x : x.lower(), self.text1)) # pasar a min



    def clean_stop_words(self) -> str:

        text_pro= [word for word in self.text1 if word not in
                        self.stop_words] # limpiar stop words

        text_pro= " ".join(text_pro) #unir el texto

        return text_pro

