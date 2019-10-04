___author___="David Martínez"
import pygame, sys, random, copy
pygame.init()

n,m=4,4
size=600,600
screen=0
TamañoEscX, TamañoEscY=0,0
negro=(0,0,0)
blanco=(255,255,255)
rojo=(255,0,0)
azul=(0,0,255)
verde=(0,255,0)
clics=0
pareja=[]
seg=0
mParejas=[]
parejas=[0]
escenario=[]
coord=[]
col=[]
c_p={}
encontrados=[]
#Diccionario con las banderas de los países :D
paises={1:"pais/Colombia.png", 2:"pais/Argentina.png", 3:"pais/Chile.png", 4:"pais/Brazil.png",
        5:"pais/Mexico.png", 6:"pais/Peru.png", 7:"pais/USA.png", 8:"pais/Albania.png",
        9:"pais/Australia.png", 10:"pais/Belgium.png", 11:"pais/Bolivia.png", 12:"pais/Canada.png",
        13:"pais/China.png", 14:"pais/England.png", 15:"pais/Finland.png", 16:"pais/France.png",
        17:"pais/Germany.png",18:"pais/Greece.png", 19:"pais/India.png", 20:"pais/Italy.png",
        21:"pais/Japan.png", 22:"pais/NorthKorea.png",23:"pais/Norway.png", 24:"pais/Paraguay.png",
        25:"pais/Portugal.png", 26:"pais/SouthAfrica.png", 27:"pais/SouthKorea.png", 28:"pais/Spain.png",
        29:"pais/Sweden.png", 30:"pais/Turkey.png", 31:"pais/UnitedKingdom.png", 32:"pais/Uruguay.png"}

nivel=1
jugando=False
campaña=True
menu=True
end=False
maxIntentos=-1
intento=0
R=0
V=255
TV=3
#Diccionario con  escenarios posibles por nivel
niveles={1:((1,4),(4,1),(2,2)), 2:((1,6),(6,1),(2,3),(3,2)), 3:((1,8),(8,1),(2,4),(4,2)), 4:((2,5), (5,2)),
       5:((2,6), (6,2)), 6:((2,7), (7,2)), 7:((2,8), (8,2), (4,4)), 8:((3,6), (6,3)), 9:((4,5), (5,4)), 10:((4,6), (6,4)),
       11:((7,4), (4,7)), 12:((6,5), (5,6)), 13:((4,8), (8,4)), 14:((6,6), (6,6)), 15:((8,5), (5,8)),
       16:((6,7), (7,6)), 17:((6,8), (8,6)), 18:((7,8), (8,7)), 19:((8,8), (8,8))}

#Se cargan todos los recursos
menuBackground= pygame.image.load("images/MenuBackground.png")
titulo=pygame.image.load("images/Titulo.png")
Bcampaña=pygame.image.load("images/button1.png")
Blibre=pygame.image.load("images/button2.png")
tapa= pygame.image.load("images/tapa.gif")
done=  pygame.image.load("images/done.png")
background= pygame.image.load("images/background2.png")
Bmensaje= pygame.image.load("images/mensaje.png")
Btapar= pygame.image.load("images/Btapar.png")
Breiniciar= pygame.image.load("images/Breiniciar.png")
Bmenu= pygame.image.load("images/BMenu.png")
lifebar= pygame.image.load("images/lifebar.png")
Bcheck= pygame.image.load("images/checkbackground.png")
Blevel= pygame.image.load("images/Blevel.png")
ok= pygame.image.load("images/Ok.png")
wrong=pygame.image.load("images/wrong.png")
fin= pygame.image.load("images/fin.png")
volver= pygame.image.load("images/back.png")
lose= pygame.image.load("images/lose.png")
win= pygame.image.load("images/win.png")

f1=pygame.font.SysFont('Arial',15)
f2=pygame.font.SysFont('Lucida Sans',25)
f3=pygame.font.SysFont('Calibri',10)
f4=pygame.font.SysFont('Trebuchet MS',15)
f6=pygame.font.SysFont('Georgia',25)
f5=pygame.font.SysFont('Arial Black',25)


