listaentrar,listausuario = [], []
comidasS, comidasD, comidasC, comidasL = [], [], [], [] 
preco_S, preco_D, preco_C, preco_LHot, preco_LTapi, preco_LSand, preco_LPiz, preco_LHam, preco_LPas = [], [], [], [], [], [], [], [], []
avaliacao, listageral = [],[]
comidastipo = 4
sabores_total = 10
diretoriocomidas = [["Dados/Comidas/salgados.txt",comidasS],["Dados/Comidas/doces.txt",comidasD],["Dados/Comidas/carnes.txt",comidasC]]
diretoriolanche=["Dados/Comidas/lanchesPiz.txt","Dados/Comidas/lanchesHam.txt","Dados/Comidas/lanchesPas.txt","Dados/Comidas/lanchesHot.txt","Dados/Comidas/lanchesTap.txt","Dados/Comidas/lanchesSan.txt"]
diretoriopreco = [["Dados/precos/preco_Sal.txt",preco_S], ["Dados/precos/preco_Doc.txt",preco_D], ["Dados/precos/preco_Car.txt",preco_C], ["Dados/precos/preco_Lhot.txt",preco_LHot], ["Dados/precos/preco_Ltap.txt",preco_LTapi], ["Dados/precos/preco_Lsan.txt",preco_LSand], ["Dados/precos/preco_Lpiz.txt",preco_LPiz], ["Dados/precos/preco_Lham.txt",preco_LHam], ["Dados/precos/preco_Lpas.txt",preco_LPas]]
diretorioavaliacao = ["Dados/avaliacao/avaliacaoS.txt","Dados/avaliacao/avaliacaoD.txt","Dados/avaliacao/avaliacaoC.txt"]
diretorioavaliacaolanche = ["Dados/avaliacao/avaliacaoLPiz.txt","Dados/avaliacao/avaliacaoLHam.txt","Dados/avaliacao/avaliacaoLPas.txt","Dados/avaliacao/avaliacaoLHot.txt","Dados/avaliacao/avaliacaoLTap.txt","Dados/avaliacao/avaliacaoLSan.txt"]

#ORDEM DOS LANCHES PIZ/HAM/PAS/HOT/TAP/SAN
arquivo = open("Dados/login.txt", "r")
arquivo2 = arquivo.readlines()
arquivo.close()
if len(arquivo2)>1:
    for contador in range(0,len(arquivo2),2):
        usuario = [arquivo2[contador].strip(),arquivo2[contador+1].strip()]
        listaentrar.append(usuario)

arquivo = open("Dados/usuario.txt", "r")
arquivo2 = arquivo.readlines()
arquivo.close()


if len(arquivo2)>1:
    for contador in range(0,len(arquivo2),5):
        usuario = [arquivo2[contador].strip(),arquivo2[contador+1].strip(),arquivo2[contador+2].strip(),arquivo2[contador+3].strip(),arquivo2[contador+4].strip()]
        listausuario.append(usuario)

for contar in range (len(diretoriocomidas)):
    arquivo = open(diretoriocomidas[contar][0], "r")
    arquivo2 = arquivo.readlines()
    arquivo.close()

    if len(arquivo2)>1:
        for contador in range(len(arquivo2)):
            valor_linha = arquivo2[contador].strip()
            diretoriocomidas[contar][1].append(valor_linha)



for j in range (len(diretoriolanche)):
    arquivo = open(diretoriolanche[j], "r")
    arquivo2 = arquivo.readlines()
    arquivo.close()

    if len(arquivo2)>1:
        valor_linha = []
        for contador in range(len(arquivo2)):
            valor_linha.append(arquivo2[contador].strip())
        comidasL.append(valor_linha)


for contar in range (len(diretoriopreco)):
    arquivo = open(diretoriopreco[contar][0], "r")
    arquivo2 = arquivo.readlines()
    arquivo.close()

    if len(arquivo2)>1:
        for contador in range(len(arquivo2)):
            valor_linha = float(arquivo2[contador].strip())
            diretoriopreco[contar][1].append(valor_linha)



for contar in range(len(diretorioavaliacao)):
    arquivo = open(diretorioavaliacao[contar], "r")
    arquivo2 = arquivo.readlines()
    arquivo.close()

    if len(arquivo2) > 1:
        lista_provisoria = []
        for contador in range(len(arquivo2)):
            valor_linha_tirando_barra = arquivo2[contador].strip()
            if valor_linha_tirando_barra == "":  # ignora linha vazia
                continue
            valor_linha = [float(linhadotexto) for linhadotexto in valor_linha_tirando_barra.split(",")]
            lista_provisoria.append(valor_linha)
           
        avaliacao.append(lista_provisoria)

