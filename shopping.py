#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 20:25:22 2021

@author: fred
"""
def shop(items):
    buttons = [Button(12, 20, 20, returnicon, returniconpressed)]
    items = []
    itemtimer = 0
    shopperx = width / 2
    shoppery = height + 100
    finished = False
    while not finished:
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                finished = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    finished = True
        action = 100
        for i in buttons:
            if i.gotpressed():
                action = i.tag
        if action == 12:
            buttons = [Button(10, width / 2 - width / 10, height * 1.1, feedicon, feediconpressed)]
            buttons.append(Button(12, 20, height * 1.1, shop, shoppressed))
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