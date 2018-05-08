def rev(s):
    a = list(s)
    a.reverse()
    return (''.join(a))
#!/usr/bin/python3
i=input('请输入字符串:');
l=str(i)
a = rev(l)
print (a)
