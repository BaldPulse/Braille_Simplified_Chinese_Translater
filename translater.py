import io
import unicodedata
f = io.open('tex.txt', 'r', encoding = 'utf8')
t = f.read()
print(t)

dic = {chr(0x2803):'b',
       chr(0x2809):'c',
       chr(0x281F):'ch',
       chr(0x2819):'d',
       chr(0x280B):'f',
       chr(0x281B):'g/j',
       chr(0x2813):'h/x',
       chr(0x2805):'k/q',
       chr(0x2807):'l',
       chr(0x280D):'m',
       chr(0x281D):'n',
       chr(0x280F):'p',
       chr(0x281A):'r',
       chr(0x280E):'s',
       chr(0x2831):'sh',
       chr(0x281E):'t',
       chr(0x2835):'z',
       chr(0x280C):'zh',
       chr(0x2814):'a',
       chr(0x282A):'ai',
       chr(0x2827):'an',
       chr(0x2826):'ang',
       chr(0x2816):'ao',
       chr(0x2822):'o/e',
       chr(0x282E):'ei',
       chr(0x2834):'en',
       chr(0x283C):'eng',
       chr(0x2817):'er',
       chr(0x280A):'i/yi',
       chr(0x282B):'ia/ya',
       chr(0x2811):'ie/ye',
       chr(0x281C):'iao/yao',
       chr(0x2833):'iu/you',
       chr(0x2829):'ian/yan',
       chr(0x2823):'in/yin',
       chr(0x282D):'iang/yang',
       chr(0x2821) : 'ing/ying',
       chr(0x2839) : 'iong/yong',
       chr(0x2832) : 'ong/weng',
       chr(0x2837) : 'ou',
       chr(0x2825) : 'u/wu',
       chr(0x283F) : 'ua/wa',
       chr(0x283D) : 'uai/wai',
       chr(0x283B) : 'uan/wan',
       chr(0x2836) : 'uang/wang',
       chr(0x283A) : 'ui/wei',
       chr(0x283B) : 'un/wen',
       chr(0x2815) : 'uo/wo',
       chr(0x282C) : 'v/yu',
       chr(0x2812) : 'un/yuan',
       chr(0x283E) : 'ue/yue',
       chr(0x2838) : 'en',
       chr(0x2801) : '1',
       chr(0x2802) : '2',
       chr(0x2804) : '3',
       chr(0x2806) : '4',
       chr(0x2800) : ' ',
       chr(0x2810) : ','
       }
print(dic)
diary = ''
for i in t:
    ch = dic.get(i)
    if not ch is None:
        diary += ch
    elif i == ' ':
        diary += ' '
    else:
        diary += '*'
        print(i, 'notfound')
print(diary)
