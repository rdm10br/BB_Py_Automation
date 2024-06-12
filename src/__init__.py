from Metodos.API import checkupContent, getApiContent, getFromAPI, getPlanilha
from Metodos.Copia import copiaMaterial, copiaSala
from Metodos.Login import login, checkup_login, getCredentials
from Metodos.Master import getData, ajusteData, AjusteSermelhor, AjusteSofiaV2
from Metodos.Mescla import atribGrup, gruposAtividades, AjusteNotaZero
# from Metodos.BQ import getBQ, fileChooser, bqOnBB
from Decorators.Main_StartUp import playwright_StartUp
from Decorators.consoleWrapper import capture_console_output, capture_console_output_async, TimeStampedStream
from src.Metodos.Master import AjusteAvaliacaoV2