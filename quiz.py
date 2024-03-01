print("Oq você sabe de programação ?")
iniciar = input("Deseja iniciar o quiz? (S/N) ")

score = 0

if iniciar != "S":
    print("Quiz encerrado, você não obteve nenhuma pontuação")
    quit()

print("""\nQual a diferença entre Hardware e Software?
      
      [A] - Hardware e um programa, dados e instruções que comandam o funcionamento de um dispositivo e Software seria uma parte física de um eletrônico
      [B] - Hardware e seria uma parte física de um eletrônico e Software e um programas, dados e instruções que comandam o funcionamento de um dispositivo""")
questao_1 = input("\nQual a alternativa correta? ")

if questao_1 == "B":
    print("\nResposta correta!")
    score += 1
else:
    print("\nResposta incorreta!")

print("""\nQual linguagem serve pra manipulação de banco de dados?
      
      [A] - JavaScript
      [B] - Python
      [C] - SQL""")
questao_2 = input("\nQual a alternativa correta? ")

if questao_2 == "C":
    print("\nResposta correta!")
    score += 1
else:
    print("\nResposta incorreta!")

print("""\nQual a diferença entre Back-end e Front-end?
      
    [A] - Back-end é o que seus usuários veem e inclui elementos visuais já Frond-end consiste nos dados e na infraestrutura que fazem sua aplicação funcionar
    [B] - Back-end consiste nos dados e na infraestrutura que fazem sua aplicação funcionar já Front-end é o que seus usuários veem e inclui elementos visuais""")
questao_3 = input("\nQual a alternativa correta? ")

if questao_3 == "B":
    print("\nResposta correta!")
    score += 1
else:
    print("\nResposta incorreta!")

print("""\nQual será a resposta desse comando: Print("1")+("1")
      
    [A] - 11
    [B] - 1
    [C] - 0
    [D] - NENHUMA DAS ALTERNATIVAS""")
questao_4 = input("\nQual a alternativa correta? ")

if questao_4 == "A":
    print("\nResposta correta!")
    score += 1
else:
    print("\nResposta incorreta!")

print(""""\nQual código ajuda a filtrar na linguagem de SQL?
      
    [A] - WHERE
    [B] - FROM
    [C] - INNER JOIN""")
questao_5 = input("\nQual a alternativa correta? ")

if questao_5 == "A":
    print("\nResposta correta!")
    score += 1
else:
    print("\nResposta incorreta!")

if score >= 4:
    print(f"\nParabens seu score foi de {score}")
else: 
    print(f"\nSeu score foi de {score}")