def fizz_buzz():
    i = 1
    while i < 101:
        print(i)
        i+=1

        if i%3==0:
         print("fizz")
        elif i%5==0:
            print("buzz")
    
        elif i%5 and 3==0:
            print("fizzbuzz")

        else:
            print(i)

fizz_buzz()