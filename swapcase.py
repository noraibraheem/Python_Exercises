"""def swap_case(s):
     
    if 0<len(s)<=1000:
        result=""
        for i in s:
            if i ==i.upper():
                result+=i.lower()
            else:
                result+=i.upper()
    return result

if __name__ == '__main__':
    s =input()
    result = swap_case(s)
    print (result)
  

print("#"*100)

def split_and_join(line):
    
   List= line.split()
   List="-".join(List)
   
   return List
   
    # write your code here

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print (result)"""
#print first name and last of string
def print_full_name(first, last):
    
       
    return print(f"Hello {first} {last}! You just deloved into python")
if __name__ == '__main__':
    first_name =input()
    last_name = input()
    print_full_name(first_name, last_name)

# how to find string
def count_substring(string, sub_string):
    if 1<=len(string)<=200:
            count = 0
            for i in range(len(string)):
                if string[i:].startswith(sub_string):
                    count += 1
            return count



