from threading import Thread
import pygame, ctypes, os, sys, runpy, numpy
import matplotlib.pyplot as plt
ctypes.windll.shcore.SetProcessDpiAwareness(1)

doc = "Assets\Physics simulator\Teoria\Moto rettilineo uniforme.pdf"

pygame.init()
Titolo = pygame.font.SysFont("Raleway", 60)
myfont = pygame.font.SysFont("Cambria Math", 30)
myfont2 = pygame.font.SysFont("Raleway", 22)
window = pygame.display.set_mode([600,600])
pygame.display.set_caption("Moto rettilineo uniforme")

def opzioni():
    v_input = ""
    v_active = False
    run = True
    while run:
        if v_active:
            color = (0,0,255)
        else:
            color = (0,0,0)
        window.fill((255,255,255))
#titolo
        Titolo_sim = Titolo.render("Moto Rettilineo Uniforme",0,(0,0,0))
        window.blit(Titolo_sim,(55,100))
#indicazioni
        ind = myfont.render("Inserire il modulo della velocità in m/s:",0,(0,0,0))
        window.blit(ind,(20,180))
#input box
        v_text = myfont.render(v_input,0,(0,0,0))
        rect_v = pygame.Rect(20,200,560,40)
        pygame.draw.rect(window,color,rect_v,2)
        window.blit(v_text,(30,210))

        if not(checkfloat(v_input)):
            error_text = myfont2.render("Inserire i dati e verificare l'assenza di caratteri speciali (escluso “.”) o/e lettere",0,(255,0,0))
            window.blit(error_text,(20,250))
#---
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
                else:
                    if v_active and len(v_input)<=28:
                        v_input += event.unicode
            if event.type == pygame.MOUSEBUTTONDOWN:     
                if rect_enter.collidepoint(pygame.mouse.get_pos()) and checkfloat(v_input):
                    t0 = pygame.time.get_ticks()
                    simulatore(0,float(v_input),t0)
                elif rect_home.collidepoint(pygame.mouse.get_pos()):
                        runpy.run_path("Physics Motion Simulator.py")
                elif rect_v.collidepoint(pygame.mouse.get_pos()):
                    v_active = True
                else:
                    v_active = False
        pygame.display.update()

def checkfloat(number):
    try: 
        float(number)
        return True
    except ValueError:
        return False

def simulatore(x,v,t0): 
    run = True
    while run:
        time = (pygame.time.get_ticks()-t0)/1000
        window.fill((255,255,255))
        if x<590:
            x = v*time

        pygame.draw.line(window,(0,0,0),(0,300),(600,300))

        pygame.draw.line(window,(0,0,0),(200,300),(200,320))
        pygame.draw.line(window,(0,0,0),(400,300),(400,320))

        pygame.draw.circle(window,(0,0,255),(x,300),10)

        duecento_m = myfont.render("200m",0,(0,0,0))
        quattrocento_m = myfont.render("400m",0,(0,0,0))
        window.blit(duecento_m,(180,330))
        window.blit(quattrocento_m,(380,330))

#pulsante per la teoria
        teoria_pul = myfont.render("Teoria>>",0,(0,0,0))
        rect_teoria = pygame.Rect(500,550,100,30)
        window.blit(teoria_pul,(500,550))

#pulsante per il menu settings
        opzioni_puls = myfont.render("<<Parametri",0,(0,0,0))
        rect_opzioni = pygame.Rect(15,550,120,30)
        window.blit(opzioni_puls,(15,550))

        grafico_puls = myfont.render("Grafico",0,(0,0,0))
        rect_grafico = pygame.Rect(500,15,100,30)
        window.blit(grafico_puls,(510,20))

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
                    t = Thread(target=Grafico, args=(v,))
                    t.start() 
        pygame.display.update()

def Grafico(v):
    t = numpy.linspace(0, 600/v, 600) 
    s = v*t
    plt.xlabel("Tempo (s)")
    plt.ylabel("Spazio (m)")
    plt.plot(t, s)
    plt.title('Grafico spazio-tempo')
    plt.legend(["x"])
    plt.show() 
opzioni()