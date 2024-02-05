class Bird:
    def fly(self):
        pass


class Sparrow(Bird):
    def fly(self):
        print("Sparrow is flying")


class Penguin(Bird):
    def swim(self):
        print("Penguin is swimming")

# LSP is upheld, as both Sparrow and Penguin are subclasses of Bird,
# and they can be used interchangeably where a Bird is expected.
