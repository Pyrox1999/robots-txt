import os
os.environ['SDL_VIDEO_WINDOW_POS'] = '100,100'
import random
import pgzrun
import pygame
import urllib.request

random.seed()

pygame.mixer.music.load("song.mp3") #Bobjt
pygame.mixer.music.play(-1)

level = -2
target = "http://localhost"
message=""

def check_robots(url):
    global message
    if not url.endswith("/"):
        url += "/"
    robots_url = url + "robots.txt"
    try:
        response = urllib.request.urlopen(robots_url)
        content = response.read().decode("utf-8")
        message=f"robots.txt for {url}:\n"+content
    except Exception as e:
        message=f"No robots.txt found at {robots_url} ({e})"

def draw():
    global level, target, message
    screen.clear()
    if level==-2:
        screen.blit("disclaimer",(0,0))
    if level == -1:
        screen.blit("title", (0, 0))
    elif level == 0:
        screen.blit("intro", (0, 0))
    elif level == 1:
        screen.blit("back", (0, 0))
        screen.draw.text("Website where to download robots.txt:", center=(400, 130), fontsize=24, color=(25, 200, 255))
        screen.draw.text(target, center=(400, 180), fontsize=24, color=(255, 255, 0))
    elif level == 2:
        check_robots(target)
        screen.draw.text(message, center=(400, 130), fontsize=24, color=(25, 200, 255))

def on_key_down(key, unicode=None):
    global level, target
    if key==keys.ESCAPE:
        pygame.quit()
    if key == keys.BACKSPACE:
        target = ""
    elif key == keys.RETURN and level == 1:
        if not target.strip():
            target = "http://localhost"
        level = 2
    elif unicode and key != keys.RETURN and level==1:
        target += unicode

def update():
    global level
    if (level == 0 or level==-2) and keyboard.RETURN:
        level +=1
    elif level -1 and keyboard.space:
        level = 0
    if level==2 and keyboard.space:
        level=0

pgzrun.go()
