import pygame 

# 球
class Ball(object):
    def __init__(self,canvas,pos, radius):
        #一個pygame物件
        self.pygame = pygame
        #畫布(物件繪製在哪邊)
        self.canvas = canvas
        #設置圓心位置
        self.pos = pos
        #球的半徑
        self.radius = radius
        #球的顏色
        self.color = (100,200,200)
        #是否實心
        self.visible = True
        self.rect = self.pygame.draw.circle(self.canvas, self.color, self.pos, self.radius)
        
    def update(self):
        if(self.visible):
            self.rect = self.pygame.draw.circle(self.canvas, self.color, self.pos, self.radius)

# 發射板
class Paddle(object):
    def __init__(self,canvas, rect):
        self.pygame = pygame
        self.canvas = canvas
        self.rect = rect
        self.color = (0, 0, 0)
        self.visible = True

    def update(self):
        if(self.visible):
            self.pygame.draw.rect(self.canvas, self.color, self.rect)
