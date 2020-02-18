import pygame as pg
from pygame.locals import *
import sys
import sqlite3

from entities import *

FPS = 60
WHITE = (255, 255, 255)
YELLOW = (250, 250, 0)


class InicioPantalla:
    def __init__(self):
        self.background_img = pg.image.load('resources/backgrounds/back_space.png').convert() #cargo el fondo
        
        self.font_texto = pg.font.Font('resources/fonts/PressStart2P.ttf', 50) #elijo fuente
        self.texto = self.font_texto.render("LA BÚSQUEDA", True, (WHITE)) #renderizo texto

        self.font_texto_start = pg.font.Font('resources/fonts/PressStart2P.ttf', 20)
        self.texto_start = self.font_texto_start.render("Empezar <espacio>", True, (WHITE))

        #self.music = pg.mixer.Sound('resources/sounds/<SONIDO>')
        

    def draw(self, screen):
        screen.blit(self.background_img, (0, 0)) #pinto el fonfo en las coordenadas elegidas
    
        screen.blit(self.texto, (120, 200)) #pinto el texto en la coordenadas elegidas
        screen.blit(self.texto_start, (400, 550))

    def handleEvents(self, event): #eventos de teclado
        for ev in event.get():
            if ev.type == QUIT: #cerrar la ventana. Hay que ponerlo en cada pantalla porque si lo pongo en el mainloop sólo me hace un evento: o cierra ventana o el handleevent de cada pantalla (lo que ponga antes) 
                pg.quit()
                sys.exit()
            if ev.type == KEYDOWN:
                if ev.key == K_SPACE: #tengo que gestionarlo
                    print("Paso a HistoriaPantalla")
                    #siguiente_pantalla()
    
    #def siguiente_pantalla(self):
     #   return HistoriaPantalla()

    def update(self, dt): #no hace nada pero si no lo pongo se la pega
        pass
       

class HistoriaPantalla: #todo igual que InicioPantalla
    def __init__(self):

        self.background_img = pg.image.load('resources/backgrounds/back_space.png').convert()
       
        self.alto_linea = 25
        self.margen = 6 
        self.font_historia = pg.font.Font('resources/fonts/PressStart2P.ttf', self.alto_linea)   
        
        self.font_saltar_intro = pg.font.Font('resources/fonts/PressStart2P.ttf', 20)
        self.saltar_intro = self.font_saltar_intro.render("Saltar intro <espacio>", True, (WHITE))

        #self.music = pg.mixer.Sound('resources/sounds/<SONIDO>')
        

    def draw(self, screen):
        screen.blit(self.background_img, (0, 0))
        screen.blit(self.saltar_intro, (300, 550))
        
        texto = ["Año 2051. Tras siglos de", 
                 "expolio, el planeta Tierra",
                 "ya no puede proporcionar", 
                 "el hogar que antaño fue",
                 "para los seres humanos.", 
                 "El fin se aproxima y un grupo",
                 "de valientes voluntarias,",
                 "bajo el mando de la capitana",
                 "Zur, emprenden la arriesgada",
                 "misión de encontrar un",
                 "nuevo hogar para la humanidad."]
        
        y = 100
        for linea in texto: #recorro la lista con el texto y voy pintando cada elemento en una linea
            linea_pygame = self.font_historia.render(linea, True, (WHITE))
            screen.blit(linea_pygame, (50, y))
            y += self.alto_linea + self.margen
              

    def handleEvents(self, event):
        for ev in event.get():
            if ev.type == QUIT:
                pg.quit()
                sys.exit()
            if ev.type == KEYDOWN:
                if ev.key == K_SPACE:
                    print("Paso a InstruccionesPantalla")
                    pantantallaActiva = InicioPantalla()

    def update(self, dt):
        pass


class InstruccionesPantalla:
    def __init__(self):

        self.background_img = pg.image.load('resources/backgrounds/back_space.png').convert()
       
        self.alto_linea = 25
        self.margen = 10 
        self.font_instrucciones = pg.font.Font('resources/fonts/PressStart2P.ttf', self.alto_linea)   
        
        self.font_saltar_instr = pg.font.Font('resources/fonts/PressStart2P.ttf', 20)
        self.saltar_instr = self.font_saltar_instr.render("Empezar <espacio>", True, (WHITE))

        #self.music = pg.mixer.Sound('resources/sounds/<SONIDO>')
        

    def draw(self, screen):
        screen.blit(self.background_img, (0, 0))
        screen.blit(self.saltar_instr, (450, 550))
        
        texto = ["Debes evitar colisionar con", 
                 "los asteroides para alcanzar",
                 "la superficie del planeta.", 
                 "Múevete arriba (KEY_UP) y",
                 "abajo (KEY_DOWN), para ello."]
        
        y = 100
        for linea in texto: #recorro la lista con el texto y voy pintando cada elemento en una linea
            linea_pygame = self.font_instrucciones.render(linea, True, (WHITE))
            screen.blit(linea_pygame, (50, y))
            y += self.alto_linea + self.margen
              

    def handleEvents(self, event):
        for ev in event.get():
            if ev.type == QUIT:
                pg.quit()
                sys.exit()
            if ev.type == KEYDOWN:
                if ev.key == K_SPACE:
                    print("Paso a JuegoPantalla")
                    

    def update(self, dt):
        pass


