import random


class Animal(object):
  def __init__(self, species, age=0):
    self._species = species
    self.__set_age(age)

  def __set_age(self, age):
      self._age = age or random.randint(1, 100)

  def get_species(self):
    return self._species

  def get_age(self):
    return self._age

  def get_complex_object(self):
    return random.Random()

  def __str__(self):
    return '%s:%s' % (self._species, self._age)


def main():
  a = Animal('Cat', 10)
  print(a)
  print(a.get_species())

if __name__ == '__main__':
  main()
