
valor1 = int(input("Informe o primero número: "))
valor2 = int(input("Informe o segundo número: "))

operacao = input("Informe a Operação com os sinais a cima: ")
resultado = 0

if(operacao == '+'):
  resultado = valor1 + valor2
elif(operacao == '-'):
  resultado = valor1 - valor2
elif(operacao == '*'):
  resultado = valor1 * valor2
elif(operacao == '/'):
  resultado = valor1 / valor2
else:
  print("ERRO")
  
print(valor1,operacao,valor2,'=',resultado)                                                                                                                                                                     
