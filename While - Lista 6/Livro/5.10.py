pontos=0
questao=1
while questao <= 3:
    resposta = str.lower(input("Resposta da questão {}: " .format(questao))
    if questao == 1 and resposta == "b":
        pontos +=1        
    elif questao == 2 and resposta == "a":
        pontos +=1
    elif questao == 3 and resposta == "d":
        pontos +=1
    questao +=1
print("O aluno fez {} ponto(s)" .format(pontos))
