from main import calcular_imc, classificar_imc

def test_imc_normal():
    assert calcular_imc(70, 1.75) == round(70 / (1.75 ** 2), 2)

def test_classificacao_normal():
    assert classificar_imc(22.0) == "Peso normal"

def test_classificacao_abaixo():
    assert classificar_imc(17.0) == "Abaixo do peso"

def test_classificacao_sobrepeso():
    assert classificar_imc(27.0) == "Sobrepeso"

def test_classificacao_obesidade():
    assert classificar_imc(35.0) == "Obesidade"