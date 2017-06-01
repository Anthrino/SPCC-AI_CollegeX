#Assembler for IBM 360

import re

#region Data Structures

mach_op_table = []
mot_entry = {"Mnemonic": "L", "Hex_Code": "58", "Length": 4, "Format": "RX"}
mach_op_table.append(mot_entry)
mot_entry = {"Mnemonic": "LR", "Hex_Code": "18", "Length": 2, "Format": "RR"}
mach_op_table.append(mot_entry)
mot_entry = {"Mnemonic": "LA", "Hex_Code": "41", "Length": 4, "Format": "RX"}
mach_op_table.append(mot_entry)
mot_entry = {"Mnemonic": "A", "Hex_Code": "5A", "Length": 4, "Format": "RX"}
mach_op_table.append(mot_entry)
mot_entry = {"Mnemonic": "AR", "Hex_Code": "1A", "Length": 2, "Format": "RR"}
mach_op_table.append(mot_entry)
mot_entry = {"Mnemonic": "ST", "Hex_Code": "50", "Length": 4, "Format": "RX"}
mach_op_table.append(mot_entry)
mot_entry = {"Mnemonic": "SR", "Hex_Code": "1B", "Length": 2, "Format": "RR"}
mach_op_table.append(mot_entry)
mot_entry = {"Mnemonic": "C", "Hex_Code": "59", "Length": 4, "Format": "RX"}
mach_op_table.append(mot_entry)
mot_entry = {"Mnemonic": "BNE", "Hex_Code": "47", "Length": 4, "Format": "RX"}
mach_op_table.append(mot_entry)
mot_entry = {"Mnemonic": "BR", "Hex_Code": "07", "Length": 2, "Format": "RR"}
mach_op_table.append(mot_entry)


# pseudo_ops = ["PROCESS", "ACONTROL", "ACTR", "ADATA", "AGO", "AIF","AINSERT", "ALIAS", "AMODE", "ANOP", "AREAD", "CATTR", "CCW", "CCW0",
# 		"CCW1", "CNOP", "COM", "COPY", "CSECT", "CXD", "DC", "DROP", "DS", "DSECT", "DXD", "EJECT", "END", "ENTRY", "EQU", "EXITCTL",
# 		"EXTRN", "GBLA", "GBLB", "GBLC", "ICTL", "ISEQ", "LCLA", "LCLB", "LCLC", "LOCTR", "LTORG", "MACRO", "MEND", "MEXIT", "MNOTE",
# 		"OPSYN", "ORG", "POP", "PRINT", "PUNCH", "PUSH", "REPRO", "RMODE", "RSECT", "SETA", "SETB", "SETC", "SPACE", "TITLE", "START",
# 		"USING", "WXTRN","XATTR"]

psuedo_op_table = ["USING", "START", "END", "DROP", "LTORG", "DS", "DC", "EQU"]
mach_ops = ["L", "LR", "LA", "A", "AR", "ST", "SR", "C", "BNE", "BR"]
sym_table = []
lit_table = []
base_table = []
int_code = []
obj_code = []
#endregion


