import pygame,math,random
from pygame.locals import *

class Boton :

	def __init__ (self,pos=(0,0),dim=(100,20),color=(255,255,255),color_texto=(0,0,0),texto='boton',fuente=None,tam=30,bold=False,italic=False,visible=True) :

		self.rect = pygame.Rect(0,0,*list(dim))
		self.rect.center = pos
		self.color = color
		self.color_texto = color_texto
		self.texto = Texto(pos=self.rect.center,texto=texto,fuente=fuente,tam=tam,color=color_texto,bold=bold,italic=italic)
		self.tam = tam
		self.visible = visible

	def eventos (self,events) :

		pass

	def tocar (self,pos) :

		if pos[0] >= self.rect.left and pos[0] < self.rect.right :
			if pos[1] >= self.rect.top and pos[1] < self.rect.bottom :
				return True
		return False

	def pulsar (self) :

		raton = pygame.mouse.get_pos()

		if self.tocar(raton) : return True
		return False

	def actualizar (self) :

		self.texto.actualizar(pos=self.rect.center)

	def dibujar (self,ventana) :

		if not self.visible : return
		pygame.draw.rect(ventana,self.color,self.rect)
		self.texto.dibujar(ventana)

class Ventana :

	def __init__ (self,pos=[10,10],dim=(20,20),color=(0,0,0),alpha=150,visible=True,arrastrar=True) :

		self.surface = pygame.Surface(dim); self.surface.fill(color); self.surface.set_alpha(alpha)
		self.rect = self.surface.get_rect(); self.rect.center = pos
		self.df = (0,0)
		self.arr = False
		self.visible = visible
		self.arrastrar = arrastrar

	def tocar (self,pos) :

		if not self.visible : return False

		if pos[0] >= self.rect.left and pos[0] < self.rect.right :
			if pos[1] >= self.rect.top and pos[1] < self.rect.bottom :
				return True
		return False

	def eventos (self,events) :

		for event in events :
			if event.type == pygame.MOUSEBUTTONDOWN :
				if event.button == 1 : self.pulsar()
			if event.type == pygame.MOUSEBUTTONUP :
				if event.button == 1 : self.soltar()

	def pulsar (self) :

		raton = pygame.mouse.get_pos()

		if not self.arrastrar : return

		if self.tocar(raton) :
			self.df = (raton[0]-self.rect.centerx,raton[1]-self.rect.centery)
			self.arr = True
			return True
		return False

	def soltar (self) :

		if not self.arrastrar : return

		self.arr = False

	def actualizar (self) :

		self.arrastrar_ventana()

	def arrastrar_ventana (self) :

		if not self.arrastrar or not self.visible : return

		raton = pygame.mouse.get_pos()
		if self.arr : self.rect.centerx = raton[0] - self.df[0]; self.rect.centery  = raton[1] - self.df[1]

	def dibujar (self,ventana) :

		if self.visible :
			ventana.blit(self.surface,(self.rect.left,self.rect.top))

class Texto :

	def __init__ (self,pos=(0,0),texto='',fuente=None,tam=30,color=(255,255,255),bold=False,italic=False) :

		self.pos = pos; self.texto = texto; self.fuent = fuente; self.tam = tam; self.color = color; self.bold = bold; self.italic = italic
		self.act_texto()

	def actualizar (self,pos=None,texto=None,fuente=None,tam=None,color=None,bold=None,italic=None) :

		if pos : self.pos = pos
		if texto : self.texto = texto
		if fuente : self.fuent = fuente
		if tam : self.tam = tam
		if color : self.color = color
		if bold : self.bold = bold
		if italic : self.italic = italic
		self.act_texto()

	def act_texto (self) :

		self.fuente = pygame.font.SysFont(self.fuent,self.tam,bold=self.bold,italic=self.italic)
		self.txt = self.fuente.render(self.texto,0,self.color)
		self.rect = self.txt.get_rect()
		self.rect.center = self.pos

	def dibujar (self,ventana) :

		ventana.blit(self.txt,self.rect)