for contar in range(len(diretorioavaliacaolanche)):
    arquivo = open(diretorioavaliacaolanche[contar], "r")
    arquivo2 = arquivo.readlines()
    arquivo.close()
    if len(arquivo2) > 1:
        listaespecifica = []
        for contador in range(len(arquivo2)):
            valor_linha_tirando_barra = arquivo2[contador].strip()
            if valor_linha_tirando_barra == "":  # ignora linha vazia
                continue
            valor_linha = [float(linhadotexto) for linhadotexto in valor_linha_tirando_barra.split(",")]
            listaespecifica.append(valor_linha)
        listageral.append(listaespecifica)
    
else:
    avaliacao.append(listageral)

def menu():
    #chama a função logo para gerar um desenho
    logo()
    #aqui sera chamada a ação do usuario para entrar/cadastrar e salvara o numero dele na lista geral dos usuarios e esse numero será armazenado na variavel login
    login = escolha_usuario1()
    #aqui sera chamada a ação do usuario para interagir com o programa e a variavel sera usada para que ela seja passada pelo programa para que seja armazenada para que possa usar depois para recuperar dados do usuario
    escolha_usuario2(login) 
#aqui é a função logo
def logo():
    #looping para gerar uma logo
    for i in range (3):
        for j in range(18):
            if i==0 or i==2:
                print("/ * ", end="")
            elif j ==1 and i ==1:
                print()
                print("    %40s     "%("SEJA BEM VINDO"))
                print("    %38s     "%("AO IFOODFEI"))
        print()

#aqui é a função onde o usuario ira escolher entre cadastrar ou entrar
def escolha_usuario1():
    while True:
        digito = input("%s\n%s\n%s\n%s\n" % ("|-----------------------|","|Digite 1 para entrar   |","|Digite 2 para cadastrar|","|-----------------------|"))
        if digito == "2":
            #caso o usuario escolha cadastrar sera chamada a função cadastrar que ira receber os dados do cadastro e ira salvar na variavel global dos usuarios e tambem ficara salvo o email e senha dele na lista de entrada   
            usuario = cadastrar()
            usuarioemail = [usuario[3],usuario[4]]
            atualizar(usuarioemail,"Dados/login.txt","login")
            atualizar(usuario,"Dados/usuario.txt","usuario")
            x = input("%s"%("Precione 'Enter' para continuar..."))
           
        elif digito=="1":
            #aqui chamara a função entrar e ira verificar se o usuario digitou corretamente caso ele digite corretamente ele podera acessar o programa e sera retornado o seu numero na lista usuario global
            verificar = entrar()
            if verificar[0] == 1:
                x = input("%s"%("Precione 'Enter' para continuar..."))
                return verificar[1]
            else: 
                print("%s"%("Login errado!!! tente novamente"))
        else:
            print("Digite o numero corretamente")
#aqui a função onde o usuario podera escolher entre ver os alimentos ou cadastrar um pedido
def escolha_usuario2(num_entrar):
    
    while True:
        digito = input("\n%s\n%s\n%s\n%s\n" % ("|--------------------------------------|","|Digite 1 para ver todas as comidas    |\n|Digite 2 para buscar e mostrar valores|\n|Digite 3 para cadastrar o seu pedido  |","|Digite 4 para sair do programa        |","|--------------------------------------|"))
        if digito == "1":
            #Aqui chamara uma função que ira listar todas as comidas
            listar_comida()
            x = input("%s"%("Precione 'Enter' para continuar..."))
            sabores()
        elif digito == "2":
            #Aqui chamara a função que buscará uma comida especifica
            buscar_comida()
            x = input("%s"%("Precione 'Enter' para continuar..."))
        elif digito == "3":
            #aqui o num_entrar esta passando o numero do usuario dele na lista de usuario global para que ele seja utilizado depois
            pedido(num_entrar)
            x = input("%s"%("Precione 'Enter' para continuar..."))
        elif digito == "4":
            #aqui o num_entrar esta passando o numero do usuario dele na lista de usuario global para que ele seja utilizado depois
            x = input("%s"%("Saindo do programa....."))
            break 
        else:
            print("Digite o numero corretamente")         
