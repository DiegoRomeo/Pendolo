import pygame, ctypes, sys, os, runpy, numpy
from threading import Thread
import matplotlib.pyplot as plt
ctypes.windll.shcore.SetProcessDpiAwareness(1)
doc = "Assets\Physics simulator\Teoria\Moto bidimensionale uniformemente accelerato.pdf"
x = 400
y = 400

pygame.init()
myfont = pygame.font.SysFont("Cambria Math", 30)
myfont2 = pygame.font.SysFont("Raleway", 40)
myfont3 = pygame.font.SysFont("Raleway", 25)
window = pygame.display.set_mode([800,800])
pygame.display.set_caption("Moto bidimensionale uniformemente accelerato")

def opzioni():
    v0x_input = ""
    v0y_input = ""
    a0x_input = ""
    a0y_input = ""
    v0x_active = False
    v0y_active = False
    a0x_active = False
    a0y_active = False
    run = True
    while run:
#colori
        if v0x_active:
            color1 = (0,0,255)
        if v0y_active:
            color2 = (0,0,255)
        if a0x_active:
            color3 = (0,0,255)
        if a0y_active:
            color4 = (0,0,255)
        if not(v0x_active):
            color1 = (255,255,255)
        if not(v0y_active):
            color2 = (255,255,255)
        if not(a0x_active):
            color3 = (255,255,255)
        if not(a0y_active):
            color4 = (255,255,255)

        window.fill((0,0,0))
#Titolo
        titolo = myfont2.render("Moto Bidimensionale Uniformemente Accelerato",0,(255,255,255))
        window.blit(titolo,(75,30))
#Indicazione 1
        ind1 = myfont.render("Inserire la componente orizzontale della velocita in m/s:",0,(255,255,255))
        window.blit(ind1,(20,100))
#input box per la velocità orizzontale
        v0x_text = myfont.render(v0x_input,0,(255,255,255))
        v0x_box = pygame.Rect(20,130,560,40)
        pygame.draw.rect(window,color1,v0x_box,2)
        window.blit(v0x_text,(30,140))
#indicazione 2
        ind2 = myfont.render("Inserire la componente verticale della velocità in m/s:",0,(255,255,255))
        window.blit(ind2,(20,220))
#input box per la velocità verticale
        v0y_text = myfont.render(v0y_input,0,(255,255,255))
        v0y_box = pygame.Rect(20,250,560,40)
        pygame.draw.rect(window,color2,v0y_box,2)
        window.blit(v0y_text,(30,260))
#indicazione 3
        ind3 = myfont.render("Inserire la componente orizzontale dell'accelerazione in m/s^2:",0,(255,255,255))
        window.blit(ind3,(20,340))
#input box per l'accelerazione orizzontale
        a0x_text = myfont.render(a0x_input,0,(255,255,255))
        a0x_box = pygame.Rect(20,370,560,40)
        pygame.draw.rect(window,color3,a0x_box,2)
        window.blit(a0x_text,(30,380))
#indicazione 4
        ind4 = myfont.render("Inserire la componente verticale dell'accelerazione in m/s^2:",0,(255,255,255))
        window.blit(ind4,(20,460))
#input box per l'accelerazione verticale
        a0y_text = myfont.render(a0y_input,0,(255,255,255))
        a0y_box = pygame.Rect(20,490,560,40)
        pygame.draw.rect(window,color4,a0y_box,2)
        window.blit(a0y_text,(30,500))

        if not(checkfloat(v0x_input)) or not(checkfloat(v0y_input)) or not(checkfloat(a0x_input)) or not(checkfloat(a0y_input)):
            error_text = myfont3.render("Inserire i dati e verificare l'assenza di caratteri speciali (escluso “.”) o/e lettere",0,(255,0,0))
            window.blit(error_text,(20,540))
#tasto enter
        Enter_text = myfont.render(">>",0,(255,255,255))
        rect_enter = pygame.Rect(740,748,40,25)
        pygame.draw.rect(window,(255,255,255),rect_enter,2)
        window.blit(Enter_text,(750,750))

