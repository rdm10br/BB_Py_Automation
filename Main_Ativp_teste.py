curso = ["Bacharelado em Educação Física",
        "Fisioterapia",
        "Terapia Ocupacional"
        ,"Nutrição"]

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
