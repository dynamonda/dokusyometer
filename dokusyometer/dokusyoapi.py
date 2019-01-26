#!/usr/bin/python

def user_datas_from_id(id):
    if isinstance(id, int) == False:
        raise TypeError
    datas = {}
    datas["name"] = "dynamonda"
    return datas

def main():
    pass

if __name__ == '__main__':
    main()
