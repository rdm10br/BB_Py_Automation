from Metodos.API import checkupContent, getApiContent, getFromAPI, getPlanilha, getAPIContentConfig
from Metodos.Copia import copiaMaterial, copiaSala
from Metodos.Login import login, checkup_login, getCredentials
from Metodos.Master import getData, ajusteData, AjusteSermelhor, AjusteSofiaV2, AjusteAvaliacaoV2
from Metodos.Mescla import ajuste_av1_av2, atribGrup, gruposAtividades, AjusteNotaZero, AjusteLinkEbook, openMescla, remove_ser, DoubleCheckDB, falecomtutor
from Metodos.BQ import getBQ, fileChooser, create_bq, junctionWindow
from Metodos.Avulsos import ajuste_AV1, ajuste_AV2, ajuste_Canal, ajuste_manual, ajuste_emp