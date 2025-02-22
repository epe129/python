def build_string(*args):
    x = ", ".join(args)
    txt = f"I like {x}!"
    # print(txt)
    return txt


build_string('Cheese','Milk','Chocolate')