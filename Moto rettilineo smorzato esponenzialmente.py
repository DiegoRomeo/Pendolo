import pygame, math, ctypes, sys, os, runpy, numpy
import matplotlib.pyplot as plt
from threading import Thread 
ctypes.windll.shcore.SetProcessDpiAwareness(1)
doc = "Assets\Physics simulator\Teoria\Moto rettilineo smorzato esponenzialmente.pdf"
pygame.init()
myfont = pygame.font.SysFont("Cambria Math", 30)
myfont2 = pygame.font.SysFont("Cambria Math", 38)
myfont3 = pygame.font.SysFont("Raleway", 22)
window = pygame.display.set_mode([600,600])
pygame.display.set_caption("Moto rettilineo smorzato esponenzialmente")

def impostazioni():
    v_input = ""
    k_input = ""
    v_active = False
    k_active = False
    run = True
    while run:
#colori
        if v_active:
            color1 = (0,0,255)
        if k_active:
            color2 = (0,0,255)
        if not(k_active):
            color2 = (0,0,0)
        if not(v_active):
            color1 = (0,0,0)

        window.fill((255,255,255))
#Titolo
        titolo = myfont2.render("Moto Rettilineo Smorzato Esponenzialmente",0,(0,0,0))
        window.blit(titolo,(12,30))
#Indicazione 1
        ind1 = myfont.render("Inserire il modulo della velocita in m/s:",0,(0,0,0))
        window.blit(ind1,(20,100))
#input box per la velocità
        v_text = myfont.render(v_input,0,(0,0,0))
        v_box = pygame.Rect(20,130,560,40)
        pygame.draw.rect(window,color1,v_box,2)
        window.blit(v_text,(30,140))
#indicazione 2
        ind2 = myfont.render("Inserire il valore assoluto del coefficiente di smorzamento",0,(0,0,0))
        ind3 = myfont.render("in 1/s:",0,(0,0,0))
        window.blit(ind2,(20,220))
        window.blit(ind3,(20,240))
#input box per k
        k_text = myfont.render(k_input,0,(0,0,0))
        k_box = pygame.Rect(20,270,560,40)
        pygame.draw.rect(window,color2,k_box,2)
        window.blit(k_text,(30,280))

        if not(checkfloat(v_input)) or not(checkfloat(k_input)):
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
                    elif k_active:
                        k_input = k_input[:-1]
                else:
                    if v_active and len(v_input)<=28:
                        v_input += event.unicode
                    elif k_active and len(k_input)<=28:
                        k_input += event.unicode
            if event.type == pygame.MOUSEBUTTONDOWN:     
                if rect_enter.collidepoint(pygame.mouse.get_pos()) and checkfloat(v_input) and checkfloat(k_input) and float(k_input)>0:
                    t0 = pygame.time.get_ticks()
                    simulatore(float(v_input),float(k_input),t0)
                elif rect_home.collidepoint(pygame.mouse.get_pos()):
                        runpy.run_path("Physics Motion Simulator.py")
                elif v_box.collidepoint(pygame.mouse.get_pos()):
                    k_active = False
                    v_active = True
                elif k_box.collidepoint(pygame.mouse.get_pos()):
                    v_active = False
                    k_active = True
                else:
                    v_active = False
                    k_active = False
        pygame.display.update()

def checkfloat(number):
    try: 
        float(number)
        return True
    except ValueError:
        return False

def simulatore(v0,k,t0):
    run = True
    while run:
        time = (pygame.time.get_ticks()-t0)/1000
        window.fill((255,255,255))

        x = v0*(1-math.e**(-k*time))/k

#100m e 200m
        pygame.draw.line(window,(0,0,0),(100,300),(100,370))
        pygame.draw.line(window,(0,0,0),(200,300),(200,370))

#asse x, v0/k e punto materiale
        pygame.draw.line(window,(0,0,0),(0,300),(600,300))
        pygame.draw.line(window,(0,0,0),(v0/k,300),(v0/k,320))
        pygame.draw.circle(window,(0,0,255),(x,300),10)

        sf_testo = myfont.render("V0/k",0,(0,0,0))
        cento_m = myfont.render("100m",0,(0,0,0))
        duecento_m = myfont.render("200m",0,(0,0,0))
#pulsante teoria
        teoria_pulsante = myfont.render("Teoria>>",0,(0,0,0))
        rect_teoria = pygame.Rect(500,550,100,100)
        window.blit(teoria_pulsante,(500,550))
#pulsante opzioni
        opzioni_puls = myfont.render("<<Parametri",0,(0,0,0))
        rect_opzioni = pygame.Rect(15,550,120,100)
        window.blit(opzioni_puls,(15,550))

        grafico_puls = myfont.render("Grafico",0,(0,0,0))
        rect_grafico = pygame.Rect(500,15,100,30)
        window.blit(grafico_puls,(510,20))

        window.blit(cento_m,(80,380))
        window.blit(duecento_m,(180,380))
        window.blit(sf_testo,(v0/k -20,330))

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
                    t = Thread(target=Grafico, args=(v0,k,))
                    t.start()
        pygame.display.update()

def Grafico(v0,k):
    t = numpy.linspace(0, 100, 600) 
    s = v0*(1-math.e**(-k*t))/k
    v = v0*numpy.e**(-k*t)
    plt.xlabel("Tempo (s)")
    plt.ylabel("Spazio (m) e velocità(m/s)")
    plt.plot(t, s)
    plt.plot(t, v)
    plt.title('Grafico spazio-tempo e velocità-tempo')
    plt.legend(["s","v"])
    plt.show()
impostazioni()

# 1pxl = 1m
#aggiungere testo indicante v0/k in m