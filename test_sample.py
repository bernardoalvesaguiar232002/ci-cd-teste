def test_soma():
    assert 1 + 1 == 2

def test_subtracao():
    assert 5 - 3 == 2

def test_string_maiuscula():
    assert "hello".upper() == "HELLO"

def test_tamanho_lista():
    minha_lista = [1, "a", True]
    assert len(minha_lista) == 3

def test_mod():
    val = 18
    val2 = 10

    assert 18 % 10 == 8