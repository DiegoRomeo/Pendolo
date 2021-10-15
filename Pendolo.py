import math, pygame, ctypes, os, sys, runpy, numpy
import matplotlib.pyplot as plt
from threading import Thread
ctypes.windll.shcore.SetProcessDpiAwareness(1)
doc = "Assets\Physics simulator\Teoria\Pendolo.pdf"

pygame.init()
myfont = pygame.font.SysFont("Bold", 30)
myfont2 = pygame.font.SysFont("Raleway", 50)
myfont3 = pygame.font.SysFont("Raleway", 25)
window = pygame.display.set_mode([1230, 615])
pygame.display.set_caption("Pendolo")
def opzioni():
    g_input = ""
    L_input = ""
    Omega_input = ""
    g_active = False
    L_active = False
    Omega_active = False
    run = True
    while run:
#colori
        if g_active:
            color1 = (0,0,255)
        if L_active:
            color2 = (0,0,255)
        if Omega_active:
            color3 = (0,0,255)
        if not(g_active):
            color1 = (255,255,255)
        if not(L_active):
            color2 = (255,255,255)
        if not(Omega_active):
            color3 = (255,255,255)

        window.fill((0,0,0))
#Titolo
        titolo = myfont2.render("Pendolo",0,(255,255,255))
        window.blit(titolo,(535,30))
#Indicazione 1
        ind1 = myfont.render("Inserire il modulo dell'accelerazione gravitazionale in m/s^2:",0,(255,255,255))
        window.blit(ind1,(20,100))
#input box per la velocità orizzontale
        g_text = myfont.render(g_input,0,(255,255,255))
        g_box = pygame.Rect(20,130,560,40)
        pygame.draw.rect(window,color1,g_box,2)
        window.blit(g_text,(30,140))
#indicazione 2
        ind2 = myfont.render("Inserire la lunghezza del filo in m:",0,(255,255,255))
        window.blit(ind2,(20,220))
#input box per la velocità verticale
        L_text = myfont.render(L_input,0,(255,255,255))
        L_box = pygame.Rect(20,250,560,40)
        pygame.draw.rect(window,color2,L_box,2)
        window.blit(L_text,(30,260))
#indicazione 3
        ind2 = myfont.render("Inserire l'angolo iniziale in gradi:",0,(255,255,255))
        window.blit(ind2,(20,340))
#input box per g
        Omega_text = myfont.render(Omega_input,0,(255,255,255))
        Omega_box = pygame.Rect(20,370,560,40)
        pygame.draw.rect(window,color3,Omega_box,2)
        window.blit(Omega_text,(30,380))

        if not(checkfloat(Omega_input))or not(checkfloat(g_input)) or not(checkfloat(L_input)):
            error_text = myfont3.render("Inserire i dati e verificare l'assenza di caratteri speciali (escluso “.”) o/e lettere",0,(255,0,0))
            window.blit(error_text,(20,420))
#tasto enter
        Enter_text = myfont.render(">>",0,(255,255,255))
        rect_enter = pygame.Rect(1170,563,40,25)
        pygame.draw.rect(window,(255,255,255),rect_enter,2)
        window.blit(Enter_text,(1180,565))
#pulsante per la schermata principale
        home_puls = myfont.render("<<",0,(255,255,255))
        rect_home = pygame.Rect(15,563,40,25)
        pygame.draw.rect(window,(255,255,255),rect_home,2)
        window.blit(home_puls,(25,565))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    if g_active:
                        g_input = g_input[:-1]
                    elif L_active:
                        L_input = L_input[:-1]
                    elif Omega_active:
                        Omega_input = Omega_input[:-1]
                else:
                    if g_active and len(g_input)<=28:
                        g_input += event.unicode
                    elif L_active and len(L_input)<=28:
                        L_input += event.unicode
                    elif Omega_active and len(Omega_input)<=28:
                        Omega_input += event.unicode
            if event.type == pygame.MOUSEBUTTONDOWN:     
                if rect_enter.collidepoint(pygame.mouse.get_pos()) and checkfloat(g_input) and checkfloat(L_input) and checkfloat(Omega_input):
                    if float(L_input)>0:
                        t0 = pygame.time.get_ticks()
                        simulatore(float(g_input),float(L_input),float(Omega_input),t0)
                elif rect_home.collidepoint(pygame.mouse.get_pos()):
                        runpy.run_path("Physics Motion Simulator.py")
                elif g_box.collidepoint(pygame.mouse.get_pos()):
                    L_active = False
                    Omega_active = False
                    g_active = True
                elif L_box.collidepoint(pygame.mouse.get_pos()):
                    g_active = False
                    Omega_active = False
                    L_active = True
                elif Omega_box.collidepoint(pygame.mouse.get_pos()):
                    L_active = False
                    g_active = False
                    Omega_active = True
                else:
                    Omega_active = False
                    L_active = False
                    g_active = False
        pygame.display.update()

def checkfloat(number):
    try: 
        float(number)
        return True
    except ValueError:
        return False

def simulatore(g,L,Omega,t0):
    theta_max = math.radians(Omega)
    run = True
    while run:
        time = (pygame.time.get_ticks()-t0)/1000

        theta = theta_max*math.cos(math.sqrt(g/L)*time)
        window.fill((0,0,0))

        x = 615 + 600*math.sin(theta)
        y = 600*math.cos(theta)

        pygame.draw.circle(window,(255,255,255),(x,y),15.0)
        pygame.draw.line(window,(255,255,255),(615,0),(x,y))

        l_filo = myfont.render(("L = {} m".format(round(L,3))),0,(255,255,255))
        T_testo = myfont.render(("T = {} s".format(round(2*math.pi*math.sqrt(L/g),3))),0,(255,255,255))
        angolo_testo = myfont.render(("Omega = {}°".format(round(Omega,3))),0,(255,255,255))

        window.blit(l_filo,(1000,40))
        window.blit(T_testo,(1000,80))
        window.blit(angolo_testo,(1000,120))


        teoria_puls = myfont.render("Teoria>>",0,(255,255,255))
        rect_teoria = pygame.Rect(1130,585,100,100)
        window.blit(teoria_puls,(1130,585))

        opzioni_puls = myfont.render("<<Parametri",0,(255,255,255))
        rect_opzioni = pygame.Rect(15,585,120,100)
        window.blit(opzioni_puls,(15,585))

        grafico_puls = myfont.render("Grafico",0,(255,255,255))
        rect_grafico = pygame.Rect(5,10,120,30)
        window.blit(grafico_puls,(15,15))

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
                    t = Thread(target=Grafico, args=(theta_max,L,g,))
                    t.start() 
        pygame.display.update()
def Grafico(theta_max,l,g):
    t = numpy.linspace(0, 2*math.pi, 10000)
    θ = theta_max*numpy.cos(math.sqrt(g/l)*t)
    v = -l*numpy.sqrt(g/l)*numpy.sin(numpy.sqrt(g/l)*t)
    a = -l*((numpy.sqrt(g/l))**2)*numpy.cos(numpy.sqrt(g/l)*t)
    plt.xlabel("Tempo (s)")
    plt.ylabel("θ(rad), v(m/s), a(m/s^2)")
    plt.plot(t, θ, "b")
    plt.plot(t, v, "r")
    plt.plot(t, a, "g")
    plt.title('Grafico θ(t), v(t) e a(t)')
    plt.legend(['θ', 'v',"a"])
    plt.show()
opzioni()
