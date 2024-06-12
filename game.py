# Librerias
import random, math, sys, pygame, os
pygame.init()



# Ventana del juego
ancho=1350
alto=750
ventana=pygame.display.set_mode((ancho,alto))
musicpath = os.path.realpath(os.path.dirname(__file__))+"/music"
path = os.path.realpath(os.path.dirname(__file__))+"/images"


# Imagenes
fondopng=pygame.image.load(path+"/fondo.png")
fondopng=pygame.transform.scale(fondopng,(1350,750))
pantallainicio=pygame.image.load(path+"/pantallainicio.png")
pantallainicio=pygame.transform.scale(pantallainicio,(1350,750))
elegirmodo=pygame.image.load(path+"/elegirmodo.png")
elegirmodo=pygame.transform.scale(elegirmodo,(1350,750))
gameoverpng=pygame.image.load(path+"/gameover.png")
gameoverpng=pygame.transform.scale(gameoverpng,(1350,750))



#Musica
musica=random.randrange(2)
if musica==0:
    pygame.mixer.music.load(musicpath+"/music.ogg")
    pygame.mixer.music.play(-1)
else:
    pygame.mixer.music.load(musicpath+"/music1.ogg")
    pygame.mixer.music.play(-1)



# Informacion sobre el jugador del modo 1
class c_jsalto:
    def __init__(self):
        self.posx=ancho/2
        self.posy=alto
        self.vlateral=20
        self.vsalto=-50
        self.gravedad=1.5
        self.numsaltos=5
        self.jugadorpng=pygame.image.load(path+"/luna.png")
        self.jugadorpng=pygame.transform.scale(self.jugadorpng,(80,90))
        self.actualizarbordes()
    def actualizarbordes(self):
        self.xmax=self.posx+70
        self.xmin=self.posx+8
        self.ymax=self.posy+75
        self.ymin=self.posy+10
    def derecha(self):
        if self.xmax+self.vlateral<ancho:
            self.posx+=self.vlateral
        else:
            self.posx=ancho-80
        self.actualizarbordes()
    def izquierda(self):
        if self.xmin-self.vlateral>0:
            self.posx-=self.vlateral
        else:
            self.posx=0
        self.actualizarbordes()
    def caer(self):
        if self.ymin<=0:
            self.vsalto=5
        self.posy+=self.vsalto
        self.vsalto+=self.gravedad
        self.actualizarbordes()
    def saltar(self):
        if self.numsaltos>0:
            self.vsalto=-20
            self.numsaltos-=1
    def pintar(self):
        ventana.blit(self.jugadorpng,(self.posx,self.posy))



# Informacion sobre el enemigo del modo 1
class c_enemigo:
    def __init__(self):
        self.reiniciar()
        self.enemigopng=pygame.image.load(path+"/marciano.png")
        self.enemigopng=pygame.transform.scale(self.enemigopng,(70,75))
    def actualizarbordes(self):
        self.xmax=self.posx+70
        self.xmin=self.posx+8
        self.ymax=self.posy+66
        self.ymin=self.posy+10
    def reiniciar(self):
        self.posx=random.choice([-50,ancho+50])
        self.posy=0
        self.altura=random.randrange(200,alto-200)
        self.onda=random.randrange(100,150)
        if self.posx<0:
            self.vlateral=random.randrange(5,15)
        else:
            self.vlateral=random.randrange(5,15)*-1
        self.actualizarbordes()
    def mover(self):
        self.posx+=self.vlateral
        self.posy=math.sin(self.posx/150)*self.onda+self.altura
        self.actualizarbordes()
    def pintar(self):
        ventana.blit(self.enemigopng,(self.posx,self.posy))