class JuegoPantalla(pg.sprite.Sprite):
    def __init__(self): 
        self.background_img = pg.image.load('resources/backgrounds/back_space.png').convert()
        
        self.score = 0
        self.lives = 1

        self.font_puntos = pg.font.Font('resources/fonts/PressStart2P.ttf', 20)
        self.marcadorP = self.font_puntos.render("Puntos:", True, WHITE)
        self.puntos = self.font_puntos.render("0", True, WHITE)
        self.font_vidas = pg.font.Font('resources/fonts/PressStart2P.ttf', 20)
        self.marcadorV = self.font_vidas.render("Vidas:", True, WHITE)
        self.vidas = self.font_vidas.render(str(self.lives), True, WHITE)
        self.font_gameover = pg.font.Font('resources/fonts/PressStart2P.ttf', 40)
        self.gameover = self.font_gameover.render("GAME OVER", True, YELLOW)
        self.font_continuar = pg.font.Font('resources/fonts/PressStart2P.ttf', 20)
        self.continuar = self.font_continuar.render("Continuar <espacio>", True, WHITE)

        self.current_time = 0 #tiempo que ha pasado desde que se creo el ultimo asteroide
        self.velocidad_nivel = 1 #lo usaré para aumentar la velocidad en los niveles
        self.creation_time = FPS//self.velocidad_nivel#tiempo que tarda en crear un asteroide
        self.level_time = 0 #contador para calcular el timpo que dura la pantalla para cambiar de nivel
        #self.music = pg.mixer.Sound('resources/sounds/<SONIDO>')
        
        self.player_group = pg.sprite.Group() #creo los grupos
        self.enemies_group = pg.sprite.Group()
        self.explosion_group = pg.sprite.Group()
        
        self.nave = Nave() #instancio la nave
        self.player_group.add(self.nave) #la meto en el grupo
        #la explosion y los asteroides no los instancio aqui porque los creo mas adelante
        
    def handleEvents(self, event):
        for ev in event.get():
            if ev.type == QUIT:
                pg.quit()
                sys.exit()
            
            if ev.type == KEYDOWN:
                if ev.key == K_SPACE:
                    if self.lives == 0:
                        print("Continuar Paso a score")      
            
            if ev.type == KEYDOWN:
                if ev.key == K_UP:
                    self.nave.go_up()
                if ev.key == K_DOWN:
                    self.nave.go_down()

        keys_pressed = pg.key.get_pressed()
        if keys_pressed[K_UP]:
            self.nave.go_up()
        if keys_pressed[K_DOWN]:
            self.nave.go_down()  
    
    def update(self, dt):     
        if self.lives > 0 and self.level_time < 3600:#si las vidas > 0 sumo puntos y la duración del juego menor a 1 min
            self.score += 1
            self.puntos = self.font_puntos.render(str(self.score), True, WHITE)
            self.test_collisions()
        
        self.create_asteriod()  #creo asteroides y los meto en enemies_group
        
        for enemy in self.enemies_group: 
            if enemy.rect.x < -40: #si el asteroide de la lista llega a la x-40(se sale de la pantalla), lo elimino del grupo
                self.enemies_group.remove(enemy)
            else:
                enemy.update(dt) #actualizo enemigo    

        for frame in self.explosion_group: #para cada frame del grupo. Si los frames que quedan para terminar son ==1:
            if frame.end_animacion() == 1: #si estoy en el ultimo frame de la animacion (16-15=1)
                self.explosion_group.empty() #vacio el grupo explosion 
                self.player_group.add(self.nave) #meto la nave en su grupo
            frame.update(dt)
        
        self.level_time += 1
        if self.level_time == 3600: #1min(60seg*60vpseg)
            print("paso a la pantalla de la animación")   

    def test_collisions(self):
        colisiones = self.nave.test_collisions(self.enemies_group) #meto en colisiones la lista de enemigos con los que ha colisionado la nave
        for b in colisiones: # si hay colisones (elementos en la lista):
            self.lives -= 1 #resta una vida
            self.vidas = self.font_vidas.render(str(self.lives), True, WHITE)
            self.enemies_group.empty() #vacio el grupo de enemigos
            self.player_group.empty() #vacio el grupo de player
            self.explosion_group.add(Explosion(self.nave.rect.x,self.nave.rect.y)) #instancio una explosion y la añado al grupo explosion

        if self.lives == 0: #si las vidas se acaban, vacio el grupo player
            self.player_group.empty()

    def create_asteriod(self): 
        self.current_time += 1 #el tiempo desde el ultimo asteroide va aumentendo en 1.
        if self.current_time == self.creation_time: #cuando llega al tiempo de cereacion(60)
            self.enemies_group.add(Asteroide(820, self.random_y())) #instancio 1 asteroide y lo meto en su grupo
            self.current_time = 0 #el tiempo vuelve a empezar
            
    def random_y(self): #retorna una posicion 'y' aleatoria en la que crearemos el asteroide
        return random.randint(0,600)
    
    def draw(self, screen):
        screen.blit(self.background_img, (0, 0))
        screen.blit(self.marcadorP, (550, 20))
        screen.blit(self.puntos, (700, 20)) 
        screen.blit(self.marcadorV, (550, 40))
        screen.blit(self.vidas, (700, 40))
        
        self.explosion_group.draw(screen)
        
        for enemy in self.enemies_group:
            screen.blit(enemy.image, enemy.rect)

        if self.lives == 0:
            screen.blit(self.gameover, (210, 300))
            screen.blit(self.continuar, (400, 550))            
        else: 
            self.player_group.draw(screen)


