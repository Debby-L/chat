#讀取檔案
#讀取檔案內容並將內容裝入清單中

def read_file(filename):
	lines = []
	with open(filename, 'r',encoding= 'utf-8-sig') as f:
		for line in f:
			# strip()除掉 \n
			lines.append(line.strip())
	return lines
#先逐行分割資料
#宣告資料順序
#建立條件預設值 = 0
#建立條件檢查內容是否符合條件'人名','貼圖',並計算在預設值中
#查詢貼圖次數後，檢查message字數，從清單設定範圍2開始到最後，並加入預設值字數長度中
#print資料內容
def convert(lines):
	person = None #預先宣告person可能沒有值
	CammyYU_word_count = 0
	Deebee_word_count = 0
	CammyYU_sticker_count = 0
	Deebee_sticker_count = 0
	for line in lines:
		s = line.split(' ')#遇到空白鍵進行分割
		time = s[0]
		name = s[1]
		if name == 'CammyYU':
			if s[2] == '貼圖':
				CammyYU_sticker_count += 1
			else:
				for m in s[2:]: #建立分割清單，將訊息m從清單第二個位置開始到底
					CammyYU_word_count += len(m) #計算字數加入個人計算值
		
		elif name == 'Deebee':
			if s[2] == '貼圖':
				Deebee_sticker_count += 1
			else:
				for m in s[2:] :
					Deebee_word_count += len(m)
	print('CammyYU說了', CammyYU_word_count,'個字', '傳了', CammyYU_sticker_count, '個貼圖')	
	print('Deebee說了', Deebee_word_count,'個字', '傳了', Deebee_sticker_count, '個貼圖')	
	
	

#寫入檔案
def write_file(filename,lines):
	with open(filename, 'w') as f:
		for line in lines:
			f.write(line + '\n')

#執行程式
def main():
	lines = read_file('[LINE]Cammy.txt')#最好使用資料原型，修改過的資料無法判讀!
	
	lines = convert(lines)
	#write_file('output.txt', lines)

main()
