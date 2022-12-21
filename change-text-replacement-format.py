# 在QQ输入法和搜狗输入法之间迁移自定义短语（文本替换）
# 自动识别迁移方向
# Transfer text replacement format between qq and sogou keyboards
# QQ   : wz=1,bcwyatt.com
# sogou: wz,1=bcwyatt.com

import re

with open('old_text.txt','r',encoding='utf-8') as f1:
    new_text = ''
    count = 0
    for line in f1: 
        if re.search('.', line): # 跳过空行
            count += 1
            # 判断替换方向 qq2sogou or sogou2qq # QQ输入法中会有'=1,'
            qq2sogou = True if re.compile(r'=\d+,').search(line) else False 
            flow = 'qq2sogou' if qq2sogou else 'sogou2qq'
            res = line.split('=', 1) if qq2sogou else  line.split(',', 1)
            input = res[0] # 缩写
            res = res[1].split(',', 1) if qq2sogou else  res[1].split('=', 1)
            pos = res[0] # 候选位置
            text = res[1] # 目标文本
            sogou = input + ',' + pos + '=' + text # qq2sogou
            QQ = input + '=' + pos + ',' + text # sogou2qq
            new_text += sogou if qq2sogou else QQ

with open('new_text.txt','w+',encoding='utf-8') as f2: 
    f2.write(new_text)

print('From {}, {} phrases transferred.'.format(flow, count))