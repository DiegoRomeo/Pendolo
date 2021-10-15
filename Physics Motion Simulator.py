import pygame, ctypes, sys, runpy
ctypes.windll.shcore.SetProcessDpiAwareness(1)

pygame.init()
window = pygame.display.set_mode([1280, 720])
pygame.display.set_icon(pygame.image.load("Assets\Physics.png"))
pygame.display.set_caption("Physics Motion Simulator")
myfont = pygame.font.SysFont("Raleway", 30)
title = pygame.font.SysFont("Lucida Calligraphy", 50)

#Sfondi
Sfondo1 = pygame.transform.smoothscale(pygame.image.load(r"Assets\Physics simulator\Sfondi\Antica Grecia.png").convert_alpha(),(1280,720))
Sfondo2 = pygame.transform.smoothscale(pygame.image.load(r"Assets\Physics simulator\Sfondi\Pisa.png").convert_alpha(), (1280,720))
Sfondo3 = pygame.transform.smoothscale(pygame.image.load(r"Assets\Physics simulator\Sfondi\Cambridge.png").convert_alpha(), (1280,720))
#Personaggi
Newton = pygame.transform.smoothscale(pygame.image.load(r"Assets\Physics simulator\Personaggi\Newton.png").convert_alpha(), (130,200))
Zenone = pygame.transform.smoothscale(pygame.image.load(r"Assets\Physics simulator\Personaggi\Zenone.png").convert_alpha(), (130,200))
Galileo = pygame.transform.smoothscale(pygame.image.load(r"Assets\Physics simulator\Personaggi\Galileo.png").convert_alpha(), (130,200))
#Pulsanti
Pergamena = pygame.transform.smoothscale(pygame.image.load(r"Assets\Physics simulator\Pulsanti\Pergamena.png").convert_alpha(), (300,100))
Pergamena2 = pygame.transform.smoothscale(pygame.image.load(r"Assets\Physics simulator\Pulsanti\Rotolo di pergamena.png").convert_alpha(), (200,120))
Lettera = pygame.transform.smoothscale(pygame.image.load(r"Assets\Physics simulator\Pulsanti\Lettera.png").convert_alpha(), (220,250))
Freccia = pygame.transform.smoothscale(pygame.image.load(r"Assets\Physics simulator\Pulsanti\Freccia.png").convert_alpha(), (70,35))
Opzioni1 = pygame.transform.smoothscale(pygame.image.load(r"Assets\Physics simulator\Pulsanti\Opzioni1.png").convert_alpha(), (100,60))

def Opzioni(m):
    music_deactivated = False
    active_musica = m
    run = True
    while run:
        window.fill((255,255,255))
        window.blit(pygame.transform.rotate(pygame.transform.smoothscale(Freccia,(50,25)),180),(20,20))
        rect_freccia1 = pygame.Rect(20,20,50,25)

        Imp_text = title.render("Impostazioni",0,(0,0,0))
        window.blit(Imp_text,(470,20))
        
        if active_musica:
            color_musica = (0,255,0)
            if music_deactivated:
                pygame.mixer.music.unpause()
                music_deactivated = not(music_deactivated)
                
        else:
            color_musica = (255,0,0)
            if not(music_deactivated):
                pygame.mixer.music.pause()
                music_deactivated = not(music_deactivated)
                

        Musica_rect = pygame.Rect(20,100,100,30)
        pygame.draw.rect(window,color_musica,Musica_rect)
        pygame.draw.rect(window,(0,0,0),Musica_rect,2)
        Musica_button = myfont.render("Musica",0,(0,0,0))
        window.blit(Musica_button,(30,105))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if rect_freccia1.collidepoint(pygame.mouse.get_pos()):
                    Antica_grecia(active_musica) 
                elif Musica_rect.collidepoint(pygame.mouse.get_pos()):
                    active_musica = not(active_musica)
        pygame.display.update()

