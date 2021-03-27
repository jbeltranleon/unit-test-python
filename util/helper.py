def process(value):
    return value + ' <- Processed'


class Utility:
    @staticmethod
    def process(value):
        return value + ' <- Processed'

    @staticmethod
    def open_file(file):
        with open(file, 'a') as f:
            print(f.read())
