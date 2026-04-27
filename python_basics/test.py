# 作者:李一安
# 2026年04月15日10时53分24秒


def test(a,b,*args,c,**kwargs):
    print(a)
    print(b)
    print(args)
    print(c)
    print(kwargs)

test(1,2,3,4,c=5,d=6,e=7)