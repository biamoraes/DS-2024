letra = 's'
while letra == 's':

    n1 = float(input("Digite a primeira nota: "))
    n2 = float(input("Digite a segunda nota: "))
    n3 = float(input("Digite a terceira nota: "))

    soma = n1 + n2 + n3
    media = soma / 3

    print(f"A média do aluno é: {round(media, 2)}")

    if media >= 7:
        print("Aluno foi APROVADO")
    elif media >= 3:
        print("Aluno está em RECUPERAÇÃO")
    else:
        print("Aluno foi REPROVADO")

    letra = input("Deseja continuar? [S/N]: ")