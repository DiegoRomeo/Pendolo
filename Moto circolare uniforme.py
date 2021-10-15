import pygame, math, ctypes, sys, os, runpy, numpy
import matplotlib.pyplot as plt
from threading import Thread
ctypes.windll.shcore.SetProcessDpiAwareness(1)
doc = "Assets\Physics simulator\Teoria\Moto circolare uniforme.pdf"

pygame.init()
myfont = pygame.font.SysFont("Cambria Math", 30)
myfont2 = pygame.font.SysFont("Cambria Math", 40)
myfont3 = pygame.font.SysFont("Raleway", 22)
window = pygame.display.set_mode([600,600])
pygame.display.set_caption("Moto circolare uniforme")

def opzioni():
    r_input = ""
    v_input = ""
    r_active = False
    v_active = False
    run = True
    while run:
#colori
        if r_active:
            color1 = (0,0,255)
        if v_active:
            color2 = (0,0,255)
        if not(v_active):
            color2 = (255,255,255)
        if not(r_active):
            color1 = (255,255,255)

        window.fill((0,0,0))
#Titolo
        titolo = myfont2.render("Moto Circolare Uniforme",0,(255,255,255))
        window.blit(titolo,(140,30))
#Indicazione 1
        ind1 = myfont.render("Inserire la lunghezza del raggio in m:",0,(255,255,255))
        window.blit(ind1,(20,100))
#input box per la velocità
        r_text = myfont.render(r_input,0,(255,255,255))
        r_box = pygame.Rect(20,130,560,40)
        pygame.draw.rect(window,color1,r_box,2)
        window.blit(r_text,(30,140))
#indicazione 2
        ind2 = myfont.render("Inserire il modulo della velocità tangenziale in m/s:",0,(255,255,255))
        window.blit(ind2,(20,220))

        v_text = myfont.render(v_input,0,(255,255,255))
        v_box = pygame.Rect(20,250,560,40)
        pygame.draw.rect(window,color2,v_box,2)
        window.blit(v_text,(30,260))

        if not(checkfloat(v_input)):
            error_text = myfont3.render("Inserire i dati e verificare l'assenza di caratteri speciali (escluso “.”) o/e lettere",0,(255,0,0))
            window.blit(error_text,(20,300))
#tasto enter
        Enter_text = myfont.render(">>",0,(255,255,255))
        rect_enter = pygame.Rect(540,548,40,25)
        pygame.draw.rect(window,(255,255,255),rect_enter,2)
        window.blit(Enter_text,(550,550))
#pulsante per la schermata principale
        home_puls = myfont.render("<<",0,(255,255,255))
        rect_home = pygame.Rect(15,548,40,25)
        pygame.draw.rect(window,(255,255,255),rect_home,2)
        window.blit(home_puls,(25,550))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    if r_active:
                        r_input = r_input[:-1]
                    elif v_active:
                        v_input = v_input[:-1]
                else:
                    if r_active and len(r_input)<=28:
                        r_input += event.unicode
                    elif v_active and len(v_input)<=28:
                        v_input += event.unicode
            if event.type == pygame.MOUSEBUTTONDOWN:     
                if rect_enter.collidepoint(pygame.mouse.get_pos()) and checkfloat(r_input) and checkfloat(v_input) and float(r_input)>0:
                    t0 = pygame.time.get_ticks()
                    simulatore(float(r_input),float(v_input),t0)
                elif rect_home.collidepoint(pygame.mouse.get_pos()):
                        runpy.run_path("Physics Motion Simulator.py")
                elif r_box.collidepoint(pygame.mouse.get_pos()):
                    v_active = False
                    r_active = True
                elif v_box.collidepoint(pygame.mouse.get_pos()):
                    r_active = False
                    v_active = True
                else:
                    r_active = False
                    v_active = False
        pygame.display.update()

def checkfloat(number):
    try: 
        float(number)
        return True
    except ValueError:
        return False

def simulatore(r,v,t0):
    v_angolare = v/r
    run = True
    while run:
        time = (pygame.time.get_ticks()-t0)/1000
        x = 300 + 200*math.cos(v_angolare*time)
        y = 300 + 200*math.sin(v_angolare*time)

        window.fill((0,0,0))
        pygame.draw.circle(window,(255,255,255),(300,300),200)
        pygame.draw.circle(window,(0,0,0),(300,300),199)
#diametro
        pygame.draw.line(window,(255,255,255),(100,300),(500,300))

        pygame.draw.circle(window,(255,255,255),(x,y),10)

        T = myfont.render("T = {}s".format(round(2*r*math.pi/v,3)),0,(255,255,255))
        window.blit(T,(480,20))
    
#pulsante teoria
        teoria_puls = myfont.render("Teoria>>",0,(255,255,255))
        rect_teoria = pygame.Rect(500,550,100,100)
        window.blit(teoria_puls,(500,550))
#pulsante opzioni
        opzioni_puls = myfont.render("<<Parametri",0,(255,255,255))
        rect_opzioni = pygame.Rect(15,550,120,100)
        window.blit(opzioni_puls,(15,550))

        grafico_puls = myfont.render("Grafico",0,(255,255,255))
        rect_grafico = pygame.Rect(5,15,100,30)
        window.blit(grafico_puls,(15,20))

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
                    t = Thread(target=Grafico, args=(v_angolare,r,))
                    t.start()
        pygame.display.update()

def Grafico(v_ang,r):
    t = numpy.linspace(0, 2*math.pi, 1000)
    x = r*numpy.cos(v_ang*t)
    y = -r*numpy.sin(v_ang*t)
    plt.xlabel("Tempo (s)")
    plt.ylabel("X e Y (m)")
    plt.plot(t, x, "b")
    plt.plot(t, y, "r")
    plt.title('Grafico delle componenti X e Y del moto')
    plt.legend(['X', 'Y'])
    plt.show()

opzioni()