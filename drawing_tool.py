class CanvasDrawer:
    def __init__(self, width: str, height: str):
        self.width = int(width)
        self.height = int(height)
        self.w_fill = "-"
        self.h_fill = "|"
        self.line_fill = "x"
        self.canvas = []

    def create_canvas(self, *args):
        canvas = [
            [[' '] for _ in range(self.width+2)
             ] for _ in range(self.height+2)
        ]
        for i in range(self.width+2):
            canvas[0][i][0] = self.w_fill
            canvas[self.height+1][i][0] = self.w_fill
        for i in range(1, self.height+1):
            canvas[i][0][0] = self.h_fill
            canvas[i][self.width+1][0] = self.h_fill
        self.canvas = canvas

    def create_line(self, x1: str, y1: str, x2: str, y2: str):
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
        if x1 == x2:
            for y in range(y1, y2 + 1):
                self.canvas[y][x1][0] = self.line_fill
        elif y1 == y2:
            for x in range(x1, x2+1):
                self.canvas[y1][x][0] = self.line_fill
        else:
            # write your own error
            raise AttributeError

    def draw_rectangle(self, x1: str, y1: str, x2: str, y2: str):
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
        for i in range(x1, x2+1):
            self.canvas[y1][i][0] = self.line_fill
            self.canvas[y2][i][0] = self.line_fill
        for i in range(y1, y2+1):
            self.canvas[i][x1][0] = self.line_fill
            self.canvas[i][x2][0] = self.line_fill

    def bucket_fill(self, x, y, color):
        x, y = int(x), int(y)
        if self.canvas[y][x][0] != " ":
            # write your own error
            raise AttributeError
        for h in range(y, 0, -1):
            for i in range(x, 0, -1):
                if self.canvas[h][i][0] == " ":
                    self.canvas[h][i][0] = color
                else:
                    break
            for i in range(x+1, self.width+2):
                if self.canvas[h][i][0] == " ":
                    self.canvas[h][i][0] = color
                else:
                    break
        # do DRY on this
        for h in range(y+1, self.height+2):
            for i in range(x, 0, -1):
                if self.canvas[h][i][0] == " ":
                    self.canvas[h][i][0] = color
                else:
                    break
            for i in range(x+1, self.width+2):
                if self.canvas[h][i][0] == " ":
                    self.canvas[h][i][0] = color
                else:
                    break

    def write_in_output(self, path: str):
        with open(path, "a") as o:
            for row in self.canvas:
                for i in row:
                    o.write(i[0])
                o.write("\n")

    FUNCTION_MAPPING = {
        "C": create_canvas,
        "L": create_line,
        "R": draw_rectangle,
        "B": bucket_fill
    }


def drawing_tool(path_to_input: str, path_to_output: str):
    with open(path_to_input, "r") as f:
        canvas = None
        for line in f:
            function_key, args = line.split(" ", 1)
            args = args.strip().split()
            if function_key == "C":
                canvas = CanvasDrawer(*args)
            if canvas:
                canvas.FUNCTION_MAPPING[function_key](canvas, *args)
                canvas.write_in_output(path_to_output)
            else:
                with open(path_to_output, "w") as o:
                    o.write("Need to create canvas before executing any operations with it")


if __name__ == "__main__":
    path_to_input = input("Please enter path to input file")
    path_to_output = input("Please enter path to output file")
    drawing_tool(path_to_input, path_to_output)

