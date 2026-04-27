from main import calcular_imc, classificar

def test_imc_normal():
    assert round(calcular_imc(70, 1.75), 2) == 22.86

def test_classificacao_sobrepeso():
    assert classificar(27.0) == "Sobrepeso"