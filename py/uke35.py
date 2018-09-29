2 // 3
4 // 5
5 // 5
7 // 7
8 // 7
10 // 3
0 // 4
12 // 4

# funk1(1, 4)  # => 5
# funk1(2, 2)  # => 4
# funk1(3, 5)  # => 8
# funk1(4, -6) # => -2

# funk2(2, 4)  # => 16
# funk2(3, 3)  # => 27
# funk2(90, 0) # => 1

# funk3(3) # => True
# funk3(2) # => False
# funk3(11) # => True
# funk3(1) # => True
# funk3(22) # => False

def funk3(n):
    if n == 1 or n == 2:
        return 1 
    else:
        return  funk3(n-1) + funk3(n-2)


for i in range(100):
    print(funk3(i))
