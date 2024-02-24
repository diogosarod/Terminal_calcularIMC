from time import sleep

def clear():
    try:
        import os
        lines = os.get_terminal_size().lines
    except AttributeError:
        lines = 130
    print("\n" * lines)

def espaco_up():
    print("\033[1;36m ==================================\033[0;0m")
    print("")

def espaco_down():
    print("")
    print("\033[1;36m ==================================\033[0;0m")
    sleep(1)

def calcular_imc(peso, altura):
    return peso / (altura * altura)

def mostrar_categoria_imc(imc):
    if imc < 18.5:
        return "\033[1;34mMagreza\033[0;0m"
    elif 18.5 <= imc <= 24.9:
        return "\033[1;34mNormal\033[0;0m"
    elif 25 <= imc <= 29.9:
        return "\033[1;34mSobrepeso\033[0;0m"
    elif 30 <= imc <= 39.9:
        return "\033[1;34mObesidade\033[0;0m"
    elif imc >= 40:
        return "\033[1;34mObesidade Grave\033[0;0m"
    else:
        return "\033[1;34mERRO NO CÓDIGO\033[0;0m"

clear()
espaco_up()
print("    Bem-vindo à Calculadora do IMC")
espaco_down()

while True:
    nome = input("   Qual o seu nome: ")

    while True:
        try:
            idade = int(input("   Qual a sua idade: "))
            peso = float(input("   Qual o seu peso (em Kg): "))
            altura = float(input("   Qual a sua altura (em metros): "))
            break
        except ValueError:
            print("\033[1;31mErro: Insira valores válidos.\033[0;0m")

    espaco_down()

    print("  \033[1;31mCarregando as informações\033[0;0m")
    sleep(0.5)
    print("         .....\033[0;0m")
    sleep(1)

    imc = calcular_imc(peso, altura)

    print(f"\033[0;32mPronto, {nome}! O seu índice de massa corporal é: {imc:.2f}\033[0;0m")
    print(f"Você está na categoria: {mostrar_categoria_imc(imc)}")

    retornar = input("Deseja refazer o teste? [S/N]: ").upper()

    if retornar != "S":
        print("Programa encerrado.")
        break
    else:
        clear()
        espaco_up()
