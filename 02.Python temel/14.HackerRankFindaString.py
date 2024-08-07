def count_substring(string, sub_string):
    a = 0
    b = len(sub_string)
    
    for i in range(len(string) - b + 1):
        if string[i:i+b] == sub_string:
            a += 1
            
    return a
            
            

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)

