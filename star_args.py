def calc_average(*args,b, c):
    mean = 0
    for arg in args:
        mean += arg
    return mean / len(args)
   # return (args+b+c)/3

print(calc_average(2, b=4, c=6))
