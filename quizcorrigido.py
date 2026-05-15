questionario = [
    {"id":1,"pergunta":"P1","altA":"A","altB":"B","altC":"C","altD":"D","altE":"E","altCorreta":"C"},
    {"id":2,"pergunta":"P2","altA":"A","altB":"B","altC":"C","altD":"D","altE":"E","altCorreta":"A"},
    {"id":3,"pergunta":"P3","altA":"A","altB":"B","altC":"C","altD":"D","altE":"E","altCorreta":"B"},
]

acertos = 0

for q in questionario:

    print("\n", q["pergunta"])
    print("A)", q["altA"])
    print("B)", q["altB"])
    print("C)", q["altC"])
    print("D)", q["altD"])
    print("E)", q["altE"])

    resposta = input("Digite a alternativa escolhida: ").upper()

    if resposta == q["altCorreta"]:
        print("Resposta correta!")
        acertos += 1
    else:
        print("Resposta errada!")
        print("Alternativa correta:", q["altCorreta"])

print("\nTotal de acertos:", acertos)
print("Total de erros:", len(questionario) - acertos)