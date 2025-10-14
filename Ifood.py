#Variaveis globais para serem acessadas pelas funções
listaentrar = []
listausuario = []
comidasS = ["Coxinha","Batata fritas", "Torta de frango"]
comidasD = ["Bolo","Brigadeiro", "Doce de leite", "Rosquinha recheada"]
comidasC = ["Bisteca","Bife"]
comidasL = ["Pizza", "Hamburguer", "Pastel"]
comidasL_Pas = ["Carne", "Calabresa","Frango", "Bauru"]
comidasL_Ham = ["X-TUDO", "X-BACON","X-SALADA"]
comidasL_Piz = ["Portuguesa", "Peperoni","Frango com catupiry", "Queijo"]
comidastipo = 4
preco_S = [6,8,12.5]
preco_D = [12,8,7,6.5]
preco_C = [30, 29]
preco_LPiz = [30,30,32,29]
preco_LHam = [20,22,25]
preco_LPas = [12,15,12,12]
#função global
def menu():
    #gera uma logo
    logo()
    #entrada do usuario
    while True:
        digito = int(input("\n|-----------------------|\n|Digite 1 para entrar   |\n|Digite 2 para cadastrar|\n|-----------------------|\n"))
        if digito ==2:    
            usuario = cadastrar()
            listausuario.append(usuario)
            listaentrar.append(usuario[3])
            listaentrar.append(usuario[4])
            x = input("Precione 'Enter' para continuar...")
           
        else:
            verificar = entrar()
            if verificar == 1:
                x = input("Precione 'Enter' para continuar...")
                break
            else: 
                print("Login errado!!! tente novamente")
    while True:
        #a escolha entre visualizar o cardapio ou pedir
        digito = int(input("\n|-------------------------------------|\n|Digite 1 para ver todas as comidas   |\n|Digite 2 para buscar                 |\n|Digite 3 para cadastrar o seu pedido |\n|-------------------------------------|\n"))
        if digito == 1:
            listar_comida()
            x = input("Precione 'Enter' para continuar...")
        elif digito == 2:
            buscar_comida()
            x = input("Precione 'Enter' para continuar...")
        elif digito == 3:
            #pedido()
            x = input("Precione 'Enter' para continuar...")    
            break        


#função que vai cadastrar o usuario
def cadastrar():
    vetor= []
    vetor.append( input("Digite seu nome:\n"))
    vetor.append(input("Digite seu CEP:(XXXXX-XXX)\n"))
    vetor.append(input("Digite seu CPF:(XXX.XXX.XXX-XX)\n"))
    vetor.append(input("Digite seu email:\n"))
    while True:
        senha = input("Digite sua senha:\n")
        confirmarsenha = input("Confirme sua senha:\n")
        if senha == confirmarsenha:
            vetor.append(senha)
            return vetor
        else:
            print("SENHAS INVALIDAS!!!!!")
#função de verificação 
def entrar():
    email = input("Digite seu email:\n")
    senha = input("Digite a sua senha:\n")
    for i in range(0,len(listaentrar),2):
        if email == listaentrar[i] and senha == listaentrar[i+1]:
            verificar = 1
        else:
            verificar = 0
        
    return verificar
#função para listar todos os alimentos
def listar_comida():
    contar = 1
    total =[] 
    maior = 0
    totalC= len(comidasC)
    totalS= len(comidasS)
    totalD= len(comidasD)
    totalL= len(comidasL)
    total.append(totalC)
    total.append(totalS)
    total.append(totalD)
    total.append(totalL)
    for i in range(0,len(total)):
        if total[i]>=maior:
            maior = total[i]

    print("|  Nº |     %-15s|     %-15s|     %-15s|     %-15s|"%("SALGADOS","DOCES","CARNES","LANCHES"))
    
    for i in range(maior):


        print(f"|  {contar}  |", end="")

        for j in range(comidastipo):

            if j==0 and i < totalS:

                print("%-20s|"% (comidasS[i]), end="")

            elif j==1 and i < totalD:

                print("%-20s|"% (comidasD[i]), end="")

            elif j==2 and i < totalC:

                print("%-20s|"% (comidasC[i]), end="")

            elif j==3 and i < totalL:

                print("%-20s|"% (comidasL[i]), end="")

            else:
                print("-xxxxxxxxxxxxxxxxxx-|", end="")
            
                
        print()
        contar +=1
#função que o usuario vai buscar o alimento            
def buscar_comida():
    escolher = 0
    while True:
        tipo = input("Digite a categoria da comida:(salgados,doces,carnes,laches)\n")
        tipo_m = tipo.lower()
        if tipo_m == "salgados" or tipo_m == "salgado":
            escolher = 1
            break
        elif tipo_m == "doces" or tipo_m == "doce":
            escolher = 2
            break
        elif tipo_m == "carnes" or tipo_m == "carne":
            escolher = 3
            break
        elif tipo_m == "lanches" or tipo_m == "lanche":
            escolher = 4
            break
        else:
            print("Digite a categoria corretamente!!!")
    while True:
        digitar = int(input("Digite o numero da comida: "))
        if escolher == 1 and digitar <= len(comidasS) and digitar>0:
            print(f"Comida: {digitar} | {comidasS[digitar-1]} | ")
            print("Preço: R$%.2f  |"% preco_S[digitar-1])
            break
        elif escolher == 2 and digitar <= len(comidasD) and digitar>0:
            print(f"Comida: {digitar} | {comidasD[digitar-1]} | ")
            print("Preço: R$%.2f  |"% preco_D[digitar-1])
            break
        elif escolher == 3 and digitar <= len(comidasC) and digitar>0:
            print(f"Comida: {digitar} | {comidasC[digitar-1]} | ")
            print("Preço: R$%.2f  |"% preco_C[digitar-1])
            break
#(REMOVER DPS) CATEGORIA LANCHE
        elif escolher == 4 and digitar <= len(comidasL) and digitar>0:

            if digitar == 1:
                print(f"Comida: {digitar} | {comidasL[digitar-1]} | ")

                for i in range(len(comidasL_Piz)):
                    print("Sabor: %-10s | "% comidasL_Piz[i-1])
                    print("Preço: R$%.2f    |\n"% preco_LPiz[i-1])
                break

            elif digitar ==2:
                print(f"Comida: {digitar} | {comidasL[digitar-1]} | ")

                for i in range(len(comidasL_Ham)):
                    print("Sabor: %-10s | "% comidasL_Ham[i-1])
                    print("Preço: R$%.2f    |\n"% preco_LHam[i-1])
                break


            elif digitar ==3:
                print(f"Comida: {digitar} | {comidasL[digitar-1]} | ")


                for i in range(len(comidasL_Pas)):
                    print("Sabor: %-10s | "% comidasL_Pas[i-1])
                    print("Preço: R$%.2f    |\n"% preco_LPas[i-1])
                break


        else:
            print("Nao foi possivel achar uma comida com esse numero!!!")
#def pedido():

#def boleto():

#função logo
def logo():
    for i in range (3):
        for j in range(6):
            if i==0 or i==2:
                print("/ * ", end="")
            elif j ==1 and i ==1:
                print("     SEJA BEM VINDO    ")
                print("      AO IFOODFEI")
        print()
#chamando a função global
menu()