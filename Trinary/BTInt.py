"""Trinary system"""

class btrit:
    """Creates new balanced trit object
    States: 1, 0, t(-1)"""
    def __init__(self,state=0):
        """Initialises trit object"""
        self.state=str(state) #initialisation when creating new trit

        for i in self.state: #exception if user does not input valid trit state
            if i not in ['1','0','t']:
                self.state=None
    #-------------------------------------------------------------------------
    def __setattr__(self,key,value):
        """Checks if changed trit state is valid"""
        self.__dict__[key]=value #so that no recursive
        #do NOT do self.key=value --> infinite recursion
        if key is "state": #checking for invalid state change
            temp=str(value)
            for i in temp:
                if i not in ['1','0','t']: #if any single state is not valid
                    #exception
                    raise TypeError("Not a valid trit state")
    #-------------------------------------------------------------------------
    def __lshift__(self,shift):
        """Bitwise left shift"""
        for i in range(shift): #shift
            self.state=self.state+'0'
            return self.state
    #-------------------------------------------------------------------------
    def __rshift__(self,shift):
        """Bitwise right shift"""
        if shift < 0:
            raise TypeError("Shift cannot be negative")
        if shift is 0:
            return self.state
        else:
            for i in range(shift): 
                if len(self.state) is not 1:
                    temp=''
                    for i in range(len(self.state)-1):
                        temp=temp+self.state[i]
                    self.state=temp #shift
                else: #case when only 1 digit remains
                    self.state='0'
                    return self.state
                    break
            return self.state
    #-------------------------------------------------------------------------
    def ztrim(self):
        """Trims leading 0s"""
        if type(self) is not btrit:
            raise TypeError("Input must be of type btrit")
        else:
            for t in self.state:
                if len(self.state) is 1:
                    break
                else:
                    if t is '0':
                        temp=''
                        for tmp in range(len(self.state)-1):
                            temp=temp+self.state[tmp+1]
                        self.state=temp
                    else:
                        break
        
                        
                
    #-------------------------------------------------------------------------
    def __eq__(self,other):
        """Equality operator"""
        #works because python ignores leading '0's in str in tests
        #might break if that changes though
        return self.state is other.state
    def __ne__(self,other):
        """Inequality operator"""
        #see comments in __eq__
        return self.state is not other.state
    def __lt__(self,other):
        """Less than operator"""
        selftemp=btrit(self.state)
        selftemp.ztrim()
        othertemp=btrit(other.state)
        othertemp.ztrim()
        if len(selftemp.state)<len(othertemp.state):
            return True
        elif len(othertemp.state)<len(selftemp.state):
            return False
        else:
            for t in range(len(selftemp.state)):
                order={'t':0,'0':1,'1':2}
                if order[othertemp.state[t]]>order[selftemp.state[t]]:
                    return True
            return False
    def __le__(self,other):
        """Less than or equal to operator"""
        return ((self.state is other.state) | (self.state<other.state))
    def __gt__(self,other):
        """Greater than operator"""
        return not (self.state<=other.state)
    def __ge__(self,other):
        """Greater than or equal to operator"""
        return not (self.state<other.state)
            
