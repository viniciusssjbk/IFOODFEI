#Variaveis globais para serem acessadas pelas funções
listaentrar = ["vini","123"]
listausuario = []
comidasS = ["Coxinha","Batata fritas", "Torta de frango"]
comidasD = ["Bolo","Brigadeiro", "Doce de leite", "Rosquinha recheada"]
comidasC = ["Bisteca","Bife"]
comidasL = [["Pizza","Portuguesa","Peperoni","Frango com catupiry","Queijo"], ["Hamburguer","X-TUDO","X-BACON","X-SALADA"], ["Pastel","Carne","Calabresa","Frango","Bauru"]]
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
           
        elif digito==1:
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
            pedido()
            x = input("Precione 'Enter' para continuar...")    
                   


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

                print("%-20s|"% (comidasL[i][0]), end="")

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
                print(f"Comida: {digitar} | {comidasL[digitar-1][0]} | ")

                for i in range(len(comidasL[0])-1):
                    print("Sabor: %-10s | "% comidasL[digitar-1][i+1])
                    print("Preço: R$%.2f    |\n"% preco_LPiz[i])
                break

            elif digitar ==2:
                print(f"Comida: {digitar} | {comidasL[digitar-1][0]} | ")

                for i in range(len(comidasL[1])-1):
                    print("Sabor: %-10s | "% comidasL[digitar-1][i+1])
                    print("Preço: R$%.2f    |\n"% preco_LHam[i])
                break


            elif digitar ==3:
                print(f"Comida: {digitar} | {comidasL[digitar-1][0]} | ")


                for i in range(len(comidasL[2])-1):
                    print("Sabor: %-10s | "% comidasL[digitar-1][i+1])
                    print("Preço: R$%.2f    |\n"% preco_LPas[i])
                break


        else:
            print("Nao foi possivel achar uma comida com esse numero!!!")


def pedido():
    totalpedido =[]
    while True:
        totalpedido.append(func_pedir())
        
        digitar = int(input("\n|-------------------------------------|\n|Digite 1 para ver adicionar pedido   |\n|Digite 2 para editar pedido          |\n|Digite 3 para finalizar pedido       |\n|Digite 4 para excluir pedido         |\n|-------------------------------------|\n"))
        if digitar ==2:
            editar(totalpedido)
        elif digitar ==3:
            boleto(totalpedido)
        elif digitar == 4:
            exluir(totalpedido)
    

def editar(total):
    print(total)
    for i in range(len(total)):
        for j in range(len(total[i])):
            print(i+1,"ºpedido: %3s"%(total[i]),end="")
        print()
    
    while True:
        digito = int(input("Digite o numero do pedido que deseja editar: \n"))
        if digito >0 and digito<=(len(total[digito-1])):
            break
        else: 
            print("Pedido não encontrado")
            x =input("Precione 'Enter' para continuar...")
    total.pop(digito-1)        
    total[digito-1].append(func_pedir())
    


def exluir():
    poste =1

def boleto():
    poste =1
#função logo
def func_pedir():
    while True:
        while True:
            digitar_catec = input("Digite a categoria do alimento:(salgados,doces,carnes,lanches)\n")
            digitar_catec = digitar_catec.lower()
            if digitar_catec =="salgados" or digitar_catec =="salgado":
                catec = 1
                break
            elif digitar_catec =="doces" or digitar_catec =="doce":
                catec = 2
                break
            elif digitar_catec =="carnes" or digitar_catec =="carne":
                catec = 3
                break
            elif digitar_catec =="lanches" or digitar_catec =="lanche":
                catec = 4
                break
            else:
                print("Categoria não encontrada!!!")
        while True:
            sabor = ""
            digitar_comida = int(input("Digite o numero da comida: \n"))
            if catec == 1 and digitar_comida>0 and digitar_comida<=len(comidasS):
                break
            elif catec == 2 and digitar_comida>0 and digitar_comida<=len(comidasD):
                break
            elif catec == 3 and digitar_comida>0 and digitar_comida<=len(comidasC):
                break
            elif catec == 4 and digitar_comida>0 and digitar_comida<=len(comidasL):
                k =0
                while k<2:
                    sabor = input("Digite o sabor desejado:\n")
                    sabor = sabor.lower()

                    for i in range(len(comidasL[digitar_comida-1])):
                        if sabor == comidasL[digitar_comida-1][i].lower():

                            k = 3
                            break
                    else:
                        print("Sabor não encontrado!!!")
                break     
            else: 
                print("Alimento não encontrado!!!")


        quantidade = int(input("Digite a quantidade:\n"))
        if catec ==1:
            pedir = [comidasS[digitar_comida-1],quantidade,sabor]
        elif catec ==2:
            pedir = [comidasD[digitar_comida-1],quantidade,sabor]
        if catec ==3:
            pedir = [comidasC[digitar_comida-1],quantidade,sabor]
        if catec ==4:
            pedir = [comidasL[digitar_comida-1][0],quantidade,sabor]
        return pedir
        
def logo():
    for i in range (3):
        for j in range(18):
            if i==0 or i==2:
                print("/ * ", end="")
            elif j ==1 and i ==1:
                print()
                print("    %40s     "%("SEJA BEM VINDO"))
                print("    %38s     "%("AO IFOODFEI"))
        print()
#chamando a função global
menu()