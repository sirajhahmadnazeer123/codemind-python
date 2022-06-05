class ip(object):
   def defang(self, address):
      address = address.split(".")
      return "[.]".join(address)
ob1 = ip()
n=input()
print(ob1.defang(n))