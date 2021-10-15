import math, pygame, ctypes, os, sys, runpy, numpy
import matplotlib.pyplot as plt
from threading import Thread
ctypes.windll.shcore.SetProcessDpiAwareness(1)
doc = "Assets\Physics simulator\Teoria\Pendolo di Newton.pdf"

pygame.init()
myfont = pygame.font.SysFont("Bold", 30)
myfont2 = pygame.font.SysFont("Raleway", 50)
myfont3 = pygame.font.SysFont("Raleway", 22)
window = pygame.display.set_mode([1230, 615])

pygame.display.set_caption("Pendolo di Newton")

def opzioni():
    g_input = ""
    L_input = ""
    Omega_input = ""
    n_input = ""
    g_active = False
    L_active = False
    Omega_active = False
    n_active = False
    run = True
    while run:
#colori
        if g_active:
            color1 = (0,0,255)
        if L_active:
            color2 = (0,0,255)
        if Omega_active:
            color3 = (0,0,255)
        if n_active:
            color4 = (0,0,255)
        if not(g_active):
            color1 = (255,255,255)
        if not(L_active):
            color2 = (255,255,255)
        if not(Omega_active):
            color3 = (255,255,255)
        if not(n_active):
            color4 = (255,255,255)

        window.fill((0,0,0))
#Titolo
        titolo = myfont2.render("Pendolo di Newton",0,(255,255,255))
        window.blit(titolo,(455,30))
#Indicazione 1
        ind1 = myfont.render("Inserire il modulo dell'accelerazione gravitazionale in m/s^2:",0,(255,255,255))
        window.blit(ind1,(20,100))
#input box 
        g_text = myfont.render(g_input,0,(255,255,255))
        g_box = pygame.Rect(20,130,560,40)
        pygame.draw.rect(window,color1,g_box,2)
        window.blit(g_text,(30,140))
#indicazione 2
        ind2 = myfont.render("Inserire la lunghezza del filo in m:",0,(255,255,255))
        window.blit(ind2,(20,220))
#input box
        L_text = myfont.render(L_input,0,(255,255,255))
        L_box = pygame.Rect(20,250,560,40)
        pygame.draw.rect(window,color2,L_box,2)
        window.blit(L_text,(30,260))
#indicazione 3
        ind3 = myfont.render("Inserire l'angolo iniziale in gradi:",0,(255,255,255))
        window.blit(ind3,(20,340))
#input box 
        Omega_text = myfont.render(Omega_input,0,(255,255,255))
        Omega_box = pygame.Rect(20,370,560,40)
        pygame.draw.rect(window,color3,Omega_box,2)
        window.blit(Omega_text,(30,380))
#indicazione 
        ind4 = myfont.render("Inserire il numero di masse oscillanti (0<n<5):",0,(255,255,255))
        window.blit(ind4,(20,460))
#input box 
        n_text = myfont.render(n_input,0,(255,255,255))
        n_box = pygame.Rect(20,490,560,40)
        pygame.draw.rect(window,color4,n_box,2)
        window.blit(n_text,(30,500))
        
        if not(checkfloat(n_input)) or not(checkfloat(Omega_input)) or not(checkfloat(L_input)) or not(checkfloat(g_input)):
            error_text = myfont3.render("Inserire i dati e verificare l'assenza di caratteri speciali (escluso “.”) o/e lettere",0,(255,0,0))
            window.blit(error_text,(20,540))

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
                    elif n_active:
                        n_input = n_input[:-1]
                else:
                    if g_active and len(g_input)<=28:
                        g_input += event.unicode
                    elif L_active and len(L_input)<=28:
                        L_input += event.unicode
                    elif Omega_active and len(Omega_input)<=28:
                        Omega_input += event.unicode
                    elif n_active and len(n_input)<=28:
                        n_input += event.unicode
            if event.type == pygame.MOUSEBUTTONDOWN:     
                if rect_enter.collidepoint(pygame.mouse.get_pos()) and checkfloat(g_input) and checkfloat(L_input) and checkfloat(Omega_input) and n_input.isdecimal():
                    if float(L_input)>0 and 0<int(n_input)<5:
                        t0 = pygame.time.get_ticks()
                        simulatore(float(g_input),float(L_input),float(Omega_input),int(n_input),t0)
                elif rect_home.collidepoint(pygame.mouse.get_pos()):
                        runpy.run_path("Physics Motion Simulator.py")
                elif g_box.collidepoint(pygame.mouse.get_pos()):
                    L_active = False
                    Omega_active = False
                    n_active = False
                    g_active = True
                elif L_box.collidepoint(pygame.mouse.get_pos()):
                    g_active = False
                    n_active = False
                    Omega_active = False
                    L_active = True
                elif Omega_box.collidepoint(pygame.mouse.get_pos()):
                    L_active = False
                    g_active = False
                    n_active = False
                    Omega_active = True
                elif n_box.collidepoint(pygame.mouse.get_pos()):
                    L_active = False
                    g_active = False
                    Omega_active = False
                    n_active = True
                else:
                    Omega_active = False
                    L_active = False
                    g_active = False
                    n_active = False
        pygame.display.update()

def checkfloat(number):
    try: 
        float(number)
        return True
    except ValueError:
        return False

