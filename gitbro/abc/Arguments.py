import re as regex
import sys as system

class Arguments:
    options: list = []
    values: list = []

    def __init__(self) -> None:
        if (len(system.argv) <= 1):
            return

        self.define_options(enumerate(system.argv))

    def define_options(self, commandArguments: enumerate):
        count = 0
        for i, commandArgument in commandArguments:
            if (count == 0):
                count += 1
                continue

            if (self.is_option(commandArgument)):
                self.options.append(commandArgument)
            else:
                self.values.append(commandArgument)

    def is_option(self, commandArgument: str):
        return regex.search('-\w+', commandArgument)

    def get_options(self, index: int = None):
        if (index is not None):
            return self.options[index] if 0 <= index < len(self.options) else None

        return self.options

    def get_values(self, index: int = None):
        if (index is not None):
            return self.values[index] if 0 <= index < len(self.values) else None

        return self.values

if __name__ == "__main__":
    a = Arguments()
    print(a.get_options())
