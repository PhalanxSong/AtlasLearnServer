# encoding: UTF-8

import os
import os.path
import re

print('-----------------------------------')
# 将正则表达式编译成Pattern对象
pattern = re.compile(r'(hello)\s(world)')
# 使用Pattern匹配文本，获得匹配结果，无法匹配时将返回None
match = pattern.match('hello hello hello world!')
# 使用Match获得分组信息
if match:
    print(match.group())

print('-----------------------------------')
match = re.match(r'dog', 'dog cat dog dadad dog dog')
if match:
    print(match.group())

print('-----------------------------------')
a = re.compile(r"""\d +  # the integral part
                   \.    # the decimal point
                   \d *  # some fractional digits""", re.X)
match = a.match("231231.4134.213.1.41.412.3.12.312.4.123.1")
if match:
    print(match.group())

print('-----------------------------------')
b = re.compile(r"\d+\.\d*")
match = b.match("231231.4134.213.1.41.412.3.12.312.4.123.1")
if match:
    print(match.group())

print('-----------------------------------')
b = re.compile(r"(\d+)(\.\d*)")
match = b.match("31.4134.21rqwwrq3.1.41.rg2e.rq4we.e1q23.1")
if match:
    print(match.groups())
    print(match.string)
    print(match.re)
    print(match.pos)
    print(match.endpos)
    print(match.lastindex)
    print(match.lastgroup)
else:
    print("no match")

print('-----------------------------------')
m = re.match(r'(\w+) (\w+)(?P<sign>.\w+)(?!\d)',
             'hello world!i\'m daddy~123456789')

print("m.string:", m.string)
print("m.re:", m.re)
print("m.pos:", m.pos)
print("m.endpos:", m.endpos)
print("m.lastindex:", m.lastindex)
print("m.lastgroup:", m.lastgroup)

print("m.group:", m.group())
print("m.group(1,2):", m.group(1, 2))
print("m.groups():", m.groups())
print("m.groupdict():", m.groupdict())
print("m.start(2):", m.start(2))
print("m.end(2):", m.end(2))
print("m.span(2):", m.span(2))
print(r"m.expand(r'\2 \1\3'):", m.expand(r'\2 \1\3'))

print('-----------------------------------')
p = re.compile(r'(\w+) (\w+)(?P<sign>.*)', re.DOTALL | re.I)

print("p.pattern:", p.pattern)
print("p.flags:", p.flags)
print("p.groups:", p.groups)
print("p.groupindex:", p.groupindex)

### output ###
# p.pattern: (\w+) (\w+)(?P<sign>.*)
# p.flags: 50 # DOTALL 16 + 34
# p.groups: 3
# p.groupindex: {'sign': 3}

print('-----------------------------------')
# 将正则表达式编译成Pattern对象
pattern = re.compile(r'world')
# 使用search()查找匹配的子串，不存在能匹配的子串时将返回None
# 这个例子中使用match()无法成功匹配
match = pattern.search('hello world!')
if match:
    # 使用Match获得分组信息
    print(match.group())
### 输出 ###
# world

print('-----------------------------------')
p = re.compile(r'\d+')
print(p.split('one111two222three333four444five'))
### output ###
# ['one', 'two', 'three', 'four', '']
