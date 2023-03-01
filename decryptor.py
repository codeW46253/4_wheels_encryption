import wheel_setup

################################################################################################



################################################################################################

class Decryptor:
    
# initial value & placeholder
    def __init__(self):
        self.encr_w1 = []
        self.encr_w2 = []
        self.encr_w3 = []
        self.encr_w4 = []
        self.alpha_list = wheel_setup.alpha_list
        
        self.encr_key1 = 0
        self.encr_key2 = 0
        self.encr_key3 = 0
        
    def order_setting(self):
        self.order = [[self.alpha_list, self.encr_w1, self.encr_w3, self.encr_w3, self.encr_w1], # from wheel
                      [self.encr_w1, self.encr_w2, self.encr_w4, self.encr_w2, self.alpha_list], # to_wheel
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
        self.encr_key1 = key1 % 69
        self.encr_key2 = key2 % 69
        self.encr_key3 = key3 % 69
   
################################################################################################

# system for character/alphabet swap
    
    def rechange(self, alpha_from_wheel, alpha_to_wheel, code, shift_key, lock, comb):
        index_of_item = alpha_from_wheel.index(code)
        new_index = index_of_item
        
        print(new_index)
        
        if lock & comb != 0:
            new_index 
            new_index 
            
        new_index -= shift_key
        
        return alpha_to_wheel[new_index]
     
################################################################################################
        
# system for decryption
    def decryption(self, code, lock):
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
                dcr_alpha = result
                
                self.order_setting() # update order setting
            
            print("\n")
            decrypted += dcr_alpha
            
            # incrementer
            self.encr_key1 += 1
            if self.encr_key1 > 69:
                self.encr_key2 += 1
                if self.encr_key2 > 69:
                    self.encr_key3 += 1
                    if self.encr_key3 > 69:
                        self.encr_key3 = 0
                        
                    self.encr_key2 = 0
                    
                self.encr_key1 = 0
                
            self.order_setting()
        
        return [decrypted]
        
################################################################################################

if __name__=="__main__":
    system_selected = Decryptor()
    system_selected.wheel_setting(0,1,2,3)
    system_selected.key_setting(0, 0, 0)
    system_selected.order_setting()
    
    decrypted = system_selected.decryption("99RIB>\'\"2W",
                                           [0, 0, 0, 0, 16, 1, 0, 0, 0, 0])
    
    print(decrypted)