#Aqui ira cadastrar o usuario
def cadastrar():
    vetor= []
    vetor.append(input("%s" %("Digite seu nome:\n")))
    while True:
        cep = input("%s" %("Digite seu CEP:(XXXXX-XXX)\n"))
        if len(cep) == 8:
            cep = cep[:5]+"-"+cep[5:]
            break
        elif len(cep)==9 and cep[5]=="-":
            break
        else:
            print("Digite um CEP valido!!!")
    vetor.append(cep)
    while True:
        cpf = input("%s" %("Digite seu CPF:(XXX.XXX.XXX-XX)\n"))
        if len(cpf) == 11:
            cpf = cpf[:3]+"."+cpf[3:6]+"."+cpf[6:9]+"-"+cpf[9:]
            break
        elif len(cpf)==14 and cpf[3]=="." and cpf[7]=="." and cpf[11]=="-":
            break
        else:
            print("Digite um CPF valido!!!")
    vetor.append(cpf)
    while True:
        email = input("%s" %("Digite seu E-mail:\n"))
        for elemento in email:
            if elemento=="@":
                verificado = 1
                break
            else:
                verificado = 0
        if verificado ==1:
            break
        else:
            print("Digite um E-mail valido!!!")

    vetor.append(email)
    while True:
        senha = input("%s" %("Digite sua senha:\n"))
        confirmarsenha = input("%s" %("Confirme sua senha:\n"))
        if senha == confirmarsenha:
            vetor.append(senha)
            #caso esteja tudo certo ira retornar todas as informações do usuario
            return vetor
        else:
            print("%s" %("SENHAS INVALIDAS!!!!!"))
#Aqui verificara se o usuario tem email e senha cadastrados
def entrar():
    email = input("%s" %("Digite seu email:\n"))
    senha = input("%s" %("Digite a sua senha:\n"))
    #aqui ira verificar se o email e senha digitado pelo usuario esta dentro da lista de entrada
    for i in range(len(listaentrar)):
        if email == listaentrar[i][0] and senha == listaentrar[i][1]:
            numero_lista = i
            verificar = 1
            break
    else:
        verificar = 0
        numero_lista=-1
    lista =[verificar,numero_lista]
    #caso esteja tudo certo ira retornar que ele esta verificado e o numero dele na lista global dos usuarios
    return lista