def first_pass():

	source_file = open("sample.txt", "r")
	sent_tokens = source_file.readlines()
	LC = 0
	BR = 0
	IR = 0
	sym_index = 0
	lit_index = 0
	inst_length = 0
	label = ""

	for sent in sent_tokens:

		code_seg = {"Relative_Addr": -1, "Mnemonic": "-", "Memory_Addr": "-", "Index": "-"}
		sent = sent.strip()
		sent = sent.replace(", ", ",")
		if(';' in sent):
			sent = re.sub(';.*', '', sent)

		word_tokens = re.findall(r"[\S]+", sent)

		#print word_tokens

		if(word_tokens.__len__() == 3):
			label = word_tokens[0]
			op = word_tokens[1]
			operands = word_tokens[2].split(',')
			if not any(s["Symbol"] == label for s in sym_table) and op != "START":
				sym_index+=1
				if(op != "DC" or op!="DS" or op!="EQU"):
					sym_table.append({"Si": sym_index, "Symbol": label, "Value": LC, "Length": 4, "Relocation": "R" })
				else:
					sym_table.append({"Si": sym_index, "Symbol": label, "Value": '-', "Length": 4, "Relocation": "R" })

		elif(word_tokens.__len__() >= 2):
			op = word_tokens[0]
			operands = word_tokens[1].split(',')
		else:
			op = word_tokens[0]

		code_seg["Relative_Addr"] = LC
		code_seg["Mnemonic"] = op

		if (op in psuedo_op_table):  # POTGET1
			if (op == "USING"):
				if(operands[0] == '*'):
					IR = LC
				else:
					IR = int(operands[0])
				BR = int(operands[1])

			elif (op ==  "LTORG"):
				if (LC % 8 != 0):
					LC += (8 - LC % 8)
				init_addr = LC
				for lit in lit_table:
					lit["Addr"] = init_addr
					if("F\'" or "A(" in lit["Symbol"]):
						lit["Length"] = 4
					# elif() Half word / Double Word if req
					init_addr += lit["Length"]
					LC += lit["Length"]



			elif (op == "DS"):
				for s in sym_table:
					if (s["Symbol"] == label):
						s["Length"] = 4
						s["Value"] = LC
						s["Relocation"] = "R"
				LC += int(operands[0].replace("F", "")) * 4

			elif (op == "DC"):
				for s in sym_table:
					if (s["Symbol"] == label):
						s["Length"] = 4
						s["Value"] = LC
						s["Relocation"] = "R"
				LC += 4


			elif (op == "EQU"):
				for s in sym_table:
					if(s["Symbol"] == label):
						s["Length"] = 1
						if(operands[0] == '*'):
							s["Value"] = LC
							s["Relocation"] = "R"
						else:
							s["Value"] = operands[0]
							s["Relocation"] = "A"

			elif (op == "START"):
				if not any(s["Symbol"] == label for s in sym_table):
					sym_index += 1
					sym_table.append({"Si": sym_index, "Symbol": label, "Value": operands[0], "Length": 1, "Relocation": "R"})
			# "END", "DROP"

		elif(op in mach_ops): #MOTGET1
			mot_entry = [mo for mo in mach_op_table if mo["Mnemonic"] == op ][0]
			inst_length = mot_entry["Length"]
			mne_memaddr = ""
			for operand in operands:
				if '=' in operand:
					if not any(l["Symbol"] == operand.replace("=", "") for l in lit_table):
						lit_index+=1
						lit_table.append({"Li": lit_index, "Symbol": operand.replace("=", ''), "Addr": "-", "Length": -1,
							 "Relocation": 'R'})
						mne_memaddr += '-' + '('+str(IR)+','+str(BR)+') ; #L'+str(lit_index)+','

				if operand.isupper() and operand.isalnum():
					for s in sym_table:
						if (s["Symbol"] == operand):
							# s["Value"] = LC
							mne_memaddr += str(s["Value"]) + '('+str(IR)+','+str(BR)+') ; #S'+str(s["Si"])+','

					if not any(s["Symbol"] == operand for s in sym_table):
						sym_index += 1
						sym_table.append({"Si": sym_index, "Symbol": operand, "Value": "-", "Length": 4, "Relocation": "R"})
						mne_memaddr += '-' + '('+str(IR)+','+str(BR)+') ; #S'+str(sym_index)+','

				elif operand.isdigit():
					mne_memaddr += str(operand) + ','

			LC += inst_length
			code_seg["Memory_Addr"] = mne_memaddr.rstrip(',')
		if(op =="DC" or op == "DS"):
			code_seg["Memory_Addr"] = operands[0]
		if(op != "LTORG" and op != "EQU"):
			int_code.append(code_seg)

	#region Output Generation

	print("Intermediate code after pass 1 :- \n")
	print('{:20}'.format("Relative Address"), '{:20}'.format("Mnemonic"),'{:20}'.format("Memory_Addr"))
	for x in int_code:
		print('{:20}'.format(str(x["Relative_Addr"])), '{:20}'.format(x["Mnemonic"]),'{:20}'.format(x["Memory_Addr"]))

	print("\n\nSymbol Table :- \n")
	print('{:5}'.format("Si"), '{:20}'.format("Symbol"), '{:20}'.format("Value"), '{:20}'.format("Length"), '{:20}'.format("Relocation") + '\n')
	for x in sym_table:
		print('{:5}'.format(str(x["Si"])),'{:20}'.format(x["Symbol"]), '{:20}'.format(str(x["Value"])), '{:20}'.format(str(x["Length"])), '{:20}'.format(x["Relocation"]))

	print("\n\nLiteral Table :- \n")
	print('{:5}'.format("Li"),'{:20}'.format("Symbol"), '{:20}'.format("Addr"), '{:20}'.format("Length"), '{:20}'.format("Relocation") + '\n')
	for x in lit_table:
		print('{:5}'.format(str(x["Li"])), '{:20}'.format(x["Symbol"]), '{:20}'.format(str(x["Addr"])), '{:20}'.format(str(x["Length"])), '{:20}'.format(x["Relocation"]))

	#endregion

	if(op == "END"):
		second_pass()


def second_pass():

	for code_seg in int_code:
		if(code_seg["Memory_Addr"] != '-'):
			if(';' and "#S" in code_seg["Memory_Addr"]):
				sym_index = re.findall('#S(\d)', code_seg["Memory_Addr"])
				for s in sym_table:
					if(s["Si"] == int(sym_index[0])):
						code_seg["Memory_Addr"] = code_seg["Memory_Addr"].replace('-', str(s["Value"]))
			elif (';' and "#L" in code_seg["Memory_Addr"]):
				lit_index = re.findall('#L(\d)', code_seg["Memory_Addr"])
				for l in lit_table:
					if (l["Li"] == int(lit_index[0])):
						code_seg["Memory_Addr"] = code_seg["Memory_Addr"].replace('-', str(l["Addr"]))
			code_seg["Memory_Addr"] = re.sub(';.*', '', code_seg["Memory_Addr"])

			if code_seg["Mnemonic"] not in psuedo_op_table:
				mot_entry = [mo for mo in mach_op_table if mo["Mnemonic"] == code_seg["Mnemonic"]][0]
				code_seg["Mnemonic"] = re.sub('.*', mot_entry["Hex_Code"], code_seg["Mnemonic"])

			elif "DS" in code_seg["Mnemonic"] or "DC" in code_seg["Mnemonic"]:
				int_value = re.findall('\D*(\d+)\D*', code_seg["Memory_Addr"])
				code_seg["Mnemonic"] = re.sub('X', '0'*(8 - hex(int(int_value[0])).__len__()), hex(int(int_value[0])).upper())
				code_seg["Mnemonic"] = 'X\'' + code_seg["Mnemonic"] + '\''
				code_seg["Memory_Addr"] = '-'

			obj_code.append(code_seg)

	print("\n\n Object code after pass 2 :- \n")
	print('{:20}'.format("Relative Address"), '{:20}'.format("Hex Code"), '{:20}'.format("Memory_Addr"))
	for x in obj_code:
		print('{:20}'.format(str(x["Relative_Addr"])), '{:20}'.format(x["Mnemonic"]), '{:20}'.format(x["Memory_Addr"]))

first_pass()


