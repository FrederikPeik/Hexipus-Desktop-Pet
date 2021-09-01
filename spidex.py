#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 13:55:33 2021

@author: fred
"""
import pygame
from pygame.locals import *
from pygame.transform import flip,scale,rotate
from random import randint
from math import sqrt, atan2, atan, pi
import playsound

width = 500
height = 500
pygame.init()
screen = pygame.display.set_mode((width, height + 200), 0)

extramount = 0

heads = []
for i in range(1, 6):
    image = pygame.image.load("/home/fred/Python/Spidex/head0" + str(i) + ".png")
    heads.append(pygame.transform.scale(image, (width, height)))
legs = []
for i in range(1, 3):
    image = pygame.image.load("/home/fred/Python/Spidex/legs0" + str(i) + ".png")
    legs.append(pygame.transform.scale(image, (width, height)))
eyes = []
for i in range(1, 4):
    image = pygame.image.load("/home/fred/Python/Spidex/eyes0" + str(i) + ".png")
    eyes.append(pygame.transform.scale(image, (width, height)))
foods = []
for i in range(9):
    image = pygame.image.load("/home/fred/Python/Spidex/fd" + str(i) + ".png")
    foods.append(pygame.transform.scale(image, (int(width / 10), int(height / 10))))
extras = []
for i in range(extramount + 1):
    image = pygame.image.load("/home/fred/Python/Spidex/ex" + str(i) + ".png")
    extras.append(pygame.transform.scale(image, (int(width / 10), int(height / 10))))

image = pygame.image.load("/home/fred/Python/Spidex/chose.png")
chose = pygame.transform.scale(image, (int(width / 10), int(height / 10)))
image = pygame.image.load("/home/fred/Python/Spidex/food.png")
food = pygame.transform.scale(image, (int(width / 10), int(height / 10)))
image = pygame.image.load("/home/fred/Python/Spidex/health.png")
health = pygame.transform.scale(image, (int(width / 10), int(height / 10)))
image = pygame.image.load("/home/fred/Python/Spidex/joy.png")
joy = pygame.transform.scale(image, (int(width / 10), int(height / 10)))
image = pygame.image.load("/home/fred/Python/Spidex/feedicon.png")
feedicon = pygame.transform.scale(image, (int(width / 5), int(height / 5)))
image = pygame.image.load("/home/fred/Python/Spidex/feediconpressed.png")
feediconpressed = pygame.transform.scale(image, (int(width / 5), int(height / 5)))
image = pygame.image.load("/home/fred/Python/Spidex/returnpressed.png")
returniconpressed = pygame.transform.scale(image, (int(width / 10), int(height / 10)))
image = pygame.image.load("/home/fred/Python/Spidex/return.png")
returnicon = pygame.transform.scale(image, (int(width / 10), int(height / 10)))
image = pygame.image.load("/home/fred/Python/Spidex/shop.png")
shopicon = pygame.transform.scale(image, (int(width / 5), int(height / 5)))
image = pygame.image.load("/home/fred/Python/Spidex/shoppressed.png")
shoppressed = pygame.transform.scale(image, (int(width / 5), int(height / 5)))
image = pygame.image.load("/home/fred/Python/Spidex/extras.png")
extrasicon = pygame.transform.scale(image, (int(width / 5), int(height / 5)))
image = pygame.image.load("/home/fred/Python/Spidex/extraspressed.png")
extraspressed = pygame.transform.scale(image, (int(width / 5), int(height / 5)))
image = pygame.image.load("/home/fred/Python/Spidex/store.png")
storeicon = pygame.transform.scale(image, (int(width / 5), int(height / 5)))
image = pygame.image.load("/home/fred/Python/Spidex/storepressed.png")
storepressed = pygame.transform.scale(image, (int(width / 5), int(height / 5)))
image = pygame.image.load("/home/fred/Python/Spidex/shopper.png")
shopper = pygame.transform.scale(image, (int(width / 5), int(height / 5)))
image = pygame.image.load("/home/fred/Python/Spidex/coins.png")
coinimage = pygame.transform.scale(image, (int(width / 10), int(height / 10)))

data = open("/home/fred/Python/Spidex/data.txt", "r")
fooddata = data.readline()
healthdata = data.readline()
joydata = data.readline()

running = True
speed = 1
multiply = 1000
give = 100
inventar = []
for i in range(9 + extramount + 1):
    inventar.append(int(data.readline()))
coins = int(data.readline())
print(coins)
data.close()

print(inventar)

class Item():
    def __init__(self):
        self.x = randint(10, width - 20)
        self.y = 0
        self.speed = randint(1, 10) / 10
        self.tag = randint(0, 8)
        self.width = foods[self.tag].get_width()
        self.height = foods[self.tag].get_height()
        self.alive = True
    def blupdate(self):
        self.y += self.speed
        screen.blit(foods[self.tag], (self.x, self.y))
        if self.y > height + 200:
            self.alive = False
        if self.x > shopperx and self.x + self.width < shopperx + width / 5:
            if self.y + self.height > shoppery:
                inventar[self.tag] += 1
                self.alive = False
                #playsound.playsound("/home/fred/Python/Spidex/buble2.mp3")

class Button():
    def __init__(self, tag, x, y, image, pressed):
        self.x = x
        self.y = y
        self.tag = tag
        self.image = image
        self.pressedimage = pressed
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.pressed = False
        self.cooldown = 50
    def gotpressed(self):
        screen.blit(self.image, (self.x, self.y))
        if self.tag < 10:
            text(str(inventar[self.tag]), (0, 0, 0), self.x, self.y, 20)
        elif self.tag > 13 and self.tag < 15 + extramount:
            text(str(inventar[self.tag - 5]), (0, 0, 0), self.x + self.width / 4, self.y + self.height, 30)
        if self.cooldown > 0:
            self.cooldown -= 1
        else:
            if mouse[0] > self.x and mouse[0] < self.x + self.width:
                if mouse[1] > self.y and mouse[1] < self.y +self.height:
                    screen.blit(self.pressedimage, (self.x, self.y))
                    if click[0]:
                        self.cooldown = 30
                        return True

class Spidex():
    def __init__(self):
        self.alive = True
        self.x = 0
        self.y = 0
        self.eyex = 0
        self.eyey = 0
        self.blink = 10
        self.health = int(healthdata)
        self.joy = int(joydata)
        self.food = int(fooddata)
        self.head = heads[0]
        self.legs = legs[0]
    def blupdate(self):
        screen.blit(self.legs, (self.x, self.y))
        screen.blit(self.head, (self.x, self.y))
        self.food -= speed
        self.blink -= randint(1, 20)
        if give < 100:
            self.food += 10 * multiply
            playsound.playsound("/home/fred/Python/Spidex/buble2.mp3")
        if give > 100:
            if give - 100 == 1:
                self.health += 10 * multiply
            playsound.playsound("/home/fred/Python/Spidex/buble2.mp3")
        if self.blink <= 0:
            self.blink = 55
        if self.food < 20:
            self.joy -= speed
        if self.food < 1:
            self.health -= speed
        if self.health < 1:
            self.alive = False
        
        if self.food > (100 * multiply):
            self.food = (100 * multiply)
        if self.food < 0:
            self.food = 0
        if self.health > (100 * multiply):
            self.health = (100 * multiply)
        if self.joy > (100 * multiply):
            self.joy = (100 * multiply)
        
        if self.blink > 50 * multiply:
            self.head = heads[4]
        elif self.joy < 25 * multiply:
            if self.head == heads[2]:
                playsound.playsound("/home/fred/Python/Spidex/buble0.mp3")
            self.head = heads[3]
        elif self.joy < 50 * multiply:
            if self.head == heads[1]:
                playsound.playsound("/home/fred/Python/Spidex/buble0.mp3")
            self.head = heads[2]
            self.eyex = mouse[0] / (width / 50) - width / 20
            self.eyey = mouse[1] / (height / 25)
            screen.blit(eyes[2], (self.eyex, self.eyey))
        elif self.joy < 75 * multiply:
            if self.head == heads[0]:
                playsound.playsound("/home/fred/Python/Spidex/buble0.mp3")
            self.head = heads[1]
            self.eyex = mouse[0] / (width / 50) - width / 20
            self.eyey = mouse[1] / (height / 50) - height / 20
            screen.blit(eyes[1], (self.eyex, self.eyey))
        elif self.joy >= 75 * multiply:
            self.head = heads[0]
            self.eyex = mouse[0] / (width / 75) - width / 20
            self.eyey = mouse[1] / (height / 60) - height / 10
            screen.blit(eyes[0], (self.eyex, self.eyey))        
        screen.blit(food, (10, 10))
        pygame.draw.rect(screen, (0, 0, 0), (20 + width / 10, 20, width / 6, 30))
        if self.food > 0:
            pygame.draw.rect(screen, (0, 255, 0), (20 + width / 10, 20, width / 6 * self.food / (100 * multiply), 30))
        screen.blit(health, (width / 3 + 10, 10))
        pygame.draw.rect(screen, (0, 0, 0), (30 + width / 10 + width / 3, 20, width / 6, 30))
        if self.health > 0:
            pygame.draw.rect(screen, (0, 255, 0), (30 + width / 10 + width / 3, 20, width / 6 * self.health / (100 * multiply), 30))
        screen.blit(joy, (width + 10 - width / 3, 10))
        pygame.draw.rect(screen, (0, 0, 0), (20 + width / 10 + width + 10 - width / 3, 20, width / 6, 30))
        if self.joy > 0:
            pygame.draw.rect(screen, (0, 255, 0), (20 + width / 10 + width + 10 - width / 3, 20, width / 6 * self.joy / (100 * multiply), 30))

def text(text, color, x, y, size):
    screen.blit(pygame.font.SysFont("", size).render(text, True, (color[0], color[1], color[2])), (x, y))

def control():
    global mouse, click, running, finish
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            finish = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
                finish = True

mainmenu = []
offset = width / 4.5
mainmenu.append(Button(10, width / 4 * 2 - offset, height * 1.1, feedicon, feediconpressed))
mainmenu.append(Button(12, width / 4 * 1 - offset, height * 1.1, shopicon, shoppressed))
mainmenu.append(Button(13, width / 4 * 3 - offset, height * 1.1, extrasicon, extraspressed))
mainmenu.append(Button(14 + extramount, width / 4 * 4 - offset, height * 1.1, storeicon, storepressed))

spidex = [Spidex()]
buttons = mainmenu

running = True
click = ()
shopperx = 0
shoppery = 0
mouse = pygame.mouse.get_pos()

def shop():
    global click, running, mouse, shopperx, shoppery
    buttons = [Button(12, 20, 20, returnicon, returniconpressed)]
    items = []
    itemtimer = 0
    shopperx = width / 2
    shoppery = height + 100
    finished = False
    while not finished:
        control()
        action = 100
        for i in buttons:
            if i.gotpressed():
                action = i.tag
        if action == 12:
            buttons = mainmenu
            finished = True
        for i in items:
            if i.alive:
                i.blupdate()
        if itemtimer > 0:
            itemtimer -= 1
        else:
            itemtimer = 100
            items.append(Item())
        
        shopperx = mouse[0]
        screen.blit(shopper, (shopperx, shoppery))
            
        pygame.display.update()
        pygame.display.flip()
        screen.fill((100, 100, 100))

mouse = ()
click = ()
running = True
mouse = (width / 2, height / 2)

while running:
    control()
    
    for i in spidex:
        i.blupdate()
        give = 100
        if not i.alive:
            running = False
    screen.blit(coinimage, (width - 70, 70))

    text(str(coins), (0, 255, 0), width - 120 - int(coins / 7), 80, 50)

    action = 100
    for i in buttons:
        if i.gotpressed():
            action = i.tag
    if action == 10:
        buttons = []
        for i in range(5):
            buttons.append(Button(i, 10 + i * (width / 5 + 5), height * 1.1, foods[i], chose))
        for i in range(4, 9):
            buttons.append(Button(i, 10 + (i - 5) * (width / 5 + 5), height * 1.25, foods[i], chose))
            
        buttons.append(Button(11, 10 + (9 - 5) * (width / 5 + 5), height * 1.25, returnicon, returniconpressed))
        
    if action == 13:
        buttons = []
        for i in range(extramount + 1):
            buttons.append(Button(i + 14, 10 + i * (width / 5 + 5), height * 1.1, extras[i], chose))
    if action == 14 + extramount:
        buttons = []
        for i in range(extramount + 1):
            buttons.append(Button(i + extramount + 1, 10 + i * (width / 5 + 5), height * 1.1, extras[i], chose))
            
        buttons.append(Button(11, 10 + (9 - 5) * (width / 5 + 5), height * 1.25, returnicon, returniconpressed))
        
    if action == 11:
        buttons = []
        offset = width / 4.5
        buttons.append(Button(10, width / 4 * 2 - offset, height * 1.1, feedicon, feediconpressed))
        buttons.append(Button(12, width / 4 * 1 - offset, height * 1.1, shopicon, shoppressed))
        buttons.append(Button(13, width / 4 * 3 - offset, height * 1.1, extrasicon, extraspressed))
        buttons.append(Button(14 + extramount, width / 4 * 4 - offset, height * 1.1, storeicon, storepressed))
        
        buttons = mainmenu

    if action < 10:
        if inventar[action] > 0:
            give = action
            inventar[action] -= 1
    if action > 13 and action < extramount + 15:
        if inventar[action - 5] > 0:
            give = action + 100 - 13
            inventar[action - 5] -= 1
            
    if action == 12: ###################################################################################################################
        shop()
            
    pygame.display.update()
    pygame.display.flip()
    screen.fill((100, 100, 100))

data = open("/home/fred/Python/Spidex/data.txt", "w")
for i in spidex:
    if i.alive:
        data.write(str(i.food) + "\n")
        data.write(str(i.health) + "\n")
        data.write(str(i.joy) + "\n")
    else:
        data.write("10000\n10000\n10000\n")
print(coins)
for i in inventar:
    data.write(str(i) + "\n")
data.write(str(coins) + "\n")
data.close()
pygame.quit()