# Gustavo, Guilherme e Gabriel
# 10/03/2026
# UMC
# Entrada de dados
amarelo_negrito = "\033[1;33m"
print("""
=================================
       FOLHA DE PAGAMENTO
=================================
""") 
nome = input("Digite o nome do funcionário: ")
cpf = input("Digite o CPF do empregado: ")

horas_normais = int(input("Digite as horas totais trabalhadas: "))
horas_extras = int(input("Digite as horas extras trabalhadas: "))
vh = float(input("Digite o valor da hora em R$: ")) #Valor da Hora
adicional_hora_extra = float(input("Digite o adicional de hora extra (%): "))

desc = float(input("Digite o desconto aplicado sobre o salário bruto (%): ")) #Desconto Aplicado sobre o Salario

# Processamento
shn = horas_normais * vh
she = horas_extras * vh 

shead = horas_extras * (adicional_hora_extra / 100) + she  #Salario Horas extras mais adicional
sb = shn + shead #Salario Bruto

sliq = sb - sb * (desc / 100) #Salario Liquido
#Saida 
print("""
=================================
       FOLHA DE PAGAMENTO
=================================
""") 
print(f"{amarelo_negrito}nome: ",nome)
print("CPF: ",cpf)
print("Salario das horas normais",shn)
print("Salario das horas extras: ",shead)
print("Salario Bruto: ",sb)
print("Salario liquido: ",sliq)
