from sklearn.metrics import f1_score
import re

def word_order(word):
	temp = ""
	#print(word,len(word))
	for i in range(len(word)):
		if ord(word[i])>122:
			res = (re.sub('.', lambda x: r'\u%04X' % ord(x.group()), word[i]))
			temp += res.lower()
			#print(res)
		else:
			temp += word[i]
	return temp.lower()

p_true_positive = 0 
p_false_negative = 0
p_false_positive = 0

dict_verb = {}
dict_noun = {}
dict_person = {}

file_name = "noun.csv"
j = 0
k =0
with open(file_name, 'r', encoding='utf-8',  errors='ignore') as f:
	for line in f:
		inputsent = line.split("\n")[0].split(",")
		if k < 5:
			k += 1
			continue
		if inputsent[1] == "xt?":
			continue
	
		gen = str(inputsent[1].split(" ")[2])
		gender = gen[0] + "."
		number = inputsent[1].split(" ")[1]
		vachan = inputsent[1].split(" ")[0].lower()
		morph = str(gender) + " " + str(number) + " " + str(vachan)
		dict_noun[morph] = inputsent[0]
		nvachan = vachan[0] + "."
		nmorph = str(gender) + " " + str(number) + " " + str(nvachan)
		dict_noun[nmorph] = inputsent[0]

file_name = "verb.csv"
with open(file_name, 'r', encoding='utf-8',  errors='ignore') as f:
	for line in f:
		inputsent = line.split("\n")[0].split(",")
		verb = inputsent[2].split(" ")
		if len(verb) == 3 and verb[1] == "[*]":
			for j in range(11):
				verb[1] = "["+str(j)+"]"
				verb[2] = "ac."
				nverb = " ".join(verb)
				dict_verb[nverb] = inputsent[1]
				verb[2] = "md."
				nnverb = " ".join(verb)
				dict_verb[nnverb] = inputsent[1]
		elif len(verb) == 3 and verb[2] == "ac./ps./md.":
			verb[2] = "ac."
			nverb = " ".join(verb)
			dict_verb[nverb] = inputsent[1]
			verb[2] = "ps."
			nverb = " ".join(verb)
			dict_verb[nverb] = inputsent[1]
			verb[2] = "md."
			nverb = " ".join(verb)
			dict_verb[nverb] = inputsent[1]
		elif len(verb) == 2 and verb[1] == "ac./ps./md.":
			verb[1] = "ac."
			nverb = " ".join(verb)
			dict_verb[nverb] = inputsent[1]
			verb[1] = "ps."
			nverb = " ".join(verb)
			dict_verb[nverb] = inputsent[1]
			verb[1] = "md."
			nverb = " ".join(verb)
			dict_verb[nverb] = inputsent[1]
		else:
			dict_verb[inputsent[2]] = inputsent[1]
dict_noun["iic."] = str(3)
dict_noun["prep."] = str(2)
dict_noun["adv."] = str(2)
dict_noun["conj."] = str(2)
dict_noun["part."] = str(2)
dict_noun["tasil"] = str(2)
dict_noun["ind."] = str(1)
dict_noun["iiv."] = str(3)
dict_noun["ca. abs."] = str(-230)
dict_noun["abs."] = str(-230)
dict_noun["ca. inf."] = str(-220)
dict_noun["pft. md. sg. 1"] = str(-151)
dict_noun["pft. md. sg. 3"] = str(-153)
dict_noun["ca. per. pft."] = str(-150)
dict_noun["impft. [vn.] ac. sg. 2"] = str(-42)
dict_noun["impft. [vn.] ac. sg. 1"] = str(-41)
dict_noun["ca. impft. ac. sg. 2"] = str(-42)
dict_noun["ca. impft. ac. sg. 3"] = str(-43)
dict_noun["ca. impft. ac. pl. 1"] = str(-47)
dict_noun["impft. ac. pl. 3"] = str(-49)
dict_noun["impft. [2] ac. sg. 3"] = str(-43)
dict_noun["ca. impft. ac. pl. 3"] = str(-49)
dict_noun["ca. impft. ps. sg. 1"] = str(-271)
dict_noun["ca. imp. ac. sg. 2"] = str(-32)
dict_noun["ca. imp. ac. sg. 3"] = str(-33)
dict_noun["pr. [vn.] md. sg. 1"] = str(-11)
dict_noun["int. pr. md. sg. 3"] = str(-13)
dict_noun["ca. pft. ac. pl. 3"] = str(-159)
dict_noun["ca. pft. ac. sg. 3"] = str(-153)
dict_noun["int. pft. md. sg. 1"] = str(-11)
dict_noun["imp. [vn.] ac. sg. 2"] = str(-32)
dict_noun["ca. imp. ac. pl. 1"] = str(-47) 
dict_noun["ca. pr. ps. sg. 1"] = str(-241)
dict_noun["ca. pr. ps. pl. 3"] = str(-249)
dict_noun["pr. ps. pl. 3 vac"] = str(-249)
dict_noun["pr. ps. pl. 3"] = str(-249)
dict_noun["ca. fut. ac. sg. 3"] = str(-53)
dict_noun["ca. per. fut. ac. sg. 3"] = str(-53)
dict_noun["ca. fut. ac. sg. 1"] = str(-51)
dict_noun["ca. fut. ac. sg. 2"] = str(-52)
dict_noun["fut. ac. sg. 3"] = str(-53)
dict_noun["ca. opt. ac. sg. 3"] = str(-23)
dict_noun["aor. [6] ac. sg. 3"] = str(-123)
dict_noun["aor. [2] ac. sg. 3."] = str(-123)



