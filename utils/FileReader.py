class FileReader:

    def __init__(self):
        pass

    def read(self, path):
        with open(path, "r") as file:
            file = file.read()
        return file