def odd_and_even(x:list[int])->list[int]:
    new_list:list[int]=list()
    for idx in range(0,len(x)):
        if idx%2==0 and x[idx]%2==1:
            new_list.append(x[idx])
    return new_list
    
def value_exists(dictionary:dict[str,int],integer:int)->bool:
    time_occur: int=0
    for key in dictionary:
        if dictionary[key]==integer:
            time_occur+=1
    if time_occur != 0:
        return True
    else:
        return False

 
test_dict : dict [str ,int] = {"a": 2 , "b": 4 , "c": 7 , "d": 1}
test_val : int = 4
print(value_exists ( test_dict , test_val ))

print(value_exists ( test_dict , 5))

def short_words(lis:list[str])->list[str]:
    new_list:list[int]=list()
    for item in lis:
        if len(item)<5:
            new_list.append(item)
        else:
            print(f"{item} is too long !")
    return new_list
my_list : list [str] = ["sun", "cloud", "sky"]
print(short_words ( my_list ))