import random
a = ['고해', '바람기억', '좋은날']


def index():
	print('1. 노래 선택')
	print('2. 리스트 출력')
	print('3. 종료')
	menu = input('메뉴 선택 : ')
	return int(menu)


def sel():
	print('1. 선택')
	print('2. 처음으로')
	select = input("메뉴 선택 : ")
	if select is not 'null':
		A = random.sample(a, 1)
		print('\n선택한 노래는 : %s \n처음으로 돌아갑니다~\n'% A)
	else:
		print('\n처음으로 돌아갑니다~\n')


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