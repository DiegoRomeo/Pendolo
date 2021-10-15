import pygame, math, ctypes, sys, os, runpy, numpy
import matplotlib.pyplot as plt
from threading import Thread
ctypes.windll.shcore.SetProcessDpiAwareness(1)
doc ="Assets\Physics simulator\Teoria\Caduta dei gravi.pdf"

pygame.init()
myfont = pygame.font.SysFont("Bold", 30)
myfont2 = pygame.font.SysFont("Bold", 40)
myfont3 = pygame.font.SysFont("Raleway",25)
window = pygame.display.set_mode([800, 800])
pygame.display.set_caption("Caduta dei gravi")

def opzioni():
    g_input = ""
    h_input = ""
    g_active = False
    h_active = False
    run = True
    while run:
#colori
        if g_active:
            color1 = (0,0,255)
        if h_active:
            color2 = (0,0,255)
        if not(h_active):
            color2 = (255,255,255)
        if not(g_active):
            color1 = (255,255,255)

        window.fill((0,0,0))
#Titolo
        titolo = myfont2.render("Caduta dei Gravi",0,(255,255,255))
        window.blit(titolo,(280,10))
#Indicazione 1
        ind1 = myfont.render("Inserire il valore assoluto dell'accelerazione gravitazionale in m/s^2:",0,(255,255,255))
        window.blit(ind1,(20,100))
#input box per l'accelerazione gravitazionale
        g_text = myfont.render(g_input,0,(255,255,255))
        g_box = pygame.Rect(20,130,560,40)
        pygame.draw.rect(window,color1,g_box,2)
        window.blit(g_text,(30,140))
#indicazione 2
        ind2 = myfont.render("Inserire l'altezza in m:",0,(255,255,255))
        window.blit(ind2,(20,220))
#input box per h
        h_text = myfont.render(h_input,0,(255,255,255))
        h_box = pygame.Rect(20,250,560,40)
        pygame.draw.rect(window,color2,h_box,2)
        window.blit(h_text,(30,260))

        if not(checkfloat(h_input)) or not(checkfloat(g_input)):
            error_text = myfont3.render("Inserire i dati e verificare l'assenza di caratteri speciali (escluso “.”) o/e lettere",0,(255,0,0))
            window.blit(error_text,(20,300))

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
                    if g_active:
                        g_input = g_input[:-1]
                    elif h_active:
                        h_input = h_input[:-1]
                else:
                    if g_active and len(g_input)<=28:
                        g_input += event.unicode
                    elif h_active and len(h_input)<=28:
                        h_input += event.unicode
            if event.type == pygame.MOUSEBUTTONDOWN:     
                if rect_enter.collidepoint(pygame.mouse.get_pos()) and checkfloat(g_input) and checkfloat(h_input) and float(h_input)>0:
                    t0 = pygame.time.get_ticks()
                    simulatore(float(g_input),float(h_input),t0)
                elif rect_home.collidepoint(pygame.mouse.get_pos()):
                        runpy.run_path("Physics Motion Simulator.py")
                if g_box.collidepoint(pygame.mouse.get_pos()):
                    h_active = False
                    g_active = True
                elif h_box.collidepoint(pygame.mouse.get_pos()):
                    g_active = False
                    h_active = True
                else:
                    g_active = False
                    h_active = False
        pygame.display.update()

def checkfloat(number):
    try: 
        float(number)
        return True
    except ValueError:
        return False

def simulatore(g,h,t0):
    T = math.sqrt(2*h/g)
    a = 2*785/(T)**2  #L'accelerazione viene riproporzionata per un'altezza di 800 pixel
    y = 0
    run = True
    while run:
        time = (pygame.time.get_ticks()-t0)/1000
        if y<785:
            y = a*(time**2)/2

        window.fill((0,0,0))
        pygame.draw.circle(window,(255,255,255),(400,y),15.0)

        g_testo = myfont.render(("g = {} m/s^2".format(round(g,3))),0,(255,255,255))
        h_testo = myfont.render(("h = {} m".format(round(h,3))),0,(255,255,255))
        T_testo = myfont.render(("T = {} s".format(round(T,3))),0,(255,255,255))

        window.blit(g_testo,(600,0))
        window.blit(h_testo,(600,40))
        window.blit(T_testo,(600,80))

#pulsante teoria
        teoria_pulsante = myfont.render("Teoria>>",0,(255,255,255))
        rect_teoria = pygame.Rect(700,750,100,100)
        window.blit(teoria_pulsante,(700,750))
#pulsante opzioni
        opzioni_puls = myfont.render("<<Parametri",0,(255,255,255))
        rect_opzioni = pygame.Rect(15,750,120,100)
        window.blit(opzioni_puls,(15,750))

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
                    t = Thread(target=Grafico, args=(g,T,h,))
                    t.start()
        pygame.display.update()
def Grafico(g,T,h):
    t = numpy.linspace(0, T, 1000)
    s = h-(g*t**2)/2
    v = -(g*t)
    plt.xlabel("Tempo (s)")
    plt.ylabel("s(m), v(m/s)")
    plt.plot(t, s,"b")
    plt.plot(t, v, "r")
    plt.title('Grafico s(t), v(t)')
    plt.legend(["s", "v"])
    plt.show()
opzioni()