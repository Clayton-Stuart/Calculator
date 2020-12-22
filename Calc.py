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
		while True:
			x1 = input("x1: ")
			try:
				x1 = float(x1)
			except:
				pass
			else:
				x1 = float(x1)
				break
		# you don't actually need the second float() conversion,
		# since the first one in the try branch will have worked
		# if we're not in the except clause.  example:
		while True:
			x2 = input("x2: ")
			try:
				x2 = float(x2)

			except:
				pass

			else:
				break

		# in fact, you don't even need the else: branch at all.
		# you can put everything that you want to happen for a
		# successful input right into the try: branch. example:
		while True:
			y1 = input("y1: ")
			try:
				y1 = float(y1)
				break
			except:
				pass

		while True:
			y2 = input("y2: ")
			try:
				y2 = float(y2)

			except:
				pass

			else:
				y2 = float(y2)
				break


		answer = math.sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1))
		print(answer)
		

	if path == "mid":

		while True:
			x1 = input("x1: ")
			try:
				x1 = float(x1)
			except:
				pass
			else:
				x1 = float(x1)
				break
		while True:
			x2 = input("x2: ")
			try:
				x2 = float(x2)

			except:
				pass

			else:
				x2 = float(x2)
				break

		while True:
			y1 = input("y1: ")
			try:
				y1 = float(y1)

			except:
				pass

			else:
				y1 = float(y1)
				break

		while True:
			y2 = input("y2: ")
			try:
				y2 = float(y2)

			except:
				pass

			else:
				y2 = float(y2)
				break
		xp1 = (x1 + x2)
		xp2 = (xp1/2)
		yp1 = (y1 + y2)
		yp2 = (yp1/2)
		print("(" + str(xp2) + ", " + str(yp2) + ")")
		print("")

	if path == "pyth":

		while True:
			s1 = input("s1: ")
			try:
				s1 = float(s1)
			except:
				pass
			else:
				s1 = float(s1)
				break

		while True:
			s2 = input("s2: ")
			try:
				s2 = float(s2)
			except:
				pass
			else:
				s2 = float(s2)
				break
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
			while True:
				side_length = input("Enter the length of a side (no units): ")
				try:
					float(side_length)
				except:
					pass
				else:
					side_length = float(side_length)
					break

			print(side_length * side_length)

		if shape == "circle":
			while True:
				radius = input("Enter the radius (no units): ")
				try:
					float(radius)
				except:
					pass
				else:
					radius = float(radius)
					break
			radius = radius * radius
			print(radius * 3.14159265358979323846264338327950288419716939937510582097494459230781640628620899862803482534211706798214808651328230664709384)

		if shape == "triangle":
			while True:
				base = input("Enter the length of the base (no units): ")
				try:
					float(base)
				except:
					pass
				else:
					base = float(base)
					break

			while True:
				height = input("Enter the height (no units): ")
				try:
					float(height)
				except:
					pass
				else:
					height = float(height)
					break
			mid = base * height
			print(mid/2)

		if shape == "rectangle":
			while True:
				length = input("Enter the length (no units): ")
				try:
					float(length)
				except:
					pass
				else:
					length = float(length)
					break

			while True:
				width = input("Enter the width (no units): ")
				try:
					float(width)
				except:
					pass
				else:
					width = float(width)
					break
			print(width * length)

		if shape == "parallelogram":
			while True:
				pass
				base = input("Enter the length of the base (no units): ")
				try:
					float(base)
				except:
					pass
				else:
					base = float(base)
					break

			while True:
				height = input("Enter the height (no units): ")
				try:
					float(height)
				except:
					pass
				else:
					height = float(height)
					break
			print(base * height)

		if shape == "regular hexagon":
			while True:
				pass
				side = input("Enter the length of the side (no units): ")
				try:
					float(side)
				except:
					pass
				else:
					side = float(side)
					break

			mid1 = 3 * math.sqrt(3)
			mid2 = mid1/2
			mid3 = side * side
			print(mid2 * mid3)

		if shape == "trapezoid":
			while True:
				pass
				base1 = input("Enter the length of the first base (no units): ")
				try:
					float(base1)
				except:
					pass
				else:
					base1 = float(base1)
					break

			while True:
				pass
				base2 = input("Enter the length of the second base (no units): ")
				try:
					float(base2)
				except:
					pass
				else:
					base2 = float(base2)
					break

			while True:
				height = input("Enter the height (no units): ")
				try:
					float(height)
				except:
					pass
				else:
					height = float(height)
					break
			bases = base1 + base2
			div_bases = bases/2
			print(div_bases * height)

		if shape == "rhombus":
			while True:
					diagonal1 = input("Enter the length of the first diagonal (no unit): ")
					try:
						float(diagonal1)
					except:
						pass
					else:
						diagonal1 = float(diagonal1)
						break

			while True:
					diagonal2 = input("Enter the length of the second diagonal (no unit): ")
					try:
						float(diagonal2)
					except:
						pass
					else:
						diagonal2 = float(diagonal2)
						break
			mid1 = diagonal2 * diagonal1
			print(mid1/2)

		print("")

	if path == "basic":
		while True:
			first_value = input("Enter the first value: ")
			try:
				float(first_value)
			except:
				pass
			else:
				first_value = float(first_value)
				break

		while True:
			second_value = input("Enter the second value: ")
			try:
				float(second_value)
			except:
				pass
			else:
				second_value = float(second_value)
				break
		
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
		value = input("Enter value: ")
		while True:
			try:
				float(value)
			except:
				pass
			else:
				value = float(value)
				break
		print(math.sqrt(float(value)))
		print("")

	if path == "exit":
		break

