import random,string,uuid

#第一种生成大写Ascii字符的方法
source=list(string.ascii_uppercase)
for i in range(0,9):
	a=str(i)
	source.append(a)


#第二种方法
as_list=[]

for i in range(65,91):
	a=str(chr(i))
	as_list.append(a)


# print(source)
# print(as_list)

#生成激活码

key_list=set()

while len(key_list)<5:
	key=''

	for j in range(20):
		key +=random.choice(source)
		
	key_list.add(key)
	# print(key)

print(key_list)



#第四种方法
'''
1个UUID是1个16字节（128位）的数字；为了方便阅读，通常将UUID表示成如下的方式：

123e4567-e89b-12d3-a456-426655440000

1个UUID被连字符分为五段，形式为8-4-4-4-12的32个字符。

其中的字母是16进制表示，大小写无关。

uuid1=基于时间戳
uuid4=基于随机数（可能重复

'''

list = []
#
for i in range(10):
	code=str(uuid.uuid1()).upper()
	if code not in list:
	    list.append(code)
print(list)



