curso = ["Engenharia Civil","Engenharia de Produção","Engenharia Elétrica","Engenharia Mecânica","Ciências Aeronáuticas"]

for i in range(len(curso)):
    print(curso[i].lower())
    print('============================')
    print(curso[i].capitalize())
    print('============================')
    print(curso[i].upper())
    print('============================')
    print(curso[i].casefold())
    print('============================')
    i+=1
