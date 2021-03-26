class name(object):
  def __init__(self, name):
    self.name = name
  def PrintName(self):
    print(self.name)

a = name('bob')
a.PrintName()
