# [Factory Design Pattern] Build a logging system using the Factory Design Pattern. Create a LoggerFactory class that 
# generates different types of loggers (e.g., FileLogger, ConsoleLogger, DatabaseLogger). Implement methods in each logger 
# to write logs to their respective destinations. Show how the Factory Design Pattern helps to decouple the logging system 
# from the application and allows for flexible log handling.

from abc import ABC, abstractmethod

class Logger(ABC):
    @abstractmethod
    def log(self, message):
        pass

class FileLogger(Logger):
    def log(self, message):
        with open('log.txt', 'a') as file:
            file.write(message + '\n')

class ConsoleLogger(Logger):
    def log(self, message):
        print(message)

class DatabaseLogger(Logger):
    def log(self, message):
        # logic to write logs to the database
        pass

class LoggerFactory:
    _logger_types = {
        "file": FileLogger,
        "console": ConsoleLogger,
        "database": DatabaseLogger,
    }

    @staticmethod
    def get_logger(logger_type):
        logger_class = LoggerFactory._logger_types.get(logger_type)
        if logger_class:
            return logger_class()
        else:
            raise ValueError("Invalid logger type")
        
def main(logger_type):
    logger = LoggerFactory.get_logger(logger_type)
    if logger:
        message = input("Enter logger message: ")
        logger.log(message)
    else:
        print('Invalid logger type entered.')

if __name__ == "__main__":
    main('console')