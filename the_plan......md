

###The Plan.....


- Get our data into Python
- Clean it up and put it in a Python variable 
- process the information to extract our meaning
- Package that meaning up somehow
- output something 

###What we need to know to do that...

- Starting up Python
- importing libraries to handle the type of task we have
- Understand how Python interacts with files on our hard drive or from an online link.
- Be able to use variables to store information 
- Use different Python data structures to organise the information so it makes sense to us.
- manipulate those variables to achieve our outcome
- summarise the findings and output the result to the screen, as a picture, as a data file for another program or as a file.

###Start up Python

1. Go to a terminal, download and run the miniconda install script
2. Use Chrome
3. you need a text editor. Text Wrangler is great. Sublime text if you've used it before, but it is more complex and may get in the way of you learning python.
4. If the terminal commands are a challenge for you, you can download the installer from the Anaconda site and auto install Anaconda (choose Python 3.XX, three something rather than Python 2).
5. once the install is done, at a terminal prompt type

```
> jupiter notebook
```	

The ">" represents the command prompt - yours may look different. You don't need to type that.


or if you used the automated installer - use the launcher on the desktop or in your start menu.

###Have a play

Can you do multiplication?

Can you do other math type operations?

It's highly likely you'll cause an error.....don't worry, while they sound serious, it's just Python being confused and asking you to change the thing that is confusing it so it can do what you have asked it to do.

Think of Python like a puppy, like Pluto.

It understands certain "key words" like run, sit, fetch, stay.

When you get an error (I say when because I still get them, I use them to hack out code when I don't want to look up the answer.)



The Python keywords will show up in a different colour in the Jupiter Notebook

###Assign a value to a variable name
- must be alphanumeric and not start with a number but can contain numbers and certain other punctuation. The '.' has a special meaning in Python variables so maybe use '_' to put breaks in your variable names.
- Use meaningful names.
- create a variable that contains your first and last name.
- can you multiply it, can you add it to itself? Can you divide it? This behaviour is called "operator overloading". As long as it makes sense, Python will do it for you. If it can't work out what you want, it will send a message pointing out what was confusing.

###Import glob

```
from glob import glob

```
```
glob('*.csv')
```

Glob will create a list of all the files ending with '.csv' . The '*' is a wildcard and stands for 'anything'

###Get that file into Python

```
with open(file,'r',encoding='latin') as fh:

	for line in fh:
		print(line)

```















 