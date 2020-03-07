#Python 3 implemnetation of Shaker_Sort

def Shaker_Sort(arr):
     n=len(arr)
     #getting the length of the listto get the end
     begin=0
     end=n-1
     swapped=True
     #if swapped is false then we can stop the sorting as the elements in the list all are in sorted order

     while swapped==True :
          #so we will continue until it is false

          for i in range(begin,end,1):
               if arr[i]>arr[i+1]:
                    #left element is greater than that of right elemnet in the list
                    arr[i],arr[i+1]=arr[i+1],arr[i]
                    #swapping the elemnets of the list
                    swapped=True
          if swapped ==False:
               break
               #we will stop as our list is totally sorted
          swapped=False

          #now have to apply bubble_sort from opposite direction as our list is not sorted
          #we have to leave the elemnet at the end as it is in its correct position
          end=end-1
          for i in range(end-1,begin-1,-1):
               if arr[i]>arr[i+1]:
                    #left element is greater than that of right elemnet in the list
                    arr[i],arr[i+1]=arr[i+1],arr[i]
                    #swapping the elemnets of the list
                    swapped=True
          #now the smallest elemnet will be in the left of the list in its correct place
          #we have to leave that and we have to apply sort on remaining
          begin=begin+1

#this is the driver code or tester

#arr=[2,10,8,1,4,1]
#sample input this can be extended over user inputs even
arr=list()
arr = list(map(int,input("Enter array: ").strip().split(',')))
Shaker_Sort(arr)
print("After Shaker_Sort the list :")
for i in range(0,len(arr),1):
     print(arr[i],end=" ")
#outpu 1 1 2 4 8 10
