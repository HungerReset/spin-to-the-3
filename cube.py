import pygame
from math import cos, sin, pi
from time import sleep

vrry = [[150,150,150],[150,150,-150],[150,-150,150],[150,-150,-150],[-150,150,150],[-150,150,-150],[-150,-150,150],[-150,-150,-150]]
erry = [[0,1],[0,2],[0,4],[1,3],[1,5],[2,3],[2,6],[4,5],[4,6],[5,7],[6,7],[7,3]]

scr = [500,500]

coords = [0,0,-250]

f = 300

def toScreen(p:list[2]) -> tuple:
    o = list()
    o.append(int(p[0] + scr[0] / 2))
    o.append(int(scr[1] - (p[1] + scr[1] / 2)))
    return o

def rotate(p:list[3], a:float, x:int) -> list[3]:
    o = [0,0,0]
    o[   0 + x   ] = p[   0 + x   ]
    o[(1 + x) % 3] = p[(1 + x) % 3] * cos(a) - p[(2 + x) % 3] * sin(a)
    o[(2 + x) % 3] = p[(2 + x) % 3] * cos(a) + p[(1 + x) % 3] * sin(a)
    return o

def proj(p:list[3]) -> tuple:
    o = []
    o.append((f * (p[0] - coords[0])) / (abs(p[2] - coords[2]) + f))
    o.append((f * (p[1] - coords[1])) / (abs(p[2] - coords[2]) + f))
    return o

screen = pygame.display.set_mode(scr)
pygame.display.set_caption('[·]')

pygame.init()

A = [pi/180,pi/120,pi/200]

w = 1

while 1:

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            k = event.key
            if k == pygame.K_ESCAPE:
                pygame.quit()
            if k == pygame.K_f:
                if   screen.get_flags() == 16777216: screen = pygame.display.set_mode(scr, pygame.NOFRAME)
                elif screen.get_flags() == 16777248: screen = pygame.display.set_mode(scr,               )
            if k == pygame.K_w:
                if w == 1: w = 10
                else: w = 1

    for v in range(len(vrry)):
        vrry[v] = rotate(vrry[v], A[0], 0)
        vrry[v] = rotate(vrry[v], A[1], 1)
        vrry[v] = rotate(vrry[v], A[2], 2)

    lrry = []

    for e in erry:
        lrry.append((toScreen(proj(vrry[e[0]])), toScreen(proj(vrry[e[1]]))))

    prry = []

    for p in vrry:
        prry.append(toScreen(proj(p)))

    screen.fill((0,0,0))

    for l in lrry:
        pygame.draw.line(screen, (255,255,255), l[0], l[1], w)

    for p in prry:
        pygame.draw.circle(screen, (255,255,255), p, int(w/2 - 1), int(w/2 - 1))

    pygame.display.update()
    
    sleep(1/60)