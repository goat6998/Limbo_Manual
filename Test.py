import Method as md


data_list = ["win", "lose", "win", "lose", "win"]
data_list2 = ["win", "lose", "win", "lose", "lose"]



with open('test.txt','w') as f:
	f.writelines([d+"\n" for d in data_list])





get_data = md.get_txt_list("test")
new_data_list = []
for row in get_data:
	if row!="":
		new_data_list.append(row)

print(new_data_list)

print( data_list==new_data_list )

md.os.system("pause")