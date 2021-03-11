#讀取檔案
#讀取檔案內容並將內容裝入清單中

def read_file(filename):
	lines = []
	with open(filename, 'r',encoding= 'utf-8-sig') as f:
		for line in f:
			# strip()除掉 \n
			lines.append(line.strip())
	return lines

#轉換成為對話格式
#設定條件式逐行檢查並加入新的清單中
def convert(lines):
	new = []
	person = None #預先宣告person可能沒有值
	for line in lines:
		if line == '小華':
			person = '小華'
			continue #幫助返回迴圈檢查對話紀錄是否與if條件式符合
		elif line == 'Jamie':
			 person = 'Jamie'
			 continue
		if person: #假如person有值的話
			new.append(person + ':' + line)
	return new

#寫入檔案
def write_file(filename,lines):
	with open(filename, 'w') as f:
		for line in lines:
			f.write(line + '\n')

#執行程式
def main():
	lines = read_file('input.txt')
	lines = convert(lines)
	write_file('output.txt', lines)

main()
