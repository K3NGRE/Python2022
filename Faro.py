#Dibuje el fondo.
### Ponga su código aquí ###
Rect(0, 0, 400, 250, relleno=gradiente('azulMediaNoche', 'azulAcero', inicio='superior'))
Rect(0, 250, 400, 250, relleno=gradiente('azulPizarraOscuro', 'azulPizarra'))
# Dibuje la roca detrás del faro y su reflejo.
### (PISTA: ¡Hay una punta de la roca que está detrás del faro!)
### Ponga su código aquí ###
Poligono(160, 280, 205, 240, 295, 210, 400, 230, 400, 280,  relleno=gradiente('azulPizarraOscuro', 'azulOscuro', inicio='superior'))
# Dibuje el faro desde arriba hacia abajo.
### Ponga su código aquí ###
Poligono(180, 285, 220, 285, 215, 220, 185, 220, relleno=gradiente('nieve', 'grisOscuro', inicio='superior'))
Poligono(185, 220, 215, 220, 210, 160, 190, 160, relleno=gradiente('carmesi', 'rojoOscuro', inicio='superior'))
Rect(203, 190, 5, 10, relleno='negro')
Rect(185, 150, 30, 10, relleno='ladrillo')
Rect(190, 130, 5, 20, relleno='carmesi')
Rect(205, 130, 5, 20, relleno='carmesi')
Rect(195, 130, 10, 20, relleno='amarillo')
Poligono(185, 130, 200, 120, 215, 130, relleno=gradiente('carmesi', 'rojoOscuro', inicio='inferior'))
Circulo(200, 140, 40, opacidad=10, relleno=gradiente('amarillo', 'oro', 'naranja', inicio='superior'))
# Dibuje la luz que viene del faro.
### Ponga su código aquí ###
Poligono(200, 140, 400, 260, 400, 340, opacidad=30, relleno=gradiente('amarillo', 'oro', 'naranja'))
#Dibuje la roca en frente del faro y su reflejo.
### Ponga su código aquí ###
Poligono(120, 290, 145, 240, 235, 265, 270, 290, relleno=gradiente('azulPizarraOscuro', 'azulOscuro', inicio='superior'))
Poligono(120, 290, 145, 340, 235, 315, 270, 290, opacidad=30, relleno=gradiente('azulPizarraOscuro', 'azulOscuro', inicio='superior'))
