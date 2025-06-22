class Number:
    def __init__(self,n): # this is instructed call of n
        self.n = n

    def __add__(self, num): # this is direct call of m
     return  self.n + num.n
    
    def __mul__(self, nam):
        return self.n * nam. n

    def __sub__(self, nam):
        return self.n - nam. n
    
    def __truediv__(self, nam):
        return self.n / nam. n
    
    def __floordiv__(self, nam):
        return self.n // nam. n


n = Number (10)
m = Number (3)

print(n + m)

print(n.__mul__(m))    ### he nahi lihala tar chalel
print(n * m)

print(n.__sub__(m))       ### he nahi lihala tar chalel
print(n - m)

print(n.__truediv__(m))       ### he nahi lihala tar chalel
print(n / m)

print(n.__floordiv__(m))        ### he nahi lihala tar chalel
# print(n // m)

# this is concept
'''
/	__truediv__	10 / 3	        = 3.3333 (float)
//	__floordiv__	10 // 3 	= 3 (integer)

'''