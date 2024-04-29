import sys, io

def capture_console_output(func):
    class ConsoleAndFile(io.StringIO):
        def write(self, data):
            sys.__stdout__.write(data)  # Write to the original stdout
            super().write(data)  # Write to the StringIO buffer

    def wrapper(*args, **kwargs):
        console_output = ConsoleAndFile()
        sys.stdout = console_output

        # Call the original function
        result = func(*args, **kwargs)

        # Restore the original stdout
        sys.stdout = sys.__stdout__

        # Get the captured output as a string
        captured_output = console_output.getvalue()

        # Write the captured output to a log file
        log_file_name = "output.log"
        with open(log_file_name, 'w') as log_file:
            log_file.write(captured_output)

        return result

    return wrapper