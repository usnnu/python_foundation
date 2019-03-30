# _*_ coding:UTF-8 _*_

#decrator


def eval_now(func):
    return func()

@eval_now
def foo():
    return 1

print(foo)
