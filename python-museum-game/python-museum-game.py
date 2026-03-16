#Jogo dos Museus - Demo de Python elaborado por Ana Cecília Rocha Veiga (https://anacecilia.digital/sobre/) para o projeto Recursos Web para GLAM (https://webmuseu.org/recursos/)

#Boas-vindas e instruções
print("JOGO DOS MUSEUS EM PYTHON")
print("Vamos testar os seus conhecimentos sobre museus?")
print("Para jogar é bem simples... Escolha o número da resposta e aperte Enter para conferir o resultado. Vamos começar!")

#Primeira Questão
print("Qual é o primeiro edifício projetado para ser um museu?")
print("1 - Louvre")
print("2 - Prado")
print("3 - Uffizi")

guess = input("Digite o número da sua resposta e aperte Enter:")

if guess == "3":
    print("Isto mesmo! A Galeria Uffizi foi projetada pelo arquiteto Giorgio Vasari, em Florença. Aberta à visitação em 1582, constava inclusive em guias turísticos da época.")
    print("Vamos em frente!")
else:
    print("A respostas correta é Uffizi! A galeria foi projetada pelo arquiteto Giorgio Vasari, em Florença. Aberta à visitação em 1582, constava inclusive em guias turísticos da época.")
    print("Vamos em frente!")

#Segunda Questão
print("Qual é o primeiro museu público da Europa?")
print("1 - British Museum")
print("2 - Ashmolean Museum")
print("3 - National Gallery")

guess = input("Digite o número da sua resposta e aperte Enter:")

if guess == "2":
    print("Você acertou! O Ashmolean Museum foi inaugurado em 1683, objetivando que se tornasse um museu da Universidade de Oxford. A coleção foi doada por Elias Ashmole.")
    print("Vamos mais uma?")
else:
    print("A respostas correta é Ashmolean Museum! Foi inaugurado em 1683, objetivando que se tornasse um museu da Universidade de Oxford. A coleção foi doada por Elias Ashmole.")
    print("Vamos mais uma?")

#Terceira Questão
print("Qual foi o primeiro museu do Brasil")
print("1 - Museu do Ipiranga")
print("2 - Museu Nacional")
print("3 - Museu Imperial")

guess = input("Digite o número da sua resposta e aperte Enter:")

if guess == "2":
    print("Resposta certa! O Museu Real, posteriormente denominado Museu Nacional, foi também a primeira instituição científica do Brasil.") 
else:
    print("A respostas correta é Museu Nacional! O Museu Real, posteriormente denominado Museu Nacional, foi também a primeira instituição científica do Brasil.")
    
print("Obrigada por jogar o Jogo dos Museus, demonstrativo programado em Python pela professora Ana Cecília Rocha Veiga da UFMG para o Projeto Recursos Web para GLAM https://webmuseu.org/recursos/")