print("--------------------CONTROLE DE GASTOS PESSOAIS--------------------")
print()

nome = input("Informe o seu nome: ")
inicio = input(f"Olá {nome}! Escreva OK para começar, ou escreva SAIR para cancelar: ").strip().upper()

while True:
    if inicio == "OK":
        print("Carregando...")
        break  
    elif inicio == "SAIR":
        print("Programa encerrado.")
        exit()  
    else:
        inicio = input("Opção inválida! Escreva somente OK ou SAIR: ").strip().upper()

renda_mensal = 0.0
soma_gastos = 0.0
descricao1 = ""
valor_gasto1 = 0.0
categoria_gasto1 = ""
descricao2 = ""
valor_gasto2 = 0.0
categoria_gasto2 = ""
descricao3 = ""
valor_gasto3 = 0.0
categoria_gasto3 = ""

while True:
    print("--------------------MENU PRINCIPAL--------------------")
    print()
    print("1. INFORMAR RENDA MENSAL")
    print()
    print("2. CADASTRAR GASTOS")
    print()
    print("3. CONSULTAR GASTOS")
    print()
    print("4. CONSULTAR SITUACAO FINANCEIRA")
    print()
    print("5. VER ESTATISTICAS")
    print()
    print("6. SAIR")
    print()
    print("----------------------------------------------------------------")
    print()
   
    menu = int(input("ESCOLHA UMA OPCAO: "))
    print()
   
    if menu == 1:
        print("----------------------1. INFORMAR RENDA MENSAL------------------------")
        print()
        renda_mensal = float(input(f"{nome}, informe a sua renda mensal total em R$: "))
        print()
        print(f"{nome}, sua renda mensal é de {renda_mensal} R$.")
        print()
        print("RENDA ATUALIZADA COM SUCESSO.")
        print()
        print("----------------------------------------------------------------------------------")
        print()
        input("Aperte ENTER para voltar ao menu inicial.")
        print()
       
    elif menu == 2:
        print("----------------------2. CADASTRAR GASTOS-------------------------")
        print()
        print("Cadastre apenas 3 gastos.")
        print()
        descricao1 = input(f"{nome}, escreva a descrição do seu primeiro gasto: ")
        valor_gasto1 = float(input("Valor total do gasto em R$: "))
        categoria_gasto1 = input("Escreva a categoria do seu gasto, (ex: Transporte, Lazer, Alimentação): ")
        print()
           
        descricao2 = input(f"{nome}, escreva a descrição do seu segundo gasto: ")
        valor_gasto2 = float(input("Valor total do gasto em R$: "))
        categoria_gasto2 = input("Escreva a categoria do seu gasto: ")
        print()
           
        descricao3 = input(f"{nome}, escreva a descrição do seu terceiro gasto: ")
        valor_gasto3 = float(input("Valor total do gasto em R$: "))
        categoria_gasto3 = input("Escreva a categoria do seu gasto: ")
        print()
        print("----------------------------------------------------------------------------------")
        print()
        input("Gastos cadastrados com sucesso! Aperte ENTER para retornar ao menu.")
        print()
   
    elif menu == 3:
        print("------------------------------CONSULTAR GASTOS------------------------------")
        print()
        print(f"DESCRIÇÃO: {descricao1}")
        print(f"VALOR GASTO: {valor_gasto1} R$.")
        print(f"CATEGORIA: {categoria_gasto1}.")
        print()
        print(f"DESCRIÇÃO: {descricao2}")
        print(f"VALOR GASTO: {valor_gasto2} R$.")
        print(f"CATEGORIA: {categoria_gasto2}.")
        print()
        print(f"DESCRIÇÃO: {descricao3}")
        print(f"VALOR GASTO: {valor_gasto3} R$.")
        print(f"CATEGORIA: {categoria_gasto3}.")
        print()  
        print("----------------------------------------------------------------------------------")
        print()            
        input("Aperte ENTER para voltar ao menu.")
        print()
                                               
    elif menu == 4:                                            
        print("--------------------4. CONSULTAR SITUACAO FINANCEIRA--------------------")
        print()
        print(f"{nome}, sua renda mensal é de: {renda_mensal}")
        print()
        soma_gastos = valor_gasto1 + valor_gasto2 + valor_gasto3
        valor_restante = renda_mensal - soma_gastos
       
        if valor_restante < 0:
            print("ATENÇÃO! A sua situação financeira é NEGATIVA!")
            print()
            print(f"Valor pendente: {abs(valor_restante)} R$. ")
            print()
        elif valor_restante == 0:
            print("Atenção, você está sem saldo!")
            print()
        else:
            print("A sua situação financeira é positiva!")
            print()
            print(f"Valor restante: {valor_restante} R$. ")
            print()
           
        print("-----------------------------------------------------------------------------------")
        print()
        input("Aperte ENTER para retornar ao menu.")
        print()
                                                                                   
    elif menu == 5:    
        print("--------------------5. VER ESTATISTICAS--------------------")
        print()
        soma_gastos = valor_gasto1 + valor_gasto2 + valor_gasto3
        print(f"SOMATÓRIO DE GASTOS: {soma_gastos}")
        print()
        quantidade_gastos = 3
        media_gastos = soma_gastos / quantidade_gastos
        print(f"MÉDIA DOS GASTOS: {media_gastos}")
        print()
        print("-----------------------------------------------------------------------------")
        print()
        input("Aperte ENTER para retornar ao menu.")
        print()
       
    elif menu == 6:
        print("Obrigado por utilizar o CONTROLE DE GASTOS PESSOAIS")
        break
    else:
        print("Opcao invalida! Escolha um numero de 1 a 6")
        print("----------------------------------------------------------------------------------")