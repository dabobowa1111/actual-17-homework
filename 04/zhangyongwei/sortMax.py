l = [(1,3),(4,7),(2,5),(2,1),(6,2),(4,1)]

print sorted(l,key=lambda x:max(x))

print sorted(l,key=lambda x: x[0] if x[0] > x[1] else x[1])