class ConfigurationManager:
    _instance = None
    def __new__(cls):
        if not cls._instance:
            cls._instance = super(ConfigurationManager, cls).__new__(cls)
            cls._instance._config_values = {}
        return cls._instance
    def set(self, key, value):
        self._config_values[key] = value
    def get(self, key):
        return self._config_values.get(key)
# Usage
config1 = ConfigurationManager()
config1.set("api_key", "123456")
config2 = ConfigurationManager()
print(config2.get("api_key"))


"""
Q. Why do we use super().__new__(cls)?

The super() here is used to call the parent class’s __new__ method.
In almost all cases, the parent is object (the root base class in Python).
So super().__new__(cls) literally asks Python’s built-in machinery:
👉 “Hey, please allocate memory for an object of type cls.”
"""

"""
this __new__ is used in : 
Singlton, Factory, Immutable Types
"""