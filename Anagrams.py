def check(str1, str2):

    if(sorted(str1)== sorted(str2)):
        print("Anagram") 
    else:
        print("Not Anagram")         
         
 
str1 =input()
str2 =input()
check(str1, str2)
#sort is mutable and sorted is immutable,i.e sort is stored in itself 

