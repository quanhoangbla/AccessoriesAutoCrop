import pickle, cv2

class Vector2:
    def __init__(self, x:int, y:int):
        self.x, self.y = x, y
    def __init__(self, data:str):
        self.x, self.y = map(int,data.split())

class LimbInfo:
    def __init__(self, name:str, pos:tuple, size:Vector2):
        self.x, self.y = pos
        self.size = size
        self.name = name
    def __init__(self, data:str):
        a = data.split()
        self.name = a[0]
        self.x,self.y = a[1:3]
        self.size = a[-1]

print(
'''
ACCESSORIES AUTO CROP - A People Playground Modding Tool
Automatically crops out accessories for each limbs!

made by Quan
''')
