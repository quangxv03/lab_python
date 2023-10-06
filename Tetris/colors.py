class Colors:
    dark_grey = (26, 31, 40)
    cyan = (21, 204, 209)
    red = (232, 18, 18)
    purple = (166, 0 ,247)
    yellow = (237, 234 ,4)
    green = (47, 230, 23)
    orange = (226, 116, 17)
    blue = (13, 64, 216)
    white = (255, 255, 255)
    brunswick_geen = (34, 81, 64)   
    teal = (53, 162, 159)
    
    @classmethod
    def get_cell_colors(cls):
        return [cls.dark_grey, cls.cyan, cls.red, cls.purple, cls.yellow, cls.green, cls.orange, cls.blue]
        