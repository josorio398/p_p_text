import p_p_text.clean_stop_words as CSW

text = 'En algún lugar de la Mancha de cuyo nombre no quiero acordarme now'


clean_text = CSW.stop_words(input_text=text).clean_stop_words()

print(text)
print(clean_text)
