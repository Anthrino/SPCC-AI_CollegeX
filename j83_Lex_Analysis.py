# Lexical Analyser for C
import re

ident_list = []
kw_list = []
op_list = []
header_files = []
func_list = []
sp_char = []
punctuations = []
strings = []
flag = 0
kws = ["auto", "break", "case", "char", "continue", "do", "default", "const",
       "double", "else", "enum", "extern", "for", "if", "goto", "float", "int",
       "long", "register", "return", "signed", "static", "sizeof", "short", "struct",
       "switch", "typedef", "union", "void", "while", "volatile", "unsigned"]

ops = ["*", "/", "%", "+", "-", "->", ".", "++", "--", "<<", ">>", "<", "<=", ">", ">=", "==", "!=", "&", "^", "|",
       "&&", "||", "?:", "=", "+=", "-=", "*=", "/=", "%=", ">>=", "<<=", "&=", "^=", "|="]

punct = ['(', ')', '[', ']', '{', '}', ',', ';', '"', '""', '*', ':']

source_file = open("sample9.c", 'r')

sent_tokens = source_file.readlines()


def mark_Keyword(sent, word_tokens):
	for word in word_tokens:
		if (word in kws):
			kw_list.append(word)
			sent = sent.replace(word, "", 1)
	return sent


def mark_Identifier(sent, word_tokens):
	for word in word_tokens:
		if (word not in func_list and word not in header_files and word not in kws and str.isalpha(word) and word not in ident_list):
			ident_list.append(word)
			sent = sent.replace(word, "", 1)
	return sent


def mark_Function(sent):
	if (re.match('.*\(.*\)', sent)):
		w = re.findall('(.*)\(.*\)', sent)
		v = re.findall('\((.*)\)', sent)
		# print("///W ")
		# print(w)
		# print("///v ")
		# print(v)
		sent = sent.replace('(', "")
		sent = sent.replace(')', "")
		if v:
			for x in v:
				mark_Function(x)
				symbs = re.findall(r"[\W]+", x)
				for symb in symbs:
					mark_Operators(sent,symb)

		# print("//Function Name  : ")
		# print(w)

		for x in w:
			x = x.strip()
			if (x not in kws and ' ' not in x and x not in punct and x):
				func_list.append(x)
			else:
				sent = mark_Punct(sent, '(')
				sent = mark_Punct(sent, ')')
	return sent


def mark_Preprocessor(sent):
	if ("#include" in sent):
		sp_char.append("#")
		ident_list.append("include")
		header_files.append(word_tokens[1] + ".h")
		punct.append("<")
		punct.append(">")
		sent = " "
	return sent


def mark_Operators(sent, symbol):
	for x in punct:
		if (x in symbol):
			sent = mark_Punct(sent, x)
			symbol = symbol.replace(x, "")
	symbol = symbol.replace(" ","")
	# print("//MODDED " +symbol)

	if (symbol in ops):
		op_list.append(symbol)
		return sent.replace(symbol, "", 1)
	elif (symbol in ['$']):
		sp_char.append(symbol)
		return sent.replace(symbol, "", 1)

	return sent

def mark_Punct(sent, symbol):
	punctuations.append(symbol)
	sent = sent.replace(symbol, "", 1)
	return sent

def mark_String(temp, sent):
	if ('\"' in temp):
		w = re.split('\".*\"', temp)
		for x in w:
			# print(x)
			temp = temp.replace(x, "")
		if ("\\n" in temp):
			# temp = temp.replace("\\n", "")
			sp_char.append("\n")
		if ("\\t" in temp):
			# temp = temp.replace("\\t", "")
			sp_char.append("\t")

		# print("// String :"+ temp)
		strings.append(temp)
		sent = sent.replace(temp, "")
	return sent
	# print("// String :"+ sent)


for sent in sent_tokens:

	if("/*" in sent):
		flag = 1
		continue
	if ("*/" in sent and flag == 1):
		flag = 0
		continue
	if("//" in sent or flag == 1):
		continue
	if flag == 0:
		sent = sent.replace("\t", "")
		temp = sent = sent.strip()
		word_tokens = re.findall(r"[\w]+", sent)
		symbols = re.findall(r"[\W]+", sent)

		sent = mark_String(temp, sent)
		sent = mark_Preprocessor(sent)
		word_tokens = re.findall(r"[\w]+", sent)

		sent = mark_Keyword(sent, word_tokens)
		sent = mark_Function(sent)
		sent = mark_Identifier(sent, word_tokens)

		for symbol in symbols:
			# print(symbol)
			sent = mark_Operators(sent, symbol)
		# print(sent)

print("\n Header Files : ")
print(header_files)
print("\n Identifiers : ")
print(ident_list)
print("\n Keywords : ")
print(kw_list)
print("\n Operators : ")
print(op_list)
print("\n Funtion Names : ")
print(func_list)
print("\n Special Characters : ")
print(sp_char)
print("\n Punctuators : ")
print(punctuations)
print("\n String statements : ")
print(strings)

# sampletext = "This is the \"\n regex tester\n to determine\n text behaviour\""+"\n"
# sampletext.replace("\".*\"", "")
# print(sampletext
# re.findall('\".*\"', sampletext)
