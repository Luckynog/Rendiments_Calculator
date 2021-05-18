#Questão 04
periodos_lista = [0] #Lista para plotar gráfico
valor_acumulado_lista = [] #Lista para plotar gráfico

def calcular_rendimentos_futuros(montante_inicial, rendimento_periodo, aporte_periodo, num_periodos, valor_inicial):
    for i in range(num_periodos):
        novo_montante = montante_inicial + ((rendimento_periodo/100) * montante_inicial) + aporte_periodo
        if i == 0:
            print(f"Após {i + 1} período, o montante será de R$ {formatar_moeda(novo_montante)}.")
        else:
            print(f"Após {i + 1} períodos, o montante será de R$ {formatar_moeda(novo_montante)}.")
        montante_inicial = novo_montante
        periodos_lista.append(i + 1)
        valor_acumulado_lista.append(novo_montante)
    
    lucro = (novo_montante - (num_periodos * aporte_periodo)) - valor_inicial
    print()
    print(f"Ao final dos períodos, retirando o valor inicial e os aporte periódicos, seu lucro será de R$ {formatar_moeda(lucro)}.")
    print()
    print("Fim do programa.")

def formatar_moeda(x):
    x = f"{x:,.2f}"
    x = x.replace(",", "@")
    x = x.replace(".", "&")
    x = x.replace("@", ".")
    x = x.replace("&", ",")
    return x

def exibir_grafico(x, y):
    import matplotlib.pyplot as plt
    plt.plot(x,y, "g--p", label = "Crescimento do montante")
    plt.legend(loc = "upper left")
    plt.show()

print("#################### Bem vindo ao seu assistente pessoal financeiro! ####################")
print()
montante_inicial = float(input("Insira o valor inicial: R$ "))
rendimento_periodo = float(input("Insira em quantos porcento será o rendimento por período: "))
aporte_periodo = float(input("Insira o valor mensal a ser aportado: R$ "))
num_periodos = int(input("Insira o número de períodos (meses) a serem considerados para o cálculo: "))
valor_inicial = montante_inicial #Guarda o valor inicial
valor_acumulado_lista.append(valor_inicial)
print()

calcular_rendimentos_futuros(montante_inicial, rendimento_periodo, aporte_periodo, num_periodos, valor_inicial) #calcula rendimentos (a)
exibir_grafico(periodos_lista, valor_acumulado_lista) #exibe o gráfico (b)