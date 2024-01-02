
def get_new_details(xyz):
    print(xyz)
    xyz['test3']=789
    print(xyz)
    print(globals())
#    print("Global TL value: ", globals()['tl'])
    return    xyz
