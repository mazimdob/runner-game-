import pgzrun,random,pyautogui
WIDTH,HEIGHT=pyautogui.size()
TITLE="Shooting running game"
print(pyautogui.size())

player=Actor("player.png")
player.pos=50,HEIGHT//2
scaryimages=["reaper.png","doll.png","ghost1.png","ghost2.png"]
enemys=[]
blade=[]
gamestate="start"
score=0
lives=3
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
    if gamestate=="start":
        screen.draw.text("press space to start \n press space to shoot the enemys \n shooting ship is 2 points \n shooting enemy is 1 point \n you have 3 lives \n every time enemy or ship hits player you lose 1 life  ",center=(WIDTH/2,HEIGHT/2),fontsize=30)
    for enemy in enemys:
        enemy.draw()
    for b in blade:
        b.draw()
    screen.draw.text(f"score->{score}",(50,50),fontsize=30)
    screen.draw.text(f"lives->{lives}",(WIDTH-300,50),fontsize=30)

def update():
    global score,lives,enemys
    if keyboard.up:
        player.y-=10
    if keyboard.down:                       
        player.y+=10
    if player.y<0:
        player.y=HEIGHT
    if player.y>HEIGHT:
        player.y=0
   
    for b in blade:
        b.x+=10
        if b.x>WIDTH:
            blade.remove(b)
        for e in enemys:
            if b.colliderect(e):
                if e.image=="ghostship.png":
                    print("ghost")
                    score=score+2
                    enemys=[]
                else:
                    score=score+1
                    blade.remove(b)
                    enemys.remove(e)
                break
    for enemy in enemys:
        enemy.x-=10
        if enemy.x<-150:
            enemys.remove(enemy)
        if player.colliderect(enemy):
            lives-=1
            if enemy.image=="ghostship.png":
                enemys=[]
            else:
                enemys.remove(enemy)

def on_key_down(key):
     if key==keys.SPACE:
        if(len(blade)<3):
            b=Actor("blade.png")
            b.pos=player.x+50,player.y
            blade.append(b)

clock.schedule_interval(create_enemy,5)
pgzrun.go()