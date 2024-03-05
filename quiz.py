# Imprime uma pergunta inicial para o usuário.
print("O que você sabe de programação ?")
# Solicita ao usuário para decidir se deseja iniciar o quiz, aguardando sua resposta.
iniciar = input("Deseja iniciar o quiz? (S/N) ")

# Inicializa a variável score, que será usada para contar o número de respostas corretas.
score = 0

# Verifica se o usuário escolheu não iniciar o quiz. Se sim, o programa é encerrado.
if iniciar != "S":
    print("Quiz encerrado, você não obteve nenhuma pontuação")
    quit() # Encerra o programa.

# Primeira pergunta do quiz.
print("""\nQual a diferença entre Hardware e Software?
      
      [A] - Hardware é um programa, dados e instruções que comandam o funcionamento de um dispositivo e Software seria uma parte física de um eletrônico
      [B] - Hardware seria uma parte física de um eletrônico e Software é um programas, dados e instruções que comandam o funcionamento de um dispositivo""")
# Captura a resposta do usuário para a primeira pergunta.
questao_1 = input("\nQual a alternativa correta? ")

# Verifica se a resposta à primeira pergunta está correta.
if questao_1 == "B":
    print("\nResposta correta!")
    score += 1 # Incrementa a pontuação.
else:
    print("\nResposta incorreta!")

# Segunda pergunta do quiz.
print("""\nQual linguagem serve pra manipulação de banco de dados?
      
      [A] - JavaScript
      [B] - Python
      [C] - SQL""")
# Captura a resposta do usuário para a segunda pergunta.
questao_2 = input("\nQual a alternativa correta? ")

# Verifica se a resposta à segunda pergunta está correta.
if questao_2 == "C":
    print("\nResposta correta!")
    score += 1 # Incrementa a pontuação.
else:
    print("\nResposta incorreta!")

# Terceira pergunta do quiz.
print("""\nQual a diferença entre Back-end e Front-end?
      
    [A] - Back-end é o que seus usuários veem e inclui elementos visuais já Frond-end consiste nos dados e na infraestrutura que fazem sua aplicação funcionar
    [B] - Back-end consiste nos dados e na infraestrutura que fazem sua aplicação funcionar já Front-end é o que seus usuários veem e inclui elementos visuais""")
# Captura a resposta do usuário para a terceira pergunta.
questao_3 = input("\nQual a alternativa correta? ")

# Verifica se a resposta à terceira pergunta está correta.
if questao_3 == "B":
    print("\nResposta correta!")
    score += 1 # Incrementa a pontuação.
else:
    print("\nResposta incorreta!")

# Quarta pergunta do quiz.
print("""\nQual será a resposta desse comando: print("1")+("1")
      
    [A] - 11
    [B] - 1
    [C] - 0
    [D] - NENHUMA DAS ALTERNATIVAS""")
# Captura a resposta do usuário para a quarta pergunta.
questao_4 = input("\nQual a alternativa correta? ")

# Verifica se a resposta à quarta pergunta está correta.
if questao_4 == "A":
    print("\nResposta correta!")
    score += 1 # Incrementa a pontuação.
else:
    print("\nResposta incorreta!")

# Quinta pergunta do quiz.
print("""\nQual código ajuda a filtrar na linguagem de SQL?
      
    [A] - WHERE
    [B] - FROM
    [C] - INNER JOIN""")
# Captura a resposta do usuário para a quinta pergunta.
questao_5 = input("\nQual a alternativa correta? ")

# Verifica se a resposta à quinta pergunta está correta.
if questao_5 == "A":
    print("\nResposta correta!")
    score += 1 # Incrementa a pontuação.
else:
    print("\nResposta incorreta!")

# Avalia o desempenho do usuário com base na pontuação alcançada e imprime uma mensagem final.
if score >= 4:
    print(f"\nParabéns! Seu score foi de {score}")
else: 
    print(f"\nSeu score foi de {score}")
