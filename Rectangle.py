'''
    Brendan Sheehan
    CS5001
    Homework 7
    
    This program creates a Rectangle class with the following parameters:
    x coordinate, y coordinate, width, height.
'''
class Rectangle:
    '''
    Class rectangle
    Attributes: x coordinate, y coordinate, width, height.
    Methods: get_x, get_y, get_width, get_height, overlap,
    intersect, str, eq.
    '''
    def __init__(self, x, y, width, height):
        '''Constructor -- creates new instances of rectangle
        Parameters:
            self -- the current object
            x -- the x coordinate of the bottom left corner
            y -- the y coordinate of the bottom left corner
            width -- the width of the rectangle
            height -- the height of the rectangle
            Preconditions:
                input values must be int, raise ValueError if not
                width and height must be positive, raise ValueError if not
        '''
    # check for valid inputs, return ValueError if values are not int
    # or if width/height are negative ints
        if not isinstance(x, int):
            raise ValueError("Value for x must be an integer")
        if not isinstance(y, int):
            raise ValueError("Value for y must be an integer")
        if not isinstance(width, int):
            raise ValueError("Value for width must be an integer")
        if not isinstance(height, int):
            raise ValueError("Value for height must be an integer")
        if width < 0:
            raise ValueError("Value for width must be a positive integer")
        if height < 0:
            raise ValueError("Value for height must be a positive integer")

    # provide values to Rectangle parameters
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def get_x(self):
        '''
        returns the x coordinate of the rectangle's bottom left corner
        '''
        return self.x

    def get_y(self):
        '''
        returns the y coordinate of the rectangle's bottom left corner
        '''
        return self.y

    def get_width(self):
        '''
        returns the rectangle's width
        '''
        return self.width

    def get_height(self):
        '''
        returns the rectangle's height
        '''
        return self.height

    def overlap(self, other):
        '''
        determines whether two rectangles have an overlap
        Parameters:
            self -- the current rectangle
            other -- another object with x,y,width,height parameters
        Returns: True if two rectangles overlap, False if not.
        Preconditions: return ValueError if other is not a rectangle
        '''
        # raise ValueError if other is not a rectangle
        if not isinstance(other, Rectangle):
            raise ValueError("other must be a Rectangle")
        
        # determine the bottom left and top right coordinates
        # of each rectangle
        x1 = self.x
        y1 = self.y
        x2 = self.x + self.width
        y2 = self.y + self.height
        
        x3 = other.x
        y3 = other.y
        x4 = other.x + other.width
        y4 = other.y + other.height

        # determine if bottom left and top right coordinates
        # of each rectangle fall inside one another
        if x1 > x4 or x3 > x2:
            return False
        if y1 > y4 or y3 > y2:
            return False
        return True
        
    def intersect(self, other):
        '''
        determines the space where two rectangles intersect.
        Parameters:
            self -- the inital rectangle
            other -- another rectangle
        Returns: a Rectangle object that covers the inital rectangles'
        intersection
        Preconditions:
            if the two rectangles do not overlap, raise ValueError
        '''
        # define intersection points
        intersect_x = max(self.x, other.x)
        intersect_y = max(self.y, other.y)
        intersect_width = min(self.x + self.width, other.x + other.width)
        intersect_height = min(self.y + self.height, other.y + other.height)

        # define width and height of intersecting rectangle
        new_width = intersect_width - intersect_x
        new_height = intersect_height - intersect_y

        # raise ValueError if rectangles dont overlap
        if intersect_x > intersect_width or intersect_y > intersect_height:
            raise ValueError("The two rectangles do not overlap")

        # return intersecting Rectangle as object
        return Rectangle(intersect_x, intersect_y,
                         new_width, new_height)

    def __str__(self):
        '''
        Returns Rectangle object as a string
        '''
        output = "(x=" + str(self.x) + ",y=" + str(self.y) +\
                 ",width=" + str(self.width) +\
                 ",height=" + str(self.height) + ")"
        return output

    def __eq__(self, other):
        '''
        Compares two rectangle objects to see if they are equal
        Parameters:
            self -- the rectangle object
            other -- a different rectangle object
        Return True if Rectangles are equal, False if not.
        '''
        # a rectangle is equal to another if the
        # parameters (x, y, width, height) are the same
        if isinstance(other, Rectangle):
            return self.x == other.x and self.y == other.y\
                   and self.width == other.width\
                   and self.height == other.height
        else:
            return False
