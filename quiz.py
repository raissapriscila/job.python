questionario = [
{"id":1,"pergunta":"P1","altA":"A","altB":"B","altC":"C","altD":"D","altE":"E","altCorreta":"C"},
{"id":2,"pergunta":"P2","altA":"A","altB":"B","altC":"C","altD":"D","altE":"E","altCorreta":"A"},
{"id":3,"pergunta":"P3","altA":"A","altB":"B","altC":"C","altD":"D","altE":"E","altCorreta":"B"},
]
resposta = []
for q in questionario:
print(q["pergunta"])
print(q["altA"])
print(q["altB"])
print(q["altC"])
print(q["altD"])
print(q["altE"])
resposta = input("Digite a alternativa escolhida:")
for i in resposta:
print(resposta)