'''
def crearMatriz(a,b):
    global parejas
    cantParejas= int((a*b)/2)
    for q in range (cantParejas):
        while True:
            rand=random.randint(1,32)
            if not rand in mParejas:
                break
        mParejas.append(rand)
        mParejas.append(rand)
    parejas.clear()
    parejas= copy.deepcopy(mParejas)

    for w in range(a):
        for e in range(b):
            add=random.choice(mParejas)
            col.append(add)
            mParejas.pop(mParejas.index(add))
        col_copy=col.copy()
        escenario.append(col_copy)
        col.clear()

def mostrarMatriz():
    cP=int((n*m)/2)
    print("\nSe ha configurado un escenario con %i parejas:"%cP)
    for i in range(n):
        for j in range(m):
            if escenario[i][j]<10:
                print("",escenario[i][j], end=" ")
            else:
                print (escenario[i][j], end=" ")
        print()
    print("¡Vuelve a la pantalla a jugar!")

def crearEscenario():
    global TamañoEscX,TamañoEscY
    TamañoEscX= m*58
    TamañoEscY= n*58
    x=int((size[0]-TamañoEscX)/2)
    y=int((size[1]-TamañoEscY)/2)

    for r in range(y,y+TamañoEscY,58):
        for t in range(x,x+TamañoEscX, 58):
            screen.blit(tapa, (t,r))
            c="%s,%s"%(t,r)
            coord.append(c)
           # pygame.draw.rect(screen,azul,(t,r,48,48))
        y+=50
    relacionar()


def relacionar():
    v=0
    for q in range(n):
        for w in range(m):
            c_p[coord[v]]=escenario[q][w]
            v+=1

def pedirTamaño():
    global n,m, jugando, campaña
    print(">>CONCÉNTRESE<<\n  Modo Libre\nIngresa el tamaño del escenario para jugar (máx. de 8x8)...\n")
    while True:
        n= int(input("¿Cuántas filas?: "))
        m= int(input("¿Cuántas columnas?: "))
        if n<9 and m<9:
            if (n*m)%2==0:
                crearMatriz(n,m)
                mostrarMatriz()
                iniciar()
                jugando=True
                campaña=False
                break

        else:
            print("No se puede crear de este tamaño, intenta de nuevo")

def menu():
    global screen, jugando, end, nivel, clics
    screen= pygame.display.set_mode(size)
    screen.blit(menuBackground, (0,0))
    screen.blit(titulo, (0, 0))
    screen.blit(Bcampaña, (150, 260))
    screen.blit(Blibre, (150, 330))
    txt1=f1.render("(Se ingresa el tamaño en la consola)", 1, blanco)
    txt2=f1.render("(¡Completa los 19 niveles!)", 1, blanco)
    screen.blit(txt1, (200, 380))
    screen.blit(txt2, (226, 308))
    rsc=f3.render("Imagen tomada de opengameart.org", 1, blanco)
    autor=f4.render("Made by David Martínez", 1, blanco)
    screen.blit(rsc, (5, size[1]-15))
    screen.blit(autor, (430, size[1]-25))

    pygame.mixer.music.load("sounds/menu.mp3")
    pygame.mixer.music.play(2)
    jugando=False
    end=False
    nivel, clics=1, 0

def SelectLevel():
    global nivel, n, m, jugando
    if nivel<20:
        esc=random.choice(niveles[nivel])
        n=esc[0]
        m=esc[1]
        crearMatriz(n,m)
        mostrarMatriz()
        iniciar()
        jugando=True
    else:
        restaurar()
        finalizar(pierde=False)

def iniciar():
    global nivel, clics, pareja
    pygame.mixer.music.stop()
    screen.blit(background, (0,0))
    #pygame.draw.rect(screen, blanco, (0,0,size[0], 40))
    #pygame.draw.rect(screen, azul, (120,size[1]-50,100, 40))
    screen.blit(Btapar, (209, size[1]-60))
    screen.blit(Breiniciar, (5, size[1]-34))
    screen.blit(Bmenu, (5, size[1]-71))
    screen.blit(Bcheck, (520, 520))
    screen.blit(Blevel, (15, 480))
    lvltxt="Nivel %s"%nivel
    lvl= f1.render(lvltxt, 1, blanco)
    screen.blit(lvl, (20, 482))
    intentosMax()
    crearBarraVida(False)
    crearEscenario()
    clics=0
    pareja.clear()



def mouse():
    cursor= pygame.mouse.get_pos()
    pos=pygame.mouse.get_pressed()

    if pos[0]:
        if jugando==False:
            if 150<cursor[0]<450 and 260<cursor[1]<310:
                print("MODO CAMPAÑA")
                SelectLevel()
            if 150<cursor[0]<450 and 330<cursor[1]<380:
                print("MODO LIBRE")
                pedirTamaño()

        else:
            if 209<cursor[0]<391 and 540<cursor[1]<592:
                revisarTapar()


def revisarTapar():
    if clics<=1:
        screen.blit(Bmensaje, (0,0))
        text=f2.render("¡Destapa otra ficha!",True, blanco)
        screen.blit(text,(10,5))
    else:
        #print(encontrados)
        tapar()

def jugar():
    global clics, pareja
    x=int((size[0]-TamañoEscX)/2)
    y=int((size[1]-TamañoEscY)/2)
    cursor= pygame.mouse.get_pos()
    pos=pygame.mouse.get_pressed()

    if pos[0]:
        if jugando==True:
            screen.blit(Bmensaje, (0,0))
        if clics<2:
            for p in range(y, y+TamañoEscY, 58):
                for q in range (x, x+TamañoEscX, 58):
                    if q<cursor[0]<q+48 and p<cursor[1]<p+48:
                        k="%s,%s"%(q,p)
                        coordenadas=(q,p)
                        if k in encontrados:
                            screen.blit(Bmensaje, (0,0))
                            text=f2.render("¡Ya encontraste esto!",True,blanco)
                            screen.blit(text,(10,5))
                        else:
                            pygame.draw.rect(screen,blanco,(q,p,48,48))
                            img=pygame.image.load(paises[c_p[k]])
                            screen.blit(img, (q,p))
                            if coordenadas in pareja:
                                screen.blit(Bmensaje, (0,0))
                                text=f2.render("¡Ya destapaste esta misma ficha!",True,blanco)
                                screen.blit(text,(10,5))

                            else:
                                pareja.append(c_p[k])
                                pareja.append(coordenadas)
                                clics+=1

                            if clics==2:
                                parejaC= copy.deepcopy(pareja)
                                revisar(parejaC)
                                pareja.clear()
        else:
            screen.blit(Bmensaje, (0,0))
            text=f2.render("¡Debes tapar las fichas!",True,blanco)
            screen.blit(text,(10,5))







def revisar(p):
    global encontrados
    if p[0]==p[2]:

        #screen.blit(Bcheck, (520, 520))
        screen.blit(ok, (526, 526))
        coord1="%s,%s"%(p[1][0],p[1][1])
        coord2="%s,%s"%(p[3][0],p[3][1])
        encontrados.append(coord1)
        encontrados.append(coord2)
        crearBarraVida(bajar=False)
        pygame.mixer.music.load("sounds/ok.wav")
        pygame.mixer.music.play(1)
    elif p[0]!=p[2]:
        screen.blit(wrong, (526, 526))
        crearBarraVida(bajar=True)
        pygame.mixer.music.load("sounds/wrong.wav")
        pygame.mixer.music.play(1)


def tapar():
        screen.blit(Bmensaje, (0,0))
        global clics
        x=int((size[0]-TamañoEscX)/2)
        y=int((size[1]-TamañoEscY)/2)

        for r in range(y,y+TamañoEscY,58):
            for t in range(x,x+TamañoEscX, 58):
                esta=False
                w="%s,%s"%(t,r)
                for a in range(encontrados.__len__()):
                    if encontrados[a]==w:
                        esta=True
                if esta:
                    screen.blit(done, (t,r))
                else:
                    screen.blit(tapa, (t,r))
            y+=50

        clics=0
        screen.blit(Bcheck, (520, 520))

def intentosMax():
    global maxIntentos
    min= int((n*m)/2)
    e=0
    for z in range(0,min,2):
        e+=1
    adicionales=e
    if min<12:
        maxIntentos=2*min
    else:
        maxIntentos= (2*min)+adicionales
    print("intentos: ", maxIntentos)

def crearBarraVida(bajar):
    global R,V,TV, intento
    vida=(R,V,0)
    if bajar:
        R+=int(255/maxIntentos)
        V-=int(255/maxIntentos)
        TV+=int(268/maxIntentos)
        intento+=1

    pygame.draw.rect(screen, vida, (10,163,40, 268))
    pygame.draw.rect(screen, blanco, (10,163,40, TV))
    screen.blit(lifebar, (5, 158))



def finalizar(pierde):
    global end, nivel, clics
    screen.blit(menuBackground, (0,0))
    screen.blit(titulo, (0, 0))
    txt=f3.render("Imagen tomada de opengameart.org", 1, blanco)
    txt2=f4.render("Made by David Martínez", 1, blanco)
    screen.blit(txt, (5, size[1]-15))
    screen.blit(txt2, (420, size[1]-25))
    screen.blit(fin, (0,274))
    if pierde:
        screen.blit(lose, (0, 329))
        pygame.mixer.music.load("sounds/lose.wav")
        pygame.mixer.music.play(1)
    else:
        screen.blit(win, (0, 329))
        pygame.mixer.music.load("sounds/win.mp3")
        pygame.mixer.music.play(1)
    screen.blit(volver, (189, 480))
    end=True
    nivel=1
    clics=0

def restaurar():
    global jugando, clics, menu, end, maxIntentos, intento, R, V, TV, campaña, pareja
    encontrados.clear()
    escenario.clear()
    coord.clear()
    maxIntentos=-1
    intento=0
    R=0
    V=255
    TV=3
    clics=0
    pareja.clear()
    jugando=False
    campaña=True



menu()
'''
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        '''
        if event.type==pygame.KEYDOWN:

            if event.key==pygame.K_ESCAPE:
                if jugando or end:
                    restaurar()
                    menu()

            if event.key==pygame.K_r:
                if jugando:
                    if not campaña:
                        encontrados.clear()
                        clics=0
                        intento=0
                        R=0
                        V=255
                        TV=3
                        iniciar()
                    else:
                        screen.blit(Bmensaje, (0,0))
                        text=f2.render("¡En modo campaña no puedes reiniciar!",True, blanco)
                        screen.blit(text,(10,5))


            if event.key==pygame.K_SPACE:
                if jugando:
                    revisarTapar()

            if event.key==pygame.K_b:
                #Para bajar la vida y hacer pruebas
                crearBarraVida(bajar=True)


            if event.key==pygame.K_RETURN:
                if end:
                    restaurar()
                    menu()

            if event.key==pygame.K_RIGHT:
                if campaña:
                    nivel+=1
                    restaurar()
                    SelectLevel()

            if encontrados.__len__()==parejas.__len__():
                if campaña:
                    nivel+=1
                    restaurar()
                    SelectLevel()
                else:
                    finalizar(pierde=False)


        if not end:
            jugar()
        mouse()

    if intento==maxIntentos:
        restaurar()
        finalizar(pierde=True)'''

    '''if nivel==20:
        finalizar(pierde=False)'''



    '''pygame.draw.rect(screen, blanco, (size[0]-200,0,200, 40))
    text=f2.render(str(int(pygame.time.get_ticks()/1000)),True, verde)
    screen.blit(text,(size[0]-100,10))'''
    pygame.display.update()


