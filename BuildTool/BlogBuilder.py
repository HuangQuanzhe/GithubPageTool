import os

blacklist = [".git"]

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
        if item[-1] == "md" and item[0].find("Index") == -1:
            articles.append(item[0])
    print(articles)
    return articles

def init_home_index_welcome():
    return """
## Welcome to HuangQuanzhe's Github Pages!
## 欢迎来到HuangQuanzhe的Github Pages
Hello! I'm HuangQuanzhe, a programmer who wanted to share and learn more.
I'm working as a cloud service development engineer
I'm interested in C/C++, Go, Java, Python, and maybe Ruby.
I also enjoy learning Docker, K8s, DataBase, Distributed file system such as Glusterfs.
This Github Page will record my learning experiences and some of the feelings of life.
    """

def init_home_index_tag(tag):
    return """
## [{}](./{}/{}Index)
    """.format(tag, tag, tag)

def init_home_index_end():
    return """
#### huangquanzhe@126.com hqzforgithub@163.com
    """

def init_tag_index_welcome(tag):
    return """
# {} 
#### [Home](../index)
    """.format(tag)

def init_tag_index_article(name):
    return """
## [{}](./{})
    """.format(name, name)

def init_tag_index_end():
    return """
#### huangquanzhe@126.com hqzforgithub@163.com
    """



class BlogBuilder:

    def __init__(self, path, mode):
        self.root_path = path
        self.mode = mode
        self.index = load_index(self.root_path)
        self.articles = {}
        for tag in self.index:
            self.articles.update({tag: load_article(self.root_path+"/"+tag)})

    def show_last(self):
        path = self.root_path + "/" + "index.md"
        print(path)
        if os.path.isfile(path):
            index_md = open(path,encoding="utf-8")
            data = index_md.read()
            print(data)

    def build_tag(self, tag):
        path = self.root_path + "/" + tag + "/" + tag + "Index.md"
        if self.mode == "rebuild":
            index_file = open(path, "w", encoding="utf-8")
            data = init_tag_index_welcome(tag)
            for arti in self.articles[tag]:
                data = data + init_tag_index_article(arti)
        data = data + init_tag_index_end()
        index_file.write(data)
        index_file.close()
        print(data)

    def build(self):
        path = self.root_path + "/index.md"
        if self.mode == "rebuild":
            index_file = open(path, "w", encoding="utf-8")
            data = init_home_index_welcome()
            for tag in self.index:
                data = data + init_home_index_tag(tag)
                self.build_tag(tag)
            data = data + init_home_index_end()
            index_file.write(data)
            

# print(load_index("./"))
BB = BlogBuilder("E:\project\HuangQuanzhe.github.io\docs", "rebuild")
BB.build()