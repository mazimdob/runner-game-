import pgzrun,random,pyautogui
WIDTH,HEIGHT=pyautogui.size()
TITLE="Shooting running game"
print(pyautogui.size())

player=Actor("player.png")
player.pos=50,HEIGHT//2
scaryimages=["reaper.png","doll.png","ghost1.png","ghost2.png"]
enemys=[]
blade=[]
speed=10
highscore=0
gamestate="start"
score=0
lives=3
music.play("backgroundsound")
music.set_volume(0.05)
def create_enemy():
    if gamestate=="play":
        ship=Actor("ghostship.png")
        ship.pos=WIDTH,random.randint(0,HEIGHT)
        enemys.append(ship)
        enemy=Actor(random.choice(scaryimages))
        enemy.pos=WIDTH,ship.y
        enemys.append(enemy)
    
def draw():
    
    
    if gamestate=="start":
        screen.fill("blue")
        screen.draw.text("press space to start \n press space to shoot the enemys \n shooting ship is 2 points \n shooting enemy is 1 point \n you have 3 lives \n every time enemy or ship hits player you lose 1 life  ",center=(WIDTH/2,HEIGHT/2),fontsize=30)
    
    elif gamestate=="play":
        screen.blit("spookyocean.jpeg",(0,0))
        player.draw()
        for enemy in enemys:


            enemy.draw()
        for b in blade:
            b.draw()
        screen.draw.text(f"score->{score}",(50,50),fontsize=30)
        screen.draw.text(f"lives->{lives}",(WIDTH-300,50),fontsize=30)
        screen.draw.text(f"highscore->{highscore}",(WIDTH//2,50),fontsize=30)
    elif gamestate=="end":
        screen.fill("red")
        screen.draw.text("Game Over \n press space to restart",center=(WIDTH/2,HEIGHT/2),fontsize=50)

def update():
    global score,lives,enemys,gamestate,speed,highscore

    if gamestate=="play":
        speed+=0.005
        if score>highscore:
            highscore=score
        if keyboard.up:
            player.y-=speed
        if keyboard.down:                       
            player.y+=speed
        if player.y<0:
            player.y=HEIGHT
        if player.y>HEIGHT:
            player.y=0
    
        for b in blade:
            b.x+=speed
            if b.x>WIDTH:
                blade.remove(b)
            for e in enemys:
                if b.colliderect(e):
                    sounds.dyingsound.play()
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
            enemy.x-=speed
            if enemy.x<-150:
                enemys.remove(enemy)
            if player.colliderect(enemy):
            
                lives-=1
                if lives==0:
                    sounds.gameoversound.play()
                    gamestate="end"
                if enemy.image=="ghostship.png":
                    enemys=[]
                else:
                    enemys.remove(enemy)

def on_key_down(key):
     global gamestate,score,lives,speed
     if key==keys.SPACE and gamestate!="play":
        sounds.startsound.play()
        gamestate="play"
        score=0
        lives=3
        speed=10
     if key==keys.SPACE  and gamestate=="play":
        if(len(blade)<3):
            sounds.shotsound.play()
            b=Actor("blade.png")
            b.pos=player.x+50,player.y
            blade.append(b)

clock.schedule_interval(create_enemy,5)
pgzrun.go()