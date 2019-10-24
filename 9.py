def rendimento_final(tipo, investimento, meses):
    if tipo==1:
        print("\n",3*"-","Poupança",3*"-")
        rendimento=0.05
        for i in range(meses):
            investimento+=investimento*rendimento
        return investimento
    if tipo==2:
        print("\n",3*"-","Poupança Plus",3*"-")
        rendimento=0.06
        for i in range(meses):
            investimento+=investimento*rendimento
        return investimento
    if tipo==3:
        print("\n",3*"-","Fundos de Renda Fixa",3*"-")
        rendimento=0.08
        for i in range(meses):
            investimento+=investimento*rendimento
        return investimento
qtd=int(input("Quantidade de clientes:"))
total_inv=total_rendido=0
for i in range (qtd):
    tipo=int(input("Tipo de Investimento do Cliente %d:\n1-Poupança\n2-Poupança Plus\n3-Fundos de renda fixa\n"%(i+1)))
    investimento=float(input("Investimento do cliente %d:"%(i+1)))
    meses=int(input("Por quantos meses o cliente deseja investir?"))
    total_inv+=investimento
    rendido=rendimento_final(tipo,investimento,meses)
    total_rendido+=rendido
    print("O cliente %d rendeu %.2f R$ por %d meses\n"%((i+1),rendido,meses))
print("Total investido no Banco: %.2f R$"%total_inv)
print("Total rendido pelo Banco: %.2f R$"%total_rendido)