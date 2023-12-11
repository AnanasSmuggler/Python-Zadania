class Colors:
    dark_grey = (26, 31, 40)
    green = (0,128,0)
    red = (255,0,0)
    orange = (255,165,0)
    yellow = (255,255,0)
    purple = (128,0,128)
    cyan = (0, 255, 255)
    blue = (0,0,255)
    white = (255,255,255)
    background_color = (0, 56, 71)
    foreground_color = (0, 71, 64)

    @classmethod
    def get_cell_colors(cls):
        return [cls.dark_grey, cls.green, cls.red, cls.orange, cls.yellow, cls.purple, cls.cyan, cls.blue]