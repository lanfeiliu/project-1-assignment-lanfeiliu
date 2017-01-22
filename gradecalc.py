import csv
import pprint
import collections
import json


table = csv.DictReader(open('gradebook.csv'))

###turn table to dictionary
orderdict = {}
for row in table:
	key = row.pop('Student') #the student name as key
	if key not in orderdict:
		orderdict[key] = row  #values are rows

#the value of each key is a ordered dictionary
#turn the value to regular dictionary
whole_dict = {}
for i in orderdict:
	whole_dict[i] = dict(orderdict[i])

pprint.pprint(whole_dict)

whole_lst = [i for i in whole_dict]
var_lst = ['weight', 'max_points']
student_lst = [i for i in whole_dict if i not in var_lst]

dict_var = {}
for i in var_lst:
	if i in whole_dict and i not in dict_var:
		dict_var[i] = whole_dict[i]

# pprint.pprint(dict_var)

#Create a dictionary of the student
dict_students = {}
for i in student_lst:
	if i in whole_dict and i not in dict_students:
		dict_students[i] = whole_dict[i]

pprint.pprint(dict_students)

#invert the nested dictionary:dict_var 
inv_dict_var = {}
for k1, subdict in dict_var.items():
	for k2, v in subdict.items():
		inv_dict_var.setdefault(k2, {})[k1] = v

pprint.pprint(inv_dict_var)

exam_lst = [i for i in inv_dict_var]
#calculate each student’s weighted average grade
def student_average(student_name):
	w_finalgrade = 0
	for exam in inv_dict_var:
		w_finalgrade += float(inv_dict_var[exam]['weight'])*int(dict_students[student_name][exam])/int(inv_dict_var[exam]['max_points'])*100

	return w_finalgrade

for name in dict_students:
	print (name + ':' + str(student_average(name)))

#calculate all student’s average score percentage of each exam
def assn_average(assn_name):
	exam_totalgrade = 0
	for name in dict_students:
		exam_totalgrade += int(dict_students[name][assn_name])
	exam_avergrade = exam_totalgrade/len(dict_students)/int(inv_dict_var[assn_name]['max_points'])*100

	return exam_avergrade

for exam in inv_dict_var:
	print (exam + ':' + str(assn_average(exam)))


def format_gradebook():
	title_lst = ['Student'] + [i for i in inv_dict_var] + ['grade']
	print('{0:<10} {1:>8}  {2:>8}  {3:>8}  {4:>8} {5:>8}'.format(*tuple(title_lst)))
	print('-'*60)

	student_lst = [name for name in dict_students]
	assn1per_lst = [int(dict_students[name]['Assn 1'])/int(inv_dict_var['Assn 1']['max_points'])*100 for name in dict_students]
	assn2per_lst = [int(dict_students[name]['Assn 2'])/int(inv_dict_var['Assn 2']['max_points'])*100 for name in dict_students]
	assn3per_lst = [int(dict_students[name]['Assn 3'])/int(inv_dict_var['Assn 3']['max_points'])*100 for name in dict_students]
	finalper_lst = [int(dict_students[name]['Final Exam'])/int(inv_dict_var['Final Exam']['max_points'])*100 for name in dict_students]
	studentaver_lst = [student_average(name) for name in dict_students]

	content_tuple_lst = zip(student_lst, assn1per_lst, assn2per_lst, assn3per_lst, finalper_lst, studentaver_lst )

	for t in content_tuple_lst:
		print('{0:<10} {1:>8.1f}% {2:>8.1f}% {3:>8.1f}% {4:>8.1f}% {5:>8.1f}%'.format(*t))
	
	print('-'*60)

	average_grade = sum(studentaver_lst)/len(student_lst)
	tail_lst = ['Average'] + [assn_average(i) for i in inv_dict_var] + [average_grade]
	print('{0:<10} {1:>8.1f}% {2:>8.1f}% {3:>8.1f}% {4:>8.1f}% {5:>8.1f}%'.format(*tuple(tail_lst)))


format_gradebook()