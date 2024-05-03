# BB_Py_Automation

## Language Switch

- [English](#english)
- [Português](#português)

---

## English

BlackBoard Python Automation with Playwright

Code made in Python and JavaScript with libraries:
aiofiles
openpyxl
pandas
playwright
pyarrow
pyperclip
pyside6
python-docx
pytest-playwright
regex
spacy
unidecode

### Getting Started

Needs Python 3.12

To install all the dependencies use this command on the console

first update your pip:
```
pip install --upgrade pip
```

then:
```
pip install -r dependencies.txt
```
and
```
python -m spacy download en_core_web_sm
```
```
python -m spacy download pt_core_news_sm
```

or if this file could not be found

```
pip install -r BB_PY_Automation\dependencies.txt
```

to fully install pplaywright use this command

```
python -m playwright install
```

To create new Methods use the command on console

```
python -m playwright codegen
```

Automation for administration of educational system based on BlackBoard platform

consuming API content and internal ID to find items and search courses

search and modifying items to whats preset

---

## Português

Automação em Python para BlackBoard com Playwright

Código feito em Python e JavaScript com as bibliotecas:
aiofiles
openpyxl
pandas
playwright
pyarrow
pyperclip
pyside6
python-docx
pytest-playwright
regex
spacy
unidecode

### Começar a utilizar

Requer Python 3.12

Para instalar todas as dependências, utilize este comando no console:

primeiro atualize o seu pip:
```
pip install --upgrade pip
```

então:
```
pip install -r dependencies.txt
```
e
```
python -m spacy download en_core_web_sm
```
```
python -m spacy download pt_core_news_sm
```

ou se o arquivo não foi encontrado

```
pip install -r BB_PY_Automation\dependencies.txt
```

para instalar completamente o playwright use esse comando

```
python -m playwright install
```

Para criar novos métodos, utilize o seguinte comando no console:

```
python -m playwright codegen
```

Automação para administração de sistema educacional baseado na plataforma BlackBoard.

Consumindo conteúdo de API e ID interno para encontrar itens e buscar cursos.

Pesquisa e modificação de itens de acordo com o predefinido.