dict_person = {"sg. 1" : 1 , "sg. 2" : 2 , "sg. 3" : 3 , "du. 1" : 4 , "du. 2" : 5, "du. 3" : 6, "pl. 1" : 7,"pl. 2" : 8, "pl. 3" : 9 }

def morhophology(morph):
	temp = morph.split(" ")
	if temp[0] == "*":
		morph = "m. " + temp[1] + " " + temp[2]
	if len(temp) == 3:
		nmorph = temp[0] + " " + temp[1] + " " + temp[2]
		if nmorph in dict_noun.keys():
			return (int(dict_noun[nmorph]))
	if morph in dict_noun.keys():
		return (int(dict_noun[morph]))
	elif morph in dict_verb:
		temp = int((-1) * (int(dict_verb[morph]) * 10))
		return(int(temp))
	elif len(morph.split(" ")) == 5:
		verbs = morph.split(" ")
		pre_verb = " ".join(verbs[:3])
		post_verb = " ".join(verbs[3:])
		# for i in range(5):
		# 	if verbs[i][0] == '[':
		# 		verbs[i] = ""
		# pre_verb = " ".join((" ".join(verbs[:3])).split(" "))
		# post_verb = " ".join((" ".join(verbs[3:])).split(" "))
		if pre_verb in dict_verb and post_verb in dict_person:
			pre_numb = int((-1) * ((int(dict_verb[pre_verb]) * 10) + int(dict_person[post_verb])))
			return (int(pre_numb))
		else:
			print(len(morph),morph)
			return (-1)
	elif len(morph.split(" ")) == 4:
		verbs = morph.split(" ")
		pre_verb = " ".join(verbs[:2])
		post_verb = " ".join(verbs[2:])
		# for i in range(4):
		# 	if verbs[i][0] == '[':
		# 		verbs[i] = ""
		# pre_verb = " ".join((" ".join(verbs[:2])).split(" "))
		# post_verb = " ".join((" ".join(verbs[2:])).split(" "))
		if pre_verb in dict_verb and post_verb in dict_person:
			pre_numb = int((-1) * ((int(dict_verb[pre_verb]) * 10) + int(dict_person[post_verb])))
			return (int(pre_numb))
		else:
			print(len(morph),morph)
			return (-1)
	else:
		print(len(morph),morph)
		return(-1)

count_true = 0
count_pred = 0
j = 0
utt_list = []
file_name = "best/newbest.txt"
with open(file_name, 'r', encoding='utf-8',  errors='ignore') as f:
	for line in f:
		word = line.split("\n")[0].split(" ")
		utt_list.append(word[0])

for i in range(0,500):
	file_name = "devraj/"+str(i)+".csv"
	flag = 0
	list_true = []
	dict_true = {}
	with open(file_name, 'r', encoding='utf-8',  errors='ignore') as f:
		for line in f:
			if flag == 0:
				flag = 1
				continue
			word = line.split("\n")[0].split(";")
			word_form = word_order(word[0])
			lemma = word_order(word[1])
			morpho = word[2]
			list_true.append(word_form)
			dict_true[word_form] = lemma +";"+str(morhophology(morpho))
	
	flag_ = 0
	max_true_positive = 0 
	max_false_negative = 0
	max_false_positive = 0
	max_fscore = 0
	utt_index = ""
	count = 0
	for k in range(10):
		count += 1
		if j+k >= 4732:
			break
		utt = utt_list[j+k]
		utt_grp = "-".join(utt.split("-")[:-1])
		#print(i,j,k,utt_grp,utt)
		if k == 0:
			pre_utt_grp = utt_grp
		if pre_utt_grp != utt_grp:
			j = j + count - 1
			p_true_positive += max_true_positive
			p_false_negative += max_false_negative
			p_false_positive += max_false_positive
			flag_ = 1
			break
		file_name = "best_csv/"+str(j+k)+".csv"
		flag = 0
		list_pred = []
		dict_pred = {}
		with open(file_name, 'r', encoding='utf-8',  errors='ignore') as f:
			for line in f:
				if flag == 0:
					flag = 1
					continue
				word = line.split("\n")[0].split(";")
				word_form = word[0]
				lemma = word[1]
				morpho = word[2]
				list_pred.append(word_form)
				dict_pred[word_form] = lemma +";"+morpho
		
		#True Comparison
		true_positive = 0
		false_positive = 0
		false_negative = 0
		for x in list_true:
			if x in list_pred:
				true_positive += min(list_pred.count(x),list_true.count(x))
			else:
				false_negative += 1
		for x in list_pred:
			if x in list_true:
				continue
			else:
				false_positive += 1
		recall = float(true_positive/(true_positive+false_negative))
		precision = float(true_positive/(true_positive+false_positive))
		if precision == 0 and recall == 0:
			f_score = 0
		else:
			f_score = float((2*recall*precision)/(recall+precision))
		#print(i,j,k,utt_grp,utt,f_score)
		if f_score > max_fscore:
			utt_index = utt
			max_fscore = f_score
			max_true_positive = true_positive
			max_false_positive = false_positive
			max_false_negative = false_negative
	if flag_ == 1:
		print(i,j,utt_index,pre_utt_grp,max_fscore)
		#print(utt_index)
		continue
	else:
		j = j + count
		p_true_positive += max_true_positive
		p_false_negative += max_false_negative
		p_false_positive += max_false_positive
		print(i,j,utt_index,count,pre_utt_grp,max_fscore)
		#print(utt_index)
	if j+k >= 4732:
		break
recall = float(p_true_positive/(p_true_positive+p_false_negative))
precision = float(p_true_positive/(p_true_positive+p_false_positive))
f_score = float((2*recall*precision)/(recall+precision))

print(f_score)
