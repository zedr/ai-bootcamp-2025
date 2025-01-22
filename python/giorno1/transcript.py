Python 3.13.1 (v3.13.1:06714517797, Dec  3 2024, 14:00:22) [Clang 15.0.0 (clang-1500.3.9.4)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
True
True
False
False
1
1
0
0
bool
<class 'bool'>
bool
<class 'bool'>
bool
<class 'bool'>
bool(1)
True
bool(0)
False
int
<class 'int'>
# Falsy
bool(0)
False
bool(False)
False
None
coniugata = False
coniugata
False
coniugata = None
coniugata
bool(coniugata)
False
not True
False
not False
True
not None
True
not bool(None)
True
not not None
False
not not not None
True
bool(coniugata)
False
coniugata is None
True
coniugata is False
False
type
<class 'type'>
type(coniugata)
<class 'NoneType'>
type(False)
<class 'bool'>
type(True)
<class 'bool'>
1
1
1.0
1.0
type(1)
<class 'int'>
type(1.0)
<class 'float'>
1.0 + 1
2.0
1.1 + 1
2.1
1 + "hello, world"
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    1 + "hello, world"
TypeError: unsupported operand type(s) for +: 'int' and 'str'
"1hello, world"
'1hello, world'
1.0 + float(1)
2.0
import string
string.ascii
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    string.ascii
AttributeError: module 'string' has no attribute 'ascii'
string.ascii_letters
'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
string.printable
'0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c'
a = ""
type(a)
<class 'str'>
# str sono string utf8
b""
b''
type(b"")
<class 'bytes'>
"hello" + "world"
'helloworld'
"hello" + b"world"
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    "hello" + b"world"
TypeError: can only concatenate str (not "bytes") to str
"hello" + (b"world").decode()
'helloworld'
3 - 2
1
3 + 3
6
3 / 2
1.5
3 // 2
1
3 /2
1.5
3 * 2
6
3 ** 2
9
import math
math.sqrt(4)
2.0
a = None
a is None
True
id(a)
4390957968
id(None)
4390957968
b = a
a is b
True
c = None
c is a
True
x = "Rigel"
y = "Alessandro"
z = "Alessandro"
x == y
False
x = y
x
'Alessandro'
x is y
True
y == z
True
y is z
True
a = 1
b = 1.0
c = 1
a is c
True
id(a)
4390972000
id(c)
4390972000
a == c
True
id(a)
4390972000
id(c)
4390972000
a == b
True
a
1
b
1.0
a is b
False
id(a)
4390972000
id(b)
4375272848
"Alessandro" * 3
'AlessandroAlessandroAlessandro'
a = "Alessandro" * 4000
b = "Alessandro" * 4000
a == b
True
a is b
False
c = "Alessandro"
d = "Alessandro"
c == d
True
c is d
True
id(a)
5368741888
id(b)
5368807424
id(c)
4384884848
id(d)
4384884848
# Usare is solo quando si vuole controllare l'identita', e.g. None, non uguaglianza del valore
a is True
False
a == True
False
# REPL - Read Eval Print Loop
bool(None)
False
eval("bool(None)")
False
a = 1
b = a
c = a
nome = "Rigel"
partecipante1 = "Veronica"
partecipanti  = ("Veronica", "Alessandro", "Martina", "Giorgia")
type(partecipanti)
<class 'tuple'>
partecipanto[0]
Traceback (most recent call last):
  File "<pyshell#120>", line 1, in <module>
    partecipanto[0]
NameError: name 'partecipanto' is not defined. Did you mean: 'partecipanti'?
partecipanti[0]
'Veronica'
partecipanti[1]
'Alessandro'
partecipanti[-1]
'Giorgia'
partecipanti[-2]
'Martina'
partecipanti[-2.0]
Traceback (most recent call last):
  File "<pyshell#125>", line 1, in <module>
    partecipanti[-2.0]
TypeError: tuple indices must be integers or slices, not float
partecipanti(0)
Traceback (most recent call last):
  File "<pyshell#126>", line 1, in <module>
    partecipanti(0)
TypeError: 'tuple' object is not callable
partecipanti.index("Veronica")
0
partecipanti.index("Maria")
Traceback (most recent call last):
  File "<pyshell#128>", line 1, in <module>
    partecipanti.index("Maria")
ValueError: tuple.index(x): x not in tuple
a = 1
a = "str"
type(partecipanti)
<class 'tuple'>
dir(partecipanti)
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']
partecipanti.count()
Traceback (most recent call last):
  File "<pyshell#133>", line 1, in <module>
    partecipanti.count()
TypeError: tuple.count() takes exactly one argument (0 given)
len(partecipanti)
4
partecipanti.
SyntaxError: invalid syntax
partecipanti.count
<built-in method count of tuple object at 0x104ee3b00>
partecipanti.count("Veronica")
1
help(partecipanti.count)
Help on built-in function count:

count(value, /) method of builtins.tuple instance
    Return number of occurrences of value.

help(partecipanti.index)
Help on built-in function index:

index(value, start=0, stop=9223372036854775807, /) method of builtins.tuple instance
    Return first index of value.

    Raises ValueError if the value is not present.

partecipanti.index("Veronica", 3)
Traceback (most recent call last):
  File "<pyshell#140>", line 1, in <module>
    partecipanti.index("Veronica", 3)
ValueError: tuple.index(x): x not in tuple
li = [1, 2, 3]
tu = (1, 2, 3)
assert True
print "1111"
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
print(print)
<built-in function print>
print(print("hello, world"))
hello, world
None
li2 = [1]
type(li2)
<class 'list'>
tu2 = (1)
type(tu2)
<class 'int'>
tu2 = (1,)
type(tu2)
<class 'tuple'>
("lalala")
'lalala'
2 + 3 * 5
17
(2 + 3) * 5
25
(2 + 3)
5
(2 + 3,)
(5,)
("Veronica")
'Veronica'
print "sasasa"
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
type(assert None)
SyntaxError: invalid syntax
help(while)
SyntaxError: invalid syntax
li2
[1]
tu2
(1,)
li2 = ["Veronica", "Alessandro", "Martina", "Giorgia"]
li2
['Veronica', 'Alessandro', 'Martina', 'Giorgia']
li2[0] = None
li2
[None, 'Alessandro', 'Martina', 'Giorgia']
len(li2)
4
tu2[0] = None
Traceback (most recent call last):
  File "<pyshell#169>", line 1, in <module>
    tu2[0] = None
TypeError: 'tuple' object does not support item assignment
tu2[1:]
()
tu2
(1,)
tu2 = ("Veronica", "Alessandro", "Martina", "Giorgia")
tu2[1:]
('Alessandro', 'Martina', 'Giorgia')
tu2
('Veronica', 'Alessandro', 'Martina', 'Giorgia')
id(tu2[1:])
4384887552
id(tu2)
4384930960
tu2 = tu2[1:]
tu2
('Alessandro', 'Martina', 'Giorgia')
li2
[None, 'Alessandro', 'Martina', 'Giorgia']
dir(li2)
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
li2.append("Giulia")
li2
[None, 'Alessandro', 'Martina', 'Giorgia', 'Giulia']
id(li2)
4384576448
li2.append("Noemi")
id(li2)
4384576448
tu2
('Alessandro', 'Martina', 'Giorgia')
milanese = "Rigel"
corsisti = ('Alessandro', 'Martina', 'Giorgia', milanese)
corsisti
('Alessandro', 'Martina', 'Giorgia', 'Rigel')
corsisti = ('Alessandro', 'Martina', 'Giorgia')
corsisti
('Alessandro', 'Martina', 'Giorgia')
milanese
'Rigel'
del(milanese)
milanese
Traceback (most recent call last):
  File "<pyshell#194>", line 1, in <module>
    milanese
NameError: name 'milanese' is not defined
corsiste = ('Martina', 'Giorgia')
li1 = []
li2 = [li1]
li2
[[]]
li1.append(li2)
li1
[[[...]]]
d = {"Rigel": 47}
d
{'Rigel': 47}
d["Samuele"] = 8
d["Rigel"]
47
d["Samuele"]
8
d
{'Rigel': 47, 'Samuele': 8}
d["Rigel"] = 18
d
{'Rigel': 18, 'Samuele': 8}
d["Rigel"]
18
d2 = {"Di Scala": d}
d2
{'Di Scala': {'Rigel': 18, 'Samuele': 8}}
d2["Bianchi"] = {"Mario": None}
d2
{'Di Scala': {'Rigel': 18, 'Samuele': 8}, 'Bianchi': {'Mario': None}}
len(d2)
2
len(d2["Di Scala"])
2
len(d2["Bianchi"])
1
len(li2)
1
li2
[[[...]]]
d3 = {1: 2}
d3[1]
2
{1, 2}
{1, 2}
tu3 = [1, 1, 2]
tu3
[1, 1, 2]
se1 = {1, 1, 2}
se1
{1, 2}
se1.add(1)
se1
{1, 2}
se1.add(3)
se1
{1, 2, 3}
se1.add(3)
se1
{1, 2, 3}
d3 = {[]: 1}
Traceback (most recent call last):
  File "<pyshell#232>", line 1, in <module>
    d3 = {[]: 1}
TypeError: unhashable type: 'list'
(1,)
(1,)
(,)
SyntaxError: invalid syntax
(1)
1
("sasa")
'sasa'
(1)
1
(1,)
(1,)
(1)
1
()
()
()
()
{(): 1}
{(): 1}
{("Rigel", "Di Scala"): 47}
{('Rigel', 'Di Scala'): 47}
d4 = {("Rigel", "Di Scala"): 47}
d4[("Rigel", "Di Scala")]
47
{{}: 47}
Traceback (most recent call last):
  File "<pyshell#246>", line 1, in <module>
    {{}: 47}
TypeError: unhashable type: 'dict'
hash(47)
47
hash(())
5740354900026072187
d4["Rigel"]
Traceback (most recent call last):
  File "<pyshell#249>", line 1, in <module>
    d4["Rigel"]
KeyError: 'Rigel'
assert True
assert False
Traceback (most recent call last):
  File "<pyshell#251>", line 1, in <module>
    assert False
AssertionError
def foo(a, b):
    return a + b

foo(2, 2)
4
assert foo(2, 2) == 4
def foo(a, b):
    return a - b

assert foo(2, 2) == 4
Traceback (most recent call last):
  File "<pyshell#259>", line 1, in <module>
    assert foo(2, 2) == 4
AssertionError
nome = "Rigel"
if nome == "Rigel":
    print("Ciao")

    
Ciao
if nome == "Alessandro":
    print("Ciao")

    

if nome != "Rigel":
    print("Ciao")

    
nome = "Maria"
if nome != "Rigel":
    print("Ciao")

    
Ciao
if foo(2, 2) != 4:
    print("Hai un errore")

    
Hai un errore
cognome = "S."

if nome == "Maria":
    if cognome == "S.":
        print("10 e lode")

        
10 e lode
nome
'Maria'
cognome
'S.'
nome = "Marco"
if nome == "Maria":
    if cognome == "S.":
        print("10 e lode")

        
if nome == "Maria:
SyntaxError: unterminated string literal (detected at line 1)
voto =  0
if nome == "Maria":
    voto += 10

    
if cognome == "S.":
    voto += 10

    
voto
10
if nome == "Maria":
    voto += 10
    if cognome == "S.":
        voto += 10
        print("10 e lode")

        
voto
10
if nome ===
SyntaxError: invalid syntax
if nome == "Maria" and cognome == "S.": voto += 10

if nome == "Maria" and cognome == "S.":
    voto += 10


voto
10
voto
10
voto += 10
voto
20
voto += 10
voto
30
voto -= 10
voto
20
s = "Rigel"
s += " Di Scala"
s
'Rigel Di Scala'
s = s + "Di Scala"
s
'Rigel Di ScalaDi Scala'
import time
time.sleep(1)
time.sleep(3)
while True:
    time.sleep(3)
    print("Ciao")

    
Ciao
Ciao
Ciao
Ciao
Ciao
Ciao
Traceback (most recent call last):
  File "<pyshell#325>", line 2, in <module>
    time.sleep(3)
KeyboardInterrupt
while False:
    time.sleep(3)
    print("Ciao")

    
while True:
    time.sleep(3)
    print("Ciao")
    break

Ciao
num = 3
while num > 0:
    time.sleep(1)
    print("Ciao! num == " + str(num))
    num -= 1

    
Ciao! num == 3
Ciao! num == 2
Ciao! num == 1
while num > 0:
    time.sleep(1)
    print("Ciao! num == " + str(num))
    num -= 1
    
KeyboardInterrupt
1 > 0
True
1 < 0
False
1 < 1
False
1 <= 1
True
1 >= 1
True
while num > 0:
    time.sleep(1)
    print("Ciao! num == " + str(num))
    num -= 1

    
num
0
num = 3
while True:
    time.sleep(1)
    print("Ciao! num == " + str(num))
    num -= 1
    if num > 0:
        break

    
Ciao! num == 3
num = 3
while True:
    time.sleep(1)
    print("Ciao! num == " + str(num))
    num -= 1
    if num <= 1:
        break
    
SyntaxError: multiple statements found while compiling a single statement
num = 3
while True:
    time.sleep(1)
    print("Ciao! num == " + str(num))
    num -= 1
    if num <= 1:
        break

    
Ciao! num == 3
Ciao! num == 2

while True:
    time.sleep(1)
    print("Ciao! num == " + str(num))
    num -= 1
    if num < 1:
        break

    
Ciao! num == 1

num = 3
while True:
    time.sleep(1)
    print("Ciao! num == " + str(num))
    num -= 1
    if num < 1:
        break

    
Ciao! num == 3
Ciao! num == 2
Ciao! num == 1
while True:
    break
while True:
    
SyntaxError: invalid syntax
while True:
    break

tu1
Traceback (most recent call last):
  File "<pyshell#364>", line 1, in <module>
    tu1
NameError: name 'tu1' is not defined. Did you mean: 'tu'?
tu2
('Alessandro', 'Martina', 'Giorgia')
for name in tu2:
    print(name)

    
Alessandro
Martina
Giorgia
for name in tu2:
    for name in tu2:
        print(name)

...         
Alessandro
Martina
Giorgia
Alessandro
Martina
Giorgia
Alessandro
Martina
Giorgia
>>> for name1 in tu2:
...     print(name1)
...     for name2 in tu2:
...         print(name2)
... 
...         
Alessandro
Alessandro
Martina
Giorgia
Martina
Alessandro
Martina
Giorgia
Giorgia
Alessandro
Martina
Giorgia
>>> tu2
('Alessandro', 'Martina', 'Giorgia')
>>> # sasasasasasa
>>> # print("sasasa")
