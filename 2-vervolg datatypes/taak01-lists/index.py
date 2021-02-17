Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> maanden =['januari','februari','maart','april','mei','juni','july','augustus','september','oktober','november','december']
>>> type(maanden)
<class 'list'>
>>> maanden[0]
'januari'
>>> maanden[6]='juli'
>>> maanden
['januari', 'februari', 'maart', 'april', 'mei', 'juni', 'juli', 'augustus', 'september', 'oktober', 'november', 'december']
>>> print(maanden)
['januari', 'februari', 'maart', 'april', 'mei', 'juni', 'juli', 'augustus', 'september', 'oktober', 'november', 'december']
>>> print(maanden). <br>
SyntaxError: invalid syntax
>>> for elem in maanden
SyntaxError: invalid syntax
>>> for elem in maanden:
	print elem
	
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(elem)?
>>> for elem in maanden:
	print(elem)

	
januari
februari
maart
april
mei
juni
juli
augustus
september
oktober
november
december
>>> len(maande[2])
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    len(maande[2])
NameError: name 'maande' is not defined
>>> len(maanden)
12
>>> len(maanden[2])
5
>>> 