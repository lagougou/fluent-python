registory = set()
def register(active=True):
    def decorate(func):
        print('running register(active=%s) ->decorate(%s)' %(active, func) )

        if active:
            registory.add(func)
        else:
            registory.discard(func)
        return func
    return decorate

@register(active=False)
def f1():
    print("running f1()")

@register()
def f2():
    print("Running f2()")