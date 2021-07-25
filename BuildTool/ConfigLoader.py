import yaml

class Config(object):

    def __init__(self, builder):
        # super(Config, self).__init__(*args))
        self.config_name = builder.config_name
        self.content = builder.content
        pass

    def __str__(self): 
        return self.config_name + "\n" + str(self.content)

    def write_config(self):
        yml_file = {}
        yml_file["config_name"] = self.config_name
        yml_file["content"] = self.content
        with open(self.config_name + ".yml", "w", encoding="utf-8") as f:
            yaml.dump(yml_file, f, encoding="utf-8", allow_unicode=True)
            # yaml.dump(self.content, f, encoding="utf-8", allow_unicode=True)
        return

    class ConfigBuilder(object):
        def __init__(self, *args):
            # super(ConfigBuilder, self).__init__(*args))
            self.config_name = "MyConfig"
            self.content = ""
            return 
            
        def add_config_name(self, name):
            self.config_name = name
            return self

        def add_content(self, content):
            self.content = content
            return self

        def build(self):
            return Config(self)

def ConfigLoader():
    

    return Config.ConfigBuilder().add_config_name("AAA_Config").build()


if __name__ == "__main__":
    c = Config.ConfigBuilder().add_config_name("AAA_Config").build()
    print(c)