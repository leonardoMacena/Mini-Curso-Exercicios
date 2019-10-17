def decora (f):
  def interna(*args, **kwargs):
    x = args[0] + 1
    return f(x)
  return interna

@decora
def test(x):
  print(x)




print(test.__name__)


test(1)
