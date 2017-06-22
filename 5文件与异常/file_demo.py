
# 1、打开文件
f = open('record.txt', 'r+', encoding='utf-8')
# 2、写入\阅读
# f.write('hello,胡明星')
print(f.readline())
# 3、关闭
f.close()