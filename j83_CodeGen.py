# Target Code generator for three-address code input

import re
index = 0
target_code = []
reg_entries = []

# Three-address input code -- edit if required
code = "t = a - b \nu = a * c \nx = b + u \nv = t + u \nv = v * x\nd = v - u\ne = v + u"
code = code.split("\n")
print("\nInput Expressions: \n")

for line in code:
	print (line)
	spline = line.replace(" ", "")
	if "=" in spline:

		# print(spline)

		expr = (re.findall(r"\w+=\S*", spline))[0].split("=")
		# print(expr)

		operands = re.split('\^|/|\*|\+|-', expr[1])
		# print(operands)

		if operands[1] in reg_entries:
			index = reg_entries.index(operands[1])
			operands[1] = "R" + str(index)

		if operands[0] in reg_entries:
			index = reg_entries.index(operands[0])
			operands[0] = "R" + str(index)
		else:
			reg_entries.append(operands[0])
			index = reg_entries.index(operands[0])
			target_code.append("MOV "+operands[0]+", "+"R"+str(index)+"\n")
			operands[0] = "R" + str(index)


		if "*" in spline:
			target_code.append("MUL "+operands[1]+", "+operands[0]+"\n")
			reg_entries[index] = expr[0]
		if "+" in spline:
			target_code.append("ADD "+operands[1]+", "+operands[0]+"\n")
			reg_entries[index] = expr[0]
		if "-" in spline:
			target_code.append("SUB "+operands[1]+", "+operands[0]+"\n")
			reg_entries[index] = expr[0]

		# if reg_entries[index] == expr[0]:
		# 	target_code.append("MOV " + "R" + str(index) + ", " + reg_entries[index] + "\n")


		# print("regEntries"+str(reg_entries))

for x in reg_entries:
	target_code.append("MOV " + "R" + str(reg_entries.index(x)) + ", " + x + "\n")

print("\nTarget code for three-address input: \n")

for line in target_code:
	print(line)
