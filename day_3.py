# what instead of iterating mechanically, we do something smarter ?
# in each line, look for all the numbers, and then just look around them to see if there's any symbol. if there is, just capture it
# OR
# in each line, look for the symbols, and then, look around them to see if there's any number in line (l-1),l and (l+1) index (i-1) to index (i+1) where i is the index of the symbol (basically look in a square around the symbol)
# there's no symbols in the first or last lines

from day_1 import find_all

f=open("day_3_input")
list_lines=f.readlines()
    
set_symbols=set()
for line in list_lines:
    for char in line.strip():
        if not char.isdigit() and char!=".":
            set_symbols.add(char)

set_symbols_str="".join(set_symbols)

def get_numbers_around(line,next_line,index):
    
    list_numbers=[]
    # number to the left
    if line[index-1].isdigit():
        digit_str=line[index-3:index]
        if "." in digit_str or any([symbol in digit_str for symbol in set_symbols]):
            print("case1")
            print("warning, digit_str ",digit_str)
        list_numbers.append(int(digit_str.strip(f".{set_symbols_str}")))
    
    # number to the right
    if line[index+1].isdigit():
        digit_str=line[index+1:index+4]
        if "." in digit_str or any([symbol in digit_str for symbol in set_symbols]):
            print("case2")
            print("warning, digit_str ",digit_str)
        list_numbers.append(int(digit_str.strip(f".{set_symbols_str}")))
    
    # numbers below, no number DIRECTLY below
    if next_line[index]==".":
        
        # number below left
        if next_line[index-1].isdigit():
            digit_str=next_line[index-3:index]
            if "." in digit_str or any([symbol in digit_str for symbol in set_symbols]):
                print("case3")
                print("warning, digit_str ",digit_str)
            list_numbers.append(int(digit_str.strip(f".{set_symbols_str}")))

        # number below right
        if next_line[index+1].isdigit():
            digit_str=next_line[index+1:index+4]
            if "." in digit_str or any([symbol in digit_str for symbol in set_symbols]):
                print("case4")
                print("warning, digit_str ",digit_str)
            list_numbers.append(int(digit_str.strip(f".{set_symbols_str}")))

    elif next_line[index].isdigit():

        # middle digit == first digit of number
        if next_line[index-1]==".":
            digit_str=next_line[index:index+3]
            if "." in digit_str or any([symbol in digit_str for symbol in set_symbols]):
                print("case5")
                print("warning, digit_str ",digit_str)

        # middle digit == last digit of number
        elif next_line[index+1]==".":
            digit_str=next_line[index-2:index+1]
            if "." in digit_str or any([symbol in digit_str for symbol in set_symbols]):
                print("case6")
                print("warning, digit_str ",digit_str)

        # middle digit == middle digit of number
        else:
            digit_str=next_line[index-1:index+2]
            if "." in digit_str or any([symbol in digit_str for symbol in set_symbols]):
                print("case7")
                print("warning, digit_str ",digit_str)
        
        num_to_add_str=digit_str.strip(f".{set_symbols_str}")
        list_numbers.append(int(num_to_add_str))
    return list_numbers


list_numbers=[]
# always check the line and the line below (avoid double counting)
for i_line in range(0,len(list_lines)):

    # find (indices of) symbols in line
    all_symbol_indices=[]
    for symbol in set_symbols:
        symbol_indices=find_all(symbol,list_lines[i_line])
        # symbol_list=[symbol for _ in range(len(symbol_indices))]
        all_symbol_indices+=symbol_indices

    # sort them in ascending order
    all_symbol_indices=sorted(all_symbol_indices)

    # run through the symbols and gather the numbers found around in a list
    for symbol_index in all_symbol_indices:
                    
        # where a symbol was found, get numbers around
        list_numbers+=get_numbers_around(list_lines[i_line],list_lines[i_line+1],symbol_index)

print("sum of numbers: ",sum(list_numbers))