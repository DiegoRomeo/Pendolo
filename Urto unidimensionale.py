import pygame, ctypes, sys, os, runpy, numpy
import matplotlib.pyplot as plt
from threading import Thread
ctypes.windll.shcore.SetProcessDpiAwareness(1)
doc = r"Assets\Physics simulator\Teoria\Urti unidimensionali.pdf"
pygame.init()
myfont = pygame.font.SysFont("Raleway", 30)
myfont2 = pygame.font.SysFont("Lucida Handwriting", 40)
myfont3 = pygame.font.SysFont("Raleway", 25)
window = pygame.display.set_mode([1000,800])
pygame.display.set_caption("Urto unidimensionale")

def opzioni():
    m1_input = ""
    v1_input = ""
    m2_input = ""
    v2_input = ""
    e_input = ""
    m1_active = False
    v1_active = False
    m2_active = False
    v2_active = False
    e_active = False
    run = True
    while run:
#colori
        if m1_active:
            color1 = (0,0,255)
        if v1_active:
            color2 = (0,0,255)
        if m2_active:
            color3 = (0,0,255)
        if v2_active:
            color4 = (0,0,255)
        if e_active:
            color5 = (0,0,255)
        if not(m1_active):
            color1 = (255,255,255)
        if not(v1_active):
            color2 = (255,255,255)
        if not(m2_active):
            color3 = (255,255,255)
        if not(v2_active):
            color4 = (255,255,255)
        if not(e_active):
            color5 = (255,255,255)

        window.fill((0,0,0))
#Titolo
        titolo = myfont2.render("Urto unidimensionale",0,(255,255,255))
        window.blit(titolo,(250,30))
#Indicazione 1
        ind1 = myfont.render("Inserire la massa n.1 in kg:",0,(255,255,255))
        window.blit(ind1,(20,100))
#input box per la velocità orizzontale
        m1_text = myfont.render(m1_input,0,(255,255,255))
        m1_box = pygame.Rect(20,130,560,40)
        pygame.draw.rect(window,color1,m1_box,2)
        window.blit(m1_text,(30,140))
#indicazione 2
        ind2 = myfont.render("Inserire il modulo della velocità della massa n.1 in m/s:",0,(255,255,255))
        window.blit(ind2,(20,220))
#input box per la velocità verticale
        v1_text = myfont.render(v1_input,0,(255,255,255))
        v1_box = pygame.Rect(20,250,560,40)
        pygame.draw.rect(window,color2,v1_box,2)
        window.blit(v1_text,(30,260))
#indicazione 3
        ind3 = myfont.render("Inserire la massa n.2 in kg:",0,(255,255,255))
        window.blit(ind3,(20,340))
#input box
        m2_text = myfont.render(m2_input,0,(255,255,255))
        m2_box = pygame.Rect(20,370,560,40)
        pygame.draw.rect(window,color3,m2_box,2)
        window.blit(m2_text,(30,380))
#indicazione 4
        ind4 = myfont.render("Inserire il modulo della velocità della massa n.2 in m/s:",0,(255,255,255))
        window.blit(ind4,(20,460))
#input box 
        v2_text = myfont.render(v2_input,0,(255,255,255))
        v2_box = pygame.Rect(20,490,560,40)
        pygame.draw.rect(window,color4,v2_box,2)
        window.blit(v2_text,(30,500))
#indicazione 5
        ind5 = myfont.render("Inserire il valore del coefficiente di restituizione (0<=e<=1):",0,(255,255,255))
        window.blit(ind5,(20,580))
#input box 
        e_text = myfont.render(e_input,0,(255,255,255))
        e_box = pygame.Rect(20,610,560,40)
        pygame.draw.rect(window,color5,e_box,2)
        window.blit(e_text,(30,620))

        if not(checkfloat(m1_input)) or not(checkfloat(m2_input)) or not(checkfloat(v1_input)) or not(checkfloat(v2_input)) or not(checkfloat(e_input)):
            error_text = myfont3.render("Inserire i dati e verificare l'assenza di caratteri speciali (escluso “.”) o/e lettere",0,(255,0,0))
            window.blit(error_text,(20,660))

