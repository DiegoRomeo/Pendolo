import pygame, ctypes, sys, os, runpy, numpy
import matplotlib.pyplot as plt
from threading import Thread
ctypes.windll.shcore.SetProcessDpiAwareness(1)
doc = "Assets\Physics simulator\Teoria\Moto parabolico.pdf"

pygame.init()
myfont = pygame.font.SysFont("Cambria Math", 30)
myfont2 = pygame.font.SysFont("Raleway", 40)
myfont3 = pygame.font.SysFont("Raleway", 25)
window = pygame.display.set_mode([800,800])
pygame.display.set_caption("Moto parabolico")

def opzioni():
    g_input = ""
    v0x_input = ""
    v0y_input = ""
    v0x_active = False
    v0y_active = False
    g_active = False
    run = True
    while run:
#colori
        if v0x_active:
            color1 = (0,0,255)
        if v0y_active:
            color2 = (0,0,255)
        if g_active:
            color3 = (0,0,255)
        if not(v0x_active):
            color1 = (255,255,255)
        if not(v0y_active):
            color2 = (255,255,255)
        if not(g_active):
            color3 = (255,255,255)

        window.fill((0,0,0))
#Titolo
        titolo = myfont2.render("Moto Parabolico",0,(255,255,255))
        window.blit(titolo,(270,30))
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
        ind2 = myfont.render("Inserire il modulo dell'accelerazione gravitazionale in m/s^2:",0,(255,255,255))
        window.blit(ind2,(20,340))
#input box per g
        g_text = myfont.render(g_input,0,(255,255,255))
        g_box = pygame.Rect(20,370,560,40)
        pygame.draw.rect(window,color3,g_box,2)
        window.blit(g_text,(30,380))

        if not(checkfloat(g_input)) or not(checkfloat(v0x_input)) or not(checkfloat(v0y_input)):
            error_text = myfont3.render("Inserire i dati e verificare l'assenza di caratteri speciali (escluso “.”) o/e lettere",0,(255,0,0))
            window.blit(error_text,(20,420))

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
                    elif g_active:
                        g_input = g_input[:-1]
                else:
                    if v0x_active and len(v0x_input)<=28:
                        v0x_input += event.unicode
                    elif v0y_active and len(v0y_input)<=28:
                        v0y_input += event.unicode
                    elif g_active and len(g_input)<=28:
                        g_input += event.unicode
            if event.type == pygame.MOUSEBUTTONDOWN:     
                if rect_enter.collidepoint(pygame.mouse.get_pos()) and checkfloat(v0x_input) and checkfloat(v0y_input) and checkfloat(g_input):
                    t0 = pygame.time.get_ticks()
                    simulatore(float(v0x_input),float(v0y_input),float(g_input),t0)
                elif rect_home.collidepoint(pygame.mouse.get_pos()):
                        runpy.run_path("Physics Motion Simulator.py")
                elif v0x_box.collidepoint(pygame.mouse.get_pos()):
                    g_active = False
                    v0y_active = False
                    v0x_active = True
                elif v0y_box.collidepoint(pygame.mouse.get_pos()):
                    g_active = False
                    v0x_active = False
                    v0y_active = True
                elif g_box.collidepoint(pygame.mouse.get_pos()):
                    v0x_active = False
                    v0y_active = False
                    g_active = True
                else:
                    v0x_active = False
                    v0y_active = False
                    g_active = False
        pygame.display.update()

def checkfloat(number):
    try: 
        float(number)
        return True
    except ValueError:
        return False

def simulatore(vx0,vy0,g,t0):
    posx = []
    posy = []
    y = 800
    run = True
    while run:
        time = (pygame.time.get_ticks()-t0)/1000
        window.fill((0,0,0))
        if y <= 800:
            x = vx0*time
            y = 800 -vy0*time + g*(1/2)*time**2 
            posx.append(x)
            posy.append(y)
        for i in range(len(posx)):
            pygame.draw.circle(window,(0,255,0),(posx[i],posy[i]),1)
        pygame.draw.circle(window,(0,0,255),(x,y),10)
#pulsante teoria
        teoria_pulsante = myfont.render("Teoria>>",0,(255,255,255))
        rect_teoria = pygame.Rect(700,30,100,100)
        window.blit(teoria_pulsante,(700,30))
#pulsante opzioni
        opzioni_puls = myfont.render("<<Parametri",0,(255,255,255))
        rect_opzioni = pygame.Rect(15,30,120,100)
        window.blit(opzioni_puls,(15,30))

        grafico_puls = myfont.render("Grafico",0,(255,255,255))
        rect_grafico = pygame.Rect(690,765,100,30)
        window.blit(grafico_puls,(700,770))

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
                    t = Thread(target=Grafico, args=(vx0,vy0,g,))
                    t.start()
        pygame.display.update()
def Grafico(vx0,vy0,g):
    t = numpy.linspace(0, 2*vy0/g, 1000)
    x = vx0*t
    y = vy0*t - (g*t**2)/2
    plt.xlabel("Tempo (s)")
    plt.ylabel("x(m), y(m)")
    plt.plot(t, x,"b")
    plt.plot(t, y, "r")
    plt.title('Grafico x(t), y(t)')
    plt.legend(["x", "y"])
    plt.show()
opzioni()