Embarking on Codewars

#Solution- Remove String Spaces
1.def no_space(x):
    return x.replace(" ", "")


2.def no_space(x):
    return ''.join(x.split())


3.def no_space(x):
    return ''.join([char for char in x if char != ' '])

