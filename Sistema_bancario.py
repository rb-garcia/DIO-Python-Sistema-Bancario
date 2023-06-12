menu = """
-------------------------------
        Sistema Bancário 
-------------------------------
        [1] Depositar
        [2] Sacar               
        [3] Extrato         
        [4] Sair         
-------------------------------
Digite a opção desejada (1-4): """

v_saldo = 0
v_limite = 500
v_saque = []
v_deposito = []
v_numero_saque = 0
c_LMITE_SAQUE = 3

while True:
    v_opcao = input(menu)

    if v_opcao == "1":
        print("")
        print("****** Realizar Depósito ******")
        ndeposito = float(input("Digite o valor do depósito: "))
        if ndeposito > 0:
            v_saldo += ndeposito
            v_deposito.append(ndeposito)
            extrato = f"Depósito de R$ {v_saldo:1.2f}"
            print(f"Depósito efetuado com sucesso no valor de R$ {ndeposito:.2f}")
        else:
            print("Depósito não realizado, digite um valor válido!!")

    elif v_opcao == "2":
        print("")
        print("******* Realizar Saque ********")
        nSaque = float(input("Digite o valor do saque: "))
        if (v_numero_saque < c_LMITE_SAQUE) and (nSaque <= v_limite) and (nSaque <= v_saldo):
            v_saldo -= nSaque
            v_saque.append(nSaque)
            v_numero_saque += 1
            extrato = f"Saque de R$ {nSaque:1.2f}"
            print(extrato)
        else:
            print("Limite de saque diário atingido ou saldo insuficiente!! Favor verificar!!")
        
    elif v_opcao == "3":
        print("")
        print("********** Extrato ***********")
        for i in v_saque:
            print(f"Saque ------------- R$ {i:1.2f}")
        for i in v_deposito:
            print(f"Depósito ---------- R$ {i:.2f}")
        print(f"Saldo ------------- R$ {v_saldo:.2f}")
    elif v_opcao == "4":
        break
    else:
        print("Opção inválida, por favor selecione uma opção válida!!")