# Informacion del objeto bonus del modo 1
class c_sumasaltos:
    def __init__(self):
        self.posx=random.randrange(20,ancho-40)
        self.posy=random.randrange(20,alto-40)
        self.sumasaltospng=pygame.image.load(path+"/estrella.png")
        self.sumasaltos0=pygame.transform.scale(self.sumasaltospng,(35,35))
        self.sumasaltos1=pygame.transform.scale(self.sumasaltospng,(37,37))
        self.sumasaltos2=pygame.transform.scale(self.sumasaltospng,(39,39))
        self.sumasaltos3=pygame.transform.scale(self.sumasaltospng,(41,41))
        self.sumasaltos4=pygame.transform.scale(self.sumasaltospng,(43,43))
        self.sumasaltos5=pygame.transform.scale(self.sumasaltospng,(45,45))
        self.sumasaltos6=pygame.transform.scale(self.sumasaltospng,(47,47))
        self.actualizarbordes()
    def cambiarpos(self):
        self.posx=random.randrange(20,ancho-40)
        self.posy=random.randrange(20,alto-40)
        self.actualizarbordes()
    def actualizarbordes(self):
        self.xmax=self.posx+30
        self.xmin=self.posx+10
        self.ymax=self.posy+30
        self.ymin=self.posy+10
    def pintar(self,n):
        if n%14==0:
            ventana.blit(self.sumasaltos0,(self.posx,self.posy))
        elif n%14==1:
            ventana.blit(self.sumasaltos1,(self.posx,self.posy))
        elif n%14==2:
            ventana.blit(self.sumasaltos2,(self.posx,self.posy))
        elif n%14==3:
            ventana.blit(self.sumasaltos3,(self.posx,self.posy))
        elif n%14==4:
            ventana.blit(self.sumasaltos4,(self.posx,self.posy))
        elif n%14==5:
            ventana.blit(self.sumasaltos5,(self.posx,self.posy))
        elif n%14==6:
            ventana.blit(self.sumasaltos6,(self.posx,self.posy))
        elif n%14==7:
            ventana.blit(self.sumasaltos6,(self.posx,self.posy))
        elif n%14==8:
            ventana.blit(self.sumasaltos5,(self.posx,self.posy))
        elif n%14==9:
            ventana.blit(self.sumasaltos4,(self.posx,self.posy))
        elif n%14==10:
            ventana.blit(self.sumasaltos3,(self.posx,self.posy))
        elif n%14==11:
            ventana.blit(self.sumasaltos2,(self.posx,self.posy))
        elif n%14==12:
            ventana.blit(self.sumasaltos1,(self.posx,self.posy))
        else:
            ventana.blit(self.sumasaltos0,(self.posx,self.posy))



# Informacion sobre el jugador del modo 2
class c_jgravedad:
    def __init__(self):
        self.posx=ancho/2
        self.posy=alto/2
        self.gravedadx=0
        self.velocidadx=0
        self.gravedady=0.05
        self.velocidady=0
        self.vidas=20
        self.jugadorpng=pygame.image.load(path+"/luna.png")
        self.jugadorpng=pygame.transform.scale(self.jugadorpng,(80,90))
        self.actualizarbordes()
    def actualizarbordes(self):
        self.xmax=self.posx+70
        self.xmin=self.posx+5
        self.ymax=self.posy+80
        self.ymin=self.posy+5
    def caer(self):
        if self.gravedadx>0:
            if self.xmin<=0:
                self.velocidadx=5
            if self.xmax<ancho-10:
                self.posx+=self.velocidadx
                self.velocidadx+=self.gravedadx
            else:
                self.posx=ancho-80
                self.velocidadx=0
        if self.gravedadx<0:
            if self.xmax>=ancho:
                self.velocidadx=-5
            if self.xmin>10:
                self.posx+=self.velocidadx
                self.velocidadx+=self.gravedadx
            else:
                self.posx=0
                self.velocidadx=0
        if self.gravedady>0:
            if self.ymin<=0:
                self.velocidady=5
            if self.ymax<alto-20:
                self.posy+=self.velocidady
                self.velocidady+=self.gravedady
            else:
                self.posy=alto-90
                self.velocidady=0
        if self.gravedady<0:
            if self.ymax>=alto:
                self.velocidady=-5
            if self.ymin>20:
                self.posy+=self.velocidady
                self.velocidady+=self.gravedady
            else:
                self.posy=0
                self.velocidady=0
        self.actualizarbordes()
    def pintar(self):
        ventana.blit(self.jugadorpng,(self.posx,self.posy))



