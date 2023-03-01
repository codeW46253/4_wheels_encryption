



alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789?!@#$%^&*()-_=+[]{}<>|\'\";:/?., \n\t"
alpha_list = []
for index in range(len(alpha)):
    alpha_list.append(alpha[index])

wheel_1 = ['Q', 'U', '_', '\n', '<',
           '+', '-', ')', ';', 'F',
           'S', '!', 'B', '[', 'O',
           'Y', '7', 'I', '?', ':',
           '6', 'J', '$', '#', '=',
           '>', 'N', 'R', 'E', 'A',
           '&', 'P', 'K', '2', '8',
           '4', '*', 'C', '^', ' ',
           'H', 'D', 'W', '\t', 'M',
           '@', 'Z', ']', 'T', '1',
           '5', '9', '3', 'X', '{',
           '(', '|', '0', ',', '/',
           "'", '?', '.', '}', 'V',
           '%', '"', 'G', 'L']

wheel_2 = ['N', '$', 'J', ']', '?',
           '!', '.', '(', '}', '*',
           'U', '@', '%', ')', 'Y',
           'R', '=', 'V', 'K', '6',
           'Z', '_', '^', '&', '3',
           '\n', '7', '|', '1', '"',
           'H', 'E', ' ', '{', '#',
           'T', '5', '8', '\t', 'B',
           '-', 'A', '0', 'P', '9',
           'M', 'X', 'F', 'S', '>',
           'W', '/', ',', '4', '[',
           '<', '?', 'O', 'C', "'",
           ';', 'L', '+', 'I', '2',
           'Q', 'G', 'D', ':']

wheel_3 = ['N', 'R', '6', ',', '(',
           '#', '7', '\t', '=', '^',
           '+', ' ', 'C', '-', '|',
           'K', '&', '3', 'P', '{',
           '2', '?', 'S', 'Q', '}',
           ';', 'Z', "'", 'W', 'T',
           '/', ')', '*', '"', 'Y',
           'D', '$', 'F', '8', '!',
           '[', '?', '%', 'A', '.',
           'G', 'H', 'O', 'J', '9',
           '5', 'I', 'B', '4', '@',
           '<', '0', '_', 'L', ']',
           '>', 'M', 'U', ':', 'E',
           'V', '1', '\n', 'X']
wheel_4 = ['#', '@', '>', '{', '2',
           'U', 'M', ']', '"', 'Z',
           'Y', '9', '_', '%', '3',
           'A', ',', 'D', 'R', 'I',
           '5', "'", '^', '.', '8',
           'N', 'X', '<', '}', ':',
           '?', 'E', '6', '|', 'O',
           'C', '\t', 'L', 'H', ';',
           'W', '-', '?', '$', 'P',
           'K', 'S', '4', '&', ' ',
           'V', '=', '*', '7', '/',
           'G', ')', '0', '+', 'Q',
           '[', 'T', 'F', 'B', '\n',
           '1', '!', '(', 'J']

################################################################################################

if __name__=="__main__":
    
    
    # debug
    len_test = False
    content_test = False
    PO2_test = False
    availability_test = False
    
    start_debug = len_test or content_test or PO2_test or availability_test
    
    if start_debug:
        print("DEBUG MODE [ACTIVE]")
        
    else:
        while True:
            find = input("Search by [I]ndex or [C]haracter?\n>>>")[0].lower()
            if find == "i":
                find_index = int(input(f"Enter integer between 0 to {len(alpha_list)}: "))
                print(f"""
Index of {find_index}
Main Wheel: {alpha_list[find_index]}
Wheel 1   : {wheel_1[find_index]}
Wheel 2   : {wheel_2[find_index]}
Wheel 3   : {wheel_3[find_index]}
Wheel 4   : {wheel_4[find_index]}
    """)
                
            if find == "c":
                find_char = input(f"Enter character: ").upper()
                
                print(f"Searching for char \"{find_char}\"")
                
                print(f"""
Character {find_char}
Main Wheel: {alpha_list.index(find_char)}
Wheel 1   : {wheel_1.index(find_char)}
Wheel 2   : {wheel_2.index(find_char)}
Wheel 3   : {wheel_3.index(find_char)}
Wheel 4   : {wheel_4.index(find_char)}
    """)
                
                
    
    if content_test:
        print(alpha_list)
        print(wheel_1)
        print(wheel_2)
        print(wheel_3)
        print(wheel_4)
    
    if len_test:
        print(len(alpha_list))
        print(len(wheel_1))
        print(len(wheel_2))
        print(len(wheel_3))
        print(len(wheel_4))
        
    if PO2_test:
        print(f"Original Lenght: {len(alpha_list)}")
        print(f"Wheel 1        : {len(wheel_1) / len(alpha_list) * 100.00}")
        print(f"Wheel 2        : {len(wheel_2) / len(alpha_list) * 100.00}")
        print(f"Wheel 3        : {len(wheel_3) / len(alpha_list) * 100.00}")
        print(f"Wheel 4        : {len(wheel_4) / len(alpha_list) * 100.00}")
        
    if availability_test:
        for item in alpha_list:
            in_wheel_1 = False
            if item in wheel_1:
                in_wheel_1 = True
                
            in_wheel_2 = False
            if item in wheel_2:
                in_wheel_2 = True
                
            in_wheel_3 = False
            if item in wheel_3:
                in_wheel_3 = True
                
            in_wheel_4 = False
            if item in wheel_4:
                in_wheel_4 = True
            
            print(f"{str(item)} in:\nWheel 1: {in_wheel_1}\nWheel 2: {in_wheel_2}\nWheel 3: {in_wheel_3}\nWheel 4: {in_wheel_4}\n")