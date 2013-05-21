def optimization(tree):
    etype = tree[0]  # element type
    if etype == "binop":    # a * 1 -->a
        a = optimization(tree[1]) # this will recursively check for (a*1) * 1
        op = tree[2]
        b = optimization(tree[3]) # 1 * (a+0)

        if op == "*" and b == ("number", "1"):
            return a
        elif op == "*" and b == ("number", "0"):   #a*0-->0
             return b  # or ("number", "0")
        elif op == "+" and b == ("number", "0"):    #a+0-->a
            return a

        return tree
