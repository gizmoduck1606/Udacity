import math
from math import sqrt
import numbers

def zeroes(height, width):
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for _ in range(width)] for __ in range(height)]
        return Matrix(g)

def identity(n):
        """
        Creates a n x n identity matrix.
        """
        I = zeroes(n, n)
        for i in range(n):
            I.g[i][i] = 1.0
        return I

class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #
    # Primary matrix math methods
    #############################
 
    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")
        
        # TODO - your code here
        if self.h==1:
            determinant_value = self[0]
        if self.h == 2:
            determinant_value = self[0][0]*self[1][1]- self[1][0]*self[0][1]
        return determinant_value
        
    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")

        # TODO - your code here
        trace_value = 0
        if isinstance(self, numbers.Number):
            pass
            trace_value = self[0][0]
        if self.h>=2:
            for i in range(self.h):
                for j in range(self.w):
                    if i==j:
                        trace_value = trace_value + self[i][j]
                    
        return trace_value
    
    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")

        # TODO - your code here
        
        if self.h == 1:
            inverse_value = 1/self[0][0]
        
        if self.w==2:
            inverse_value = (1/self.determinant())*(self.trace()*identity(2)-self)
        
        return inverse_value
        
    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        # TODO - your code here
        
        transpose =[]
        row = []
        
        for j in range(self.w):
            for i in range(self.h):
                row.append(self[i][j])
            transpose.append(row)
            row =[]
        
        return Matrix(transpose)

    def is_square(self):
        return self.h == self.w

    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same") 
        #   
        # TODO - your code here
        #
        
        sumber = []
        row= []
        for i in range(self.h):
            for j in range(self.w):
                row.append(self[i][j]+other[i][j])
            sumber.append(row)
            row=[]
#             
        return Matrix(sumber)
        

    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        #   
        # TODO - your code here
        #
        neg_matrix =[]
        row =[]
        for i in range(self.h):
            for j in range(self.w):
                row.append(-1*self[i][j])
            neg_matrix.append(row)
            row =[]
        return Matrix(neg_matrix)

    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        #   
        # TODO - your code here
        #
        sub = []
        row= []
        for i in range(self.h):
            for j in range(self.w):
                row.append(self[i][j]-other[i][j])
            sub.append(row)
            row=[]
            
        return Matrix(sub)
    
    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        #   
        # TODO - your code here
        #
        #a_rows = len(self)
        #b_columns = len(other[0])
        #result = [[0 for col in range(b_columns)] for row in range(a_rows)]
        #for i in range(self.shape[0]): 
        #    for j in range(self.shape[1]): 
        #        for k in range(len(other)): 
        #            result[i][j] += self[i][k] * other[k][j] 
        if isinstance(other,numbers.Number):
            pass
            c= zeroes(self.h, self.w)
            for i in range(0,self.h):
                for j in range(0,self.w):
                    c[i][j] = other* self[i][j]
        
        else:
            c = zeroes(self.h, other.w)
            for i in range(0,self.h):
                for j in range(0,other.w):
                    for k in range(0,self.w):
                        c[i][j] += self[i][k]*other[k][j]
               
        return c
        
  

                       
                       

    def __rmul__(self, other):

        if isinstance(other, numbers.Number):
            pass
            for i in range(0,self.h):
                for j in range(0,self.w):
                    self[i][j] = other * self[i][j]
           
        
        return self

          
     
            