def Antica_grecia(m):
    if m:
        pygame.mixer.music.load("Assets\Physics simulator\Musiche\Antica Grecia.mp3")
        pygame.mixer.music.play(loops=-1)
    run = True
    while run:
        window.fill((255,255,255))
        window.blit(Sfondo1,(0,0))
        window.blit(Zenone,(575,520))

        window.blit(Opzioni1,(20,20))
        rect_opzioni = pygame.Rect(20,20,100,60)

        window.blit(Freccia,(1180,650))
        rect_freccia2 = pygame.Rect(1180,650,100,35)

        box1 = pygame.Rect(120,180,245,30)
        if box1.collidepoint(pygame.mouse.get_pos()):
            color1 = (255,255,0)
        else:
            color1 = (0,0,0)
        Moto_rett_uni = myfont.render("Moto rettilineo uniforme",0,color1)
        window.blit(Pergamena,(100,145))
        window.blit(Moto_rett_uni,(125,185))

        box2 = pygame.Rect(510,180,245,30)
        if box2.collidepoint(pygame.mouse.get_pos()):
            color2 = (255,255,0)
        else:
            color2 = (0,0,0)
        Moto_circ_uni = myfont.render("Moto circolare uniforme",0,color2)
        window.blit(Pergamena,(490,145))
        window.blit(Moto_circ_uni,(515,185))

        box3 = pygame.Rect(900,180,245,30)
        if box3.collidepoint(pygame.mouse.get_pos()):
            color3 = (255,255,0)
        else:
            color3 = (0,0,0)
        Achille_tart = myfont.render("Achille e la tartaruga",0,color3)
        window.blit(Pergamena,(880,145))
        window.blit(Achille_tart,(905,185))
    
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                sys.exit()
            if keys[pygame.K_RIGHT]:
                Pisa(m)
            if event.type == pygame.MOUSEBUTTONDOWN:     
                if box1.collidepoint(pygame.mouse.get_pos()):
                    runpy.run_path("Moto rettilineo uniforme.py")
                elif box2.collidepoint(pygame.mouse.get_pos()):
                    runpy.run_path("Moto circolare uniforme.py")
                elif box3.collidepoint(pygame.mouse.get_pos()):
                    runpy.run_path("Achille e la tartaruga.py")
                elif rect_freccia2.collidepoint(pygame.mouse.get_pos()):
                    Pisa(m)
                elif rect_opzioni.collidepoint(pygame.mouse.get_pos()):
                    Opzioni(m)
        pygame.display.update()
def Pisa(m):
    if m:
        pygame.mixer.music.load("Assets\Physics simulator\Musiche\Pisa.mp3")
        pygame.mixer.music.play(loops=-1)
    run = True
    while run:
        window.fill((255,255,255))
        window.blit(Sfondo2,(0,0))
        window.blit(Galileo,(575,500))

        window.blit(Freccia,(1180,650))
        rect_freccia2 = pygame.Rect(1180,650,100,35)
        window.blit(pygame.transform.rotate(Freccia,180),(30,650))
        rect_freccia1 = pygame.Rect(30,650,100,50)
#
        box4 = pygame.Rect(77,170,110,30)
        if box4.collidepoint(pygame.mouse.get_pos()):
            color4 = (255,0,255)
        else:
            color4 = (0,0,0)
        Pendolo = myfont.render("Pendolo",0,color4)
        window.blit(Pergamena2,(30,145))
        window.blit(Pendolo,(87,185))
#
        box5 = pygame.Rect(295,150,160,110)
        if box5.collidepoint(pygame.mouse.get_pos()):
            color5 = (255,0,255)
        else:
            color5 = (0,0,0)
        Moto = myfont.render("Moto",0,color5)
        rett = myfont.render("rettilineo",0,color5)
        uni = myfont.render("uniformemente",0,color5)
        acc = myfont.render("accelerato",0,color5)
        window.blit(Pergamena2,(280,145))
        window.blit(Moto,(305,165))
        window.blit(rett,(305,185))
        window.blit(uni,(305,205))
        window.blit(acc,(305,225))
#
        box6 = pygame.Rect(555,150,140,110)
        if box6.collidepoint(pygame.mouse.get_pos()):
            color6 = (255,0,255)
        else:
            color6 = (0,0,0)
        Moto2 = myfont.render("Moto",0,color6)
        bidi = myfont.render("bidimensionale",0,color6)
        uni2 = myfont.render("uniformemente",0,color6)
        acc2 = myfont.render("accelerato",0,color6)
        window.blit(Pergamena2,(540,145))
        window.blit(Moto2,(565,165))
        window.blit(bidi,(565,185))
        window.blit(uni2,(565,205))
        window.blit(acc2,(565,225))

        box7 = pygame.Rect(853,150,90,85)
        if box7.collidepoint(pygame.mouse.get_pos()):
            color7 = (255,0,255)
        else:
            color7 = (0,0,0)
        cad = myfont.render("Caduta",0,color7)
        dei = myfont.render("dei",0,color7)
        gravi = myfont.render("gravi",0,color7)
        window.blit(Pergamena2,(800,145))
        window.blit(cad,(863,175))
        window.blit(dei,(878,195))
        window.blit(gravi,(869,215))
