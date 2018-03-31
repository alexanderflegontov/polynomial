

def is_iterable(object):
    try:
        it = list(object)
    except TypeError:
        return False
    return True

def is_number_noexcept(object):
# This method is specially for optimizing the multiplication operator
# so this should not throw exceptions
    try:
        float(object)
        object+0
    except:
        return False
    return True
    
def is_number(object): # or is_scalar as you wish
    #it can raise exceptions
    try:
        float(object)
        0 + object
        return True
    except ValueError: # example: 'a' or 'some string'
        raise
        return False
    except TypeError: # example: '1', tuple, list, any type that does not translate to number
        raise
        return False

def isList_of_multiple_scalars(listArgs):
    for item in listArgs:
        if is_number(item) == False: # here can raise exceptions
            return False
    return True
            
"""
example: coeffs = [3,-2,1] -> 3x2-2x+1
"""
class Polynomial(object):
    #coeffs = []

    def IsEmpty(self):
        return len(self.coeffs) == 0
    
    def non_copy_constructor(self):
        self.coeffs = []
        
    def copy_constructor(self, otherPoly):
        self.coeffs = otherPoly.coeffs[:]
    
    # example: args = [0,3,0,-2,1,0,0] -> [3,0,-2,1,0,0] -> 3x5-2x3+1x2
    def __init__(self, *args): 
        super(Polynomial,self).__init__()
        self.non_copy_constructor()
        #print("[IN] {0}".format(args))
        if len(args)==1:
            obj = args[0]
            if isinstance(obj, Polynomial):
                # copy constructor
                self.copy_constructor(obj)
                self.trim()
            elif is_iterable(obj):
                # from list or tuple
                if isList_of_multiple_scalars(obj):
                    self.coeffs = [item for item in obj]
                    self.trim()
            elif is_number(obj):  # if it is not number then it raises exception
                # from single scalar
                self.coeffs = [obj]
                self.trim()
            else:
                raise TypeError("what are you trying to put here? Please put for example: [1,2,3]")
                pass
        elif len(args)==0:
            #print("__init__(): len(args)==0")
            pass
        elif is_iterable(args):
            # multiple scalars
            #print("__init__(): Here is len(args) > 1")
            if isList_of_multiple_scalars(args): # if one elem is not number then exception raises here
                self.coeffs = [item for item in args]
                self.trim()
        else:
            raise TypeError("what are you trying to put here? Please put for example: [1,2,3]")
            pass

        #print("[OUT] {0}({1})".format(self.__class__.__name__, self.coeffs))

 
    def __call__(self, val):
        res = 0
        pwr = 1
        self_coeffs = list(reversed(self.coeffs))
        for co in self_coeffs:
            res += co*pwr
            pwr *= val
        return res


    def __add__(self, val):
        res = []
        tmpPoly = val
        if isinstance(val, Polynomial) == False:
            tmpPoly = self.__class__(val)
        
        if tmpPoly.IsEmpty():
            res = self.coeffs
        else:
            self_N = len(self.coeffs)
            val_N = len(tmpPoly.coeffs)
            max_len = self_N if self_N > val_N else val_N
            res = [0]*max_len
            
            self_coeffs = self.coeffs
            for i in range(0, self_N, 1):
                res[-i-1] +=  self_coeffs[-i-1]

            val_coeffs = tmpPoly.coeffs
            for i in range(0, val_N, 1):
                res[-i-1] +=  val_coeffs[-i-1]
            
        return self.__class__(res)
        
    def __radd__(self, val):
        return self.__add__(val)
    
    def __sub__(self, val):
        return (self.__neg__()+val).__neg__()
        
    def __rsub__(self, val):
        return (-self) + val

    def __mul__(self, val):
        res = []
        if(self.IsEmpty() == False):
            if is_number_noexcept(val):
                #print("__mul__(): is_number_noexcept? True")
                res = [co*val for co in self.coeffs]
            else:
                #print("__mul__(): is_number_noexcept? False")
                tmpPoly = val
                if isinstance(val, Polynomial) == False:
                    tmpPoly = self.__class__(val)
                
                if(tmpPoly.IsEmpty() == False):
                    self_coeffs = self.coeffs
                    val_coeffs = tmpPoly.coeffs
                    self_N = len(self.coeffs)
                    val_N = len(tmpPoly.coeffs)
                    res = [0]*(self_N+val_N-1)
                     
                    for i in range(0,self_N, 1):
                        for j in range(0,val_N, 1):
                            res[-i-j-1] += self_coeffs[-i-1]*val_coeffs[-j-1]
                    
        return self.__class__(res)
        
    def __rmul__(self, val):
        return self*val

    def __eq__(self, val):
        tmpPoly = val
        if isinstance(val, Polynomial) == False:
            tmpPoly = self.__class__(val)       # we try to cast to Polynomial type
        return self.coeffs == tmpPoly.coeffs

    def __ne__(self, val):
        return (self.__eq__(val) != True)
        
    def __neg__(self):
        if self.IsEmpty():
            return self.__class__()
        return self.__class__([-co for co in self.coeffs])

    def __repr__(self):
        return "{0}({1})".format(self.__class__.__name__, self.coeffs)

    def __str__(self):
        # Return string formatted as ax3 + bx2 + cx + d
        self_coeffs = self.coeffs
        n = len(self_coeffs)
        outSTR = ''
        for i in range(0,n,1):
            sig = ''
            cur_coeff = self_coeffs[-i-1]
            if cur_coeff != 0:
                if cur_coeff > 0:
                    sig = '+'
                else:
                    sig = '-'
            else:
                continue
    
            X = 'x' if i >= 1 else ''
            pow = str(i) if i >= 2 else ''
            co = str(abs(cur_coeff))
            # if you need to degree_sign please uncomment out the following two line:
            #degree_sign = '^' if i >= 2 else ''
            #pow = degree_sign+pow
            monom = sig+co+X+pow if (i!=(n-1)) or (cur_coeff < 0) else co+X+pow 
            outSTR = monom + outSTR
        if outSTR == '':
            return '0'
        return outSTR  

    def trim(self):
        #compress a Polynomial and remove trailing 0-coeffs
        coeffs = self.coeffs
        if coeffs and len(coeffs)>0:
            offset = 0
            if coeffs[offset]==0:
                n = len(coeffs)
                while offset < n and coeffs[offset]==0:
                    offset += 1	
                #print(coeffs[:offset])
                del coeffs[:offset]
 		
    def __del__(self):
        #print("Delete {0}({1})".format(self.__class__.__name__, self.coeffs))
        del self.coeffs[:]
        
if __name__ == '__main__':

    p1 = Polynomial([7,2,3,0])
    print("p1 = {0}".format(p1))
    
    p2 =  [2,4,5] - p1
    print("p2 = {0}".format(p2))
    
    p3 =  p1 - [2,4,5] 
    print("p3 = {0}".format(p3))
    
    p4 = Polynomial(0,2,3,3)
    print("p4 = {0}".format(p4))
    
    p5 = Polynomial(1)
    print("p5 = {0}".format(p5))


    try:
        p6 = Polynomial([1,2,'2',4])
    except:
        print("p6 exception!!!!")

    try:
        p7 = Polynomial([1,2,'xdss',4])
    except:
        print("p7 exception!!!!")

    try:
        p8 = Polynomial([1,2,[2],4])
    except:
        print("p8 exception!!!!")

    try:
        p9 = Polynomial([2,3,[5,[86],[''],7],4,5])
    except:
        print("p9 exception!!!!")
    
    try:
        d = {'dict': 1, 'dictionary': 2}
        p10 = Polynomial(d, d)
    except:
        print("p10 exception!!!!")
        
        
        
