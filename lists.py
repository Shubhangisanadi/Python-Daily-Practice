
a = [10, 20]
a.append(30)
print(a)      # --> dusri value ko add krta h like 30

b = [10, 30]
b.insert(1, 20)
print(b)      # --> index par item add krta hai

c = [1, 2]
c.extend([3,4])
print(c)      # --> dusri list ke item add krta hai

d = [40, 50, 60]
d.remove(50)
print(d)      # --> di hui value ka itme remove karta hai


e = [40, 50, 60]
e.pop()
print(e)      # --> item remove karta hai aur removed item return karta hai. default: last item


f = [10, 20]
f.clear()
print(f)      # --> saare itmes ko remove karta hai


g = [70, 50, 40]
print(g.index(50))   # --> value ka pehla index batata hai

h = [10, 30, 10, 50, 10]
print(h.count(10))   # --> value kitni baar aayi hai count krta hai

i = [30, 10, 90]
i.sort()
print(i)        # --> list ko ascending order me arrange karta hai like 1 to 10

j = [60, 30, 20]
j.reverse()
print(j)        # --> list ke current order ko ulta krta hai like 20, 30, 60

k = [30, 80]
a = k.copy()
print(a)       # --> list ki shallow copy banata hai


mylist = [ 1, 44, 60, 77, 90, 37]
#print(sum(mylist))

#print(max(mylist))

#print(min(mylist))

print(mylist)