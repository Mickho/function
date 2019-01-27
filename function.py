# function 函式/功能
#用來收納程式
#是個功能

def wash(dry):
	print('wash')
	print('Add wash')
	print('route')
	if dry:
		print('烘衣')

wash(True) #use function dry=True
wash(False) # dry=False

def say_hi():
	print('hi')

say_hi()

def add(x, y): 
	print(x + y)

add(3, 4)
add(123, 333)

def add(x=1, y=2): #參數可以有預設值 可以直接印
	print(x + y)

add()
add(y=5)

def wash(dry=False, water=8):
	print('wash')
	print('Add wash')
	print('route')
	print('加水', water, '分滿')
	if dry:
		print('烘衣')

wash() #use function dry=True


def add(x, y):
	return x + y #回傳將結果存上

result = add(3,4)
print(result)

def average(numbers): #平均
	avg = sum(numbers) / len(numbers) #加總
	return avg
a = average([1, 2, 3]) #將結果存到a, 因為有return功能
print(a)

print(average([1, 2, 3]))
print(average([12, 23, 34]))