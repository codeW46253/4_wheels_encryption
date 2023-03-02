
import wheel_setup

################################################################################################
# Encryption
#
# See step and order for setting wheel on "Setting.txt" file
#
# Decrypt any text with this step:
#   1) call "Encryptor" class
#   2) set the wheels selection according to this list:
#       0 - wheel_setup.wheel_1
#       1 - wheel_setup.wheel_2
#       2 - wheel_setup.wheel_3
#       3 - wheel_setup.wheel_4
#   
#   3) enter 3 level shift key [main lock for encryption] only arround 0<= x <= lenght
#      of main character's arrangement
#   4) call "encryption" function from "Encryptor" class and push your code and shift keys
#
# You will get an encrypted text and additional key at the end as a singgle list
#
################################################################################################


################################################################################################
class Encryptor:
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
        self.order = [[self.alpha_list, self.encr_w2, self.encr_w4, self.encr_w2, self.encr_w1], # from wheel
                      [self.encr_w1, self.encr_w3, self.encr_w3, self.encr_w1, self.alpha_list], # to_wheel
                      [0b00001, 0b00010, 0b00100, 0b01000, 0b10000], # lock
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
    def change(self, from_wheel, to_wheel, code, shift_key):
		"""rechange(wheel for character input referencing, wheel for character output
        referencing, code, shift key, additional lock, combination [from order_setting]"""
        index_of_item = from_wheel.index(code)
        new_index = index_of_item + shift_key
        pass_key = False
        if new_index >= wheel_setup.alpha_len:
            new_index = new_index % wheel_setup.alpha_len
            pass_key = True
			
        return [to_wheel[new_index], pass_key]
    
################################################################################################
# code for encryption
    def encryption(self, code):
        """decryption(code, additional lock)"""
        self.order_setting()
        code_parting = []
        for i in range(len(code)):
            if code[i] != "\n" or code[i] != "\t":
                code_parting.append(code[i].upper())
                
            else:
                code_parting.append(code[i])
            
        encrypted = ""
        a_key = []
		
        for i in range(len(code_parting)):
            create_a_key = 0
            encr_alpha = code_parting[i]
            for j in range(self.order_lenght):
                result = self.change(self.order[0][j],
									 self.order[1][j],
									 encr_alpha,
									 self.order[3][j])
				
                if result[1]:
                    create_a_key += self.order[2][j]
                
                self.order_setting() # update order setting
            
            encrypted += result[0]
            a_key.append(create_a_key)
            
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
        
        return [encrypted, a_key]
    
		  
		  
		  
		  
		  
