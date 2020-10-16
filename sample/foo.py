class Foo:            # Declare a class with a method
  def __init__(self, p):
    self._p = p

  def foo(self, x):
    return 2 * x + self._p

  def foo_get(self):
    return Bar.bar_get()


class Bar:
  @staticmethod
  def bar_get():
    return Bar()


def main():
  foo = Foo(3)           # Create an instance of Foo
  print(foo.foo(32))    # 64
  print(foo.foo_get())  # Bar instance


if __name__ == '__main__':
  main()