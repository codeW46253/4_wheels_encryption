import random

debug = not False

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789?!@#$%^&*()-_=+[]{}<>|\'\";:/?., \n\t"
alpha_list = []

for index in range(len(alpha)):
    alpha_list.append(alpha[index])

index_list = []
while len(index_list) < 69:
    new_item = random.randint(0, 68)
    
    if new_item not in index_list:
        index_list.append(new_item)
        
new_alpha_list = []
for i in range(len(alpha)):
    new_alpha_list.append(" ")        

for i in range(len(alpha_list)):
    new_alpha_list[i] = alpha_list[index_list[i]]
    
        
 
print(f"last: {new_alpha_list} \n {len(new_alpha_list)} from {len(alpha)}")