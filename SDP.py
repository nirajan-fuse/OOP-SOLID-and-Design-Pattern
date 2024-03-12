# [Singleton Design Pattern] Implement a configuration manager using the Singleton Design Pattern. The configuration manager 
# should read configuration settings from a file and provide access to these settings throughout the application. Demonstrate 
# how the Singleton Design Pattern ensures that there is only one instance of the configuration manager, preventing unnecessary 
# multiple reads of the configuration file.

class SingletonType(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonType,cls).__call__(*args, **kwargs)
        return cls._instances[cls]
    
class ConfigurationManager(metaclass=SingletonType):
    def __init__(self) -> None:
        with open('config.txt', 'r') as file:
            self.__config = file.read()
        print("Configuration Settings")

    def get_config(self):
        return self.__config
    
def main():
    cm1 = ConfigurationManager()
    cm2 = ConfigurationManager()
    print(cm2.get_config())
    print(cm1==cm2)

if __name__ == "__main__":
    main()