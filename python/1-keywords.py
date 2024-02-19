def outer():
  name="keshav"
  def inner():
    nonlocal name 
    print(name)
    name="Jha"
    #return name
  #name=inner(name)
  inner() 
  print(name)

outer()