#aqui é a função que lista todas as comidas
def listar_comida():
    #contar ele que vai gerar o numero dos alimentos
    contar = 1
    #aqui ira receber todas as listas de comidas
    total =[] 
    #aqui é a varivel que vai verificar qual das listas tem maior quantidade
    maior = 0
    #aqui esta recendo todas as quantidade de todas as listas
    totalC= len(comidasC)
    totalS= len(comidasS)
    totalD= len(comidasD)
    totalL= len(comidasL)
    #aqui esta jogando na variavel total
    total.append(totalC)
    total.append(totalS)
    total.append(totalD)
    total.append(totalL)
    #verifica qual a lista maior para que depois nao tenha espaços em branco em vão
    for i in range(0,len(total)):
        if total[i]>=maior:
            maior = total[i]
    #aqui os nomes das categorias
    print("|  %-3s|     %-15s|     %-15s|     %-15s|     %-15s|"%("Nº","SALGADOS","DOCES","CARNES","LANCHES"))
    #primeiro o loop vai gerar os numeros
    for i in range(maior):


        print("|  %-3s|"%(contar), end="")
        #depois ira verificar se no caso na linha tem alimento na lista caso tenha ele colocara o nome caso nao escreverá xxxxx
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
#função que ira buscar uma comida especifica           
def buscar_comida():
    #primeiro o usuario ira digitar a categoria
    while True:
        tipo = input("%s"%("Digite a categoria da comida:(salgados,doces,carnes,laches)\n"))
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
            print("%s"%("Digite a categoria corretamente!!!"))


    #em seguida o numero da comida
    while True:
        while True:
                digitar = input("%s"%("Digite o numero da comida: \n"))
                if(digitar.isdigit()):
                    digitar = int(digitar)
                    break
        #ira verificar se existe e depois ira mostrar o numero da comida e o nome dela em seguida em baixo mostrara o preço 
        #no caso dos lanches mostrara o preço de cada sabor
        #por fim ira mostrar suas avaliação 
        if escolher == 1 and digitar <= len(comidasS) and digitar>0:

            print("Comida: %d | %-9s| "% (digitar,comidasS[digitar-1]))
            print("Preço: R$%-10.2f  |"% preco_S[digitar-1])

            estrela =""
            estrela_vazia = 0

            for i in range (len(avaliacao[0][digitar-1])):
                print("Avaliação: ", end="")
                #aqui para verificar se a avaliação possui nota quebrada
                if avaliacao[0][digitar-1][i]%1!=0:
                    
                    for j in range(int(avaliacao[0][digitar-1][i])):
                        estrela +="★ "
                        estrela_vazia+=1

                    else:
                        estrela +="⯪ "
                        estrela_vazia+=1

                else:

                    for k in range(int(avaliacao[0][digitar-1][i])):
                        estrela +="★ "
                        estrela_vazia+=1

                for m in range(5-estrela_vazia):
                    estrela += "☆ "
                print("%-10s|"%(estrela))

                estrela = ""
                estrela_vazia=0

            break


        elif escolher == 2 and digitar <= len(comidasD) and digitar>0:

            print("Comida: %d | %-9s| "% (digitar,comidasD[digitar-1]))
            print("Preço: R$%-10.2f  |"% preco_D[digitar-1])

            estrela =""
            estrela_vazia = 0

            for i in range (len(avaliacao[1][digitar-1])):
                print("Avaliação: ", end="")
                estrela_vazia = 0
                if avaliacao[1][digitar-1][i]%1!=0:

                    for j in range(int(avaliacao[1][digitar-1][i])):
                        estrela +="★ "
                        estrela_vazia+=1

                    else:
                        estrela +="⯪ "
                        estrela_vazia+=1

                else:

                    for k in range(int(avaliacao[1][digitar-1][i])):
                        estrela +="★ "
                        estrela_vazia+=1
                for m in range(5-estrela_vazia):
                    estrela += "☆ "    
                print("%-10s|"%(estrela))
                estrela = ""
                estrela_vazia=0
            break

        elif escolher == 3 and digitar <= len(comidasC) and digitar>0:

            print("Comida: %d | %-9s| "% (digitar,comidasC[digitar-1]))
            print("Preço: R$%-10.2f  |"% preco_C[digitar-1])
 
            estrela =""
            estrela_vazia = 0
            for i in range (len(avaliacao[2][digitar-1])):
                
                print("Avaliação: ", end="")

                if avaliacao[2][digitar-1][i]%1!=0:

                    for j in range(int(avaliacao[2][digitar-1][i])):
                        estrela +="★ "
                        estrela_vazia+=1

                    else:
                        estrela +="⯪ "
                        estrela_vazia+=1

                else:

                    for k in range(int(avaliacao[2][digitar-1][i])):
                        estrela +="★ "
                        estrela_vazia+=1

                for m in range(5-estrela_vazia):
                    estrela += "☆ "

                print("%-10s|"%(estrela))
                estrela = ""
                estrela_vazia=0

            break

        elif escolher == 4 and digitar <= len(comidasL) and digitar>0:
            #AQUI ENTRA AS CATEGORIAS LANCHES
            if digitar == 1:
                print("Comida: %d | %-9s| "%(digitar,comidasL[digitar-1][0]))
                
                for i in range(len(comidasL[0])-1):
                    print("Sabor: %-13s | "% comidasL[digitar-1][i+1])
                    print("Preço: R$%-10.2f  |"% preco_LPiz[i])

                    estrela =""
                    estrela_vazia = 0
                    for k in range (len(avaliacao[3][0][i])):
                        print("Avaliação: ", end="")
                        if avaliacao[3][0][i][k]%1!=0:

                            for j in range(int(avaliacao[3][0][i][k])):
                                estrela +="★ "
                                estrela_vazia+=1

                            else:
                                estrela +="⯪ "
                                estrela_vazia+=1

                        else:

                            for k in range(int(avaliacao[3][0][i][k])):
                                estrela +="★ "
                                estrela_vazia+=1
                        for m in range(5-estrela_vazia):
                            estrela += "☆ "    
                        print("%-10s|"%(estrela))

                        estrela = ""
                        estrela_vazia=0
                        
                    print("--------------------------")  

                break
               
               
            elif digitar ==2:
                print("Comida: %d | %-9s| "%(digitar,comidasL[digitar-1][0]))

                for i in range(len(comidasL[1])-1):
                    print("Sabor: %-13s | "% comidasL[digitar-1][i+1])
                    print("Preço: R$%-10.2f  |"% preco_LHam[i])

                    estrela =""
                    estrela_vazia=0

                    for k in range (len(avaliacao[3][1][i])):
                        print("Avaliação: ", end="")
                        if avaliacao[3][1][i][k]%1!=0:
                            for j in range(int(avaliacao[3][1][i][k])):
                                estrela +="★ "
                                estrela_vazia+=1

                            else:
                                estrela +="⯪ "
                                estrela_vazia+=1

                        else:
                            for k in range(int(avaliacao[3][1][i][k])):
                                estrela +="★ "
                                estrela_vazia+=1

                        for m in range(5-estrela_vazia):
                            estrela += "☆ "            
                        print("%-10s|"%(estrela))
                        estrela = ""
                        estrela_vazia=0
                    print("--------------------------")
                break


            elif digitar ==3:
                print("Comida: %d | %-9s| "%(digitar,comidasL[digitar-1][0]))


                for i in range(len(comidasL[2])-1):
                    print("Sabor: %-13s | "% comidasL[digitar-1][i+1])
                    print("Preço: R$%-10.2f  |"% preco_LPas[i])
 
                    estrela =""
                    estrela_vazia=0
                    for k in range (len(avaliacao[3][2][i])):
                        print("Avaliação: ", end="")
                        if avaliacao[3][2][i][k]%1!=0:

                            for j in range(int(avaliacao[3][2][i][k])):
                                estrela +="★ "
                                estrela_vazia+=1

                            else:
                                estrela +="⯪ "
                                estrela_vazia+=1

                        else:

                            for k in range(int(avaliacao[3][2][i][k])):
                                estrela +="★ "
                                estrela_vazia+=1
                        for m in range(5-estrela_vazia):
                            estrela += "☆ "            
                        print("%-10s|"%(estrela))
                        estrela = ""
                        estrela_vazia=0
                    print("--------------------------")
                break

            elif digitar ==4:
                print("Comida: %d | %-9s| "%(digitar,comidasL[digitar-1][0]))


                for i in range(len(comidasL[3])-1):
                    print("Sabor: %-13s | "% comidasL[digitar-1][i+1])
                    print("Preço: R$%-10.2f  |"% preco_LHot[i])
 
                    estrela =""
                    estrela_vazia=0
                    for k in range (len(avaliacao[3][3][i])):
                        print("Avaliação: ", end="")
                        if avaliacao[3][3][i][k]%1!=0:

                            for j in range(int(avaliacao[3][3][i][k])):
                                estrela +="★ "
                                estrela_vazia+=1

                            else:
                                estrela +="⯪ "
                                estrela_vazia+=1

                        else:

                            for k in range(int(avaliacao[3][3][i][k])):
                                estrela +="★ "
                                estrela_vazia+=1
                        for m in range(5-estrela_vazia):
                            estrela += "☆ "            
                        print("%-10s|"%(estrela))
                        estrela = ""
                        estrela_vazia=0
                    print("--------------------------")
                break
            elif digitar ==5:
                print("Comida: %d | %-9s| "%(digitar,comidasL[digitar-1][0]))


                for i in range(len(comidasL[4])-1):
                    print("Sabor: %-13s | "% comidasL[digitar-1][i+1])
                    print("Preço: R$%-10.2f  |"% preco_LTapi[i])
 
                    estrela =""
                    estrela_vazia=0
                    for k in range (len(avaliacao[3][4][i])):
                        print("Avaliação: ", end="")
                        if avaliacao[3][4][i][k]%1!=0:

                            for j in range(int(avaliacao[3][4][i][k])):
                                estrela +="★ "
                                estrela_vazia+=1

                            else:
                                estrela +="⯪ "
                                estrela_vazia+=1

                        else:

                            for k in range(int(avaliacao[3][4][i][k])):
                                estrela +="★ "
                                estrela_vazia+=1
                        for m in range(5-estrela_vazia):
                            estrela += "☆ "            
                        print("%-10s|"%(estrela))
                        estrela = ""
                        estrela_vazia=0
                    print("--------------------------")
                break
            elif digitar ==6:
                print("Comida: %d | %-9s| "%(digitar,comidasL[digitar-1][0]))


                for i in range(len(comidasL[5])-1):
                    print("Sabor: %-13s | "% comidasL[digitar-1][i+1])
                    print("Preço: R$%-10.2f  |"% preco_LSand[i])
 
                    estrela =""
                    estrela_vazia=0
                    for k in range (len(avaliacao[3][5][i])):
                        print("Avaliação: ", end="")
                        if avaliacao[3][5][i][k]%1!=0:

                            for j in range(int(avaliacao[3][5][i][k])):
                                estrela +="★ "
                                estrela_vazia+=1

                            else:
                                estrela +="⯪ "
                                estrela_vazia+=1

                        else:

                            for k in range(int(avaliacao[3][5][i][k])):
                                estrela +="★ "
                                estrela_vazia+=1
                        for m in range(5-estrela_vazia):
                            estrela += "☆ "            
                        print("%-10s|"%(estrela))
                        estrela = ""
                        estrela_vazia=0
                    print("--------------------------")
                break

        else:
            print("%s"%("Nao foi possivel achar uma comida com esse numero!!!"))

