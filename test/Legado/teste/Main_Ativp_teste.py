from unidecode import unidecode
curso = ['Formação Pedagógica em Matemática para Graduados',
        'Formação Pedagógica em Pedagogia para Graduados',
        'Formação de Docente para a Educação Básica - Geografia',
        'Formação de Docente para a Educação Básica - História',
        'Formação de Docente para a Educação Básica - Letras',
        'Formação de Docente para a Educação Básica - História',
        'Segunda Licenciatura em Geografia',
        'Segunda Licenciatura em História',
        'Segunda Licenciatura em Letras - Espanhol',
        'Segunda Licenciatura em Letras - Inglês',
        'Segunda Licenciatura em Letras - Português',
        'Segunda Licenciatura em Matemática',
        'Segunda Licenciatura em Pedagogia']

for i in range(len(curso)):
    # print(curso[i].lower())
    # print('============================')
    # print(curso[i].capitalize())
    print('============================')
    print(curso[i].upper())
    print('============================')
    # print(curso[i].casefold())
    # print('============================')
    print(unidecode(curso[i]))
    # print('============================')
    i+=1
