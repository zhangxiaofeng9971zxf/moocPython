import jieba  #一个超级屌的第三方分中文的词库
txt = open('三体.txt','r',encoding='utf-8').read()#打开三体.txt
words = jieba.lcut(txt)
delwords = {'一个'}
counts = {}
for word in words:
    if len(word)== 1:
        continue
    else:
        counts[word]=counts.get(word,0) +1 #字典.get(键，值) 若这个键不在字典中，则把默认的值跟键对应起来
    #所以这里的意思是 若一个词出现过，则+1，若没出现过，则把0赋予这个键
for word in delwords:
    del counts[word]
items = list(counts.items())   #以列表形式返回可遍历的(键, 值) 元组数组
items.sort(key=lambda x:x[1],reverse=True) #.sort 是把列表按照键值对的第二个数 从大到小排序
for i in range(10):
    word,counts = items[i]
    print('{0:<10}{1:>5}'.format(word,counts))

