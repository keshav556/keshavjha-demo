def divide(a,b):
  if b==0:
    raise Exception("CAnnot divide by Zero")
  return a/b
try:
  result=divide(10,20)
except Exception as e:
  print("error occured:",e)
