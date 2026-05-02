import pgzrun,random,pyautogui
WIDTH,HEIGHT=pyautogui.size()
TITLE="Shooting running game"
print(pyautogui.size())

player=Actor("player.png")
player.pos=50,HEIGHT//2
scaryimages=["reaper.png","doll.png","ghost1.png","ghost2.png"]
enemys=[]
blade=[]
def create_enemy():
    ship=Actor("ghostship.png")
    ship.pos=WIDTH,random.randint(0,HEIGHT)
    enemys.append(ship)
    enemy=Actor(random.choice(scaryimages))
    enemy.pos=WIDTH,ship.y
    enemys.append(enemy)
    
def draw():
    screen.blit("spookyocean.jpeg",(0,0))
    player.draw()
    for enemy in enemys:
        enemy.draw()
    for b in blade:
        b.draw()

def update():
    if keyboard.up:
        player.y-=10
    if keyboard.down:                       
        player.y+=10
    if player.y<0:
        player.y=HEIGHT
    if player.y>HEIGHT:
        player.y=0
    if keyboard.space:
        b=Actor("blade.png")
        b.pos=player.x+50,player.y
        blade.append(b)
    for b in blade:
        b.x+=10
        if b.x>WIDTH:
            blade.remove(b)
        for e in enemys:
            if b.colliderect(e):
                try:
                    blade.remove(b)
                    enemys.remove(e)
                except:
                    pass
    for enemy in enemys:
        enemy.x-=10
        if enemy.x<-150:
            enemys.remove(enemy)

clock.schedule_interval(create_enemy,5)
pgzrun.go()
