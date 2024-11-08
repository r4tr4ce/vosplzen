import turtle
import math

def vykresli(x, y, n):
	turtle.setup(width=252, height=252)
	okno = turtle.Screen()
	okno.title("🐢")

	#GPT 100px!
	# Původní hodnoty délky a pozice iniciálů a úhelníku
	height_M_original = 50  # Výška čáry "M"
	angle_45_M_length = 35  # Šikmé čáry pod úhlem 45° pro "M"
	height_V_original = 58  # Šikmé čáry pod úhlem pro "V"
	spacing_MV = 60  # Mezera mezi "M" a "V"???????
	spacing_V_polygon = 3  # Mezera mezi "V" a úhelníkem (přibližná pozice 125 - 60)blbost
	polygon_side_length = 21  # Délka strany n-úhelníku

	# Horizontální projekce pro "M" šikmou čáru pod 45°
	proj_M_x1 = angle_45_M_length * math.cos(math.radians(45))

	# Horizontální projekce pro "V" šikmou čáru pod 66°
	proj_V_x1 = height_V_original * math.cos(math.radians(66))

	spacing_MV = 60-2*proj_M_x1##přece
	spacing_V_polygon = 125-60-proj_V_x1

	# Výpočet celkové horizontální délky (šířky)
	total_x_width_original = proj_M_x1 + proj_M_x1 + spacing_MV + proj_V_x1 + proj_V_x1 + spacing_V_polygon + polygon_side_length

	# Poměrné délky pro každý segment
	scale_factor_x = 100 / total_x_width_original  # Škálování pro 99 px [99px!=100px??????]

	# Škálované hodnoty
	scaled_proj_M_x1 = proj_M_x1 *scale_factor_x
	scaled_proj_V_x1 = proj_V_x1 * scale_factor_x
	scaled_spacing_MV = spacing_MV * scale_factor_x
	scaled_spacing_V_polygon = spacing_V_polygon * scale_factor_x
	scaled_polygon_side_length = polygon_side_length * scale_factor_x
	"""
	# Výstup škálovaných hodnot
	{
		"total_x_width_original": total_x_width_original,
		"scale_factor_x": scale_factor_x,
		"scaled_proj_M_x1": scaled_proj_M_x1,
		"scaled_proj_V_x1": scaled_proj_V_x1,
		"scaled_spacing_MV": scaled_spacing_MV,
		"scaled_spacing_V_polygon": scaled_spacing_V_polygon,
		"scaled_polygon_side_length": scaled_polygon_side_length
	}"""



	
	zelvuska = turtle.Turtle()
	zelvuska.speed(1)
	#	90
	#180	0
	#	270
	"""
	pen.goto(x, y-50)
	pen.setheading(0)
	pen.forward(100)#60)
	"""
	zelvuska.penup()
	zelvuska.goto(x, y-50*scale_factor_x)
	zelvuska.width(5)
	zelvuska.color("blue")
	zelvuska.pendown()
	zelvuska.setheading(90)
	zelvuska.forward(50*scale_factor_x)
	zelvuska.setheading(-45)
	zelvuska.forward(35*scale_factor_x)
	zelvuska.setheading(45)
	zelvuska.forward(35*scale_factor_x)
	#######
	#pen.setheading(-180)
	#pen.forward(35*math.cos(math.radians(45)))#9.579324454729578)
	zelvuska.setheading(-90)
	zelvuska.forward(50*scale_factor_x)
	zelvuska.penup()

	zelvuska.goto(x +60*scale_factor_x, y)
	zelvuska.pendown()
	zelvuska.setheading(-66)
	zelvuska.forward(58*scale_factor_x)
	zelvuska.setheading(66)
	zelvuska.forward(58*scale_factor_x)
	zelvuska.penup()

	zelvuska.goto(x+125*scale_factor_x, y-50*scale_factor_x)
	zelvuska.setheading(0)
	zelvuska.pendown()
	zelvuska.color("red")
	uhel = 360/n
	for _ in range(n):
		zelvuska.forward(21*scale_factor_x)
		zelvuska.left(uhel)
	zelvuska.hideturtle()
	turtle.done()

vykresli(-100, 100, 7)
