def digit_count(digit):
    digit=str(digit)
    count=0
    for i in digit:
        count+=1
    return int(count)
    
def digit_diff(digit,digit_2):
    diff=digit_count(digit_2)-digit_count(digit)
    return int(abs(diff))

def row_converter(row):
	last=0
	for i in row:
		last+=1
	n=int(last/3)
	
	count=digit_count(last)
	space=count
	total=space*n
	difference=digit_diff(1,3*n)
	sec_space=1*space
	magic_row=[i for i in range(n)]
	magic_row.append('')
	last_row=''   
	magic_row[0]=' '*total+' '*difference+'1'
	total-=1
	
	for i in range(1,n):
		espace=0
		if digit_count(row[i])>1:
			espace=count-digit_count(row[i])-1
		magic_row[i]=' '*(total+espace)+str(row[i])+' '*(sec_space+count-digit_count(row[3*n-i]))+str(row[3*n-i])

		sec_space=sec_space+2*space
		total=total-1*count

	for i in range(n,2*n+1):
		last_row=last_row+' '*abs(count-digit_count(row[i]))+str(row[i])+' '*space
	magic_row[n]=last_row  
	return magic_row

def display(row):
    for i in row:
        print(i)

   
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
   sum=int(1+3*n*(n+1)/2)
   row=[i for i in range(1,total+1)]
   display(row_converter(row))
   print('')
   print("Magic trangle is : ")
   if (n%2==0):
           magic_row=even_row(row,m,n,total)
           display(row_converter(magic_row))
   else:
           magic_row=odd_row(row,m,n,total)
           display(row_converter(magic_row))
   
   print("")
   print("Sum = ",sum)   
a=1
while(a!=0):
   main()
   a=int(input("0 to out: "))
