# First and Follow parser for a given grammar

source_file = open("grammar.txt", "r")
grammar = source_file.readlines()
non_terms = []
prods = []
firsts = []
first_elems = []
follow_elems = []
follows = []

print("\nSymbol reference : id = '#', epsilon = '@' \n\nGrammar:- \n")

for x in grammar:
	print(x)

#First/Follows parsing recursive function
def ff_parser(key, value, lister, mode):
	if value in non_terms:
		lister.pop(lister.index({key: value}))
		elem = [x for x in lister if x.keys()[0] == value]
		for x in elem:
			lister = ff_parser(value, x.values()[0], lister, mode)
		elem = [x for x in lister if x.keys()[0] == value]
		if mode == 0:
			for x in elem:
				z = x.values()[0]
				y = {key: z}

				if z == '@':
					index = 1
					for item in [p.values()[0].split('|') for p in prods if p.keys()[0] == key]:
						for p in item:
							z = p[index]
							y = {key: z}
							if y not in firsts:
								lister.append(y)
				elif y not in firsts:
					lister.append(y)
		else:
			for x in elem:
				y = {key: x.values()[0]}
				if y not in lister:
					lister.append(y)
	return lister


# Splitting productions to create initial firsts list
for prod in grammar:
	prod = prod.replace(' ', '').replace('\n', '').replace('id', '#')
	items = prod.split("->")
	non_terms.append(items[0])
	prods.append({items[0]: items[1]})
	if '|' in items[1]:
		for item in items[1].split('|'):
			first_elems.append({items[0]: item[0]})
			firsts.append({items[0]: item[0]})
	else:
		first_elems.append({items[0]: items[1][0]})
		firsts.append({items[0]: items[1][0]})

# Resolving non-terminals present in the firsts list using recursive calls
for elem in first_elems:
	key = elem.keys()[0]
	value = elem.values()[0]
	if elem in firsts:
		firsts = ff_parser(key, value, firsts, 0)
	# print elem

# Splitting productions to create initial follows list
for prod in prods:
	if prod == prods[0]:
		follows.append({prod.keys()[0]: '$'})
		follow_elems.append({prod.keys()[0]: '$'})
	for item in prod.values()[0].split('|'):
		flag = '<:>'
		for c in item:
			if '<:>' not in flag and c in non_terms:
				elem = [x for x in firsts if x.keys()[0] == c]
				for x in elem:
					q = x.values()[0]
					if q != "@" and {flag: q} not in follows:
						follows.append({flag: q})
						follow_elems.append({flag: q})
			if '<:>' not in flag and {flag: c} not in follows:
				follows.append({flag: c})
				follow_elems.append({flag: c})
				flag = '<:>'
			if c in non_terms:
				flag = c
		if '<:>' not in flag:
			follows.append({flag: prod.keys()[0]})
			follow_elems.append({flag: prod.keys()[0]})

# Resolving non-terminals present in the follows list using recursive calls
for elem in follow_elems:
	key = elem.keys()[0]
	value = elem.values()[0]
	if elem in follows:
		follows = ff_parser(key, value, follows, 1)

# print firsts
# print prods
# print follows

def printer(lister, str):
	lister.sort()

	print("\n\n"+str+" for the productions :- ")
	non = ""
	for elem in lister:
		if non != elem.keys()[0]:
			non = elem.keys()[0]
			print("\n"+non+" => " + elem.values()[0],)
		else:
			print(", " + elem.values()[0],)

printer(firsts, "Firsts")
printer(follows, "Follows")
