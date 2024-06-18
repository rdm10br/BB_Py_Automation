# import io, sys
# from contextlib import redirect_stdout
# from unidecode import unidecode


# # def capture_print_statements(func):
# #     def wrapper(*args, **kwargs):
# #         buffer = io.StringIO()
# #         with redirect_stdout(buffer):
# #             func(*args, **kwargs)
# #         return buffer.getvalue()
# #     return wrapper


# # @capture_print_statements
# # def my_function(*args):
# #     unidecode(*args)
# #     print(*args)


# # output = my_function('áç')
# # print(output)
# print('óçé')
import os
import regex as re
from unidecode import unidecode
path = r'C:\Users\013190873\Downloads\1 Transformação Digital , Sistemas Computacionais e o Futuro da Tecnologia .docx'
file_name = os.path.basename(path)
BQ_name = re.sub(r'.docx','',file_name).upper()
unidade = ''.join([ch for ch in BQ_name if ch.isdigit()])
match unidade[0]:
        case '1' :
            item = 'BQ 01'
        case '2' :
            item = 'BQ 02'
        case '3' :
            item = 'BQ 03'
        case '4' :
            item = 'BQ 04'
BQ_name = unidecode(BQ_name)
BQ_name = re.sub(r'\d','',BQ_name)
BQ_name = re.sub(r'\s+', ' ', BQ_name)
BQ_name = f'{BQ_name} - {item}_GRADUACAO'
print(BQ_name)