#tasto enter
        Enter_text = myfont.render(">>",0,(255,255,255))
        rect_enter = pygame.Rect(940,748,40,25)
        pygame.draw.rect(window,(255,255,255),rect_enter,2)
        window.blit(Enter_text,(950,750))

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
                    if m1_active:
                        m1_input = m1_input[:-1]
                    elif v1_active:
                        v1_input = v1_input[:-1]
                    elif m2_active:
                        m2_input = m2_input[:-1]
                    elif v2_active:
                        v2_input = v2_input[:-1]
                    elif e_active:
                        e_input = e_input[:-1]
                else:
                    if m1_active and len(m1_input)<=28:
                        m1_input += event.unicode
                    elif v1_active and len(v1_input)<=28:
                        v1_input += event.unicode
                    elif m2_active and len(m2_input)<=28:
                        m2_input += event.unicode
                    elif v2_active and len(v2_input)<=28:
                        v2_input += event.unicode
                    elif e_active and len(e_input)<=28:
                        e_input += event.unicode
            if event.type == pygame.MOUSEBUTTONDOWN:     
                if rect_enter.collidepoint(pygame.mouse.get_pos()) and checkfloat(m1_input) and checkfloat(v1_input) and checkfloat(m2_input) and checkfloat(v2_input) and checkfloat(e_input):
                    if (float(m1_input)+float(m2_input))>0 and float(v1_input)>0 and float(v2_input)>0 and 0<=float(e_input)<=1:
                        t0 = pygame.time.get_ticks()
                        simulatore(float(m1_input),float(v1_input),float(m2_input),-float(v2_input),float(e_input),t0)
                elif rect_home.collidepoint(pygame.mouse.get_pos()):
                        runpy.run_path("Physics Motion Simulator.py")
                elif m1_box.collidepoint(pygame.mouse.get_pos()):
                    e_active = False
                    v2_active = False
                    m2_active = False
                    v1_active = False
                    m1_active = True
                elif v1_box.collidepoint(pygame.mouse.get_pos()):
                    e_active = False
                    v2_active = False
                    m2_active = False
                    m1_active = False
                    v1_active = True
                elif m2_box.collidepoint(pygame.mouse.get_pos()):
                    e_active = False
                    v2_active = False
                    v1_active = False
                    m1_active = False
                    m2_active = True
                elif v2_box.collidepoint(pygame.mouse.get_pos()):
                    e_active = False
                    m2_active = False
                    v1_active = False
                    m1_active = False
                    v2_active = True
                elif e_box.collidepoint(pygame.mouse.get_pos()):
                    v2_active = False
                    m2_active = False
                    v1_active = False
                    m1_active = False
                    e_active = True
                else:
                    e_active = False
                    m1_active = False
                    v1_active = False
                    m2_active = False
                    v2_active = False
        pygame.display.update()

def checkfloat(number):
    try: 
        float(number)
        return True
    except ValueError:
        return False

def simulatore(m1,v1,m2,v2,e,t0):
    x1 = 0
    x2 = 900
    collision = 0
    v1f = ((m1-e*m2)*v1 + m2*v2*(1+e))/(m1+m2)
    v2f = ((m2-e*m1)*v2 + m1*v1*(1+e))/(m1+m2)
    run = True
    while run:
        time = (pygame.time.get_ticks()-t0)/1000
        if abs(x2-x1)>100 and collision ==0:
            x1 = v1*time
            x2 = 900+v2*time
            a = x1
            b = x2
        elif collision == 1:
            if x1>=0 and x2<=900:
                x1 = a+v1f*(time-c)
                x2 = b+v2f*(time-c)
        else:
            collision = 1
            c = (pygame.time.get_ticks()-t0)/1000


        window.fill((255,255,255))
        pygame.draw.rect(window,(0,0,255),(x1,150,100,100),0)
        pygame.draw.rect(window,(255,0,0),(x2,150,100,100),0)

        m1_text = myfont.render(("m1"),0,(255,255,255))
        m2_text = myfont.render(("m2"),0,(255,255,255))

        pygame.draw.rect(window,(0,0,0),(0,485,1000,315),0)
        v1f_text = myfont.render("v1f = {} m/s".format(round(v1f,3)),0,(255,255,255))
        v2f_text = myfont.render("v2f = {} m/s".format(round(v2f,3)),0,(255,255,255))
        indicazione = myfont.render("Con v1f e v2f si intendono le velocità, dopo la collisione, delle rispettive masse.",0,(255,255,255))

        window.blit(v1f_text,(15,500))
        window.blit(v2f_text,(15,530))
        window.blit(indicazione,(15,570))

        window.blit(m1_text,(x1+30,170))
        window.blit(m2_text,(x2+30,170))
  
#pulsante teoria
        teoria_pulsante = myfont.render("Teoria>>",0,(255,255,255))
        rect_teoria = pygame.Rect(900,770,100,100)
        window.blit(teoria_pulsante,(900,770))
#pulsante opzioni
        opzioni_puls = myfont.render("<<Parametri",0,(255,255,255))
        rect_opzioni = pygame.Rect(15,770,120,100)
        window.blit(opzioni_puls,(15,770))

        grafico_puls = myfont.render("Grafico",0,(0,0,0))
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
                    t = Thread(target=Grafico, args=(v1,v2,v1f,v2f,))
                    t.start()
        pygame.display.update()

def Grafico(v1,v2,v1f,v2f):
    t_collision = (-900)/(v2-v1)
    t = numpy.linspace(0, 2*t_collision, 600) 
    plt.xlabel("Tempo (s)")
    plt.ylabel("Velocità (m/s)")
    plt.plot(t, numpy.piecewise(t, [t < t_collision,t > t_collision],[v1,v1f]))
    plt.plot(t, numpy.piecewise(t, [t < t_collision,t > t_collision],[v2,v2f]))
    plt.title('Grafico velocità-tempo')
    plt.legend(["v1","v2"])
    plt.show()

opzioni()