# Informacion del enemigo del modo 2
class c_proyectil:
    def __init__(self):
        self.size=random.choice([40,60,80])
        self.reiniciar()
        self.proyectilpng=pygame.image.load(path+"/asteroide.png")
        self.proyectilpng=pygame.transform.scale(self.proyectilpng,(self.size,self.size))
        self.proyectilpng=pygame.transform.rotate(self.proyectilpng,random.choice([0,90,180]))
        self.actualizarbordes()
    def actualizarbordes(self):
        if self.size==40:
            self.xmax=self.posx+38
            self.xmin=self.posx+5
            self.ymax=self.posy+38
            self.ymin=self.posy+5
        elif self.size==60:
            self.xmax=self.posx+50
            self.xmin=self.posx+8
            self.ymax=self.posy+50
            self.ymin=self.posy+5
        elif self.size==80:
            self.xmax=self.posx+65
            self.xmin=self.posx+8
            self.ymax=self.posy+68
            self.ymin=self.posy+8
    def reiniciar(self):
        self.v=random.randrange(3,6)
        self.tipo=random.choice(["vertical","horizontal"])
        self.sentido=random.choice(["positivo","negativo"])
        if self.tipo=="horizontal":
            self.posy=random.randrange(alto)
            if self.sentido=="positivo":
                self.posx=0
                self.velocidadx=self.v
                self.velocidady=0
            elif self.sentido=="negativo":
                self.posx=ancho
                self.velocidadx=-self.v
                self.velocidady=0
        elif self.tipo=="vertical":
            self.posx=random.randrange(ancho)
            if self.sentido=="positivo":
                self.posy=0
                self.velocidadx=0
                self.velocidady=self.v
            elif self.sentido=="negativo":
                self.posy=alto
                self.velocidadx=0
                self.velocidady=-self.v
        self.actualizarbordes()
    def mover(self):
        self.posx+=self.velocidadx
        self.posy+=self.velocidady
        self.actualizarbordes()
    def pintar(self):
        ventana.blit(self.proyectilpng,(self.posx,self.posy))



# Informacion del objeto bonus del modo 2
class c_sumavidas:
    def __init__(self):
        self.posx=random.randrange(20,ancho-40)
        self.posy=random.randrange(20,alto-40)
        # años despues de haber escrito el codigo me encuentro con esto
        # solo puedo decir xd
        # no se en que estaba pensado en su momento
        # lo dejo asi para reirme las siguientes veces que vea esto
        self.sumavidaspng=pygame.image.load(path+"/estrella.png")
        self.sumavidas0=pygame.transform.scale(self.sumavidaspng,(35,35))
        self.sumavidas1=pygame.transform.scale(self.sumavidaspng,(37,37))
        self.sumavidas2=pygame.transform.scale(self.sumavidaspng,(39,39))
        self.sumavidas3=pygame.transform.scale(self.sumavidaspng,(41,41))
        self.sumavidas4=pygame.transform.scale(self.sumavidaspng,(43,43))
        self.sumavidas5=pygame.transform.scale(self.sumavidaspng,(45,45))
        self.sumavidas6=pygame.transform.scale(self.sumavidaspng,(47,47))
        self.sumavidas6=pygame.transform.scale(self.sumavidaspng,(35,35))
        self.sumavidas5=pygame.transform.scale(self.sumavidaspng,(37,37))
        self.sumavidas4=pygame.transform.scale(self.sumavidaspng,(39,39))
        self.sumavidas3=pygame.transform.scale(self.sumavidaspng,(41,41))
        self.sumavidas2=pygame.transform.scale(self.sumavidaspng,(43,43))
        self.sumavidas1=pygame.transform.scale(self.sumavidaspng,(45,45))
        self.sumavidas0=pygame.transform.scale(self.sumavidaspng,(47,47))        
        self.actualizarbordes()
    def cambiarpos(self):
        self.posx=random.randrange(20,ancho-40)
        self.posy=random.randrange(20,alto-40)
        self.actualizarbordes()
    def actualizarbordes(self):
        self.xmax=self.posx+30
        self.xmin=self.posx+10
        self.ymax=self.posy+30
        self.ymin=self.posy+10
    def pintar(self,n):
        if n%14==0:
            ventana.blit(self.sumavidas0,(self.posx,self.posy))
        elif n%14==1:
            ventana.blit(self.sumavidas1,(self.posx,self.posy))
        elif n%14==2:
            ventana.blit(self.sumavidas2,(self.posx,self.posy))
        elif n%14==3:
            ventana.blit(self.sumavidas3,(self.posx,self.posy))
        elif n%14==4:
            ventana.blit(self.sumavidas4,(self.posx,self.posy))
        elif n%14==5:
            ventana.blit(self.sumavidas5,(self.posx,self.posy))
        elif n%14==6:
            ventana.blit(self.sumavidas6,(self.posx,self.posy))
        elif n%14==7:
            ventana.blit(self.sumavidas6,(self.posx,self.posy))
        elif n%14==8:
            ventana.blit(self.sumavidas5,(self.posx,self.posy))
        elif n%14==9:
            ventana.blit(self.sumavidas4,(self.posx,self.posy))
        elif n%14==10:
            ventana.blit(self.sumavidas3,(self.posx,self.posy))
        elif n%14==11:
            ventana.blit(self.sumavidas2,(self.posx,self.posy))
        elif n%14==12:
            ventana.blit(self.sumavidas1,(self.posx,self.posy))
        else:
            ventana.blit(self.sumavidas0,(self.posx,self.posy))



