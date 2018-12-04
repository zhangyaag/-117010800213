import jieba
path = 'D:\\hongloumeng\\红楼梦.txt'
#根据路径以GB18030的格式读取文件内容
txt = open(path,'r',encoding = 'GB18030').read()
words = jieba.lcut(txt)
#通过结果分析，记录需要排除的一些不是人名的名词
excludes = ['这会子','少不得','宝钗道','周瑞家',
            '贾母笑','悄悄的','贾政道','袭人道' ,
            '为什么','怎么样','下回分解' ,'宝钗笑','黛玉笑']
#定义空的词典类型
counts = {}
for word in words:
    if len(word) == 1 or len(word) == 2:
        continue
    else:
        counts[word] = counts.get(word,0) + 1
for word in excludes:
    del counts[word]
items = list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
for i in range(15):
    word,count = items[i]
    print('{0:<10}{1:>5}'.format(word,count))

