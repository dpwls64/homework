

'''
2. my_split() 함수 구현 : str 내용 중 ch를 기준으로 분리하여 List에 저장 후 return 함수

   def my_split(str, ch):
'''



l = []
result = []

str = input("Input String : ")
ch = input("Input Standard : ")

def my_split(str, ch):



    a = str.find(ch)
    l.append(a)
   
    
    while str[a+1:].find(ch) != -1:
      
        a = str[a+1:].find(ch) + a + 1
    
        
        l.append(a)
        

    result.append(str[0:l[0]])
    
    

    for i in range(len(l)-1):
        result.append(str[l[i]+1:l[i+1]])
        b = (str[l[i+1]+1 : ])

    result.append(b)
    return result


print(my_split(str,ch))
