# Challenge Summary
Write a function called breadth first

Arguments: tree
Return: list of all values in the tree, in the order they were encountered
## Whiteboard Process

![](ch17w.png)


## visualization

![](ch17.jpg)



## Approach & Efficiency
I followed the approach that the code takes the least time and space, where B(o) takes space and time and be simple to be easy to understand

## Solution
```

     def breadth_first(self,root):
        visit=[]
        rot=[]
        if root!=None:
            current = root
            rot+=[current]

            try:
                while rot!=[]:
                    rot+=[rot[0].left]
                    rot+=[rot[0].right]
                    visit+=[rot[0].value]
                    del rot[0]
            except:

                return visit
```