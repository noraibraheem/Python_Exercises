#generator 
#it it an usual function but it uses yield
#by using next()it resumes from where it called yield not from begining
#when called it not start automitically it only gives you the control

def my_generator():
    yield 1
    yield 2
    yield 3
    yield 4

print(my_generator())

mygen=my_generator()
print(next(mygen))
print("hello world")
print(next(mygen))
print("hello world")
#print(next(mygen))
#print("hello world")
#print(next(mygen))
#print("hello world")

for i in mygen:
    print(i)