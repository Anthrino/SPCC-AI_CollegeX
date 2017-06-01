# Recursive Descent Parser for a given grammar

print("\nGrammar Specifications :- \n E -> x A T \n A -> + | - | * | / \n T -> ( E ) \n T -> x")
inp_exp = input("\nEnter the expression to be parsed (please end with '$' ): ")
inp_exp.replace(' ','')
index = 0

def char_match(string, index, char):
	print(index, string[index])
	if char == 1:
		if str.isalnum(string[index]):
			index += 1
			return index
		else:
			print("Incorrect syntax encountered.")
			return 0					
	elif char == 2:
		if string[index] in "+ - * /":
			index += 1
			return index
		else:
			print("Incorrect syntax encountered.")
			return 0
	else:
		if string[index] == char:
			index += 1
			return index
		else:
			print("Incorrect syntax encountered.")
			return 0						

def E(inp_exp, index):
	if str.isalnum(inp_exp[index]):
		index = char_match(inp_exp, index, 1)
		index = char_match(inp_exp, index, 2)
		index = T(inp_exp, index)
	return index

def T(inp_exp, index):
	if inp_exp[index] == '(':
		index = char_match(inp_exp, index, '(')
		index = E(inp_exp, index)
		index = char_match(inp_exp, index, ')')
		return index
	elif str.isalnum(inp_exp[index]):
		index = char_match(inp_exp, index, 1)
		return index
	else:
		return index			
				
index = E(inp_exp, index)

if inp_exp[index] == '$':
	print("Input expression satisfies given grammar.")
else:
	print("Input expression does not comply with the given grammar.")


