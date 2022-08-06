g = {}
a = {'test.txt': 'tosin', 'test2.txt': 'gabriel', 'test3.txt': 'tosin'}
x = lambda b: a[b]
for i in a:	
    if x(i) in g:
    	g[x(i)].append(i)
    else:
    	g[x(i)] = [i]