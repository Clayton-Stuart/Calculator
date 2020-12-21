import math

while True:

	path = input("Type help for options, or type a formula, or calculator: ")

	path = path.lower()

	if path == "help":
		print("""Formula Calculators:
			Distance Formula: type \"dist\"
			Midpoint Formula: type \"mid\"
			Pythagorean Theorum Calculator: type \"pyth\"
			Area of Shapes: type \"area\"
			""")
		print("""Other Calculators
			Basic Calculator: type \"basic\"
			Square Root Calculator: type \"sqrt\"
			""")

	while path == "help":
		path = input("Type help for options, or type a formula, or calculator: ")

		path = path.lower()

		if path == "help":
			print("""Formula Calculators:
			Distance Formula: type \"dist\"
			Midpoint Formula: type \"mid\"
			Pythagorean Theorum Calculator: type \"pyth\"
			Area of Shapes: type \"area\"
			""")
			print("""Other Calculators
			Basic Calculator: type \"basic\"
			Square Root Calculator: type \"sqrt\"
			""")


	path = path.lower()
	if path == "dist":
		x1 = input("x1: ")
		x1 = float(x1)
		x2 = input("x2: ")
		x2 = float(x2)
		y1 = input("y1: ")
		y1 = float(y1)
		y2 = input("y2: ")
		y2 = float(y2)
		answer = math.sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1))
		print(answer)
		

	if path == "mid":
		x1 = input("x1: ") 
		x1 = float(x1)
		x2 = input("x2: ")
		x2 = float(x2)
		y1 = input("y1: ")
		y1 = float(y1)
		y2 = input("y2: ") 
		y2 = float(y2)
		xp1 = (x1 + x2)
		xp2 = (xp1/2)
		yp1 = (y1 + y2)
		yp2 = (yp1/2)
		xp2 = str(xp2)
		yp2 = str(yp2)
		print("(" + xp2 + ", " + yp2 + ")")
		print("")

	if path == "pyth":
		s1 = input("Side 1 length (No unit): ")
		s2 = input("Side 2 length (No unit): ")
		s1 = float(s1)
		s2 = float(s2)
		s12 = s1*s1
		s22 = s2*s2
		s32 = s12 + s22
		s3 = math.sqrt(s32)
		print(s3)
		print("")

	if path == "area":
		message = "Enter circle, square, triangle, rectangle, regular hexagon, trapezoid, rhombus, or parallelogram: "

		shape = input(message)
		shape = shape.lower()
		available_shapes = ["circle", "square", "triangle", "rectangle", "parallelogram", "regular hexagon", "trapezoid", "rhombus"]
		while True:
			if shape in available_shapes:
				break
			else:
				shape = input(message)
				shape = shape.lower()

		if shape == "square":
			side_length = input("Enter the length of a side (no units): ")
			side_length = float(side_length)
			print(side_length * side_length)

		if shape == "circle":
			radius = input("Enter the radius: ")
			radius = float(radius)
			radius = radius * radius
			print(radius * 3.14159265358979323846264338327950288419716939937510582097494459230781640628620899862803482534211706798214808651328230664709384)

		if shape == "triangle":
			base = input("Enter the base length (no unit): ")
			base = float(base)
			height = input("Enter the height (no unit): ")
			height = float(height)
			mid = base * height
			print(mid/2)

		if shape == "rectangle":
			length = input("Enter the length (no unit): ")
			width = input("Enter the width (no unit): ")
			length = float(length)
			width = float(width)
			print(width * length)

		if shape == "parallelogram":
			base = input("Enter the base (no unit): ")
			height = input("Enter the height (no unit): ")
			base = float(base)
			height = float(height)
			print(base * height)

		if shape == "regular hexagon":
			side = input("Enter the side length (no unit): ")
			side = float(side)
			mid1 = 3 * math.sqrt(3)
			mid2 = mid1/2
			mid3 = side * side
			print(mid2 * mid3)

		if shape == "trapezoid":
			base1 = input("Enter the length of the first base (no unit): ")
			base1 = float(base1)
			base2 = input("Enter the length of the second base (no unit): ")
			base2 = float(base2)
			height = input("Enter the height (no unit): ")
			height = float(height)
			bases = base1 + base2
			div_bases = bases/2
			print(div_bases * height)

		if shape == "rhombus":
			diagonal1 = input("Enter the length of the first diagonal (no unit): ")
			diagonal2 = input("Enter the length of the second diagonal (no unit): ")
			diagonal1 = float(diagonal1)
			diagonal2 = float(diagonal2)
			mid1 = diagonal2 * diagonal1
			print(mid1/2)

		print("")

	if path == "basic":
		first_value = input("Enter your first value: ")
		first_value = float(first_value)
		second_value = input("Enter your second value: ")
		second_value = float(second_value)
		operation = input("Enter +, -, /, *: ")
		if operation == "+":
			print(first_value + second_value)
		elif operation == "-":
			print(first_value - second_value)
		elif operation == "/":
			print(first_value / second_value)
		elif operation == "*":
			print(first_value * second_value)
		print("")

	if path == "sqrt":
		value = input("Enter value: ")
		print(math.sqrt(float(value)))
		print("")







input("")
