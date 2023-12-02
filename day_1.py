f=open("day_1_input")

def part1_v1():
    # place holder for sum
    num=0
    for line in f.readlines():
        # how to check if a string character can be int-y-fied ?
        num_string=''

        for char in line:
            try:
                int(char)
            except ValueError:
                pass # maybe line.remove(char) ?
            else:
                num_string+=char
        
        tens=int(num_string[0])
        units=int(num_string[-1])
        num+=10*tens+units

    return num

def find_all(sub,str):
    
    list_return=[]
    # look for instance of string
    # if not found, return currently built set
    # if found, attach index to list, jump to next position and repeat

    i_sub=str.find(sub)
    while i_sub!=-1:
        list_return.append((i_sub))
        i_sub=str.find(sub,i_sub+1)
    
    return list_return

# not working atm
def part2_v1():

    dict_alphabetic_digits={
        'one':1,
        'two':2,
        'three':3,
        'four':4,
        'five':5,
        'six':6,
        'seven':7,
        'eight':8,
        'nine':9
    }

    # place holder for sum
    num=0
    lines=f.readlines()
    for i_line,line in enumerate(lines):

        list_digits_total=[]
        list_digit_indices_total=[]
        
        for digit in dict_alphabetic_digits:
            list_digit_indices=find_all(digit,line)
            list_digits=[digit for _ in list_digit_indices]

            list_digit_indices_total+=list_digit_indices
            list_digits_total+=list_digits
        
        for digit in range(1,10):
            list_digit_indices=find_all(str(digit),line)
            list_digits=[digit for _ in list_digit_indices]

            list_digit_indices_total+=list_digit_indices
            list_digits_total+=list_digits

        final_list=list(zip(list_digit_indices_total,list_digits_total))
        final_list.sort(key=lambda item: item[0])
        
        def decode(num):
            if num in dict_alphabetic_digits:
                return dict_alphabetic_digits[num]
            else:
                return int(num)

        tens=decode(final_list[0][1])
        units=decode(final_list[-1][1])
        if len(final_list)<2:
            print("WARNING: have none- or single-value list "+str(final_list)+" from line "+line.strip())
            aux=units
        else:
            aux=10*tens+units
        
        num+=aux

    return num

if __name__=='__main__':
    print(part2_v1())