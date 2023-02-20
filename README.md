# Football Tournament Tracker

## Github Set-up
**These instructions apply to `git bash`**

* Clone repo into local directory using `git clone https://github.com/WBL2-Football-Project/football`

* Everytime you open your local project run the command `git pull` this will get any updates other members have made

* When uploading changes to the project use `git commit -a -m "Change Notes"` then `git push` to publish changes to the repo.

* When adding a new file first use `git add <file-name>` before committing or pushing changes

* For pushing to a new branch first use `git checkout <branch-name>` to switch branch or `git checkout -b <branch-name>` to create a new branch. Then use `git push origin <branch-name>` to push changes to specific branch.

## Project Set-up

1. Install all required libraries being used in the project by running `pip install -r requirements.txt`

## Detailed Instruction for pytest (by using console)

1. Installation is done by requirements.txt or by `pip install pytest` manually.
2. How to add tests to the program.

If you have simple program like:
```python
# pytest - test and presentation how to use
#

# use classes & methods
class Square:
	def __init__(self, length:int, width:int):
		self.length = length
		self.width = width
	def calculate_surface(self):
		return self.length*self.width
	def some_calculation(self):
		return (1+self.length)*(1+self.width)

if __name__ == '__main__':
	square=Square(10,20)
	print(f"square surface={square.calculate_surface()} calculation={square.some_calculation()}")
```

To define test we need to add code like below:

```python
from unittest import TestCase

class SquaresTesting(TestCase):
	def test_surface(self):
		square=Square(10,20)
		self.assertTrue(square.calculate_surface()==10*20)
		square=Square(20,30)
		self.assertTrue(square.calculate_surface()==20*30)
	def test_some_calculation(self):
		square=Square(10,20)
		self.assertTrue(square.some_calculation()==(1+10)*(1+20))

```
which expects any used resources defined (e.g.Square)

Finally entire source code looks like below:

```python
# pytest - test and presentation how to use
#

# use classes & methods
class Square:
	def __init__(self, length:int, width:int):
		self.length = length
		self.width = width
	def calculate_surface(self):
		return self.length*self.width
	def some_calculation(self):
		return (1+self.length)*(1+self.width)

# how to use pytes
from unittest import TestCase

class SquaresTesting(TestCase):
	def test_surface(self):
		square=Square(10,20)
		self.assertTrue(square.calculate_surface()==10*20)
		square=Square(20,30)
		self.assertTrue(square.calculate_surface()==20*30)
	def test_some_calculation(self):
		square=Square(10,20)
		self.assertTrue(square.some_calculation()==(1+10)*(1+20))

if __name__ == '__main__':
	square=Square(10,20)
	print(f"square surface={square.calculate_surface()} calculation={square.some_calculation()}")
```

3. We can start the program test by: 
`python -m pytest pytest_test_and_presentation.py`
which presents the following results:

![Alt text](https://github.com/WBL2-Football-Project/football/blob/main/tests/pytest-presentation-results.jpg "presentation tests results")

4. Summary
With OOP approach, we likely add separate test object for every class created. Every test object defines as many particular tests as needed to check everything related. Before combining new branch into the main source, we need to have all the necessary tests defined and completed to avoid risk of disordering the other works.

## VSCODE integration for debugging and pytesting .py files

1. We've done debugging and testing configuration with definitions shown below:

```json
{
	"configurations": [
		{
			"name": "Python: Current File",
			"type": "python",
			"request": "launch",
			"program": "${file}",
			"console": "integratedTerminal",
			"justMyCode": true
		},
		{
			"name": "Python: Current File Tests",
			"type": "python",
			"request": "launch",
			"module": "pytest",
			"console": "integratedTerminal",
			"justMyCode": true
		}
	]
}
```

2. To use it editing the particular source file, click 'debug' button on left side then choose one of the debuggin option from 'Run and debug' on top and click the related play button or hit Cmd/Ctrl+D shortcut.
