from main import calcular_imc, classificar

# Testes de cálculo do IMC
def test_imc_normal():
    assert round(calcular_imc(70, 1.75), 2) == 22.86

def test_imc_sobrepeso():
    assert round(calcular_imc(90, 1.75), 2) == 29.39

def test_imc_abaixo_do_peso():
    assert round(calcular_imc(50, 1.75), 2) == 16.33

# Testes de classificação
def test_classificacao_sobrepeso():
    assert classificar(27.0) == "Sobrepeso"

def test_classificacao_abaixo_do_peso():
    assert classificar(17.0) == "Abaixo do peso"

def test_classificacao_peso_normal():
    assert classificar(22.0) == "Peso normal"

def test_classificacao_obesidade():
    assert classificar(35.0) == "Obesidade"