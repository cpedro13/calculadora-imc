def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def classificar(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 25:
        return "Peso normal"
    elif imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidade"

if __name__ == "__main__":
    while True:
        peso = float(input("Peso (kg): "))
        altura = float(input("Altura (m): "))

        imc = calcular_imc(peso, altura)
        print(f"IMC: {imc:.2f} — {classificar(imc)}")

        input("\nPressione ENTER para calcular novamente...")