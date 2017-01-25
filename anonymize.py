#to run python3 in windows7, in terminal type in, e.g.
#py -3 part2.py

import re
import json
import random

if __name__ == '__main__':
	f = open("mbox.txt")

#collect email address
email_lst = []

for i in f:
	line = i.rstrip()
	line = line.replace("<", "").replace(">", "").replace(";", "").replace(")", "")
	#to find all email address that contain @ and '.' 
	x = re.findall('\S+@[a-z]+\.\S+', line)
	if len(x) > 0:
		for i in x:
			#only keep email address beginning with letter
			m = re.search('^[a-z]',i) 
			if m:
				if i not in email_lst:
					email_lst.append(i)
print (email_lst)

#to check email address
# file_lines = open("mbox_d.txt","w")
# file_lines.write(json.dumps(email_lst))
# file_lines.close()

#assign each key with unique random ID
randome_lst = random.sample(range(10001, 10001+len(email_lst)), len(email_lst))
d_email_id = dict(zip(email_lst, randome_lst))

print (d_email_id)

#to check email address and their ID
# file_lines = open("mbox_d2.txt","w")
# file_lines.write(json.dumps(d_email_id))
# file_lines.close()

str_f = open("mbox.txt").read()  #the str_f can be printed  well formated in gitbash
#for check the type of f
# file_lines = open("mbox-f.txt","w")
# file_lines.write(str_f)
# file_lines.close()
#print (type(f)) #str

for k in d_email_id:
	#use same name so can input replaced string for each different k
	#replace email address with %%emailID%%
	str_f = str_f.replace(k,"%%{}%%".format(str(d_email_id[k])))

#write email address replaced with ID
file_lines = open("mbox-anon.txt","w")
file_lines.write(str_f)
file_lines.close()

# Write the mapping from anon ID to email address to mbox-anon-key.txt
str_f2 = str(open("mbox-anon.txt").read())
# print (str_f2.replace('100', 'hahaha'))

for k in d_email_id:
	# print (d_email_id[k])
	# print (type(d_email_id[k]))
	#use same name so can input replaced string for each different k
	#replace the str begin and end with %% and with number in the center to email address
	# str_f3 = re.sub(r'%%k%%',k,str_f2)
	# my_regex = r"%%" + re.escape(str(d_email_id[k])) + r"%%"
	# str_f3 = re.sub(my_regex,k,str_f2)
	str_email_id = str(d_email_id[k])
	# print (type(str_email_id))
	# str_f3 = str_f2.replace('%%%%s%%%%' % str_email_id, k)
	# str_f3 = str_f2.replace('%%' + str_email_id + '%%', k)
	# str_f3 = re.sub(r'%%{0}%%'.format(str_email_id),k,str_f2)
	str_f2 = str_f2.replace('%%', '')
	# if d_email_id[k] in str_f2:
	str_f2 = str_f2.replace(str_email_id, k)


file_lines = open("mbox-anon-key.txt","w")
file_lines.write(str_f2)
file_lines.close()