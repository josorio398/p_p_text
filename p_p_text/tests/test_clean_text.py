import p_p_text.clean_text as ct

text = 'Un perro necesita salir a caminar 125 @hola #hola'
ouput = ct.CleanText(text)

def test_c_numbers():
    assert ouput.c_numbers() == 'Un perro necesita salir a caminar  @hola #hola'

def test_c_mentions():
    assert ouput.c_numbers() == 'Un perro necesita salir a caminar  @hola #hola'

def test_c_emojis():
    assert ouput.c_emojis() == 'Un perro necesita salir a caminar      hola  hola'

def test_c_hasgtags():
    assert ouput.c_hasgtags() == 'Un perro necesita salir a caminar 125 @hola  '