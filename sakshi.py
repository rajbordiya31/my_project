class shape():
    def area(self):
        return 'undefined'
class rectangle():
    def area(self,l,b):
        return f"Area of rectangle is {l*b} "
class circle():
     def area(self,r):
         return f"Area of circle is {3.14*r**2}"
s1=shape()
print(s1)    

r1=rectangle()
print(r1.area(2,8))

c1=circle()
print(c1.area(6))