def simulatore(g,L,Omega,n,t0):
    theta_max = math.radians(Omega)
    collision = 0
    run = True
    while run:
        time = (pygame.time.get_ticks()-t0)/1000

        theta = theta_max*math.cos(math.sqrt(g/L)*time)
        if math.sin(theta)>0:
            collision = 1
        elif math.sin(theta)<0: 
            collision = 0

        window.fill((0,0,0))
        if collision == 0:
            if n == 1:
                x1 = 555 + 600*math.sin(theta)
                y1 = 600*math.cos(theta)
                x5 = 675
                y5 = 600
                x2 = 585
                y2 = 600
                x3 = 615
                y3 = 600
                x4 = 645
                y4 = 600
            elif n == 2:
                x1 = 555 + 600*math.sin(theta)
                y1 = 600*math.cos(theta)
                x5 = 675
                y5 = 600
                x2 = 585 + 600*math.sin(theta)
                y2 = 600*math.cos(theta)
                x3 = 615
                y3 = 600
                x4 = 645
                y4 = 600
            elif n == 3:
                x1 = 555 + 600*math.sin(theta)
                y1 = 600*math.cos(theta)
                x5 = 675
                y5 = 600
                x2 = 585 + 600*math.sin(theta)
                y2 = 600*math.cos(theta)
                x3 = 615 + 600*math.sin(theta)
                y3 = 600*math.cos(theta)
                x4 = 645
                y4 = 600
            elif n == 4:
                x1 = 555 + 600*math.sin(theta)
                y1 = 600*math.cos(theta)
                x5 = 675
                y5 = 600
                x2 = 585 + 600*math.sin(theta)
                y2 = 600*math.cos(theta)
                x3 = 615 + 600*math.sin(theta)
                y3 = 600*math.cos(theta)
                x4 = 645 + 600*math.sin(theta)
                y4 = 600*math.cos(theta)

        elif collision == 1:
            if n == 1:
                x1 = 555
                y1 = 600
                x5 = 675 + 600*math.sin(theta)
                y5 = 600*math.cos(theta)
                x2 = 585
                y2 = 600
                x3 = 615
                y3 = 600
                x4 = 645
                y4 = 600
            elif n == 2:
                x1 = 555
                y1 = 600
                x5 = 675 + 600*math.sin(theta)
                y5 = 600*math.cos(theta)
                x2 = 585
                y2 = 600
                x3 = 615
                y3 = 600
                x4 = 645 + 600*math.sin(theta)
                y4 = 600*math.cos(theta)
            elif n == 3:
                x1 = 555
                y1 = 600
                x5 = 675 + 600*math.sin(theta)
                y5 = 600*math.cos(theta)
                x2 = 585
                y2 = 600
                x3 = 615 + 600*math.sin(theta)
                y3 = 600*math.cos(theta)
                x4 = 645 + 600*math.sin(theta)
                y4 = 600*math.cos(theta)
            elif n == 4:
                x1 = 555
                y1 = 600
                x5 = 675 + 600*math.sin(theta)
                y5 = 600*math.cos(theta)
                x2 = 585 + 600*math.sin(theta)
                y2 = 600*math.cos(theta)
                x3 = 615 + 600*math.sin(theta)
                y3 = 600*math.cos(theta)
                x4 = 645 + 600*math.sin(theta)
                y4 = 600*math.cos(theta)
#sfera centrale
        pygame.draw.circle(window,(255,255,255),(x3,y3),15.0)
        pygame.draw.line(window,(255,255,255),(615,0),(x3,y3))
#sfera centro-sinistra
        pygame.draw.circle(window,(255,255,255),(x2,y2),15.0)
        pygame.draw.line(window,(255,255,255),(585,0),(x2,y2))
#sfera centro-destra
        pygame.draw.circle(window,(255,255,255),(x4,y4),15.0)
        pygame.draw.line(window,(255,255,255),(645,0),(x4,y4))
#sfera sinistra
        pygame.draw.circle(window,(255,255,255),(x1,y1),15.0)
        pygame.draw.line(window,(255,255,255),(555,0),(x1,y1))
#sfera destra
        pygame.draw.circle(window,(255,255,255),(x5,y5),15.0)
        pygame.draw.line(window,(255,255,255),(675,0),(x5,y5))

        l_filo = myfont.render(("L = {} m".format(round(L,3))),0,(255,255,255))
        T_testo = myfont.render(("T = {} s".format(round(2*math.pi*math.sqrt(L/g),3))),0,(255,255,255))
        angolo_testo = myfont.render(("Omega = {}°".format(round(Omega,2))),0,(255,255,255))

        window.blit(l_filo,(1000,40))
        window.blit(T_testo,(1000,80))
        window.blit(angolo_testo,(1000,120))

#pulsante teoria
        teoria_pulsante = myfont.render("Teoria>>",0,(255,255,255))
        rect_teoria = pygame.Rect(1130,585,100,100)
        window.blit(teoria_pulsante,(1130,585))
#pulsante opzioni
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
                    t = Thread(target=Grafico, args=(L,g,n,))
                    t.start()
        pygame.display.update()

def Grafico(l,g,n):
    t = numpy.linspace(0, 2*math.pi, 10000)
    U = (n*g*l/2)*numpy.cos(numpy.sqrt(g/l)*t)**2
    K = (n*g*l/2)*numpy.sin(numpy.sqrt(g/l)*t)**2
    plt.xlabel("Tempo (s)")
    plt.ylabel("U(J) e K(J)")
    plt.plot(t, U, "b")
    plt.plot(t, K, "r")
    plt.title("Grafico dell'energia potenziale e dell'energia cinetica per m = 1kg")
    plt.legend(["U", "K"])
    plt.show()
opzioni()
