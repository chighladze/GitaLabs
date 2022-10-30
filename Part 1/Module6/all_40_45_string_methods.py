txt_lower = 'hello world!'
txt_upper = 'Hello World!'

print(txt_lower.capitalize())
print(txt_upper.casefold())
print(txt_lower.center(20))
print(txt_lower.count('l'))
print(txt_lower.encode())
print(txt_upper.endswith('!'))
print("H\te\tl\tl\to".expandtabs(2))
print(txt_upper.find('lo'))
print('Hello World! {s}'.format(s=22))
point = {'x': 4, 'y': -5}
print('{x} {y}'.format_map(point))
txt = "Hello, welcome to my world."
print(txt.index("welcome"))
print('Hello World!22'.isalnum())
print(txt_upper.isalpha())
print(txt_upper.isascii())
print(txt_upper.isdecimal())
print("\u0030".isdecimal())
print('50800'.isdigit())
print('giorgi'.isidentifier())
print(txt_lower.islower())
print("523".isnumeric())
print(txt_upper.isprintable())
print(' '.isspace())
print(txt.istitle())
print('JAKAHAA'.isupper())
lst = ['1', '2', '3', 'dkjfjdf']
print(' '.join(lst))
print(txt_upper.ljust(22), 'ggg')
print('KJKJJKJ'.lower())
print('   sdjksjd   '.lstrip())
intab = "aeiou"
outtab = "12345"
trantab = str.maketrans(intab, outtab)
str = "this is string!!!"
print(str.translate(trantab))
print(txt_upper.partition(' '))
print(txt_upper.replace('l', 'v'))
print(txt_upper.rfind('l'))
print(txt_upper.rindex('l'))
print(txt_upper.rjust(50, '*'))
print('.'.rpartition('.'))
print(txt_upper.rsplit(' '))
print(txt.strip())
print(txt_upper.split())
print(txt_upper.splitlines())
print(txt_upper.startswith('H'))
print('       skjskjs         '.strip())
print(txt.swapcase())
print(txt_lower.title())
s = 'ABCDBCA'
translation = s.maketrans({ord('A'): 'a', ord('B'): ord('b')})
print(s.translate(translation))
print(txt_lower.upper())
s = '100'
print(s.zfill(6))





