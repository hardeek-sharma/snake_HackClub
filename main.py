class Snake:
    pass


class Apple:
    pass


class Game:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def board_matrix(self):
        board_render = []
        for i in range(self.height):
            row_render = []
            for j in range(self.width):
                row_render.append(None)
            board_render.append(row_render)
        return board_render

    def render(self):
        matrix = self.board_matrix()

        print("Height:", self.height)
        print("Width:", self.width)
        print("-", "-" * self.width * 3, "-", sep="")
        for row in matrix:
            print("|", end="")

            for element in row:
                print(" ", end="")

                if element is None:
                    print(" ", end="")

                print(" ", end="")

            print("|")

        print("-", "-" * self.width * 3, "-", sep="")


g = Game(10, 10)
g.render()
