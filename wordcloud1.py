import wordcloud
import jieba
#要想成图需要以下3步
from scipy.misc import imread #步骤1
mask = imread('lou.jpg')#步骤2
f = open('hong','r',encoding='utf-8')
t =f.read()
f.close()
ls = jieba.lcut(t)
txt = ''.join(ls)
stopword = {'现在','这时','是的','当然','那么','但当时','不过','然后','所以','没有','另外','是啊','程心说','程心问','同时','其实','为什么','字幕'
            ,'很好','于是','好了','但现在','什么','后来','是吗','谢谢','与此同时','很快','天啊','好的'
            ,'接着','他说','这样','号和','不不','不知道','在这里','以后','好吧','也就是说','首先','道'
            '不是','在这里','以前','当时','你好','而且','也许','说道','一般来说','因此','在这种情况下','可是','最后','这样一来','的话','一般','在这个问题上'
            ,'实际上','再说','通常来说','只有这样','这些','这种','如果','情况','可以'}
w = wordcloud.WordCloud( font_path='/home/zxf/moocPython/simsun.ttf',mask=mask,width=700,height=500,background_color='white',max_words=200,
                         stopwords=stopword)
#make= make 这是步骤3
w.generate(txt)
w.to_file('w1.png')
