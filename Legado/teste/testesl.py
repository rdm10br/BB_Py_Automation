# if str("['Saúde III']").upper() == "['SAÚDE III']":
#     print('true')
# elif "cu" == "cru" :
#     print("teste")
# else:
#     print('false')

#STRING FORMATTING
# print('{:5} | {:5} | {:5}'.format('teste0','teste1','teste2'))

# import logging
# import sys

# # Define the log file name
# log_file_name = "output.log"

# # Configure logging to write to the log file
# logging.basicConfig(filename=log_file_name, level=logging.INFO)

# # Create a handler to write log messages to stdout as well
# stdout_handler = logging.StreamHandler(sys.stdout)
# stdout_handler.setLevel(logging.INFO)
# stdout_handler2 = logging.StreamHandler(sys.stdout)
# stdout_handler2.setLevel(print)
# logging.getLogger().addHandler(stdout_handler)
# logging.getLogger().addHandler(stdout_handler2)

# # Example usage
# logging.info("This will be logged and printed to console.")
# logging.info("Another message.")

# # Optionally, remove the stdout handler to stop console logging
# logging.getLogger().removeHandler(stdout_handler)
# logging.getLogger().removeHandler(stdout_handler2)

# import sys
# import io

# class ConsoleAndFile(io.StringIO):
#     def write(self, data):
#         sys.__stdout__.write(data)  # Write to the original stdout
#         super().write(data)  # Write to the StringIO buffer

# # Create a buffer to capture console output
# console_output = ConsoleAndFile()
# sys.stdout = console_output

# # Example usage
# print("This will be printed on the console and captured.")
# print("Another message.")

# # Restore the original stdout
# sys.stdout = sys.__stdout__

# # Get the captured output as a string
# captured_output = console_output.getvalue()

# # Write the captured output to a log file
# log_file_name = "output.log"
# with open(log_file_name, 'w') as log_file:
#     log_file.write(captured_output)

import sys, io, asyncio, aiofiles

def capture_console_output_async(func):
    class ConsoleAndFile(io.StringIO):
        def write(self, data):
            sys.__stdout__.write(data)  # Write to the original stdout
            super().write(data)  # Write to the StringIO buffer

    async def wrapper(*args, **kwargs):
        console_output = ConsoleAndFile()
        sys.stdout = console_output

        # Call the original async function
        result = await func(*args, **kwargs)

        # Restore the original stdout
        sys.stdout = sys.__stdout__

        # Get the captured output as a string
        captured_output = console_output.getvalue()

        # Write the captured output to a log file
        log_file_name = "output.log"
        async with aiofiles.open(log_file_name, 'w') as log_file:
            await log_file.write(captured_output)

        return result

    return wrapper

# Example usage
@capture_console_output_async
async def example_async_function():
    print("This will be printed on the console and captured in an async function.")
    print("Another message.")

# Call the async function
asyncio.run(example_async_function())