def t():
    num = []
    for i in range(10):
        yield num
        #num.append(i)
    #return num

    # ジェネレータが使えるなら、ジェネレータを使う

def other_func(func):
    print(func(10))

def test_func(x):
    return x * 2

other_func(lambda x: x * 2)

y = None
x = 1 if y else 2
print(x)

def base(x):
    def plus(y):
        return x + y
    return plus

plus  = base(10)
print(plus(10))

# グローバル変数によって書き換えられる恐れがあるため、base関数の中で定義する