# Todos los eventos y chequeos necesarios
class c_eventos:
    def __init__(self):
        self.puntos=0
    def escribir_puntos(self):
        fuente=pygame.font.Font(None,50)
        puntos=fuente.render("SCORE:",0,(0,0,0))
        ventana.blit(puntos,(1100,450))
        textopuntos=fuente.render(str(self.puntos),0,(0,0,0))
        ventana.blit(textopuntos,(1250,450))
    def escribir_maxpuntos(self):
        fuente=pygame.font.Font(None,50)
        puntos=fuente.render("MAX SCORE:",0,(0,0,0))
        ventana.blit(puntos,(10,120))
        textopuntos=fuente.render(str(puntosmaximos),0,(0,0,0))
        ventana.blit(textopuntos,(250,120))
        



# Actualiza y prepara pantalla para el nuevo fotograma
    def updatepantalla(self):
        pygame.display.update()
        pygame.display.flip()
        clock=pygame.time.Clock()
        clock.tick(60)



# Eventos del modo 1
    def teclasjuegosalto(self):
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key==pygame.K_UP:
                    jsalto.saltar()
        tecla=pygame.key.get_pressed()
        if tecla[pygame.K_RIGHT]:
            jsalto.derecha()
        if tecla[pygame.K_LEFT]:
            jsalto.izquierda()
    def fueralaterales(self,i):
        if listaenemigos[i].posx>ancho+100:
            listaenemigos[i].reiniciar()
        if listaenemigos[i].posx<-100:
            listaenemigos[i].reiniciar()
    def colision_sumasaltos(self,i):
        if jsalto.xmin>listasumasaltos[i].xmax:
            return
        elif jsalto.xmax<listasumasaltos[i].xmin:
            return
        elif jsalto.ymin>listasumasaltos[i].ymax:
            return
        elif jsalto.ymax<listasumasaltos[i].ymin:
            return
        else:
            self.puntos+=1
            jsalto.numsaltos=5
            listasumasaltos[i].cambiarpos()
            effect=pygame.mixer.Sound(musicpath+"/sound.ogg")
            effect.play()
    def muertemodo1(self):
        if self.bajosuelo()==True:
            return True
        for i in range(len(listaenemigos)):
            if self.colision_enemigos(i)==True:
                return True
    def bajosuelo(self):
        if jsalto.posy>alto-50:
            return True
        return False
    def colision_enemigos(self,i):
        if jsalto.xmin>listaenemigos[i].xmax:
            return False
        elif jsalto.xmax<listaenemigos[i].xmin:
            return False
        elif jsalto.ymin>listaenemigos[i].ymax:
            return False
        elif jsalto.ymax<listaenemigos[i].ymin:
            return False
        return True
    def escribir_saltos(self):
        fuente=pygame.font.Font(None,50)
        saltos_restantes=fuente.render("JUMPS:",0,(0,0,0))
        ventana.blit(saltos_restantes,(30,120))
        textosaltos=fuente.render(str(jsalto.numsaltos),0,(0,0,0))
        ventana.blit(textosaltos,(170,120))


# Eventos modo 2
    def teclasjuegogravedad(self):
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key==pygame.K_RIGHT:
                    jgravedad.velocidadx/=1.5
                    jgravedad.gravedadx=0.4
                if event.key==pygame.K_LEFT:
                    jgravedad.velocidadx/=1.5
                    jgravedad.gravedadx=-0.4
                if event.key==pygame.K_UP:
                    jgravedad.velocidady/=1.5
                    jgravedad.gravedady=-0.4
                if event.key==pygame.K_DOWN:
                    jgravedad.velocidady/=1.5
                    jgravedad.gravedady=0.4
    def proyectilesfueramapa(self,i):
        if listaproyectiles[i].posx>ancho+100:
            listaproyectiles[i].reiniciar()
        if listaproyectiles[i].posx<-100:
            listaproyectiles[i].reiniciar()
        if listaproyectiles[i].posy>alto+100:
            listaproyectiles[i].reiniciar()
        if listaproyectiles[i].posy<-100:
            listaproyectiles[i].reiniciar()
    def colision_sumavidas(self,i):
        if jgravedad.xmin>listasumavidas[i].xmax:
            return
        elif jgravedad.xmax<listasumavidas[i].xmin:
            return
        elif jgravedad.ymin>listasumavidas[i].ymax:
            return
        elif jgravedad.ymax<listasumavidas[i].ymin:
            return
        else:
            self.puntos+=3
            jgravedad.vidas=20
            listasumavidas[i].cambiarpos()
    def muertemodo2(self,cuentabucles):
        for i in range(len(listaproyectiles)):
            if self.colision_proyectiles(i)==True:
                return True
        if cuentabucles%20==0:
            jgravedad.vidas-=1
        if jgravedad.vidas<0:
            return True
    def colision_proyectiles(self,i):
        if jgravedad.xmin>listaproyectiles[i].xmax:
            return False
        elif jgravedad.xmax<listaproyectiles[i].xmin:
            return False
        elif jgravedad.ymin>listaproyectiles[i].ymax:
            return False
        elif jgravedad.ymax<listaproyectiles[i].ymin:
            return False
        return True
    def escribir_vidas(self):
        fuente=pygame.font.Font(None,50)
        tiempo_restante=fuente.render("TIME:",0,(0,0,0))
        ventana.blit(tiempo_restante,(30,120))
        textovidas=fuente.render(str(jgravedad.vidas),0,(0,0,0))
        ventana.blit(textovidas,(140,120))



