# Challenge Summary
Write a function called fizz buzz tree

Arguments: k-ary tree

Return: new k-ary tree

Determine whether or not the value of each node is divisible by 3, 5 or both. Create a new tree with the same structure as the original, but the values modified as follows:

If the value is divisible by 3, replace the value with “Fizz”

If the value is divisible by 5, replace the value with “Buzz”

If the value is divisible by 3 and 5, replace the value with “FizzBuzz”

If the value is not divisible by 3 or 5, simply turn the number into a String.

## Whiteboard Process

![](ch18w.png)


## visualization

![](ch18v.png)



## Approach & Efficiency
I followed the approach that the code takes the least time and space, where B(o) takes space and time and be simple to be easy to understand

## Solution
```

    def fizz_buzz_tree(self, root):

        rot = []
        if root != None:
            current = root
            rot += [current]

            try:
                while rot != []:
                    rot += [rot[0].left]
                    rot += [rot[0].right]

                    if rot[0].value%3==0 and rot[0].value%5==0:
                       rot[0].value="FizzBuzz"


                    elif rot[0].value % 3 == 0 :
                        rot[0].value= "Fizz"


                    elif rot[0].value % 5 == 0 :
                        rot[0].value="Buzz"



                    del rot[0]
            except:

                return root
        else:
            raise Exception("tree is empty")
```