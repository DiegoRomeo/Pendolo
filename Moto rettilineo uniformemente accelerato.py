import pygame, ctypes, sys, os, runpy, numpy, cmath
from threading import Thread
import matplotlib.pyplot as plt
ctypes.windll.shcore.SetProcessDpiAwareness(1)
doc = "Assets\Physics simulator\Teoria\Moto rettilineo uniformemente accelerato.pdf"
pygame.init()
myfont = pygame.font.SysFont("Cambria Math", 30)
myfont2 = pygame.font.SysFont("Cambria Math", 38)
myfont3 = pygame.font.SysFont("Raleway", 22)
window = pygame.display.set_mode([600,600])
pygame.display.set_caption("Moto rettilineo uniformemente accelerato")

def impostazioni():
    v_input = ""
    a_input = ""
    v_active = False
    a_active = False
    run = True
    while run:
#colori
        if v_active:
            color1 = (0,0,255)
        if a_active:
            color2 = (0,0,255)
        if not(a_active):
            color2 = (0,0,0)
        if not(v_active):
            color1 = (0,0,0)

        window.fill((255,255,255))

        titolo = myfont2.render("Moto Rettilineo Uniformemente Accelerato",0,(0,0,0))
        window.blit(titolo,(12,30))

        ind1 = myfont.render("Inserire il modulo della velocita in m/s:",0,(0,0,0))
        window.blit(ind1,(20,100))

        v_text = myfont.render(v_input,0,(0,0,0))
        v_box = pygame.Rect(20,130,560,40)
        pygame.draw.rect(window,color1,v_box,2)
        window.blit(v_text,(30,140))

        ind2 = myfont.render("Inserire modulo dell'accelerazione in m/s^2",0,(0,0,0))
        window.blit(ind2,(20,220))

        a_text = myfont.render(a_input,0,(0,0,0))
        a_box = pygame.Rect(20,270,560,40)
        pygame.draw.rect(window,color2,a_box,2)
        window.blit(a_text,(30,280))

        if not(checkfloat(v_input)) or not(checkfloat(a_input)):
            error_text = myfont3.render("Inserire i dati e verificare l'assenza di caratteri speciali (escluso “.”) o/e lettere",0,(255,0,0))
            window.blit(error_text,(20,320))

#tasto enter
        Enter_text = myfont.render(">>",0,(0,0,0))
        rect_enter = pygame.Rect(540,548,40,25)
        pygame.draw.rect(window,(0,0,0),rect_enter,2)
        window.blit(Enter_text,(550,550))

        #pulsante per la schermata principale
        home_puls = myfont.render("<<",0,(0,0,0))
        rect_home = pygame.Rect(15,548,40,25)
        pygame.draw.rect(window,(0,0,0),rect_home,2)
        window.blit(home_puls,(25,550))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    if v_active:
                        v_input = v_input[:-1]
                    elif a_active:
                        a_input = a_input[:-1]
                else:
                    if v_active and len(v_input)<=28:
                        v_input += event.unicode
                    elif a_active and len(a_input)<=28:
                        a_input += event.unicode
            if event.type == pygame.MOUSEBUTTONDOWN:     
                if rect_enter.collidepoint(pygame.mouse.get_pos()) and checkfloat(v_input) and checkfloat(a_input):
                    if float(a_input)>0:
                        t0 = pygame.time.get_ticks()
                        simulatore(float(v_input),float(a_input),t0)
                elif rect_home.collidepoint(pygame.mouse.get_pos()):
                        runpy.run_path("Physics Motion Simulator.py")
                elif v_box.collidepoint(pygame.mouse.get_pos()):
                    a_active = False
                    v_active = True
                elif a_box.collidepoint(pygame.mouse.get_pos()):
                    v_active = False
                    a_active = True
                else:
                    v_active = False
                    a_active = False
        pygame.display.update()

def checkfloat(number):
    try: 
        float(number)
        return True
    except ValueError:
        return False

def simulatore(v0,a,t0):
    run = True
    while run:
        time = (pygame.time.get_ticks()-t0)/1000
        window.fill((255,255,255))

        x = v0*time + ((a)*time**2)/2

#100m e 200m
        pygame.draw.line(window,(0,0,0),(100,300),(100,370))
        pygame.draw.line(window,(0,0,0),(200,300),(200,370))

        pygame.draw.line(window,(0,0,0),(0,300),(600,300))
        pygame.draw.circle(window,(0,0,255),(x,300),10)

        cento_m = myfont.render("100m",0,(0,0,0))
        duecento_m = myfont.render("200m",0,(0,0,0))

        teoria_puls = myfont.render("Teoria>>",0,(0,0,0))
        rect_teoria = pygame.Rect(500,550,100,100)
        window.blit(teoria_puls,(500,550))

        opzioni_puls = myfont.render("<<Parametri",0,(0,0,0))
        rect_opzioni = pygame.Rect(15,550,120,100)
        window.blit(opzioni_puls,(15,550))

        grafico_puls = myfont.render("Grafico",0,(0,0,0))
        rect_grafico = pygame.Rect(500,15,100,30)
        window.blit(grafico_puls,(510,20))


        window.blit(cento_m,(80,380))
        window.blit(duecento_m,(180,380))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if rect_teoria.collidepoint(pygame.mouse.get_pos()):
                    os.startfile(doc)
                elif rect_opzioni.collidepoint(pygame.mouse.get_pos()):
                    impostazioni()
                elif rect_grafico.collidepoint(pygame.mouse.get_pos()):
                    t = Thread(target=Grafico, args=(v0,a,))
                    t.start()
        pygame.display.update()

def Grafico(v0,a):
    vf = numpy.sqrt(v0**2 + a*1200)
    t = numpy.linspace(0, (vf-v0)/a, 1000) 
    v = v0+a*t
    s = v0*t + (a*t**2)/2
    a = (a*t)/t
    plt.xlabel("Tempo (s)")
    plt.ylabel("Spazio(m), Velocità(m/s) e Accelerazione(m/s^2)")
    plt.plot(t, s,"b")
    plt.plot(t, v, "r")
    plt.plot(t, a, "g")
    plt.title('Grafico s(t), v(t), a(t)')
    plt.legend(["s", "v", "a"])
    plt.show()
impostazioni()