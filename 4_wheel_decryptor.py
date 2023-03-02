
import wheel_setup

################################################################################################
# Decryption
#
# See step and order for setting wheel on "Setting.txt" file
#
# Decrypt any text with this step:
#   1) call "Decryptor" class
#   2) set the wheels selection acording to this list:
#       0 - wheel_setup.wheel_1
#       1 - wheel_setup.wheel_2
#       2 - wheel_setup.wheel_3
#       3 - wheel_setup.wheel_4
#   
#   3) enter 3 level shift key [main lock for encryption] only arround 0<= x <= lenght
#      of main character's arrangement
#   4) call "decryption" function from "Decryptor" class and push your code, shift keys
#      and special key [produced by encryption of text/code]
#
#
################################################################################################


################################################################################################
class Decryptor:
    def __init__(self):
        self.encr_w1 = []
        self.encr_w2 = []
        self.encr_w3 = []
        self.encr_w4 = []
        self.alpha_list = wheel_setup.alpha_list
        
        self.encr_key1 = 0
        self.encr_key2 = 0
        self.encr_key3 = 0
        
    # step setting for encryption and decryption [Don't edit unless you know how to handle it]
    def order_setting(self):
        self.order = [[self.alpha_list, self.encr_w1, self.encr_w3, self.encr_w3, self.encr_w1], # from wheel
                      [self.encr_w1, self.encr_w2, self.encr_w4, self.encr_w2, self.alpha_list], # to wheel
                      [0b10000, 0b01000, 0b00100, 0b00010, 0b00001], # lock
                      [self.encr_key1, self.encr_key2, self.encr_key3, self.encr_key2, self.encr_key1] # key
        ]
        
        self.order_lenght = 5
            
################################################################################################
# settings : 1) Wheel
#            2) Shift key
    def wheel_setting(self, w1, w2, w3, w4):
        wheels = [wheel_setup.wheel_1,
                  wheel_setup.wheel_2,
                  wheel_setup.wheel_3,
                  wheel_setup.wheel_4]
        
        self.encr_w1 = wheels[w1]
        self.encr_w2 = wheels[w2]
        self.encr_w3 = wheels[w3]
        self.encr_w4 = wheels[w4]
        
    def key_setting(self, key1, key2, key3):
        self.encr_key1 = key1 % wheel_setup.alpha_len
        self.encr_key2 = key2 % wheel_setup.alpha_len
        self.encr_key3 = key3 % wheel_setup.alpha_len

################################################################################################
# code for character/alphabet swap
    def rechange(self, alpha_from_wheel, alpha_to_wheel, code, shift_key, lock, comb):
        """rechange(wheel for character input referencing, wheel for character output
        referencing, code, shift key, additional lock, combination [from order_setting]"""
        index_of_item = alpha_from_wheel.index(code)
        new_index = index_of_item
        
        print(new_index)
        
        if lock & comb != 0:
            new_index 
            new_index 
            
        new_index -= shift_key
        
        return alpha_to_wheel[new_index]
     
################################################################################################
# code for decryption
    def decryption(self, code, lock):
        """decryption(code, additional lock)"""
        self.order_setting()
        code_parting = []
        for i in range(len(code)):
            if code[i] != "\n" or code[i] != "\t":
                code_parting.append(code[i].upper())
                
            else:
                code_parting.append(code[i])
            
        decrypted = ""
        
        for i in range(len(code_parting)):
            single_pswrd = lock[i]
            dcr_alpha = code_parting[i]
            for j in range(self.order_lenght):
                result = self.rechange(self.order[0][j],
                                       self.order[1][j],
                                       dcr_alpha,
                                       self.order[3][j],
                                       single_pswrd,
                                       self.order[2][0])
                
                self.order_setting() # update order setting
            
            decrypted += result
            
            # incrementer
            self.encr_key1 += 1
            if self.encr_key1 > wheel_setup.alpha_len:
                self.encr_key2 += 1
                if self.encr_key2 > wheel_setup.alpha_len:
                    self.encr_key3 += 1
                    if self.encr_key3 > wheel_setup.alpha_len:
                        self.encr_key3 = 0
                        
                    self.encr_key2 = 0
                    
                self.encr_key1 = 0
                
            self.order_setting()
        
        return [decrypted]




    
    
