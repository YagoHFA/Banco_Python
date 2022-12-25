from ContaB import Conta



listaC = []
listaB = {}
c = Conta()

while True:
    ops = int(input('''
[0] Para cadastar cliente
[1] Para vincular Conta Bacaria
[2] Ir para Operaçoes
[3] Para Sair \n'''))
    if ops == 0:
        listaC.append(str(input("Digite o nome que deseja cadastrar: "))) 
    if ops == 1:
        nome = input("Digite o nome: ")
        contat = input("digite a conta: ")
        listaB[nome] = contat
    if ops == 3:
        break    
    if ops == 2:


        while True:

            op = input(
                    '''
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair\n'''
                    )
            if op == 'd':
                des = float(input("Deposite um valor: "))
                c.depositar(des)  
            if op == 's':
                sac = float(input("Retire um valor: "))
                c.sacar(sac)
            if op == 'e':
                print("Extrato:")
                print(c.extrato())
            if op == 'q':
                break    
            