#aqui onde o usuario ira escolher seu pedido e podera escolher em editar, acidionar,finalizar ou excluir
def pedido(num_login):
    #ira mostrar a lista das comidas novamente
    listar_comida()
    #aqui ira receber todos os pedidos do usuario
    totalpedido =[]
    #aqui ira receber o pedido
    totalpedido.append(func_pedir())
    while True:
        listar_comida()
        digitar = input("\n%s\n%s\n%s\n%s\n%s\n%s\n"%("|-------------------------------------|","|Digite 1 para adicionar pedido       |","|Digite 2 para editar pedido          |","|Digite 3 para finalizar pedido       |","|Digite 4 para excluir pedido         |","|-------------------------------------|"))
        if digitar =="1":
            #chama a função para acrescentar na lista total do pedido do usuario
            totalpedido.append(func_pedir())
        elif digitar =="2":
            #aqui a função recebe a lista total do pedido do usuario
            digito = editar(totalpedido)
            #aqui sera substituido pelo novo valor do usuario
            totalpedido[digito - 1] = func_pedir()
            
        elif digitar =="3":
            #aqui sera gerado o o boleto para finalizar a compra
            boleto(totalpedido,num_login)
            print("%s"%("pagamento concluido"))
            x = input("%s"%("Precione 'Enter' para continuar"))
            
            #caso o usuario queira poderá fazer o feedback dos alimentos pedidos
            print("%s"%("|-----------------------------------------------------------------------------------------------------|"))
            digitar = input("%s"%("| Digite 'sim' para fazer o feedback dos alimentos ou precione 'Enter' para retornar a pagina inicial.|\n|-----------------------------------------------------------------------------------------------------|\n"))
            if digitar.lower() == "sim" or digitar.lower()=="s" or digitar.lower()=="yes" or digitar.lower()=="y":
                feedback(totalpedido)
            break

        elif digitar == "4":
            #aqui se o usuario queira poderá ser exluido os pedidos
            exluir(totalpedido)
            x = input("%s"%("Precione 'Enter' para continuar"))
    
