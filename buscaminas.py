import pygame,sys,random,math,copy,time
from pygame.locals import *
import interfaz

ANCHO,ALTO = (500,600)
COLOR = (130,150,130)
FOTOGRAMAS = 60

MINA = 100

class Niveles :

	def __init__ (self,dim=10,n_minas=20,ancho=500) :

		self.ANCHO = ancho
		self.ALTO = ancho
		self.n_minas = n_minas
		self.dim = dim
		self.anch = round(ancho/dim)

dificultad = {"facil":Niveles(dim=8,n_minas=10,ancho=480),"medio":Niveles(dim=14,n_minas=40,ancho=560),"dificil":Niveles(dim=20,n_minas=99,ancho=560)}

def init_tabla (dim,n_minas) :

	tabla=[]
	for i in range(dim) : tabla.append([0]*dim)
	for m in range(n_minas) :
		while True :
			fila = random.randint(0,dim-1); columna = random.randint(0,dim-1)
			if tabla[fila][columna]!=MINA : tabla[fila][columna]=MINA; break
	for f in range(dim) :
		for c in range(dim) :
			if tabla[f][c] == MINA : continue
			for i in [-1,0,1] :
				for j in [-1,0,1] :
					if f+i < 0 or f+i >= dim or c+j < 0 or c+j >= dim : continue
					if tabla[f+i][c+j] == MINA : tabla[f][c] += 1
	return tabla

class Vent_MinasRestantes (interfaz.Ventana) :

	def __init__ (self,*args,**kwargs) :

		super().__init__(*args,**kwargs)

		self.n_minas = 0
		self.texto_P = interfaz.Texto(pos=(self.rect.centerx+25,self.rect.centery),texto='P',fuente=None,tam=30,color=(250,50,50)) 
		self.texto_nminas = interfaz.Texto(pos=(self.rect.centerx-15,self.rect.centery),texto=str(self.n_minas),fuente=None,tam=30,color=(255,255,255))

	def actualizar (self) :

		if not self.visible : return
		super().actualizar()
		self.texto_P.actualizar(pos=(self.rect.centerx+25,self.rect.centery))
		self.texto_nminas.actualizar(pos=(self.rect.centerx-15,self.rect.centery),texto=str(self.n_minas))

	def dibujar (self,ventana) :

		if not self.visible : return
		super().dibujar(ventana)
		self.texto_P.dibujar(ventana)
		self.texto_nminas.dibujar(ventana)

class Vent_Cronometro (interfaz.Ventana) :

	def __init__ (self,*args,**kwargs) :

		super().__init__(*args,**kwargs)
		self.timeInit = 0

	def dibujar (self,ventana) :

		if not self.visible : return
		super().dibujar(ventana)
		txt = ticks_texto(pygame.time.get_ticks()-self.timeInit)
		fuente = pygame.font.Font(None,30); texto = fuente.render(txt,0,(255,255,255))
		rect = texto.get_rect(); rect.center = self.rect.center
		ventana.blit(texto,rect)

class Vent_Pausa (interfaz.Ventana) :

	def __init__ (self,*args,**kwargs) :

		super().__init__(*args,**kwargs)
		self.bot_continuar = interfaz.Boton(pos=(self.rect.centerx,self.rect.centery-20),dim=(150,30),color=(100,175,100),color_texto=(255,255,255),texto='Continuar',tam=30)
		self.bot_salir = interfaz.Boton(pos=(self.rect.centerx,self.rect.centery+20),dim=(150,30),color=(175,100,100),color_texto=(255,255,255),texto='Salir',tam=30)
		self.salir = False

	def eventos (self,events) :

		if not self.visible : return
		super().eventos(events)
		for event in events :
			if event.type == pygame.MOUSEBUTTONDOWN :
				if event.button == 1 :
					if self.bot_continuar.pulsar() : self.poner_pausa()
					if self.bot_salir.pulsar() : self.salir = True

	def poner_pausa (self) :

		self.visible = not self.visible
		self.arr = False

	def actualizar (self) :

		if not self.visible : return
		super().actualizar()
		self.bot_continuar.rect.center = (self.rect.centerx,self.rect.centery-20)
		self.bot_salir.rect.center = (self.rect.centerx,self.rect.centery+20)
		self.bot_continuar.actualizar()
		self.bot_salir.actualizar()

	def dibujar (self,ventana) :

		if not self.visible : return
		super().dibujar(ventana)
		self.bot_continuar.dibujar(ventana)
		self.bot_salir.dibujar(ventana)

