# Auger
Auger is a project to automatically generate unit tests for Python code.

See
[these slides](http://goo.gl/PuZsgX)
or
[this blog](http://chrislaffra.blogspot.com/2016/12/auger-automatic-unit-test-generation.html)
entry for more information.

This is a fork of the original repository: [https://github.com/laffra/auger](https://github.com/laffra/auger)

Since the library is not totally compatible with python 3, I decided to edit it a bit and make it compatible with it.

I did it with the objective of maintain it for the future version of python, so, please if you have suggestions or improvements to push, feel free to contribute to it.

# Running Auger
    
To generate a unit test for any class or module, for Python 2 or 3, do this:

```python
import auger

with auger.magic([ <any list of modules or classes> ]):
    <any code that exercises your application>
```

# A Simple Example

Here is a simple example that does not rely on Auger at all:

```python
class Foo:                # Declare a class with a method
    def bar(self, x):
        return 2 * x      # Duplicate x and return it

def main():
    foo = Foo()           # Create an instance of Foo
    print(foo.bar(32))    # Call the bar method and print the result

main()
```

Inside the `main` function we call the `bar` method and it will print 64.

# Running Auger on our Simple Example

To generate a unit test for this class, we run the code again, but this time in the context of Auger:

```python
import auger
import foo
from foo import Foo

with auger.magic([Foo]):
    foo.main()
```

This will print out the following:

    64
    Auger: generated test: tests/test_Foo.py




# Some error you could have
* Sometimes it does not include all the libraries;
* Sometimes you need to include:
```python
import sys
sys.path.append("..")
```
* Sometimes you have to add some ```()``` to the methods.



# Benefits of Auger

By automatically generating unit tests, we dramatically cut down the cost of software
development. The tests themselves are intended to help developers get going on their unit testing
and lower the learning curve for how to write tests.

# Known limitations of Auger

Auger does not do try to substitue parameters with synthetic values such as `-1`, `None`, or `[]`. 
Auger also does not act well when code uses exceptions. Auger also does not like methods that have a decorator.

Auger only records a given execution run and saves the run as a test. Auger does not know if the code actually
works as intended. If the code contains a bug, Auger will simply record the buggy behavior. There is no free
lunch here. It is up to the developer to verify the code actually works.
