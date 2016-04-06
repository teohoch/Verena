import turtle

constelaciones = {
	"leo": "x320y25r62c95l5c46r142c50r110c33x320y25l186c28l36c24r49c19r61c29r75c15",
	"cancer": "x200y0l70c63r35c33l180c33r110c59",
	"canisminor": "x146y140l29c25",
	"osamenor": "x-2y-232r74c41l40c26l25c28r84c16r94c31r99c17",
	"aries": "x-235y41r54c9l40c19l54c76",
	"cepheus": "x-128y-237r47c49r112c41r70c55r118c43r5c63r131c54",
	"cassioppeia": "x-102y-147r181c24l60c18r68c24l105c26",
	"canismajor": "x70y344r12c56r36c20l80c23l180c23l20c55r70c31r180c31r1c26",
	"gemini": "x142y38r138c20r89c63l9c27l25c9l22c12x142y38r76c42l30c20r8c38r87c18",
	"auriga": "x-10y-23r50c54l136c48l102c38r80c64r69c38r93c54r41c38",
	"piscis": "x-256y127r99c44l7c40r5c42l48c18l15c14r44c20x-256y127r56c12l15c19r14c17l3c39r17c19l9c66r4c26r103c25l118c18l26c25l94c19l76c21"
}

texto_menu = "Bienvenido a la Constelacion de Santa Maria\n" \
			 "Opciones:\n" \
			 "|------------------------------------------\n" \
			 "| 1 - Buscar constelaciones\n" \
			 "| 2 - Ingresar Constelacion\n" \
			 "| 3 - Distancia entre dos constelaciones\n" \
			 "| 4 - Salir\n" \
			 "|------------------------------------------\n"

pantalla = turtle.Screen()
pantalla.screensize(880,880)
pantalla.setup(width=900,height=900)
pantalla.bgpic("image.gif")
turtle.speed(0)
turtle.up()
turtle.setx(0)
turtle.sety(-440)
turtle.down()
turtle.color("white")
turtle.circle(440)
turtle.up()
turtle.sety(-200)
turtle.down()
turtle.circle(200)

pantalla.exitonclick()