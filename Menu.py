import pygame,sys
from pygame.locals import *
import BuscaMinas
import Interfaz

ANCHO,ALTO = (275,400)
COLOR = (50,60,50)
FOTOGRAMAS = 60

class Bot_Dificultad (Interfaz.Boton) :

	def __init__ (self,*args,**kwargs) :

		super().__init__(*args,**kwargs)

	def eventos (self,events) :

		for event in events :
			if event.type == pygame.MOUSEBUTTONDOWN :
				if event.button == 1 : self.pulsar()

	def pulsar (self) :

		if super().pulsar() :

			BuscaMinas.BuscaMinas(self.texto.texto)

class Menu :

	def __init__ (self) :

		pass

	def iniciar_ventana (self) :

		pygame.display.set_caption("Busca Minas")
		return pygame.display.set_mode((ANCHO,ALTO))

	def start (self) :

		ventana = self.iniciar_ventana()
		pygame.display.set_caption("Busca Minas")
		pygame.display.init()
		pygame.font.init()

		fondo = pygame.image.load("Imagenes/fondo.png"); fondo = pygame.transform.scale(fondo,(ANCHO,ALTO))
		rect_fondo = fondo.get_rect(); rect_fondo.centerx = ANCHO/2; rect_fondo.centery = ALTO/2
		vent = Interfaz.Ventana(pos=(ANCHO/2,ALTO/2+30),dim=(200,250),alpha=50,arrastrar=False)
		fuente_titulo = pygame.font.SysFont('comicsansms',33)
		titulo = Interfaz.Texto(pos=(ANCHO/2,50),texto='BUSCA MINAS',fuente=None,tam=40,color=(200,150,50))
		boton_facil = Bot_Dificultad(pos=(ANCHO/2,ALTO/2-30),dim=(150,30),color=(150,200,200),color_texto=(50,50,50),texto='facil')
		boton_medio = Bot_Dificultad(pos=(ANCHO/2,ALTO/2+30),dim=(150,30),color=(200,200,150),color_texto=(50,50,50),texto='medio')
		boton_dificil = Bot_Dificultad(pos=(ANCHO/2,ALTO/2+90),dim=(150,30),color=(200,150,150),color_texto=(50,50,50),texto='dificil')
		ventanas = [vent]
		botones = [boton_facil,boton_medio,boton_dificil]

		clock = pygame.time.Clock()

		salir = False
		while not salir :

			clock.tick(FOTOGRAMAS)

			# Eventos

			events = pygame.event.get()

			for v in ventanas :
				v.eventos(events)
			for b in botones :
				b.eventos(events)

			for event in events :

				if event.type == pygame.QUIT :
					salir = True
				if event.type == pygame.MOUSEBUTTONDOWN :
					if event.button == 1 :
						self.iniciar_ventana()

			# Actualizamos

			# Dibujamos

			ventana.fill(COLOR)
			#ventana.blit(fondo,rect_fondo)
			vent.dibujar(ventana)
			titulo.dibujar(ventana)
			boton_facil.dibujar(ventana)
			boton_medio.dibujar(ventana)
			boton_dificil.dibujar(ventana)

			# Actualizamos ventana

			pygame.display.update()


if __name__ == '__main__' :

	menu = Menu()
	menu.start()