class Vent_GanarJuego (interfaz.Ventana) :

	def __init__ (self,*args,**kwargs) :

		super().__init__(*args,**kwargs)
		self.bot_salir = interfaz.Boton(pos=(self.rect.centerx,self.rect.centery+20),dim=(150,30),color=(175,100,100),color_texto=(255,255,255),texto='Salir',tam=30)
		self.titulo = interfaz.Texto(pos=(self.rect.centerx,self.rect.centery-60),texto='¡¡¡Felicidades!!!',fuente=None,tam=60,color=(255,255,255))
		self.texto_duracion = interfaz.Texto(pos=(self.rect.centerx-120,self.rect.centery+90),texto='Tiempo:',fuente=None,tam=35,color=(255,255,255))
		self.duracion = interfaz.Texto(pos=(self.rect.centerx-10,self.rect.centery+90),texto='',fuente=None,tam=40,color=(200,200,100))
		self.salir = False
		self.tiempo_fin = 0

	def eventos (self,events) :

		if not self.visible : return
		super().eventos(events)
		for event in events :
			if event.type == pygame.MOUSEBUTTONDOWN :
				if event.button == 1 :
					if self.bot_salir.pulsar() : self.salir = True

	def dibujar (self,ventana) :

		if not self.visible : return
		super().dibujar(ventana)
		self.titulo.dibujar(ventana)
		self.texto_duracion.dibujar(ventana)
		self.duracion.actualizar(texto=ticks_texto(self.tiempo_fin))
		self.duracion.dibujar(ventana)
		self.bot_salir.dibujar(ventana)

class Vent_PerderJuego (interfaz.Ventana) :

	def __init__ (self,*args,**kwargs) :

		super().__init__(*args,**kwargs)
		self.bot_salir = interfaz.Boton(pos=(self.rect.centerx,self.rect.centery+20),dim=(150,30),color=(175,100,100),color_texto=(255,255,255),texto='Salir',tam=30)
		self.titulo = interfaz.Texto(pos=(self.rect.centerx,self.rect.centery-60),texto='FIN',fuente=None,tam=100,color=(255,255,255))
		self.titulo2 = interfaz.Texto(pos=(self.rect.centerx,self.rect.centery+80),texto='Has sido explotado por una mina!!!',fuente=None,tam=30,color=(210,180,180))
		self.salir = False

	def eventos (self,events) :

		if not self.visible : return
		super().eventos(events)
		for event in events :
			if event.type == pygame.MOUSEBUTTONDOWN :
				if event.button == 1 :
					if self.bot_salir.pulsar() : self.salir = True

	def dibujar (self,ventana) :

		if not self.visible : return
		super().dibujar(ventana)
		self.bot_salir.dibujar(ventana)
		self.titulo.dibujar(ventana)
		self.titulo2.dibujar(ventana)

class Casilla :

	COLOR_TOCANDO = (150,200,150)
	COLOR_LINEA = (50,80,50)
	ANCH_LINEA = 3

	colores = {(False,0):(100,150,100),(False,1):(100,200,100),(True,0):(170,150,120),(True,1):(200,180,150)}
	colores_texto = {0:(0,0,0),1:(100,100,200),2:(100,200,100),3:(200,100,100),4:(200,100,200),5:(200,200,100),6:(100,200,200),7:(100,100,100),8:(0,255,0),MINA:(255,0,0)}

	def __init__ (self,valor=0,pos=(0,0),dim=(50,50),visible=False,color=0) :

		self.valor = valor
		self.pos = tuple(pos)
		self.dim = tuple(dim)
		self.visible = False
		self.color = color
		self.rect = pygame.Rect(*pos,*dim)
		self.rect.center = pos
		self.tocando = False
		self.marcado = False
		self.bordes = {"top":False,"bottom":False,"left":False,"right":False}
		self.pos_lineas = {"top":((0,0),(1,0)),"bottom":((0,1),(1,1)),"left":((0,0),(0,1)),"right":((1,0),(1,1))}
		self.texto_bandera = interfaz.Texto(pos=self.rect.center,texto='P',fuente=None,tam=self.rect.width,color=(250,50,50))
		txt = str(self.valor)
		if self.valor == MINA : txt = 'X'
		self.texto_valor = interfaz.Texto(pos=self.rect.center,texto=txt,fuente=None,tam=self.rect.width,color=self.colores_texto[self.valor])

		self.sonido_pulsar = pygame.mixer.Sound("Sonidos/pulsar.aiff")
		self.sonido_marcar = pygame.mixer.Sound("Sonidos/marcar.aiff")
		self.sonido_fallar = pygame.mixer.Sound("Sonidos/fallar.aiff")

	def tocar (self,pos) :

		if pos[0] >= self.rect.left and pos[0] < self.rect.right :
			if pos[1] >= self.rect.top and pos[1] < self.rect.bottom :
				return True
		return False

	def on_visible (self) :

		if self.valor != MINA : self.sonido_pulsar.play()
		else : self.sonido_fallar.play()
		self.visible = True

	def on_marcar (self) :

		self.sonido_marcar.play()
		self.marcado = not self.marcado

	def pulsar (self) :

		raton = pygame.mouse.get_pos()
		if self.tocar(raton) and not self.visible : self.on_visible()

	def marcar (self) :

		if self.visible : return
		raton = pygame.mouse.get_pos()
		if self.tocar(raton) : self.on_marcar()

	def actualizar (self) :

		raton = pygame.mouse.get_pos()

		if self.visible : self.marcado = False
		if self.tocar(raton) : self.tocando = True
		else : self.tocando = False 

	def dibujar (self,ventana) :

		c = self.colores[(self.visible,self.color)]
		if not self.visible :
			if self.tocando : c = self.COLOR_TOCANDO
		pygame.draw.rect(ventana,c,self.rect)
		if not self.visible and self.marcado :
			self.texto_bandera.dibujar(ventana)
		if self.visible and self.valor != 0 :
			self.texto_valor.dibujar(ventana)

	def dibujar_lineas (self,ventana) :

		for i in ("top","bottom","left","right") :
			if self.bordes[i] :
				pos1 = list(self.pos_lineas[i][0]); pos1[0] = self.rect.left + pos1[0]*self.rect.width; pos1[1] = self.rect.top + pos1[1]*self.rect.height
				pos2 = list(self.pos_lineas[i][1]); pos2[0] = self.rect.left + pos2[0]*self.rect.width; pos2[1] = self.rect.top + pos2[1]*self.rect.height
				pygame.draw.line(ventana,self.COLOR_LINEA,pos1,pos2,self.ANCH_LINEA)

