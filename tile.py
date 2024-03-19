class Tile:
    def __init__(self, collapsed=False, tiles=[0,1,2,3,4]):
        self.collapsed = collapsed
        self.tiles = tiles

    def __str__(self):
        return f"Collapsed: {self.collapsed}, Tiles: {self.tiles}"
        

