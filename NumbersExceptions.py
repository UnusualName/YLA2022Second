a = input().replace(' ', '')
a = a.replace('\n', '')
a = a.replace('\t', '')

er = 6

if a.count('(') <= 1 and a.count(')') <= 1:
    if a.count('(') == 1:
        if a.count('(') == a.count(')') and a.find('(') <= a.find(')'):
            a = a.replace('(', '')
            a = a.replace(')', '')
            er -= 1
    else:
        a = a.replace('(', '')
        a = a.replace(')', '')
        er -= 1
if a[0:2] == '+7':
    er -= 1
elif a[0] == '8':
    er -= 1
    a = '+7' + a[1:]
if a[-1] != '-':
    er -= 1
if a.count('--') == 0:
    a = a.replace('-', '')
    er -= 1

if a[1:].isdigit():
    er -= 1
if len(a) == 12:
    er -= 1
if er == 0:
    print(a)
else:
    print('error')
