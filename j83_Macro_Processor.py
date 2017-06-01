import re

source_file = open('macro_sample.txt','r')
sent_tokens = source_file.readlines()

def pass1():

	macro_name_table, arg_list_arr, alas, macro_def_table = ([] for i in range(4))
	mdt_index, mnt_index, ala_index = (0 for i in range(3))
	int_code = ""

	for sent in sent_tokens:

		mdt_entry = {'Index': 0, 'Definition': "null"}
		mnt_entry = {'Index': 0, 'Macro Name': "null", 'MDT Index': 0}
		ala_entry = {'Index': 0, 'Argument': "null", 'Value': '-'}
		sent = sent.strip()
		sent = sent.replace(", ", ",")
		if(';' in sent):
			sent = re.sub(';.*', '', sent)

		word_tokens = re.findall(r"[\S]+", sent)

		if("MACRO" in sent):
			flag = 1
			continue

		if flag == 0:
			int_code += sent+"\n"

		if flag >= 1:
			# sent = sent.replace("\t", " ")
			mdt_index += 1
			mdt_entry = {'Index': mdt_index, 'Definition': sent}
			macro_def_table.append(mdt_entry)
			if flag == 1:
				macro_name = word_tokens[0]
				mnt_index += 1
				operands = word_tokens[1].split(',')
				mnt_entry = {'Index': mnt_index, 'Macro Name': macro_name, 'MDT Index': mdt_index}
				macro_name_table.append(mnt_entry)
				for operand in operands:
					ala_index += 1
					if '=' in operand:
						ala_entry = {'Index': ala_index, 'Argument': re.findall('(.*)=', operand)[0],
						             'Value': re.findall('=(.*)', operand)[0]}
					else:
						ala_entry = {'Index': ala_index, 'Argument': operand, 'Value': '-'}
					alas.append(ala_entry)
				arg_list_arr.append(alas)
			flag += 1

		if "MEND" in sent:
			flag = 0
			alas = []
			ala_index = 0

	print("\nIntermediate code after pass 1 :- \n")
	print(int_code)

	# region Output Code Pass 1
	print("\n\nMacro Name Table :- \n")
	print('{:10}'.format("Index"), '{:20}'.format("Macro Name"), '{:20}'.format("MDT Index"))
	for x in macro_name_table:
		print('{:10}'.format(str(x["Index"])), '{:20}'.format(x["Macro Name"]), '{:20}'.format(str(x["MDT Index"])))

	for alas in arg_list_arr:
		print("\n\nArgument List Array for "+macro_name_table[arg_list_arr.index(alas)]["Macro Name"]+":- \n")
		print('{:10}'.format("Index"), '{:20}'.format("Argument"), '{:20}'.format("Value"))
		for x in alas:
			print('{:10}'.format(str(x["Index"])), '{:20}'.format(x["Argument"]), '{:20}'.format(x["Value"]))

	print("\n\nMacro Definition Table :- \n")
	print('{:10}'.format("Index"), '{:20}'.format("Definiton"))
	for x in macro_def_table:
		print('{:10}'.format(str(x["Index"])), '{:20}'.format(x["Definition"]))

	#endregion

	pass2(int_code, macro_name_table, macro_def_table, arg_list_arr)

def pass2(int_code, macro_name_table, macro_def_table, arg_list_arr):
	fin_code = ""
	sent_tokens = int_code.split('\n')
	for sent in sent_tokens:
		# sent = sent.replace('\t', " ")
		word_tokens = re.findall(r"[\S]+", sent)
		flag = -1
		for word in word_tokens:
			mnt_entries = [mnt for mnt in macro_name_table if mnt["Macro Name"] == word]
			if len(mnt_entries)>0:
				mnt_entry = mnt_entries[0]
				flag = 1
				continue
			if flag == 1:
				operands = word
				ops = operands.split(',')

				for ala_entry in arg_list_arr[mnt_entry["Index"]-1]:
					if ala_entry["Index"] <= len(ops):
						ala_entry["Value"] = ops[ala_entry["Index"]-1]
				for mdt_entry in macro_def_table:
					if mdt_entry["Index"] == mnt_entry["MDT Index"]:
						flag = 2
						continue
					if mdt_entry["Index"] >= mnt_entry["MDT Index"] and 'MEND' in mdt_entry["Definition"]:
						flag = 1
						break
					if flag == 2:
						sent = mdt_entry["Definition"]
						for ala_entry in arg_list_arr[mnt_entry["Index"]-1]:
							if ala_entry["Argument"] in mdt_entry["Definition"]:
								sent = sent.replace(ala_entry["Argument"], ala_entry["Value"])
						fin_code += sent +'\n'
				flag = 0
		if flag == -1:
			fin_code += sent +'\n'

	# region Output pass 2
	print("\n\nArgument List Arrays for Pass 2 :- ")
	for alas in arg_list_arr:
		print("\nArgument List Array for "+macro_name_table[arg_list_arr.index(alas)]["Macro Name"]+":- \n")
		print('{:10}'.format("Index"), '{:20}'.format("Argument"))
		for x in alas:
			print('{:10}'.format(str(x["Index"])), '{:20}'.format(x["Value"]))
	print("\nOutput Code after second pass :- \n")
	print(fin_code)

	# endregion

pass1()