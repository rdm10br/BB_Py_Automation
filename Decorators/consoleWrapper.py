import sys, io, asyncio, aiofiles, time, logging


class TimeStampedStream:
    """
    Class to make the main print/output stream show the time when it's executed.
    
    usually like this in the main method
    `sys.stdout = TimeStampedStream(sys.stdout)`
    """
    def __init__(self, stream):
        self.stream = stream

    def write(self, data):
        timestamp = time.strftime("[%Y-%m-%d %H:%M:%S] ")
        lines = data.split("\n")
        for line in lines :
            if line.strip():
                self.stream.write(timestamp + line)
            else:
                self.stream.write("\n")
        
    def flush(self):
        self.stream.flush()

# Example usage
# print("This will be printed with time.")
# print("Another message.")

# Redirect sys.stdout to TimeStampedStream
sys.stdout = TimeStampedStream(sys.stdout)


def capture_console_output(func):
    """
    Function to create a log file of the console.

    Args:
        func (func): the main function you want a log

    Returns:
        creates a log file of what's showned on the console.
    """
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

        timer = time.strftime('%d-%m-%Y-%H-%M-%S')
        # Write the captured output to a log file
        log_file_name = rf"Logs\output-{timer}.log"
        with open(log_file_name, 'w') as log_file:
            log_file.write(captured_output)

        return result

    return wrapper


def capture_console_output_async(func):
    """
    Function to create a log file of the console for async methods.

    Args:
        func (func): the main function you want a log

    Returns:
        creates a log file of what's showned on the console.
    """
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

        timer = time.strftime('%d-%m-%Y-%H-%M-%S')
        # Write the captured output to a log file
        log_file_name = rf"Logs\output-{timer}.log"
        async with aiofiles.open(log_file_name, 'w') as log_file:
            await log_file.write(captured_output)

        return result

    return wrapper

# Example usage
# @capture_console_output_async
# async def example_async_function():
#     print("This will be printed on the console and captured in an async function.")
#     print("Another message.")

# # Call the async function
# asyncio.run(example_async_function())