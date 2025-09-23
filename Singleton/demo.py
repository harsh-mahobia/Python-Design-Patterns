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