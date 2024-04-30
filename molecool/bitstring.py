import numpy as np

class BitString:
    """
    Simple class to implement a config of bits
    """

    def __init__(self, N):
        """ Initialize the class with a given size N.

        Parameters:
        ----------
        N (int): The size of the configuration array.

        Returns:
        ----------
        None 
        """
        self.N = N
        self.config = np.zeros(N, dtype=int) 
    
    def __repr__(self):
        """ Return a string representation of the BitString object.

        Parameters:
        ----------
        self: An instance of a class with an init() method

        Returns:
        ----------
        str: A string representing the BitString object, in the format 'BitString("{self.config}")'
        """
        return f'BitString("{self.config}")' 
    
    def __eq__(self, other):
        """ Check if two instances are equal based on their integer values.

        Parameters:
        ----------
        self: An instance of a class with an init() method
        other: Another instance of a class with an int() method

        Returns:
        ----------
        True if the integer values of self and other are equal, False otherwise
        """
        return self.int() == other.int()
    
    def __len__(self):
        """ This method returns the value of the attribute 'N' which represents the length of the object.
        
        Parameters:
        ----------
        self: An instance of a class with an init() method

        Returns:
        ----------
        int: The length of the object.
        """
        return self.N

    def on(self):
        """ Counts the number of '1' in the binary representation of the config attribute of the object.

        Parameters:
        ----------
        self: An instance of a class with an init() method

        Returns:
        ----------
        int: Number of '1' in the binary representation of the config attribute.
        """
        binary = str(self.config)
        return binary.count('1')  
    
    def off(self):
        """ Counts the number of '0' in the binary representation of the config attribute of the object.

        Parameters:
        ----------
        self: An instance of a class with an init() method

        Returns:
        ----------
        int: Number of '0' in the binary representation of the config attribute.
        """
        binary = str(self.config)
        return binary.count('0') 
    
    def flip_site(self,i):
        """ Flips the value of site i in the configuration and returns the count of zeros in the configuration.

        Parameters:
        ----------
        i (int): Index of the site to flip

        Returns:
        ----------
        int: Number of zeros in the configuration after flipping site i
        """
        self.config[i] = 1 if self.config[i] == 0 else 0
    
    def int(self):
        """ Converts a binary string into an integer.

        Parameters:
        ----------
        self: An instance of a class with an init() method

        Returns:
        ----------
        int: The integer value representing the binary string of the config.
        """

        return int(''.join(map(str, self.config)), 2)

    def set_config(self, s:list[int]):
        """  Sets the configuration of the object to the binary representation of the given 
        an array.

        Parameters:
        ----------
        self: An instance of a class with an init() method
        s (list[int]): A list of integers representing the configuration.

        Returns:
        ----------
        None
        """
        s = np.array(s)
        self.config = np.zeros(self.N, dtype=int)
        self.config[-len(s):] = s
        
    def set_int_config(self, dec:int):
        """ Sets the configuration of the object to the binary representation of the given integer.

        Parameters:
        ----------
        self: An instance of a class with an init() method
        dec (int): The integer value to be converted to binary and set as configuration.

        Returns:
        ----------
        None
        """
        binary = [int(i) for i in bin(dec)[2:]]
        self.config = np.zeros(self.N, dtype=int)
        self.config[-len(binary):] = binary