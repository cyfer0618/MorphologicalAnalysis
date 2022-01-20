import json
import numpy as np
import io, re

text_list = []
for i in range(1,16):
	# if i == 16:
	# 	i = "remove"
	file_name = "old_text/text/new_"+str(i)+".txt"
	with open(file_name, 'r', encoding='utf-8',  errors='ignore') as f:
		for line in f:
			word = line.split("\n")[0].split(" ")
			text_list.append(" ".join(word[1:-1]))
			#print(utt_grp)
			#exit(1)

new_text_list = []
for i in range(1,2):
	# if i == 16:
	# 	i = "remove"
	file_name = "best/rem_nbest.txt"
	with open(file_name, 'r', encoding='utf-8',  errors='ignore') as f:
		for line in f:
			word = line.split("\n")[0]
			new_text_list.append(word)

ebm_list = []
dict_ebm = {}
for i in range(1,2):
	# if i == 16:
	# 	i = "remove"
	file_name = "old_ebm/new_"+str(i)+"/ebm.json"
	file_name = "extra.json"
	print(file_name)
	with open(file_name, 'r', encoding='utf-8',  errors='ignore') as f:
		for line in f:
			word = line.split("\n")[0].split(" ")[1]
			line_num = int("".join(word[1:-2]))
			#print(line_num)
			list_ = line.split("\n")[0].split("'nodeslist': ")[1]
			dict_ = list_[:-2]
			new_word = dict_.split(", ")
			dict_ebm[(i-1)*2000+int(line_num)] = []
			for j in range(len(new_word)):
				try:
					morph = re.search('@\((.+?)\)', new_word[j]).group(1)
					lemma = re.search('(.+?)@', new_word[j]).group(1)
					word_form = re.search('=>(.+?)]', new_word[j]).group(1)
					string = word_form.replace(" ", "")  +";"+ lemma.replace(" ", "")  + ";" +str(morph)
					dict_ebm[(i-1)*2000+int(line_num)].append(string)
					print(string)
				except AttributeError:
					pass
			#exit(1)
			print()
exit(1)


new_ebm_list = []
new_dict_ebm = {}
for i in range(1,3):
	# if i == 16:
	# 	i = "remove"
	file_name = "old_ebm/newbest_"+str(i)+"/ebm.json"
	#file_name = "extra.json"
	print(file_name)
	with open(file_name, 'r', encoding='utf-8',  errors='ignore') as f:
		for line in f:
			word = line.split("\n")[0].split(" ")[1]
			line_num = int("".join(word[1:-2]))
			#print(line_num)
			list_ = line.split("\n")[0].split("'nodeslist': ")[1]
			dict_ = list_[:-2]
			new_word = dict_.split(", ")
			new_dict_ebm[(i-1)*2000+int(line_num)] = []
			for j in range(len(new_word)):
				try:
					morph = re.search('@\((.+?)\)', new_word[j]).group(1)
					lemma = re.search('(.+?)@', new_word[j]).group(1)
					word_form = re.search('=>(.+?)]', new_word[j]).group(1)
					string = word_form.replace(" ", "")  +";"+ lemma.replace(" ", "")  + ";" +str(morph)
					new_dict_ebm[(i-1)*2000+int(line_num)].append(string)
					#print(string)
				except AttributeError:
					pass
			#exit(1)
			#print()
#exit(1)


file_name = "best/best.txt"
i = 0
count = 0
flag = 1
with open(file_name, 'r', encoding='utf-8',  errors='ignore') as f:
	for line in f:
		word = line.split("\n")[0]
		if word in text_list:
			ind = text_list.index(word)
			yfile = open("best_csv/"+str(i)+".csv", 'w+', encoding='utf-8')
			yfile.write("word;lemma;morphology\n")
			if ind not in dict_ebm.keys():
				count += 1
				print("1",word)
				i += 1
				continue
			for j in range(len(dict_ebm[ind])):
				yfile.write(dict_ebm[ind][j]+"\n")
		elif word in new_text_list:
			ind = new_text_list.index(word)
			yfile = open("best_csv/"+str(i)+".csv", 'w+', encoding='utf-8')
			yfile.write("word;lemma;morphology\n")
			if ind not in new_dict_ebm.keys():
				count += 1
				print("2",word)
				i += 1
				continue
			for j in range(len(new_dict_ebm[ind])):
				#print("2")
				yfile.write(new_dict_ebm[ind][j]+"\n")
		else:
			count += 1
			print("3",word)

		i+=1
print(count)