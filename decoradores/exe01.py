def media():
  valores = []
  def calcula_media(valor):
    valores.append(valor)
    return sum(valores)/len(valores)
  return calcula_media

x = media()
print(x(1))
print(x(2))
print(x(3))
