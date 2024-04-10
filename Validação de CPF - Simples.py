# // Validação de CPF - Simples

# Função para validação do CPF
def valida1(n1, x): #n1 é uma lista
    soma = digito = resto =0 #armazendando e inicializando
    cont=x
    for i in n1:
        soma += i*cont
        cont -=1
    resto =soma%11 #Verificar o resto
    if resto < 2:
        digito=0
    else:
        digito=11 - resto
    return digito


#programa principal
cpfnum=[] #lista 
digiuno=digiduo=cpfd1=cpfd2=0 #Variavel para armazenar o digito, d1 e d2 guarda os digitos passados pelo usuário
cpfval=""


print("Dgite seu número de CPF (Somente números)")
cpf=input()


#Validação dos digitos 
for i in range(0,9,1): #Considerar que o CPF deve ter 9 números, mostra somente os primeiros números, sem mostrar os dois últimos. 
    cpfnum.append(int(cpf[i:i+1]))#Armazena na lista e transforma a varíavel cpf em inteiro
#print(cpfnum)
digiuno=valida1(cpfnum, 10)
cpfnum.append(digiuno) #Colocado no final da lista, o digito descoberto na linha 24
digiduo=valida1(cpfnum, 11)
cpfnum.append(digiduo)
#Tranformar noamente em uma string para mostrar ao usuário 
for i in cpfnum :
    cpfval += str(i)
cpfd1 = int(cpf[-2:-1]) #ou cpf[(9:10)]
cpfd2=int(cpf[-1]) #Colocando somente o -1, mostra o número caracter por ser de trás para frente 
#Comparações
if digiuno == cpfd1 and digiduo == cpfd2 :
    print(f"O CPF de número {cpf} é valido")
else:
    print(f"O CPF de número{cpf} é inválido")
    print(f"O correto seria {cpfval}")