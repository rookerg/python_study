tamp = [1, 2] + [3, 4]

tamp.remove(3)
tamp.remove(1)
tamp = [1, 1, 1, 1]
tamp.remove(1)
#모든 같은 데이터를 지우지않는다
#하나만 지운다.
#[1, 1, 1]

print(tamp)

tamp = [1, 1, 1, 1]


def check(num):
        if num == 1:
            return False
        else:
            return True

#print(check(231321))
#print(True)

#tamp = [1, 2, 3, 1, 1]
#tamp = Fillter(check, tamp)
#tamp = list(tamp)


tamp = [1, 2, 3, 4, 5]
tamp = [[1, 2], [3, 4]]


#print(tamp[0])
#print(tamp[0][0])

tamp = [
    {"a", "c"}
    ,{"b", "d"}    
]


tamp = [
    {"key":"value", "name":"이름"}
    ,{"b":"d", "aa":"bb"}    
]

#print(tamp[0])
print(tamp[0]["name"])








