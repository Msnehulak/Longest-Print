FILE_NAME = 'ReadmeExample.md'

class CreateReadMe:
    def __init__(self, data: list):
        with open(FILE_NAME, 'r', encoding='utf-8') as f:
            self.readme = f.read()

        self.data = data
        self.stopwatch = self.data

    def main(self):
        for stemp in self.stopwatch:
            old = f"{{{{ {stemp['id']} }}}}"
            new = f"{stemp['duration']:.6f}"
            self.readme = self.readme.replace(old, new)

        with open("README.md", 'w', encoding='utf-8') as f:
            f.write(self.readme)

