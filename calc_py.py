# coding=utf8
art = ('\n'*150 + "\n░█████╗░░█████╗░██╗░░░░░░█████╗░██╗░░░██╗██╗░░░░░░█████╗░██████╗░░█████╗░██████╗░░█████╗░\n██╔══██╗██╔══██╗██║░░░░░██╔══██╗██║░░░██║██║░░░░░██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗\n██║░░╚═╝███████║██║░░░░░██║░░╚═╝██║░░░██║██║░░░░░███████║██║░░██║██║░░██║██████╔╝███████║\n██║░░██╗██╔══██║██║░░░░░██║░░██╗██║░░░██║██║░░░░░██╔══██║██║░░██║██║░░██║██╔══██╗██╔══██║\n╚█████╔╝██║░░██║███████╗╚█████╔╝╚██████╔╝███████╗██║░░██║██████╔╝╚█████╔╝██║░░██║██║░░██║\n░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░░╚═════╝░╚══════╝╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝")
print(art)
alternativas = [1, 2, 3, 4, 5]
operadores = [' + ', ' - ', ' x ', ' ÷ ']
numeros = []
histórico = []


def operador():
    while True:
        print(
            '\nEscolha um operador:\n➕ [1]  ➖ [2]  ✖️  [3]  ➗ [4]  Histórico [5]')
        try:
            escolha = int(input("Digite o número da operação desejada: "))
            if escolha not in alternativas:
                raise ValueError
            return escolha
            break
        except ValueError:
            print(art)
            print("\nCaráter invalido digite novamente!")


def calculadora():
    while True:
        try:
            if escolha == 5:
                print(art)
                print('\nHISTÓRICO:')
                for _ in histórico:
                    print(_)
                break
            numero = (float(input('-> ')))
            numeros.append(numero)

            if len(numeros) >= 2 and escolha == 1:
                resultado = sum(numeros)
            if len(numeros) >= 2 and escolha == 2:
                x = numeros[0]
                for _ in numeros[1:]:
                    x -= _
                resultado = x
            if len(numeros) >= 2 and escolha == 3:
                x = numeros[0]
                for _ in numeros[1:]:
                    x *= _
                resultado = x
            if len(numeros) >= 2 and escolha == 4:
                if numeros[1] == 0:
                    numeros.clear()
                    print(art)
                    print('\nÉ ímpossivel dividir um número por 0')
                    break
                x = numeros[0]
                for _ in numeros[1:]:
                    x /= _
                resultado = x
        except:
            if len(numeros) <= 1:
                print(art)
                print(
                    '\nPara realizar o calculo são necesarios no minimo dois numeros!!!')
            else:
                k = (operadores[escolha - 1].join(map(str, numeros)))
                t = (f'{k} = {resultado}')
                histórico.append(t)
                print(art)
                print(f'\nResultado: {t}')
            numeros.clear()
            break


while True:
    escolha = operador()
    calculadora()