#aqui é a função onde o usuario ira cadastrar seu pedido
def func_pedir():
    while True:
        while True:
            #primeiro ele ira escrever a categoria
            digitar_catec = input("%s"%("Digite a categoria do alimento:(salgados,doces,carnes,lanches)\n"))
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
                sabores()
                catec = 4
                break
            else:
                print("%s"%("Categoria não encontrada!!!"))
        while True:
            #depois ira escrever o numero do alimento
            sabor = ""
            while True:
                digitar_comida = input("%s"%("Digite o numero da comida: \n"))
                if(digitar_comida.isdigit()):
                    digitar_comida = int(digitar_comida)
                    break
                
            if catec == 1 and digitar_comida>0 and digitar_comida<=len(comidasS):
                break
            elif catec == 2 and digitar_comida>0 and digitar_comida<=len(comidasD):
                break
            elif catec == 3 and digitar_comida>0 and digitar_comida<=len(comidasC):
                break
            elif catec == 4 and digitar_comida>0 and digitar_comida<=len(comidasL):
                k =0
                #caso o alimento tenha tenha sabor e esteja dentro da categoria lanches o usuario precisara escrever o sabor
                while k<2:
                    sabor = input("%s"%("Digite o sabor desejado:\n"))
                    sabor = sabor.lower()
                    #aqui ira verificar se o sabor que o usuario digitou pertence a lista do alimento que ele tinha informado antes 
                    for i in range(len(comidasL[digitar_comida-1])):
                        if sabor == comidasL[digitar_comida-1][i].lower():
    
                            k = 3
                            break
                    else:
                        print("%s"%("Sabor não encontrado!!!"))
                break     
            else: 
                print("%s"%("Alimento não encontrado!!!"))

        #aqui é a quantidade
        while True:
            quantidade = input("%s"%("Digite a quantidade:\n"))
            if quantidade.isdigit():
                quantidade = int(quantidade)
                break
        
        if catec ==1:
            pedir = [comidasS[digitar_comida-1],quantidade,sabor,catec, digitar_comida-1]
        elif catec ==2:
            pedir = [comidasD[digitar_comida-1],quantidade,sabor,catec, digitar_comida-1]
        if catec ==3:
            pedir = [comidasC[digitar_comida-1],quantidade,sabor,catec, digitar_comida-1]
        if catec ==4:
            pedir = [comidasL[digitar_comida-1][0],quantidade,sabor,catec, digitar_comida-1]
        #aqui ira retornar como forma de lista tudo que o usuario pediu será enviado na ordem: (nome da comida)/(quantidade)/(sabor)/(numero da categoria) e (numero da comida)
        return pedir
