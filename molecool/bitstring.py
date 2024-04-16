import numpy as np

class BitString:
    """
    Simple class to implement a config of bits
    """
    def __init__(self, N):
        self.N = N
        self.config = np.zeros(N, dtype=int) 

    def __repr__(self):
        return f'BitString("{self.config}")' 

    def __eq__(self, other):
        return self.int() == other.int()
    
    def __len__(self):
        return self.N

    def on(self):
        binary = str(self.config)
        return binary.count('1')  
    
    def off(self):
        binary = str(self.config)
        return binary.count('0') 
    
    def flip_site(self,i):
        self.config[i] = 1 if self.config[i] == 0 else 0
    
    def int(self):
        return int(''.join(map(str, self.config)), 2)

    def set_config(self, s:list[int]):
        s = np.array(s)
        self.config = np.zeros(self.N, dtype=int)
        self.config[-len(s):] = s
        
    def set_int_config(self, dec:int):
        binary = [int(i) for i in bin(dec)[2:]]
        self.config = np.zeros(self.N, dtype=int)
        self.config[-len(binary):] = binary