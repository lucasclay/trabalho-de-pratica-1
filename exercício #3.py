nome= (input('Escreva o nome do Aluno:'))
n1= float(input('Primeira nota do aluno:'))
n2= float(input('Segunda nota do aluno:'))
média = (n1 + n2) / 2

print ('A média de {} foi {}'.format(nome,média))

if média >= 7:
    print(f'o aluno foi aprovado')
if média < 7 :
    print(f'o aluno foi reprovado')





