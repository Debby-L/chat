
lines = []
with open('3.txt','r', encoding= 'utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())#去除換行
#清單分割法
for line in lines:
	s = line.split(' ')#分割資料時間名字/內容
	time = s[0][:5] #分割時間/名字
	name = s[0][5:]
	print(time)
	print(name)
	print(s)