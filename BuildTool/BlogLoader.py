def load_index(root):
    pass

def load_folder(root):
    pass

def load_article(folder):
    pass


class BlogLoader:

    def __init__(self, path):
        self.path = path
        self.index = load_index(self.path)
        self.folders = load_folder(self.path)
        self.articles = {}
        for folder in self.folders:
            self.articles.update(load_article(folder))
