class PancakeSort:
    """ PancakeSort Algorithm Implementation in Python 3.0+

        arr : Unorded list
        output : Return list in ascending order.
        time complexity : O(n^2)

        Example :
        >>> sort = PancakeSort()
        >>> sort([4, 2, 6, 5, 9, 8])
        [2, 4, 5, 6, 8, 9]
    """

    def __init__(self):
        print("Pancake Sort Algorithm is Initialized")

    def __call__(self, A):
        end=len(A)
        res=[]
        while end>1:
            maxInd=A.index(max(A[:end])) #step 1 get max
            if maxInd==end-1: #if Max already at the end then its in the right place decrement end and continue
                end-=1
                continue

            #making the max element at Index 0, unless if it already was at index 0
            if maxInd!=0:
                A[:maxInd+1]=reversed(A[:maxInd+1])
                res.append(maxInd+1) #append flipping size which is maxInd+1
                
                
            #Now max is at ind=0, flip whole array to make it at the "end"
            A[:end]=reversed(A[:end])
            res.append(end)
            
            end-=1 #decrement end
        return res    

sort = PancakeSort()
print(sort([10, 9, 5, 11, 2]))
