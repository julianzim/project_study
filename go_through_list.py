def go_through(lst, res):
    if lst == []:
        return 'ты еблан?'
    for i in lst:
        if isinstance(i, list):
            go_through(i, res)
        else:
            res.append(i)
    return res

inp = [[3,4], [5,6], [7,8]]

res = []
print(go_through(inp, res))