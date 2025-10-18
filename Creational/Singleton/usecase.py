class SingletonMeta(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if not cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]



class DatabaseConnection(metaclass=SingletonMeta):
    def __init__(self, connection_string):
        self.connection_string = connection_string
        self.connection = self._create_connection()

    def _create_connection(self):
        # Here, you'd typically establish a connection to the database.
        # For the sake of this example, we'll just simulate it.
        return f"Connected to {self.connection_string}"
        
    def query(self, sql_query):
        # Simulating a query execution
        return f"Executing '{sql_query}' on {self.connection_string}"