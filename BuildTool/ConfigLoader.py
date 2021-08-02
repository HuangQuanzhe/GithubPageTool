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

def ConfigLoader(file_name):
    with open(file_name, encoding="utf-8") as f:
        data = yaml.load(f)
        print(data)
        return Config.ConfigBuilder() \
            .add_config_name(data["config_name"]) \
            .add_content(data["content"]) \
            .build()


if __name__ == "__main__":
    # c = Config.ConfigBuilder().add_config_name("AAA_Config").build()
    # print(c)
    ConfigLoader("AAA_Config.yml")