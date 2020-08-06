#CONVERTING 12 HOUR TO 24 HOUR TIME FORMAT USING LIST METHOD
s='12:40:03PM'
if 'PM' in s:
    a=s.replace('PM','')
    t=list(map(int,a.split(":")))
    if t[0]!=12:
        t[0]+=12
    h="{:02d}:{:02d}:{:02d}".format(t[0],t[1],t[2])
    print(h)
if 'AM' in s:
    a=s.replace('AM','')
    t=list(map(int,a.split(":")))
    if t[0] ==12:
        t[0]=00
    h="{:02d}:{:02d}:{:02d}".format(t[0],t[1],t[2])
    print(h)
'''
OUTPUT:
12:40:03
'''
#==============================================================
#USING STRING CONVERSION METHOD
def hour(s):
    if s[-2:]=='PM' and s[:2] =='12':
        return s[:-2]
    elif s[-2:]=='AM' and s[:2] =='12':
        return '00'+s[2:-2]
    elif s[-2:]=='AM':
        return s[:-2]
    else:
        return str(int(s[:2])+12)+s[2:-2]
print(hour('05:30:20 PM'))
print(hour('12:23:30 AM'))
'''
OUTPUT:
17:30:20
00:23:30
'''