#
        box8 = pygame.Rect(1062,170,170,30)
        if box8.collidepoint(pygame.mouse.get_pos()):
            color8 = (255,0,255)
        else:
            color8 = (0,0,0)
        moto_parab = myfont.render("Moto parabolico",0,color8)
        window.blit(Pergamena2,(1050,145))
        window.blit(moto_parab,(1072,185))

        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                sys.exit()
            if keys[pygame.K_LEFT]:
                Antica_grecia(m)
            if keys[pygame.K_RIGHT]:
                Cambridge(m)
            if event.type == pygame.MOUSEBUTTONDOWN:     
                if box4.collidepoint(pygame.mouse.get_pos()):
                    runpy.run_path("Pendolo.py")
                elif box5.collidepoint(pygame.mouse.get_pos()):
                    runpy.run_path("Moto rettilineo uniformemente accelerato.py")
                elif box6.collidepoint(pygame.mouse.get_pos()):
                    runpy.run_path("Moto bidimensionale uniformemente accelerato.py")
                elif box7.collidepoint(pygame.mouse.get_pos()):
                    runpy.run_path("Caduta dei gravi.py")
                elif box8.collidepoint(pygame.mouse.get_pos()):
                    runpy.run_path("Moto parabolico.py")
                elif rect_freccia1.collidepoint(pygame.mouse.get_pos()):
                    Antica_grecia(m)
                elif rect_freccia2.collidepoint(pygame.mouse.get_pos()):
                    Cambridge(m)
        pygame.display.update()

def Cambridge(m):
    if m:
        pygame.mixer.music.load("Assets\Physics simulator\Musiche\Cambridge.mp3")
        pygame.mixer.music.play(loops=-1)
    run = True
    while run:
        window.fill((255,255,255))
        window.blit(Sfondo3,(0,0))
        window.blit(Newton,(575,500))

        window.blit(pygame.transform.rotate(Freccia,180),(30,650))
        rect_freccia1 = pygame.Rect(30,650,100,50)

        box9 = pygame.Rect(145,150,90,95)
        if box9.collidepoint(pygame.mouse.get_pos()):
            color9 = (255,0,0)
        else:
            color9 = (0,0,0)
        Pend = myfont.render("Pendolo",0,color9)
        di = myfont.render("di",0,color9)
        Newt = myfont.render("Newton",0,color9)
        window.blit(Lettera,(100,145))
        window.blit(Pend,(155,185))
        window.blit(di,(185,205))
        window.blit(Newt,(155,225))
#
        box10 = pygame.Rect(545,150,180,70)
        if box10.collidepoint(pygame.mouse.get_pos()):
            color10 = (255,0,0)
        else:
            color10 = (0,0,0)
        urto = myfont.render("Urto",0,color10)
        unid = myfont.render("unidimensionale",0,color10)
        window.blit(Lettera,(530,145))
        window.blit(urto,(615,185))
        window.blit(unid,(555,205))

        box11 = pygame.Rect(968,180,200,80)
        if box11.collidepoint(pygame.mouse.get_pos()):
            color11 = (255,0,0)
        else:
            color11 = (0,0,0)
        Moto = myfont.render("Moto",0,color11)
        rett = myfont.render("rettilineo",0,color11)
        smo = myfont.render("smorzato",0,color11)
        esp = myfont.render("esponenzialmente",0,color11)
        window.blit(Lettera,(960,145))
        window.blit(Moto,(1045,185))
        window.blit(rett,(1025,205))
        window.blit(smo,(1025,225))
        window.blit(esp,(978,245))

        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                sys.exit()
            if keys[pygame.K_LEFT]:
                Pisa(m)
            if event.type == pygame.MOUSEBUTTONDOWN:     
                if box9.collidepoint(pygame.mouse.get_pos()):
                    runpy.run_path("Pendolo di Newton.py")    
                elif box10.collidepoint(pygame.mouse.get_pos()):
                    runpy.run_path("Urto unidimensionale.py")     
                elif box11.collidepoint(pygame.mouse.get_pos()):
                    runpy.run_path("Moto rettilineo smorzato esponenzialmente.py")
                elif rect_freccia1.collidepoint(pygame.mouse.get_pos()):
                    Pisa(m)
        pygame.display.update()
Antica_grecia(True)

#streamlit
#heroku
#x = l*cos(alfa); y = l*sin(alfa); cateto = h*cot(alfa)
#teoria
#simulazione iniziale
#grafici