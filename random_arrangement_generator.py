
import random

# Random Arrangement Generator
#
# Create an arrangement of characters for each wheels
# in "wheel_setup.py".
#

def rand_arrange():
    # change this for availability of characters
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789?!@#$%^&*()-_=+[]{}<>|\'\";:/\\., \n\t"
    alpha_list = []
    alpha_len = 0

    for index in range(len(alpha)):
        alpha_list.append(alpha[index])
        alpha_len += 1
    
    # set a randomize arrangement of indexes
    index_list = []
    while len(index_list) < alpha_len:
        new_item = random.randint(0, alpha_len - 1)
    
        if new_item not in index_list:
            index_list.append(new_item)
        
    # set an arrangement of characters by a randomized arrangement of indexes
    new_alpha_list = []
    for i in range(len(alpha)):
        new_alpha_list.append(" ")        
    
    for i in range(len(alpha_list)):
        new_alpha_list[i] = alpha_list[index_list[i]]
        
    return [alpha, new_alpha_list]
    
        
if __name__ == "__main__":
    alpha, new_alpha_list = rand_arrange()
    print(f"last: {new_alpha_list} \n {len(new_alpha_list)} from {len(alpha)}")

    
    
    
    
