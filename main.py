from PIL import Image

class Vector2:
    def __init__(self, x,y):
        self.x, self.y = x,y
    def __repr__(self):
        return f"Vector2({self.x}, {self.y})"

class LimbInfo:
    def __init__(self, *args):
        if len(args)==1:
            a = args[0].split()
            self.name = a[0]
            self.x,self.y = a[1:3]
            self.size = Vector2(*a[-2:])
        else:
            self.name = args[0]
            self.x, self.y = args[1:3]
            self.size = args[-2:-1]
    def __repr__(self):
        return f"LimbInfo({self.name}, ({self.x}, {self.y}), {repr(self.size)})"

class Color:
    def __init__(self, *args):
        self.r, self.g, self.b, self.a = args
    def __repr__(self):
        return f"Color({self.r}, {self.g}, {self.b}, {self.a})"

def _input(a:str, check):
    err=True
    r:any
    while err:
        try:
            r=check(input(a))
            err=False
        except:err=True
    return r
print(
'''
ACCESSORIES AUTO CROP - A People Playground Modding Tool
Automatically crops out accessories for each limbs!

made by Quan
''')

def acs_check(n):
    img=Image.open(n).convert("RGBA")
    if img.width/img.height!=18/79:raise
    return img

def get_pixel(pxls, x:int, y:int) -> Color:
    return Color(pxls[y,x])

def set_pixel(pxls, x:int, y:int, col:Color) -> None:
    pxls[y, x] = (col.r, col.g, col.b, col.a)

def set_pixels(pxls, x:int, y:int, width:int, height:int, col:Color) -> None:
    for i in range(y,y+height):
        for j in range(x,x+width):
            set_pixel(pxls, j, i, col)

def shift_size_down(img:Image.Image, n:int)->Image.Image:
    return img.resize((img.width, img.height+n))

def shift_size_up(img:Image.Image, pxls, n:int) -> Image.Image:
    r = shift_size_down(img, n)

img:Image.Image = _input("Please specify Accessories Path : ", acs_check)
pxls = img.load()
Limbs:list[LimbInfo] = [LimbInfo("Head", (6, 68), Vector2(11, 11)), LimbInfo("UpperBody", (7, 58), Vector2(9, 9)), LimbInfo("MiddleBody", (7, 48), Vector2(9, 9)), LimbInfo("LowerBody", (7, 35), Vector2(9, 12)), LimbInfo("UpperLegFront", (9, 18), Vector2(5, 16)), LimbInfo("LowerLegFront", (9, 3), Vector2(5, 14)), LimbInfo("FootFront", (9, 0), Vector2(9, 3)), LimbInfo("UpperLeg", (9, 18), Vector2(5, 16)), LimbInfo("LowerLeg", (9, 3), Vector2(5, 14)), LimbInfo("Foot", (9, 0), Vector2(9, 3)), LimbInfo("UpperArmFront", (0, 54), Vector2(5, 13)), LimbInfo("LowerArmFront", (0, 37), Vector2(5, 16)), LimbInfo("UpperArm", (0, 54), Vector2(5, 13)), LimbInfo("LowerArm", (0, 37), Vector2(5, 16))]