# Bucle de la pantalla de inicio
eventos=c_eventos()
inicio=True
while inicio:
    eventos.updatepantalla()
    ventana.fill([255,255,255])
    ventana.blit(pantallainicio,(0,0))
    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key==pygame.K_RETURN:
                inicio=False
                escojermodo=True



# Bucle principal del juego
puntosmaximos=0
while True:



# Bucle para escojer modo de juego
    while escojermodo:
        eventos.updatepantalla()
        ventana.fill([255,255,255])
        ventana.blit(elegirmodo,(0,0))
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key==pygame.K_1:
                    escojermodo=False
                    modo1=True
                    modo2=False
                if event.key==pygame.K_2:
                    escojermodo=False
                    modo1=False
                    modo2=True



# Chequea y juega al modo 1
    if modo1==True:
        eventos.puntos=0
        jsalto=c_jsalto()
        listaenemigos=[]
        for i in range(4):
            listaenemigos.append(c_enemigo())
        listasumasaltos=[]
        for i in range(10):
            listasumasaltos.append(c_sumasaltos())
        jugandomodo1=True
        cuentabucles=0
        while jugandomodo1:
            cuentabucles+=1
            eventos.updatepantalla()
            ventana.blit(fondopng,(0,0))
            eventos.teclasjuegosalto()
            eventos.escribir_saltos()
            eventos.escribir_puntos()
            for i in range(len(listasumasaltos)):
                listasumasaltos[i].pintar(cuentabucles+i)
                eventos.colision_sumasaltos(i)
            jsalto.caer()
            jsalto.pintar()              
            for i in range(len(listaenemigos)):
                listaenemigos[i].mover()
                listaenemigos[i].pintar()
                eventos.fueralaterales(i)
            if cuentabucles%250==0:
                listaenemigos.append(c_enemigo())
            if eventos.muertemodo1()==True:
                jugandomodo1=False
                modoanterior=1



# Chequea y juega el modo 2
    if modo2==True:
        eventos.puntos=0
        jgravedad=c_jgravedad()
        listaproyectiles=[]
        for i in range(8):
            listaproyectiles.append(c_proyectil())
        listasumavidas=[]
        for i in range(5):
            listasumavidas.append(c_sumavidas())
        jugandomodo2=True
        cuentabucles=0
        while jugandomodo2:
            cuentabucles+=1
            eventos.updatepantalla()
            ventana.blit(fondopng,(0,0))
            eventos.teclasjuegogravedad()
            eventos.escribir_vidas()
            eventos.escribir_puntos()
            for i in range(len(listasumavidas)):
                listasumavidas[i].pintar(cuentabucles+3*i)
                eventos.colision_sumavidas(i)
            for i in range(len(listaproyectiles)):
                listaproyectiles[i].mover()
                listaproyectiles[i].pintar()
                eventos.proyectilesfueramapa(i)
            jgravedad.caer()
            jgravedad.pintar()
            if cuentabucles%250==0:
                listaproyectiles.append(c_proyectil())
            if eventos.muertemodo2(cuentabucles)==True:
                jugandomodo2=False
                modoanterior=2



# Pantalla de muerte
    gameover=True
    if eventos.puntos>puntosmaximos:
        puntosmaximos=eventos.puntos
    while gameover:
        eventos.updatepantalla()
        ventana.blit(gameoverpng,(0,0))
        eventos.escribir_puntos()
        eventos.escribir_maxpuntos()
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key==pygame.K_RETURN:
                    gameover=False
                    if modoanterior==1:
                        modo1=True
                    if modoanterior==2:
                        modo2=True
                if event.key==pygame.K_SPACE:
                    gameover=False
                    escojermodo=True