def actualizar_casillas (casillas) :

	for i in range(1) :
		ceros_visibles(casillas)

	for f in range(len(casillas)) :
		for c in range(len(casillas[f])) :
			casilla = casillas[f][c]
			if casilla.visible :
				for cas in casilla.bordes :
					casilla.bordes[cas] = False
				continue
			if c-1 >= 0 :
				if casillas[f][c-1].visible : casilla.bordes["top"] = True
				else : casilla.bordes["top"] = False
			if f-1 >= 0 :
				if casillas[f-1][c].visible : casilla.bordes["left"] = True
				else : casilla.bordes["left"] = False
			if c+1 < len(casillas[f]) :
				if casillas[f][c+1].visible : casilla.bordes["bottom"] = True
				else : casilla.bordes["bottom"] = False
			if f+1 < len(casillas) :
				if casillas[f+1][c].visible : casilla.bordes["right"] = True
				else : casilla.bordes["right"] = False

def ceros_visibles (casillas) :

	for f in range(len(casillas)) :
		for c in range(len(casillas[f])) :
			casilla = casillas[f][c]
			if casilla.valor == 0 and casilla.visible :
				tocar_cero(casillas,f,c)

def tocar_cero (casillas,fila,columna) :

	for i in (-1,0,1) :
		for j in (-1,0,1) :
			if i == 0 and j == 0 : continue
			auxf = fila+i; auxc = columna+j
			if auxf >= 0 and auxf < len(casillas) and auxc >= 0 and auxc < len(casillas) :
				casillas[auxf][auxc].visible = True

def init_casillas (dif) :

	d = dificultad[dif]

	casillas = []
	tabla = init_tabla(d.dim,d.n_minas)
	dim = d.dim
	anch = d.anch
	for i in range(dim) :
		fila = []
		for j in range(dim) :
			x = round(i*anch+(anch/2)); y = round(j*anch+(anch/2)+(d.ALTO-d.ANCHO))
			color = 0
			if j % 2 == 0 and i % 2 != 0 : color = 1
			if j % 2 != 0 and i % 2 == 0 : color = 1
			fila.append(Casilla(valor=tabla[i][j],pos=(x,y),dim=(anch,anch),color=color,visible=False))
		casillas.append(copy.copy(fila))

	return casillas

def no_marcar_casilla (casillas) :

	for fila in casillas :
		for casilla in fila :
			casilla.tocando = False

def casillas_marcadas (casillas) :

	m = 0
	for fila in casillas :
		for casilla in fila :
			if casilla.marcado : m += 1
	return m

def ganar_juego (n_minas,casillas) :

	minas_ocultas = 0
	for fila in casillas :
		for casilla in fila :
			if not casilla.visible :
				if casilla.valor != MINA : return False
				minas_ocultas += 1
	if minas_ocultas == n_minas : return True
	return False

