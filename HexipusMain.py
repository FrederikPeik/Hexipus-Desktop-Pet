#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 22:18:11 2021

@author: fred
"""

import pygame
from pygame.locals import *
from random import randint
from time import sleep
from numpy import sin, cos, pi

pygame.init()
bigfont = pygame.font.SysFont("", 100)
font = pygame.font.SysFont("", 50)
def textobjekt(text, color, pos, chosenfont = font):
    textflache = chosenfont.render(text, True, color)
    screen.blit(textflache, pos)

width = 1200
height = 1200
zoom = 0.5

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

particles = []
def particlecloud(position, color, shape, speed = 10 * zoom, size = 20 * zoom, number = 100, time = 20 * zoom):
    for i in range(number):
        particles.append(Particle(position, color, shape, speed, randint(0, size), randint(0, time)))
        
class Particle():
    def __init__(self, position, color, shape, speed, size, time):
        self.alive = True
        self.x = position[0]
        self.y = position[1]
        rand = randint(0, 360) * pi / 180
        randspeed = randint(50, 150) / 100 * speed
        self.dx = cos(rand) * randspeed
        self.dy = sin(rand) * randspeed
        self.color = color
        self.shape = shape
        self.size = size
        self.time = time
    def blupdate(self):
        if self.alive:
            self.x += self.dx
            self.y += self.dy
            self.time -= 1
            if self.time < 1:
                self.alive = False
            if self.shape == "rect":
                pygame.draw.rect(screen, self.color, (self.x - self.size / 2, self.y - self.size / 2, self.size, self.size))
            else:
                print("sry shape not supported")

class Regler():
    def __init__(self,x,y,lange,text,wert, maxw):
        self.x = x
        self.y = y
        self.lange = lange
        self.rx = x + lange / 2
        self.aktiv = False
        self.text = text
        self.wert = wert
        self.maxwert = maxw * 1.1111111111111111111
    def draw(self):
        pygame.draw.rect(screen,(100,100,100),(self.x,self.y,self.lange,round(self.lange / 10)))
        pygame.draw.rect(screen,(200,200,200),(self.rx,self.y - self.lange / 7 / 8,self.lange / 10,self.lange / 7))
        textgrund,textkasten = textobjekt(self.text + "   " + str(round(self.wert)),font)
        textkasten.center = ((self.x + (self.lange / 2)),self.y - self.lange / 10)
        screen.blit(textgrund, textkasten)
    def get_regler(self):
        self.rx = self.wert * (self.lange / self.maxwert) + self.x
    def get_wert(self):
        self.wert = (self.rx - self.x) * (self.maxwert / self.lange)

class Button():
    def __init__(self, tag, x, y, image, pressed, buttonid = 0):
        self.x = x
        self.y = y
        self.tag = tag
        self.id = buttonid
        self.image = image
        self.pressedimage = pressed
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.pressed = False
        self.cooldown = 5
    def gotpressed(self):
        screen.blit(self.image, (self.x, self.y))
        if self.cooldown > 0:
            self.cooldown -= 1
        else:
            if mouse[0] > self.x and mouse[0] < self.x + self.width:
                if mouse[1] > self.y and mouse[1] < self.y +self.height:
                    screen.blit(self.pressedimage, (self.x, self.y))
                    if click[0]:
                        self.cooldown = 5
                        return True

image = pygame.image.load("chose.png")
chose = pygame.transform.scale(image, (int(width / 10 * zoom), int(height / 10 * zoom)))
image = pygame.image.load("food.png")
food = pygame.transform.scale(image, (int(width / 10 * zoom), int(height / 10 * zoom)))
image = pygame.image.load("health.png")
health = pygame.transform.scale(image, (int(width / 10 * zoom), int(height / 10 * zoom)))
image = pygame.image.load("joy.png")
joy = pygame.transform.scale(image, (int(width / 10 * zoom), int(height / 10 * zoom)))
image = pygame.image.load("feedicon.png")
feedicon = pygame.transform.scale(image, (int(width / 5 * zoom), int(height / 5 * zoom)))
image = pygame.image.load("feediconpressed.png")
feediconpressed = pygame.transform.scale(image, (int(width / 5 * zoom), int(height / 5 * zoom)))
image = pygame.image.load("returnpressed.png")
returniconpressed = pygame.transform.scale(image, (int(width / 10 * zoom), int(height / 10 * zoom)))
image = pygame.image.load("return.png")
returnicon = pygame.transform.scale(image, (int(width / 10 * zoom), int(height / 10 * zoom)))
image = pygame.image.load("shop.png")
shopicon = pygame.transform.scale(image, (int(width / 5 * zoom), int(height / 5 * zoom)))
image = pygame.image.load("shoppressed.png")
shoppressed = pygame.transform.scale(image, (int(width / 5 * zoom), int(height / 5 * zoom)))
image = pygame.image.load("extras.png")
extrasicon = pygame.transform.scale(image, (int(width / 5 * zoom), int(height / 5 * zoom)))
image = pygame.image.load("extraspressed.png")
extraspressed = pygame.transform.scale(image, (int(width / 5 * zoom), int(height / 5 * zoom)))
image = pygame.image.load("store.png")
storeicon = pygame.transform.scale(image, (int(width / 5 * zoom), int(height / 5 * zoom)))
image = pygame.image.load("storepressed.png")
storepressed = pygame.transform.scale(image, (int(width / 5 * zoom), int(height / 5 * zoom)))
image = pygame.image.load("shopper.png")
shopper = pygame.transform.scale(image, (int(width / 5 * zoom), int(height / 5 * zoom)))
image = pygame.image.load("coins.png")
coinimage = pygame.transform.scale(image, (int(width / 10 * zoom), int(height / 10 * zoom)))

sprite = []
numbers = [1, 0, 6, 1, 4]
for i in range(0, 5):
    sprite.append([])
    for o in range(0, numbers[i] + 1):
        filename = str(i) + str(o) + ".png"
        image = pygame.image.load(filename)
        scale = 700
        sprite[i].append(pygame.transform.scale(image, (int(scale * zoom), int(scale * zoom))))

extramount = 0

foods = []
for i in range(9):
    image = pygame.image.load("fd" + str(i) + ".png")
    foods.append(pygame.transform.scale(image, (int(width / 10 * zoom), int(height / 10 * zoom))))
extras = []
for i in range(extramount + 1):
    image = pygame.image.load("ex" + str(i) + ".png")
    extras.append(pygame.transform.scale(image, (int(width / 10 * zoom), int(height / 10 * zoom))))

data = open("data.txt", "r")
fooddata = data.readline()
healthdata = data.readline()
joydata = data.readline()

speed = 1
multiply = 1000
give = 100
inventar = []
give = 100
for i in range(9 + extramount + 1):
    inventar.append(int(data.readline()))
coins = int(data.readline())
data.close()

class Hexipus():
    def __init__(self):
        self.alive = True
        self.dx = sprite[0][0].get_width()
        self.dy = sprite[0][0].get_height()
        self.x = width * zoom / 2 - self.dx / 2
        self.y = (height / 2 - 100) * zoom - self.dy / 2
        self.head = (self.x + 5 * scale * zoom, self.y + scale * zoom, 22 * scale * zoom, 22 * scale * zoom)
        self.sprite = [0, 0, 0, 0, 0]
        self.eyetime = 100
        self.blinktime = 100
        self.legtime = 100
        self.ohtime = 0
        self.shivtime = 0
        self.shivdir = 0
        self.health = int(healthdata)
        self.joy = int(joydata)
        self.food = int(fooddata)
        self.state = 0
    def blupdate(self):
        if self.alive:
            
            self.head = (self.x + 4 * scale * zoom / 30, self.y + scale * zoom / 30, 22 * scale * zoom / 30, 22 * scale * zoom / 30)
            
            self.eyetime -= randint(-5, 10)
            self.blinktime -= speed
            self.legtime -= randint(-1, 5)
            self.joy -= speed
            
            if self.food < 1:
                self.health -= speed * 5
                self.joy -= speed * 10
            else:
                self.food -= speed
            if self.health < 1:
                self.alive = False
            
            if self.eyetime < 1:
                self.sprite[2] = randint(0, 4)
                self.eyetime = 100
            
            if self.legtime < 1:
                self.sprite[0] = not self.sprite[0]
                self.legtime = 200
                if self.sprite[0]:
                    self.legtime = 50
            
            if self.blinktime < 1:
                self.sprite[3] = not self.sprite[3]
                self.blinktime = randint(100, 200)
                if self.sprite[3]:
                    self.blinktime = 5
                    
            if self.ohtime:
                self.ohtime -= 1
            if self.ohtime < 1:
                self.ohtime = 0
                self.sprite[4] = self.state
            
            if self.joy > 100 * multiply:
                self.joy = 100 * multiply
            if self.health > 100 * multiply:
                self.health = 100 * multiply
            if self.food > 100 * multiply:
                self.food = 100 * multiply
            
            mood = self.joy / multiply
            if mood > 75:
                self.state = 3
            elif mood > 50:
                self.state = 2
            elif mood > 25:
                self.state = 0
            else:
                self.state = 1
            
        else:
            self.sprite[2] = 5
            self.sprite[4] = 0
        
        ind = 0
        for i in self.sprite:
            screen.blit(sprite[ind][i], (self.x, self.y))
            ind += 1
        screen.blit(food, (10 * zoom, 10 * zoom))
        pygame.draw.rect(screen, (0, 0, 0), ((20 + width / 10) * zoom, 20 * zoom, width / 6 * zoom, 30 * zoom))
        if self.food > 0:
            pygame.draw.rect(screen, (0, 255, 0), ((20 + width / 10) * zoom, 20 * zoom, width / 6 * self.food / (100 * multiply) * zoom, 30 * zoom))
        screen.blit(health, ((width / 3 + 10) * zoom, 10 * zoom))
        pygame.draw.rect(screen, (0, 0, 0), ((30 + width / 10 + width / 3) * zoom, 20 * zoom, width / 6 * zoom, 30 * zoom))
        if self.health > 0:
            pygame.draw.rect(screen, (0, 255, 0), ((30 + width / 10 + width / 3) * zoom, 20 * zoom, width / 6 * self.health / (100 * multiply) * zoom, 30 * zoom))
        screen.blit(joy, ((width + 10 - width / 3) * zoom, 10 * zoom))
        pygame.draw.rect(screen, (0, 0, 0), ((20 + width / 10 + width + 10 - width / 3) * zoom, 20 * zoom, width / 6 * zoom, 30 * zoom))
        if self.joy > 0:
            pygame.draw.rect(screen, (0, 255, 0), ((20 + width / 10 + width + 10 - width / 3) * zoom, 20 * zoom, width / 6 * self.joy / (100 * multiply) * zoom, 30 * zoom))
    
    def pet(self):
        particlecloud(mouse, (0, 255, 0), "rect")
        self.joy += randint(1, 100) * speed
        if randint(0, 2):
            self.eyetime = 100
            self.sprite[2] = 6
        else:
            self.sprite[3] = not self.sprite[0]
            self.blinktime = 20
            
    def look(self):
        self.eyetime = 100
        xdif = mouse[0] - (self.x + self.dx / 2)
        ydif = mouse[1] - (self.y + self.dy / 2)
        if abs(xdif) > abs(ydif):
            if xdif > 0:
                self.sprite[2] = 1
            else:
                self.sprite[2] = 3
        else:
            if ydif > 0:
                self.sprite[2] = 4
            else:
                self.sprite[2] = 2
        particlecloud(mouse, (0, 0, 255), "rect")
    
    def feed(self, give):
        if self.food < 100 * multiply:
            self.food += hunger[give] * 5
            if hunger[give] > 50:
                self.eyetime = 100
                self.sprite[2] = 6
        hunger[give] = 0
        self.ohtime = randint(10, 50)
        self.sprite[4] = 4
        particlecloud((self.x + self.dx / 2, self.y + self.dy * 0.55), (randint(0, 255), randint(0, 255), randint(0, 255)), "rect")

def menu(menutype):
    output = []
    if menutype == "main":
        offset = width / 30 * zoom
        xpos = (width / 4 + offset) * zoom
        ypos = (height - height / 5) * zoom
        output = [Button("feed", xpos * 0, ypos, feedicon, feediconpressed),
                  Button("shop", xpos * 1, ypos, shopicon, shoppressed),
                  Button("extras", xpos * 2, ypos, extrasicon, extraspressed),
                  Button("store", xpos * 3, ypos, storeicon, storepressed)]
    if menutype == "feed":
        offset = width / 30 * zoom
        xpos = (width / 5 + offset) * zoom
        ypos = (height - height / 5) * zoom
        for i in range(0, 5):
            output.append(Button("food", 10 + i * xpos, ypos, foods[i], chose, i))
        offset = width / 30 * zoom
        xpos = (width / 5 + offset) * zoom
        ypos = (height - height / 10) * zoom
        for i in range(4, 9):
            output.append(Button("food", 10 + (i - 5) * xpos, ypos, foods[i], chose, i))
        output.append(Button("main", (width - width / 7) * zoom, height / 10 * zoom, returnicon, returniconpressed))
    return(output)

screen = pygame.display.set_mode((int(width * zoom), int(height * zoom)))

running = True
click = (0, 0)
shopperx = 0
shoppery = 0
mouse = pygame.mouse.get_pos()
hunger = []
for i in range(0, extramount + 10):
    hunger.append(10)

buttons = menu("main")

hexy = Hexipus()

running = True
while running:
    
    oldclick = click
    control()
    
    action = ""
    for i in buttons:
        if i.gotpressed():
            if i.tag == "feed":
                buttons = menu("feed")
            elif i.tag == "food":
                hexy.feed(i.id)
            else:
                buttons = menu("main")
    
    if oldclick[0] and not click[0] and mouse[0] > hexy.head[0] and mouse[0] < hexy.head[0] + hexy.head[2]:
        if mouse[1] > hexy.head[1] and mouse[1] < hexy.head[1] + hexy.head[3]:
            hexy.pet()
        elif hexy.eyetime < 90:
            hexy.look()
    elif oldclick[0] and not click[0] and hexy.eyetime < 90:
        hexy.look()
            
    hexy.blupdate()
    
    for i in range(0, len(hunger) - 1):
        hunger[i] += speed / 10
    
    for i in particles:
        i.blupdate()
    
    pygame.display.update()
    pygame.display.flip()
    screen.fill((100, 100, 100))
    
    sleep(1 / zoom / 100)
    
    if not hexy.alive:
        hexy.blupdate()
        pygame.display.update()
        pygame.display.flip()
        while running:
            control()
    if not running:
        break

data = open("data.txt", "w")

if hexy.alive:
    data.write(str(int(hexy.food)) + "\n")
    data.write(str(int(hexy.health)) + "\n")
    data.write(str(int(hexy.joy)) + "\n")
else:
    data.write(str(100 * multiply) + "\n" + str(100 * multiply) + "\n" + str(100 * multiply) + "\n")

for i in inventar:
    data.write(str(i) + "\n")
data.write(str(coins) + "\n")
data.close()
pygame.quit()
