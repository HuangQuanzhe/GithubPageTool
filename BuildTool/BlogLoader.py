import os

from ConfigLoader import Config

blacklist = [".git","__articles"]

def load_index(root):
    folders = os.walk(root)
    root_folder = []
    for res in folders:
        for folder in res[1]:
            if folder in blacklist:
                continue
            root_folder.append(folder)
        break
    return root_folder

def load_article(folder):
    res = os.listdir(folder)
    articles = []
    for name in res:
        # print(name)
        item = name.split(".")
        if len(item) < 2:
            continue
        if item[-1] == "md":
            articles.append(name)
    # print(articles)
    return articles

def load_resouce(folder):
    res = os.listdir(folder)
    articles = []
    for name in res:
        # print(name)
        item = name.split(".")
        if len(item) < 2:
            continue
        if item[-1] != "md":
            articles.append(name)
    # print(articles)
    return articles


def load_arch(root):
    arch = {}
    index_list = load_index(root)
    arch["__articles"] = load_article(root)
    arch["__resouces"] = load_resouce(root)
    for index in index_list:
        arch[index] = load_arch(root+"\\"+index)

    return arch


if __name__ == "__main__":
    content = load_arch("C:\hqzforgithub@163.com\HuangQuanzhe.github.io\docs")
    # print(content)
    c = Config.ConfigBuilder().add_config_name("AAA_Config").add_content(content).build()
    print(c)
    c.write_config()