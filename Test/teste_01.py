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
from pathlib import Path

file_path = "/path/to/your/file.txt"
file_name = Path(file_path).name
print(file_name)