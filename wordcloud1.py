import wordcloud
import jieba
f = open('三体.txt','r',encoding='utf-8')
t =f.read()
f.close()
ls = jieba.lcut(t)
txt = ''.join(ls)
stopword = {'现在','这时','是的','当然','那么','但当时','不过','然后','所以','没有','另外','是啊','程心说','程心问','同时','其实','为什么','字幕'
            ,'很好','于是','好了','但现在','什么','后来','是吗','谢谢','与此同时','很快','天啊','好的'
            ,'接着','他说','这样','号和','不不','不知道','在这里','以后','好吧','也就是说','首先',
            '不是','在这里','以前','当时','你好','而且','也许'}
w = wordcloud.WordCloud( font_path='/home/zxf/moocPython/simsun.ttf',width=1000,height=700,background_color='white',max_words=150,
                         stopwords=stopword)
w.generate(txt)
w.to_file('outfile1.png')
