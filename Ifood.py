listaentrar = []
listausuario = []

def menu():
    logo()
    while True:
        digito = int(input("\n|-----------------------|\n|Digite 1 para entrar   |\n|Digite 2 para cadastrar|\n|-----------------------|\n"))
        if digito ==2:    
            usuario = cadastrar()
            listausuario.append(usuario)
            listaentrar.append(usuario[3])
            listaentrar.append(usuario[4])
            
        else:
            verificar = entrar()
            if verificar == 1:
                break
            else: 
                print("Login errado!!! tente novamente")

        


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

def entrar():
    email = input("Digite seu email:\n")
    senha = input("Digite a sua senha:\n")
    for i in range(0,len(listaentrar),2):
        if email == listaentrar[i] and senha == listaentrar[i+1]:
            verificar = 1
        else:
            verificar = 0
        
    return verificar

#def lista_comida():


#def buscar_comida():

#def editar_pedido():

#def fazer_pedido():

#def boleto():

def logo():
    for i in range (3):
        for j in range(6):
            if i==0 or i==2:
                print("/ * ", end="")
            elif j ==1 and i ==1:
                print("     SEJA BEM VINDO    ")
                print("      AO IFOODFEI")
        print()
menu()