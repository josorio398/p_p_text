import p_p_text.clean_text as ct

import pytest

@pytest.mark.parametrize("text_input,text_output",[("hola125","hola"),("234hola123","hola"),("@hola","@hola"),("ho23la","hola")])

def test_c_numbers(text_input,text_output):
    ouput = ct.CleanText(text_input)
    assert ouput.c_numbers() == text_output