def morir (casillas) :

	for fila in casillas :
		for casilla in fila :
			if casilla.valor == MINA and casilla.visible : return True
	return False

def ocultar_ventanas (ventanas) :

	for ventana in ventanas :
		ventana.visible = False

def ticks_texto (ticks) :

	segundos_totales = round(ticks/1000)
	minutos = int(segundos_totales/60); segundos = segundos_totales - minutos*60
	txt_min = str(minutos); txt_seg = str(segundos)
	if minutos < 10 : txt_min = '0' + txt_min
	if segundos < 10 : txt_seg = '0' + txt_seg
	return txt_min + ":" + txt_seg

def BuscaMinas (dif) :

	# Creamos ventana

	d = dificultad[dif]
	ANCHO = d.ANCHO
	ALTO = d.ALTO

	ventana = pygame.display.set_mode((d.ANCHO,d.ALTO))
	pygame.display.set_caption("Busca Minas")
	pygame.display.init()
	pygame.font.init()
	pygame.display.update()
	pygame.mixer.init()

	casillas = init_casillas(dif)
	vent_minas_restantes = Vent_MinasRestantes(pos=(70,30),dim=(120,25))
	vent_cronometro = Vent_Cronometro(pos=(70,60),dim=(120,25)); vent_cronometro.timeInit = pygame.time.get_ticks()
	vent_pausa = Vent_Pausa(pos=(d.ANCHO/2,d.ALTO/2),dim=(300,180),visible=False,arrastrar=True)
	vent_ganarjuego = Vent_GanarJuego(pos=(d.ANCHO/2,d.ALTO/2),dim=(425,300),alpha=200,visible=False,arrastrar=False)
	vent_perderjuego = Vent_PerderJuego(pos=(d.ANCHO/2,d.ALTO/2),dim=(425,300),alpha=200,visible=False,arrastrar=False)
	ventanas = [vent_minas_restantes,vent_cronometro,vent_pausa,vent_ganarjuego,vent_perderjuego]
	pausa = False
	en_juego = True

	# Bucle principal

	clock = pygame.time.Clock()
	SALIR = False
	while not SALIR :

		clock.tick(FOTOGRAMAS)

		# Eventos

		events = pygame.event.get()

		for v in ventanas : v.eventos(events)

		if vent_pausa.salir : break
		if vent_ganarjuego.salir : break
		if vent_perderjuego.salir : break

		for event in events :
			if event.type == pygame.QUIT :
				SALIR = True
				break
			if event.type == pygame.MOUSEBUTTONDOWN :
				if event.button == 1 :
					aux = True
					for v in ventanas :
						if v.tocar(pygame.mouse.get_pos()) : aux = False
					if pausa : aux = False
					if not en_juego : aux = False
					if aux :
						for fila in casillas :
							for casilla in fila :
								casilla.pulsar()
				elif event.button == 3 :
					aux = True
					for v in ventanas :
						if v.tocar(pygame.mouse.get_pos()) : aux = False
					if pausa : aux = False
					if not en_juego : aux = False
					if aux :
						for fila in casillas :
							for casilla in fila :
								casilla.marcar()
			if event.type == pygame.KEYDOWN :
				if event.key == pygame.K_ESCAPE :
					vent_pausa.poner_pausa()

		# Actualizamos

		aux = True
		for v in ventanas :
			if v.arr : aux = False; no_marcar_casilla(casillas); break
		if pausa :  aux = False; no_marcar_casilla(casillas)
		if not en_juego : aux = False; no_marcar_casilla(casillas)
		if aux :
			for fila in casillas :
				for casilla in fila :
					casilla.actualizar()
		actualizar_casillas(casillas)
		for v in ventanas : v.actualizar()
		cm = casillas_marcadas(casillas); vent_minas_restantes.n_minas = d.n_minas - cm
		pausa = vent_pausa.visible
		if ganar_juego(d.n_minas,casillas) and en_juego : en_juego = False; vent_ganarjuego.tiempo_fin=pygame.time.get_ticks()-vent_cronometro.timeInit; ocultar_ventanas(ventanas); vent_ganarjuego.visible = True
		if morir(casillas) and en_juego : en_juego = False; ocultar_ventanas(ventanas); vent_perderjuego.visible = True

		# Dibujamos

		ventana.fill(COLOR)
		for fila in casillas :
			for casilla in fila :
				casilla.dibujar(ventana)
		for fila in casillas :
			for casilla in fila :
				casilla.dibujar_lineas(ventana)
		for v in ventanas :
			v.dibujar(ventana)

		# Actualizamos ventana

		pygame.display.update()

# Al arrancar el script

if __name__ == '__main__' :

	BuscaMinas("dificil")