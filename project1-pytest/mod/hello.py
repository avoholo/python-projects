class Hello:

    def __init__(self, name) -> None:
        self.name = name

    def hello(self):
        print(f"Hello {self.name}.", end="")