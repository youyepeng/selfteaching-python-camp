text = '''
愚公移山
太行、王屋二山，方七百里，高万仞。本在冀州之南，河阳之北。
　　北山愚公者，年且九十，面山而居。惩山北之塞，出入之迂也。聚室而谋曰：“吾与汝毕力平险，指通豫南，达于汉阴，可乎？”杂然相许。其妻献疑曰：“以君之力，曾不能损魁父之丘，如太行、王屋何？且焉置土石？”杂曰：“投诸渤海之尾，隐土之北。”遂率子孙荷担者三夫，叩石垦壤，箕畚运于渤海之尾。邻人京城氏之孀妻有遗男，始龀，跳往助之。寒暑易节，始一反焉。
　　河曲智叟笑而止之曰：“甚矣，汝之不惠。以残年余力，曾不能毁山之一毛，其如土石何？”北山愚公长息曰：“汝心之固，固不可彻，曾不若孀妻弱子。虽我之死，有子存焉；子又生孙，孙又生子；子又有子，子又有孙；子子孙孙无穷匮也，而山不加增，何苦而不平？”河曲智叟亡以应。
　　操蛇之神闻之，惧其不已也，告之于帝。帝感其诚，命夸娥氏二子负二山，一厝朔东，一厝雍南。自此，冀之南，汉之阴，无陇断焉。

How The Foolish Old Man Moved Mountains
Yugong was a ninety-year-old man who lived at the north of two high mountains, Mount Taixing and Mount Wangwu.
Stretching over a wide expanse of land, the mountains blocked yugong’s way making it inconvenient for him and his family to get around. One day yugong gathered his family together and said,”Let’s do our best to level these two mountains. We shall open a road that leads to Yuzhou. What do you think?”
All but his wife agreed with him. “You don’t have the strength to cut even a small mound,” muttered his wife. “How on earth do you suppose you can level Mount Taixin and Mount Wanwu? Moreover, where will all the earth and rubble go?” “Dump them into the Sea of Bohai!” said everyone.
So Yugong, his sons, and his grandsons started to break up rocks and remove the earth. They transported the earth and rubble to the Sea of Bohai.
Now Yugong’s neighbour was a widow who had an only child eight years old. Evening the young boy offered his help eagerly.
Summer went by and winter came. It took Yugong and his crew a full year to travel back and forth once.
On the bank of the Yellow River dwelled an old man much respected for his wisdom. When he saw their back-breaking labour, he ridiculed Yugong saying,”Aren’t you foolish, my friend? You are very old now, and with whatever remains of your waning strength, you won’t be able to remove even a corner of the mountain.”
Yugong uttered a sigh and said,”A biased person like you will never understand. You can’t even compare with the widow’s little boy!”
“Even if I were dead, there will still be my children, my grandchildren, my great grandchildren, my great great grandchildren. They descendants will go on forever. But these mountains will not grow any taler. We shall level them one day!” he declared with confidence.
The wise old man was totally silenced. When the guardian gods of the mountains saw how determined Yugong and his crew were, they were struck with fear and reported the incident to the Emperor of Heavens.
Filled with admiration for Yugong, the Emperor of Heavens ordered two mighty gods to carry the mountains away. '''

 # 统计text中每个英语单词出现的次数
 # 返回一个按词频降序排序的数组
def stats_text_en(text):
    words = []
    # 1): text to list
    elements = text.split()
    # 2): del symbol such as ,.*-! in every words
    for e in elements:
        for s in ',.*-!':
            e = e.replace(s,'')
        if(len(e)):
            words.append(e)
    # 3): count every words
    counter ={}
    wordset = set(words)
    for w in wordset:
        counter[w] = words.count(w)
    
    # 4): sort counter
    # 发现一个特点，这里对counter排序后，其实并不会改变counter，
    # 也就是排序后的结果需要另一个对象保存。这和C语言有很明显的不同。
    return sorted(counter.items(),key=lambda x: x[1],reverse=True)

 # 统计text中每个汉字出现的次数。返回一个字频降序排序的数组
 # 思考：
 # 1、对比，文单词以空格为分割，可用split函数分割出。而中文呢？中文汉字是固定长度。
 #    不用考虑分割问题。计数汉字，就和计数英语字符一样。
 # 2、中英文混合情况需要考虑吗？这又涉及到单词or汉字的判断。先从简单开始，仅考虑只有汉字情况。
def stats_text_cn(text):
    counter = {}
    wordset = set(text)
    for w in wordset:
        counter[w] = text.count(w)
    return sorted(counter.items(),key=lambda x: x[1],reverse=True)


def stats_tex():
    en = stats_text_en(text)
    cn = stats_text_cn(text)
    return en+cn