class AnimacionPantalla:
    def __init__(self):
        self.background_img = pg.image.load('resources/backgrounds/back_space.png').convert() #cargo el fondo
        
        self.alto_linea = 25
        self.margen = 10 
        self.font_texto = pg.font.Font('resources/fonts/PressStart2P.ttf', 20) #elijo fuente
        self.texto = self.font_texto.render("", True, (WHITE)) #renderizo texto

        #self.music = pg.mixer.Sound('resources/sounds/<SONIDO>')
        
    def handleEvents(self, event):
        for ev in event.get():
            if ev.type == QUIT:
                pg.quit()
                sys.exit()
    
    def update(self, dt):
        pass

    def draw(self, screen):
        screen.blit(self.background_img, (0, 0)) #pinto el fonfo en las coordenadas elegidas

        texto = ["Capitana Zur: Hemos superado la nube",
                 "              de asteroides.",
                 "              ¡Podemos aterrizar!"]
        
        y = 50
        for linea in texto: #recorro la lista con el texto y voy pintando cada elemento en una linea
            linea_pygame = self.font_texto.render(linea, True, (WHITE))
            screen.blit(linea_pygame, (20, y))
            y += self.alto_linea + self.margen
        
class ScorePantalla:
    def __init__(self):
        self.background_img = pg.image.load('resources/backgrounds/back_space.png').convert()
        
        self.font_puntuacion = pg.font.Font('resources/fonts/PressStart2P.ttf', 28)
        self.puntuacion = self.font_puntuacion.render("Puntuación", True, (WHITE))
        
        self.font_texto_salir = pg.font.Font('resources/fonts/PressStart2P.ttf', 20)
        self.texto_salir = self.font_texto_salir.render("Salir <espacio>", True, (WHITE))

        #self.music = pg.mixer.Sound('resources/sounds/<SONIDO>')
        
        self.alto_linea = 25
        self.margen = 6 
        self.scores = []
        self.read_database() 

    def read_database(self): #leo la base de datos
        conn = sqlite3.connect('data/database.db')
        cursor = conn.cursor()

        rows = cursor.execute('SELECT * from score;')
        self.scores = []
        for row in rows:
            self.scores.append(row)
            
        conn.commit()
        conn.close()  
    '''
    def write_database(self):
        conn = sqlite3.connect('data/database.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO score(name, score) VALUES(?,?)')
        
            
        conn.commit()
        conn.close()          
    '''

    def draw(self, screen):
        screen.blit(self.background_img, (0, 0))
    
        screen.blit(self.puntuacion, (250, 100))
        screen.blit(self.texto_salir, (500, 550))
        
        y = 150 #recorro la base de datos y pinto cada linea
        for row in self.scores:
            row_scores = self.font_puntuacion.render(row[0]+'-'+str(row[1]), True, (WHITE))
            screen.blit(row_scores, (200, y))
            y += self.alto_linea + self.margen     

    def handleEvents(self, event):
        for ev in event.get():
            if ev.type == QUIT:
                pg.quit()
                sys.exit()
            if ev.type == KEYDOWN:
                if ev.key == K_SPACE:
                    print("Paso a InicioPantalla")

    def update(self, dt):
        pass
                  





