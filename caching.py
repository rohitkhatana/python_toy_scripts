import time

def complex_computation(a,b):
    time.sleep(.5)
    return a+b

cache = {}

def cached_computation(a,b):
    if (a,b) in cache:
        return cache[(a,b)]
    else:
        result = complex_computation(a,b)
        cache[(a,b)] = result
        return result

def top_arts():
    key = 'top'
    if key in cache:
        print cache[key]
    else:
        cache[key]=['s','s']
        print cache

print top_arts()
    
"""start_time = time.time()
print cached_computation(5, 3)
print "the first computation took %f seconds" % (time.time() - start_time)

start_time2 = time.time()
print cached_computation(5, 3)
print "the second computation took %f seconds" % (time.time() - start_time2)
"""
