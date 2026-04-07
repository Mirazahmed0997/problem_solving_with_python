
data=[1,2,3,4,5,6,7,8,9,10,11]

def batch_generator(batch_size,data):
    for i in range(0,len(data),batch_size):
        yield data[i:i+batch_size]

x=batch_generator(3,data)

print(next(x))
print(next(x))
print(next(x))
print(next(x))
