import math

def print_help():
	print("""Formula Calculators:
		Distance Formula: type \"dist\"
		Midpoint Formula: type \"mid\"
		Pythagorean Theorum Calculator: type \"pyth\"
		Area of Shapes: type \"area\"
			""")
	print("""Other Calculators:
		Basic Calculator: type \"basic\"
		Square Root Calculator: type \"sqrt\"
			""")
	print("\n Or, type \"exit\" to quit")

def path_input():
	func_path = input("Type help for options, or type a formula, or calculator: ")
	func_path = func_path.lower()
	return func_path

def get_float(prompt):
	while True:
		x = input(prompt)
		try:
			x = float(x)
			break
		except:
			pass
	return x


while True:

	path = path_input()

	if path == "help":
		print_help()


	while path == "help":
		path = path_input()

		if path == "help":
			print_help()


	path = path.lower()
	if path == "dist":

		x1 = get_float("x1: ")
		x2 = get_float("x2: ")
		y1 = get_float("y1: ")
		y2 = get_float("y2: ")

		answer = math.sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1))
		print(answer)
		print("")
		

	if path == "mid":

		x1 = get_float("x1: ")
		x2 = get_float("x2: ")
		y1 = get_float("y1: ")
		y2 = get_float("y2: ")

		xp1 = (x1 + x2)
		xp2 = (xp1/2)
		yp1 = (y1 + y2)
		yp2 = (yp1/2)
		print("(" + str(xp2) + ", " + str(yp2) + ")")
		print("")

	if path == "pyth":

		s1 = get_float("Side 1: ")
		s2 = get_float("Side 2: ")
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
			side_length = get_float("Enter the length of a side (no units): ")

			print(side_length * side_length)

		if shape == "circle":
			radius = get_float("Enter the radius (no units): ")
			radius = radius * radius
			print(radius * 3.14159265358979323846264338327950288419716939937510582097494459230781640628620899862803482534211706798214808651328230664709384)

		if shape == "triangle":
			base = get_float("Enter the length of the base (no units)")

			height = get_float("Enter the height (no units): ")
			mid = base * height
			print(mid/2)

		if shape == "rectangle":
			length = get_float("Enter the length (no units): ")
			width = get_float("Enter the width (no units): ")
			print(width * length)

		if shape == "parallelogram":
			base = get_float("Enter the length of the base (no units): ")
			height = get_float("Enter the height (no units): ")
			print(base * height)

		if shape == "regular hexagon":
			side = get_float("Enter the length of the side (no units): ")

			mid1 = 3 * math.sqrt(3)
			mid2 = mid1/2
			mid3 = side * side
			print(mid2 * mid3)

		if shape == "trapezoid":
			base1 = get_float("Enter the length of the first base (no units): ")
			base2 = get_float("Enter the length of the second base (no units): ")
			height = get_float("Enter the height (no units): ")

			bases = base1 + base2
			div_bases = bases/2
			print(div_bases * height)

		if shape == "rhombus":
			diagonal1 = get_float("Enter the length of the first diagonal (no unit): ")
			diagonal2 = get_float("Enter the length of the second diagonal (no unit): ")

			mid1 = diagonal2 * diagonal1
			print(mid1/2)

		print("")

	if path == "basic":
		first_value = get_float("Enter the first value: ")
		second_value = get_float("Enter the second value: ")
		
		opperators = ["+", "-", "/", "*"]

		while True:
			operation = input("Enter +, -, /, *: ") 
			if operation in opperators:
				break

			else:
				pass

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
		value = get_float("Enter Value: ")
		print(math.sqrt(float(value)))
		print("")

	if path == "exit":
		break