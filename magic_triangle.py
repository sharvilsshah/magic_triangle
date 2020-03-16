def display(row,m,n,total):
   start=n
   print(" "*start,1)
   
   space=0
   k=total-1
   for i in range(1,n):
                if space==0:
                  print(" "*(start-i),row[i],row[k])
                else:
                  new_space=int((space+int((i-2))))
                  print(" "*(start-i),row[i]," "*new_space,row[k])
                space+=1
                k-=1
      
   print(" "*(start-n),end=" ")
   for i in range(m,2*m):
      print(row[i-1],end=" ")

   sum=1+3*n*(n+1)/2
   print('')
   print("Sum is : ",int(sum))

   
def odd_row(row,m,n,total):
   row1=row[0:int(m/2)]
   row2=row[total:total-int(m/2):-1]
   row3=row[n:total-int((m/2))+1]
   row4=row[int((m/2)):n]
   row1[1],row3[1]=row3[1],row1[1]
   row2.append(row1.pop(1))
   magic_row=row1+row2+row3+row4
   return magic_row
        
def even_row(row,m,n,total): 
        magic_row=[" " for i in range(total)]
        middle=int((m+1)/2)
        magic_row[n]=row[n]
        for i in range(middle-1):
                magic_row[i]=row[i]
        for i in range(n):
                magic_row[2*n+i]=row[2*n-i]
        for i in range(middle-1):
                magic_row[m+i]=row[n-1-i]
        for i in range(middle-1):
                magic_row[m+middle-1+i]=row[total-middle-i]
        for i in range(middle-1):
                magic_row[middle+i-1]=row[2*n+middle-1+i]
        return magic_row
def main():
   m=int(input("Enter the no of Elements in one side>2: "))
   n=m-1
   total=3*n
   row=[i for i in range(1,total+1)]
   display(row,m,n,total)
   print('')
   print("Magic trangle is : ")
   if (n%2==0):
           magic_row=even_row(row,m,n,total)
           display(magic_row,m,n,total)
   else:
           magic_row=odd_row(row,m,n,total)
           display(magic_row,m,n,total)

   print("")
#  display(row,m,n,total)

a=1
while(a!=0):
   main()
   a=int(input("0 to out: "))



