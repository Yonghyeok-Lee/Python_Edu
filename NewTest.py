a = ['고해', '바람기억', '좋은날']


def index():
	print('1. 숫자 선택')
	print('2. 리스트 출력')
	print('3. 종료')
	menu = input('메뉴 선택: ')
	return int(menu)


def sel():
	number = input("숫자를 선택하세요 : ")
	for num in number:
		if number == 1:
			num = a[0]
		elif number == 2:
			num = a[1]
		else:
			num = a[2]
	print('\n선택한 노래는 : %s \n처음으로 돌아갑니다~\n'% num)
	return index()

def list():
	print('\n곡 리스트!! : %s \n처음으로 돌아갑니다~\n'% a)


def run():
	while True:
		menu= index()
		if menu== 1:
			sel()
		elif menu== 2:
			list()
		elif menu== 3:
			print('\n안녕~~~')
			break

if __name__ == "__main__":
    run()