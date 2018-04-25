def rev(s):
    a = list(s)
    a.reverse()
    return (''.join(a))
a = input("Please enter a string:")
print (rev(a))
