# -*- coding:utf-8 -*-
import sys  # 导入sys模块
import pygame  # 导入pygame模块
import random
import levelLoad
from map import Map
from levelLoad import levelLoad
from levelLoad import dataLoad
from pygame.locals import *

# 导入背景图片
background_image_filename = 'background.jpg'
ground0_image_filename='ground0.jpg'
ground1_image_filename='ground1.jpg'
ground2_image_filename='ground2.jpg'
ground3_image_filename='ground3.jpg'


# 初始化pygame，为使用硬件做准备
pygame.init()

# 创建一个窗口,先做一个1000*600的
screen = pygame.display.set_mode((1000, 600), 0, 32)

# 格子范围：先设定为从（150，80）到（900，580）
x_begin=150
x_end=900
y_begin=80
y_end=580

# 设置窗口标题
pygame.display.set_caption("gamename")

# 加载图片并转换
background = pygame.image.load(background_image_filename)
ground0 = pygame.image.load(ground0_image_filename)
ground1 = pygame.image.load(ground1_image_filename)
ground2 = pygame.image.load(ground2_image_filename)
ground3 = pygame.image.load(ground3_image_filename)


#建立一个Map类对象
a_map=Map()

#从文件中导入地图
levelLoad(a_map,1)

# 游戏主循环
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            # 接收到退出时间后退出程序
            exit()
    # 将背景图画上去
    screen.blit(background, (-100, 0))
    
    #先假设格子是15*10的,将各个块进行放缩,先算出每一块的长宽
    blockWidth=(x_end-x_begin)//a_map.rowNumber
    blockHeight=(y_end-y_begin)//a_map.columnNumber
    ground0=pygame.transform.smoothscale(ground0,(blockWidth,blockHeight))
    ground1=pygame.transform.smoothscale(ground1,(blockWidth,blockHeight))
    ground2=pygame.transform.smoothscale(ground2,(blockWidth,blockHeight))
    ground3=pygame.transform.smoothscale(ground3,(blockWidth,blockHeight))

    #下面开始一块一块地画
    for i in range(a_map.columnNumber):
        for j in range(a_map.rowNumber):
            styleNum=3-a_map.maps[i][j].canPlantOn-2*a_map.maps[i][j].canZombieOn
            if styleNum==0:
                screen.blit(ground0,(x_begin+blockWidth*j,y_begin+blockHeight*i))
            if styleNum==1:
                screen.blit(ground1,(x_begin+blockWidth*j,y_begin+blockHeight*i))
            if styleNum==2:
                screen.blit(ground2,(x_begin+blockWidth*j,y_begin+blockHeight*i))
            if styleNum==3:
                screen.blit(ground3,(x_begin+blockWidth*j,y_begin+blockHeight*i))

            
     # 刷新画面
    pygame.display.update()