def tempo_valor_desejado(valor_inicial,taxa_rendimento,valor_desejado):
    meses=0
    while valor_inicial<valor_desejado:
        aumento=valor_inicial*(taxa_rendimento/100)
        valor_inicial+=aumento
        print(valor_inicial)
        meses+=1
    return meses
taxa=float(input("Insira a a taxa do rendimento, em porcentagem, sem o '%', exemplo: 3\n"))
meta=float(input("Qual valor você deseja atingir?"))
n=int(input("Quantas vezes deseja calcular?"))
for a in range(n):
    valor=float(input("Valor a ser calculado:"))
    print("Irá demorar",tempo_valor_desejado(valor,taxa,meta),"meses.")
