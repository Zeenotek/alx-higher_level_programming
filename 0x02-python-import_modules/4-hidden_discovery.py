#!/usr/bin/python3
if name == "_main_":

    import hidden_4
    names = dir(hidden_4)
    for i in names:
        if i[:2] != "__":
            print("{:s}".format(i))
