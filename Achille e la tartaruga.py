import pygame, ctypes, os, runpy
ctypes.windll.shcore.SetProcessDpiAwareness(1)
doc = "Assets\Physics simulator\Teoria\Achille e la tartaruga.pdf"


v1 = 10 #pxl/s
v2 = 20 #pxl/s

Achille = pygame.transform.scale(pygame.image.load("Assets\Achille.png"), (60,80))
Tartaruga = pygame.transform.scale(pygame.image.load("Assets\Turtle.png"), (80,60))

pygame.init()
myfont = pygame.font.SysFont("Cambria Math", 30)
myfont2 = pygame.font.SysFont("Raleway",25)
window = pygame.display.set_mode([600,600])
pygame.display.set_icon(pygame.image.load("Assets\Turtle.png"))
pygame.display.set_caption("Paradosso di Zenone")
t0 = pygame.time.get_ticks()
run = True
while run:
    window.fill((255,255,255))
    time = (pygame.time.get_ticks()-t0)/1000
    x1 = 200 + v1*time
    x2 = v2*time
#x1 e x2
    pygame.draw.line(window,(0,0,0),(x1,300),(x1,370))
    pygame.draw.line(window,(0,0,0),(x2,300),(x2,370))

#asse x e punti materiali
    pygame.draw.line(window,(0,0,0),(0,300),(600,300))
 
    x1_testo = myfont.render("X1",0,(0,0,0))
    x2_testo = myfont.render("X2",0,(0,0,0))
#pulsante
    teoria_pulsante = myfont.render("Teoria>>",0,(0,0,0))
    rect_teoria = pygame.Rect(500,550,100,100)
    window.blit(teoria_pulsante,(500,550))
#--------
    window.blit(x1_testo,(x1-20,380))
    window.blit(x2_testo,(x2-20,380))

    window.blit(Achille,(x2-25,220))
    window.blit(Tartaruga,(x1-35,257))

#pulsante per la schermata principale
    home_puls = myfont.render("<<",0,(0,0,0))
    rect_home = pygame.Rect(15,548,40,25)
    pygame.draw.rect(window,(0,0,0),rect_home,2)
    window.blit(home_puls,(25,550))

    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if rect_teoria.collidepoint(pygame.mouse.get_pos()):
                    os.startfile(doc)
            elif rect_home.collidepoint(pygame.mouse.get_pos()):
                        runpy.run_path("Physics Motion Simulator.py")
    pygame.display.update()
pygame.quit()

# 1pxl = 1m