#pulsante per la schermata principale
        home_puls = myfont.render("<<",0,(255,255,255))
        rect_home = pygame.Rect(15,748,40,25)
        pygame.draw.rect(window,(255,255,255),rect_home,2)
        window.blit(home_puls,(25,750))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    if v0x_active:
                        v0x_input = v0x_input[:-1]
                    elif v0y_active:
                        v0y_input = v0y_input[:-1]
                    elif a0x_active:
                        a0x_input = a0x_input[:-1]
                    elif a0y_active:
                        a0y_input = a0y_input[:-1]
                else:
                    if v0x_active and len(v0x_input)<=28:
                        v0x_input += event.unicode
                    elif v0y_active and len(v0y_input)<=28:
                        v0y_input += event.unicode
                    elif a0x_active and len(a0x_input)<=28:
                        a0x_input += event.unicode
                    elif a0y_active and len(a0y_input)<=28:
                        a0y_input += event.unicode
            if event.type == pygame.MOUSEBUTTONDOWN:     
                if rect_enter.collidepoint(pygame.mouse.get_pos()) and checkfloat(v0x_input) and checkfloat(v0y_input) and checkfloat(a0x_input) and checkfloat(a0y_input):
                    t0 = pygame.time.get_ticks()
                    simulatore(float(v0x_input),float(v0y_input),float(a0x_input),float(a0y_input),t0)
                elif rect_home.collidepoint(pygame.mouse.get_pos()):
                        runpy.run_path("Physics Motion Simulator.py")
                elif v0x_box.collidepoint(pygame.mouse.get_pos()):
                    v0y_active = False
                    a0x_active = False
                    a0y_active = False
                    v0x_active = True
                elif v0y_box.collidepoint(pygame.mouse.get_pos()):
                    v0x_active = False
                    a0x_active = False
                    a0y_active = False
                    v0y_active = True
                elif a0x_box.collidepoint(pygame.mouse.get_pos()):
                    v0x_active = False
                    v0y_active = False
                    a0y_active = False
                    a0x_active = True
                elif a0y_box.collidepoint(pygame.mouse.get_pos()):
                    v0x_active = False
                    v0y_active = False
                    a0x_active = False
                    a0y_active = True
                else:
                    v0x_active = False
                    v0y_active = False
                    a0x_active = False
                    a0y_active = False
        pygame.display.update()

def checkfloat(number):
    try: 
        float(number)
        return True
    except ValueError:
        return False

def simulatore(v0x,v0y,a0x,a0y,t0):
    posx = []
    posy = []
    run = True
    while run:
        time = (pygame.time.get_ticks()-t0)/1000

        x = 400+ v0x*time + a0x*(time**2)*(1/2)
        y = 400- v0y*time - a0y*(time**2)*(1/2)

        posx.append(x)
        posy.append(y)

        window.fill((0,0,0))
#assi x e y
        pygame.draw.line(window,(255,255,255),(0,400),(800,400))
        pygame.draw.line(window,(255,255,255),(400,0),(400,800))
        x_testo = myfont.render("x",0,(255,255,255))
        y_testo = myfont.render("y",0,(255,255,255))

        window.blit(x_testo,(770,410))
        window.blit(y_testo,(380,20))

        for i in range(len(posx)):
            pygame.draw.circle(window,(0,0,255),(posx[i],posy[i]),1)
        pygame.draw.circle(window,(255,255,255),(x,y),10)
    
        #pulsante teoria
        teoria_pulsante = myfont.render("Teoria>>",0,(255,255,255))
        rect_teoria = pygame.Rect(700,750,100,100)
        window.blit(teoria_pulsante,(700,750))
#pulsante opzioni
        opzioni_puls = myfont.render("<<Parametri",0,(255,255,255))
        rect_opzioni = pygame.Rect(15,750,120,100)
        window.blit(opzioni_puls,(15,750))

        grafico_puls = myfont.render("Grafico",0,(255,255,255))
        rect_grafico = pygame.Rect(700,15,100,30)
        window.blit(grafico_puls,(710,20))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if rect_teoria.collidepoint(pygame.mouse.get_pos()):
                    os.startfile(doc)
                elif rect_opzioni.collidepoint(pygame.mouse.get_pos()):
                    opzioni()
                elif rect_grafico.collidepoint(pygame.mouse.get_pos()):
                    t = Thread(target=Grafico, args=(v0x,v0y,a0x,a0y,))
                    t.start()
        pygame.display.update()
def Grafico(vx0,vy0,ax,ay):
    t = numpy.linspace(0, 100, 1000)
    x = vx0*t + (ax*t**2)/2
    y = vy0*t + (ay*t**2)/2
    vx = vx0+ax*t
    vy = vy0+ay*t 
    plt.xlabel("Tempo (s)")
    plt.ylabel("x(m), y(m), vx(m/s) e vy(m/s)")
    plt.plot(t, x,"b")
    plt.plot(t, y, "r")
    plt.plot(t, vx,"y")
    plt.plot(t, vy, "g")
    plt.title('Grafico x(t), y(t), vx(t) e vy(t)')
    plt.legend(["vx", "vy", "ax", "ay"])
    plt.show()
opzioni()
# 1 pxl = 1 m