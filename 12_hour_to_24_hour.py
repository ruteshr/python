#CONVERTING 12 HOUR TO 24 HOUR TIME FORMAT
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