#aqui é a função onde o usuario podera editar o seu pedido   
def editar(total):
    print()
    #aqui sera listado todos os pedidos do usuario
    for i in range(len(total)):
        if total[i][2]=="":
            print(f"{i+1}º pedido: {total[i][0]} | quantidade: {total[i][1]}\n")
        else:
            print(f"{i+1}º pedido: {total[i][0]} | quantidade: {total[i][1]} | sabor: {total[i][2]}\n")
    #aqui o usuario pode escolher qual pedido pode ser editado
    while True:
        while True:
            digito = input("%s"%("Digite o número do pedido que deseja editar: \n"))
            if digito.isdigit():
                digito = int(digito)
                break

        
        if digito>0 and digito <= len(total):
            break
        else:
            print("%s"%("Pedido não encontrado."))

        print("%s"%("Por favor, digite um número válido."))
    
    return digito
#aqui o usuario podera escolher em exluir o pedido    
def exluir(total):
    #poderá excluir tudo ou apenas um pedido
    digito = input("%s"%("\n|-------------------------------------|\n|Digite 1 para exluir todos os pedidos|\n|Digite 2 para exluir um pedido       |\n|Digite 3 para cancelar               |\n|-------------------------------------|\n"))
    if digito =="1":
        del total
        escolha_usuario2()

    elif digito =="2":
        print()
        for i in range(len(total)):
            if total[i][2] =="":
                print(f"{i+1}º pedido: {total[i][0]} | quantidade: {total[i][1]}\n")
            else:
                print(f"{i+1}º pedido: {total[i][0]} | quantidade: {total[i][1]} | sabor: {total[i][2]}\n")
        
        while True:
            #aqui ele ira escolher qual pedido será exlcuido
            while True:
                digito = input("%s"%("Digite o número do pedido que deseja excluir: \n"))
            
                if digito.isdigit():
                    digito = int(digito)
                    break
            
            if digito>0 and digito <= len(total):
                break
            else:
                print("%s"%("Pedido não encontrado."))
        del total[digito - 1]
 
#aqui sera gerado o boleto ira receber a quantidade total de pedidos do usuario e o numero dele na lista global de usuario       
def boleto(total,num_login):
    precototal = 0
    print()
    print()
    print("--------------------------------------------------------")
    #aqui pegara as informações do usuario
    print(f"{listausuario[num_login][0]} CEP: {listausuario[num_login][1]} CPF: {listausuario[num_login][2]} \n")
    #aqui sera listado todos os pedidos do usuario e o preço de cada alimento sera calculado para jogar no preço total da compra
    #para calcular o preço pegara o preço dele normal e sera multiplicado pela quantidade
    for i in range(len(total)):
            if total[i][2]=="":
                print(f"{i+1}º pedido: {total[i][0]} | quantidade: {total[i][1]}\n")
            else:
                print(f"{i+1}º pedido: {total[i][0]} | quantidade: {total[i][1]} | sabor: {total[i][2]}\n")
            if total[i][3] == 1:
                precototal += (preco_S[total[i][4]]*total[i][1])

            elif total[i][3] == 2:
                precototal += (preco_D[total[i][4]]*total[i][1])

            elif total[i][3] == 3:
                precototal += (preco_C[total[i][4]]*total[i][1])
            #aqui verificara qual o sabor do alimento pois cada lanche possui preços diferentes para seus sabores
            elif total[i][3] == 4:
                if total[i][4] == 0:
                    
                    for j in range(len(comidasL[0])):
                        if total[i][2] == comidasL[0][j].lower():
                            precototal += (preco_LPiz[j-1]*total[i][1]) 
                               
                elif total[i][4] == 1:

                    for k in range(len(comidasL[1])):
                        if total[i][2] == comidasL[1][k].lower():
                            precototal += (preco_LHam[k-1]*total[i][1])
                          
                elif total[i][4] == 2: 
                    for n in range(len(comidasL[2])):
                        if total[i][2] == comidasL[2][n].lower():
                            precototal += (preco_LPas[n-1]*total[i][1]) 
                elif total[i][4] == 3: 
                    for n in range(len(comidasL[3])):
                        if total[i][2] == comidasL[3][n].lower():
                            precototal += (preco_LHot[n-1]*total[i][1]) 
                elif total[i][4] == 4: 
                    for n in range(len(comidasL[4])):
                        if total[i][2] == comidasL[4][n].lower():
                            precototal += (preco_LTapi[n-1]*total[i][1]) 
                elif total[i][4] == 5: 
                    for n in range(len(comidasL[5])):
                        if total[i][2] == comidasL[5][n].lower():
                            precototal += (preco_LSand[n-1]*total[i][1]) 
    #mostrara o preço total
    print("O preço total é de: R$ %.2f"% precototal) 
    print("--------------------------------------------------------")      
