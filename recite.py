from sys import argv
import re 

script, filename = argv 
new_file ='背诵版—'+filename

file = open(filename,'r',encoding = 'utf-8')
file = file.read()

iteration = re.findall('[^。，\n \u3000 ； ： ‘ ’ “ ” ？ ！]', file)
file_list=list(file)

count= 0
m=0
for i in file_list:

	if i in iteration :
		if count%2 == 1:
		
			file_list[m] = 'X'
		count = count + 1

	m = m+1
	
y = ''
for i in file_list:
	y = y + i
	
b = open(new_file, 'w',encoding = 'utf-8')
b.write(y)
b.close()

print('done')


	

