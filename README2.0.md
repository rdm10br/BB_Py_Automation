# BB_Py_Automation

## Visão Geral

O projeto **BB_Py_Automation** é uma suíte de automação Python para manipulação de cursos, usuários e conteúdos na plataforma Blackboard, utilizando Playwright para automação de navegador, integração com APIs REST, manipulação de planilhas e controle de execução assíncrona e concorrente. O sistema é altamente modular, com uso extensivo de decoradores para controle de fluxo, logging, internacionalização e gerenciamento de contexto.

---

## Funcionalidades Principais

- **Automação de Login**: Realiza login automatizado na plataforma Blackboard, captura e gerencia cookies de sessão.
- **Execução em Lote**: Processa múltiplos cursos/usuários em lote, com controle de concorrência e paralelismo.
- **Inscrição e Remoção Automática**: Inscreve e remove automaticamente usuários em cursos, com tratamento de exceções e feedback detalhado.
- **Integração com APIs Blackboard**: Consulta e manipula dados de cursos, usuários e conteúdos via endpoints REST públicos e privados.
- **Manipulação de Planilhas**: Lê e escreve status de processamento em planilhas Excel, permitindo controle e reprocessamento.
- **Internacionalização**: Suporte a múltiplos idiomas via pacotes de linguagem.
- **Logging Avançado**: Captura e exibe logs com timestamp, além de redirecionamento de saída para análise posterior.
- **Controle de Pausa**: Permite pausar e retomar execuções de forma controlada.
- **Configuração por Variáveis de Ambiente**: Utiliza `.env` para configuração dinâmica de URLs e parâmetros sensíveis.

---

## Estrutura dos Principais Módulos

### `src/Decorators/Main_StartUp.py`

- **Decoradores de Inicialização**:
  - `playwright_StartUp`: Inicializa Playwright, realiza login, executa função customizada para cada linha da planilha, com suporte a inscrição automática.
  - `playwright_StartUp_nosub_test`: Versão sem inscrição automática, com execução concorrente em lotes.
- **Funções utilitárias**:
  - `login_block`: Realiza login e captura cookies.
  - `loop_block`: Processa cada linha da planilha, consulta status via API, executa função customizada e atualiza status na planilha.

### `src/Decorators/Inscryption.py`

- **Inscrição Automática**:
  - `Auto_Sub`: Inscreve o usuário autenticado em um curso específico, preenchendo formulário via automação.
- **Remoção Automática**:
  - `Auto_Unsub`: Remove o usuário autenticado de um curso, com tratamento de exceções caso não seja encontrado.

### `src/Decorators/consoleWrapper.py`

- **Logging e Captura de Saída**:
  - `TimeStampedStream`: Adiciona timestamp a cada linha de saída.
  - `capture_console_output_async`: Decorador para capturar e redirecionar saída do console.

### `src/Decorators/pause_control.py`

- **Controle de Pausa**:
  - `PauseWrapper`: Permite pausar e retomar execuções Playwright.
  - `with_pause_control`: Decorador para adicionar controle de pausa a funções assíncronas.

### `src/Decorators/language_pack.py`

- **Internacionalização**:
  - `lang_pack`, `lang_pack_async`: Decoradores para carregar pacotes de idioma e traduzir mensagens.

### `src/Metodos/getPlanilha.py` (presumido)

- **Manipulação de Planilhas**:
  - Métodos para ler status, IDs e escrever resultados em planilhas Excel.

### `src/Metodos/checkup_login.py` (presumido)

- **Validação de Sessão**:
  - Função para checar e renovar login Playwright.

---

## Como Usar

1. **Configuração**
   - Crie um arquivo `.env` com a variável `BASE_URL` apontando para a instância Blackboard desejada.
   - Instale as dependências: `pip install -r requirements.txt`

2. **Execução**
   - Execute um dos scripts principais (ex: `Main_expurgo.py`, `Main_Open_Mescla.py`) conforme a necessidade.
   - Os scripts processam a planilha de entrada, realizam login, e executam as ações configuradas para cada linha.

3. **Personalização**
   - Para adicionar novas ações, crie funções customizadas e utilize os decoradores fornecidos para controle de contexto, logging e internacionalização.

---

## Exemplos de Uso

```python
from Decorators.Main_StartUp import playwright_StartUp

@playwright_StartUp(timeout=120000, headless=True, autoSub=True)
async def processar_curso(page, index):
    # Sua lógica customizada aqui
    ...
```

---

## Requisitos

- Python 3.8+
- Playwright
- requests
- python-dotenv
- openpyxl (para manipulação de Excel)
- Outras dependências listadas em `requirements.txt`

---

## Observações

- O projeto foi desenvolvido para automação de tarefas administrativas em ambientes Blackboard, podendo ser adaptado para outras plataformas com ajustes mínimos.
- O uso de decoradores permite fácil extensão e manutenção do código.
- O controle de concorrência e pausa garante robustez em execuções longas ou sensíveis.

---

## Licença

Projeto de uso interno. Consulte o responsável pelo projeto para informações sobre distribuição e uso externo.