#aqui é a função para fazer o feedback dos alimentos
def feedback(total):
    #mostrara um alimento que foi feito na compra
    for i in range(len(total)):
        print("--------------------------")
        if total[i][2]=="":
            print("%10s"%total[i][0])
        else:
            print("%8s de %s "%(total[i][0], total[i][2]))
        print("--------------------------")
        while True:
            #o usuario pode avaliar o alimento entre 1 e 5
            while True:
                digito = input("%s"%("Digite entre 0 e 5 para esse alimento:\n"))
                if digito.isdigit():
                    digito = float(digito)
                    break
            if 0.0 <= digito <= 5.0:
                break
        print()
        #aqui verifica onde o alimento pertence para ele ficar salvo na lista avaliação
        if total[i][3] == 1:
            avaliacao[0][total[i][4]].append(digito)
        elif total[i][3] == 2:
            avaliacao[1][total[i][4]].append(digito)
        elif total[i][3] == 3:
            avaliacao[2][total[i][4]].append(digito)
        elif total[i][3] == 4:
            #aqui verifica o sabor pois cada sabor dos lanches possui avaliações diferentes
            if total[i][4] == 0:
                
                for j in range(len(comidasL[0])):
                    if total[i][2] == comidasL[0][j].lower():
                        avaliacao[3][0][j-1].append(digito) 
                            
            elif total[i][4] == 1:

                for k in range(len(comidasL[1])):
                    if total[i][2] == comidasL[1][k].lower():
                        avaliacao[3][1][k-1].append(digito) 
                        
            elif total[i][4] == 2: 
                for n in range(len(comidasL[2])):
                    if total[i][2] == comidasL[2][n].lower():
                        avaliacao[3][2][n-1].append(digito)  
            elif total[i][4] == 3: 
                for n in range(len(comidasL[3])):
                    if total[i][2] == comidasL[3][n].lower():
                        avaliacao[3][3][n-1].append(digito)
            elif total[i][4] == 4: 
                for n in range(len(comidasL[4])):
                    if total[i][2] == comidasL[4][n].lower():
                        avaliacao[3][4][n-1].append(digito)
            elif total[i][4] == 5: 
                for n in range(len(comidasL[5])):
                    if total[i][2] == comidasL[5][n].lower():
                        avaliacao[3][5][n-1].append(digito)  
    else:
        substituir(avaliacao)
def sabores():

    print()
    for i in range(len(comidasL)):
        for j in range(18):
            print("_", end="")
    print()
    for i in range(len(comidasL)):
        print("|%-18s"%comidasL[i][0], end="")
    print()
    for i in range(len(comidasL)):
        for j in range(18):
            print("_", end="")
    print()
    for k in range(sabores_total-2):
        for i in range(len(comidasL)):
            print("|%-18s"%comidasL[i][k+1][:18], end="")
        print()
    for m in range(len(comidasL)):
            print("|%-18s"%comidasL[m][-1][:18], end="")
    print()
    for i in range(len(comidasL)):
        for j in range(18):
            print("_", end="")
    print()

def atualizar(valor,texto_arquivo,chave = ""):

    arquivo = open(texto_arquivo, "r")
    arquivo2 = arquivo.readlines()
    arquivo.close()
    arquivo = open(texto_arquivo, "w")
    for linha in (arquivo2):
            arquivo.write(f"{linha}")

    for linha in (valor):
        arquivo.write(f"{linha}\n")    
    arquivo.close()

    atualizarvariaveis(texto_arquivo, chave)  

def atualizarvariaveis(texto,variavel):
    arquivo = open(texto, "r")
    arquivo2 = arquivo.readlines()
    arquivo.close()
    if variavel == "login":
        global listaentrar
        listaentrar = [] 
        for contador in range(0,len(arquivo2),2):
            usuario = [arquivo2[contador][:-1],arquivo2[contador+1][:-1]]
            listaentrar.append(usuario)
    elif variavel == "usuario":
        global listausuario
        listausuario = [] 
        for contador in range(0,len(arquivo2),5):
            usuario = [arquivo2[contador][:-1],arquivo2[contador+1][:-1],arquivo2[contador+2][:-1],arquivo2[contador+3][:-1],arquivo2[contador+4][:-1]]
            listausuario.append(usuario)
    
def substituir(valor):
    for i in range(0, 3):
        arquivo = open(diretorioavaliacao[i], "w")
        for linha in (valor[i]):
            if len(linha) > 0:  # evita escrever linhas vazias
                arquivo.write(",".join(map(str, linha)) + "\n")
        arquivo.close()

    for j in range(0, 5):
        arquivo = open(diretorioavaliacaolanche[j], "w")
        for linha in (valor[3][j]):
            if len(linha) > 0:
                arquivo.write(",".join(map(str, linha)) + "\n")
        arquivo.close()

    
#aqui chamara a função menu
menu()