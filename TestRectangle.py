'''
    Brendan Sheehan
    CS5001
    Homework 7

    This program tests the Rectangle class.  Imports from
    Rectangle.py, and tests the Rectangle class by creating objects,
    calling methods on those objects, and making sure the values of
    the attributes are what we expect
'''

from Rectangle import Rectangle
import unittest

class RectangleTest(unittest.TestCase):

    def test_init(self):
        '''
        tests the __init__ method which creates new rectangles
        '''

        # test 1 - initializing rectangle with valid
        # parameters (positive ints)
        rectangle_one = Rectangle(1, 1, 5, 10)
        self.assertEqual(rectangle_one.x, 1)
        self.assertEqual(rectangle_one.y, 1)
        self.assertEqual(rectangle_one.width, 5)
        self.assertEqual(rectangle_one.height, 10)

        # test 2 - initializing rectangle with valid
        # parameters (- x coord)
        rectangle_two = Rectangle(-1, 1, 5, 10)
        self.assertEqual(rectangle_two.x, -1)
        self.assertEqual(rectangle_two.y, 1)
        self.assertEqual(rectangle_two.width, 5)
        self.assertEqual(rectangle_two.height, 10)

        # test 3 - initializing rectangle with valid
        # parameters (-y coord)
        rectangle_three = Rectangle(1, -1, 5, 10)
        self.assertEqual(rectangle_three.x, 1)
        self.assertEqual(rectangle_three.y, -1)
        self.assertEqual(rectangle_three.width, 5)
        self.assertEqual(rectangle_three.height, 10)

        # test 4 - initializing rectangle with valid
        # parameters (-x, -y coord)
        rectangle_four = Rectangle(-1, -1, 5, 10)
        self.assertEqual(rectangle_four.x, -1)
        self.assertEqual(rectangle_four.y, -1)
        self.assertEqual(rectangle_four.width, 5)
        self.assertEqual(rectangle_four.height, 10)

        # test 5 - initializing rectangle with valid
        # parameters (x=0, y=0)
        rectangle_five = Rectangle(0, 0, 5, 10)
        self.assertEqual(rectangle_five.x, 0)
        self.assertEqual(rectangle_five.y, 0)
        self.assertEqual(rectangle_five.width, 5)
        self.assertEqual(rectangle_five.height, 10)

        # test 6 - initializing rectangle with invalid
        # parameters (- width) returns ValueError
        with self.assertRaises(ValueError):
            rectangle_six = Rectangle(1, 1, -5, 10)

        # test 7 - intializing rectangle with invalid
        # parameters (-height) returns ValueError
        with self.assertRaises(ValueError):
            rectangle_svn = Rectangle(1, 1, 5, -10)

        # test 8 - initializing rectangle with invalid
        # parameters (x input = str) returns ValueError
        with self.assertRaises(ValueError):
            rectangle_eight = Rectangle('1', 1, 5, 10)

        # test 9 - initializing rectangle with invalid
        # parameters (y input = str) returns ValueError
        with self.assertRaises(ValueError):
            rectangle_nine = Rectangle(1, '1', 5, 10)

        # test 10 - initializing rectangle with invalid
        # parameters (width input = str) returns ValueError
        with self.assertRaises(ValueError):
            rectangle_ten = Rectangle(1, 1, '5', 10)

        # test 11 - initializing rectangle with invalid
        # parameters (height input = str) returns ValueError
        with self.assertRaises(ValueError):
            rectangle_elvn = Rectangle(1, 1, 5, '10')

        # test 12 - initializing rectangle with invalid
        # parameters (x input = float) returns ValueError
        with self.assertRaises(ValueError):
            rectangle_twlv = Rectangle(1.0, 1, 5, 10)

        # test 13 - initializing rectangle with invalid
        # parameters (y input = float) returns ValueError
        with self.assertRaises(ValueError):
            rectangle_thrtn = Rectangle(1, 1.0, 5, 10)

        # test 14 - initializing rectangle with invalid
        # parameters (width input = float) returns ValueError
        with self.assertRaises(ValueError):
            rectangle_frtn = Rectangle(1, 1, 5.0, 10)

        # test 15 - initializing rectangle with invalid
        # parameters (height input = float) returns ValueError
        with self.assertRaises(ValueError):
            rectangle_ftn = Rectangle(1, 1, 5, 10.0)                      
    
    def test_get_x(self):
        '''
        tests the get_x method which returns the x coordinate
        of the rectangle's bottom left corner as an int
        '''
        # test 1 - returns a positive x coord
        rectangle_one = Rectangle(1, 1, 5, 10)
        self.assertEqual(rectangle_one.x, 1)

        # test 2 - returns a negative x coord
        rectangle_two = Rectangle(-1, 1, 5, 10)
        self.assertEqual(rectangle_two.x, -1)

        # test 3 - returns a 0 x coord
        rectangle_three = Rectangle(0, 1, 5, 10)
        self.assertEqual(rectangle_three.x, 0)

    def test_get_y(self):
        '''
        tests the get_y method which returns the y coordinate
        of the rectangle's bottom left corner as an int
        '''
        # test 1 - returns a positive y coord
        rectangle_one = Rectangle(1, 1, 5, 10)
        self.assertEqual(rectangle_one.y, 1)

        # test 2 - returns a negative y coord
        rectangle_two = Rectangle(1, -1, 5, 10)
        self.assertEqual(rectangle_two.y, -1)

        # test 3 - returns a 0 y coord
        rectangle_three = Rectangle(1, 0, 5, 10)
        self.assertEqual(rectangle_three.y, 0)

    def test_get_width(self):
        '''
        tests the get_width method which returns the
        rectangle's width as an int
        '''
        # test 1 - returns width as a positive int
        rectangle_one = Rectangle(1, 1, 5, 10)
        self.assertEqual(rectangle_one.width, 5)

    def test_get_height(self):
        '''
        tests the get_height method which returns the
        rectangle's height as an int
        '''
        # test 1 - returns height as a positive int
        rectangle_one = Rectangle(1, 1, 5, 10)
        self.assertEqual(rectangle_one.height, 10)

    def test_overlap(self):
        '''
        tests the overlap method which determines whether
        two rectangles have an overlap
        '''
        # test 1 - top left corner overlap returns True
        rectangle_one = Rectangle(0, 0, 5, 5)
        rectangle_two = Rectangle(2, 2, 5, 5)
        self.assertTrue(rectangle_one.overlap(rectangle_two))

        # test 2 - top right corner overlap returns True
        rectangle_one = Rectangle(5, 0, 5, 5)
        rectangle_two = Rectangle(3, 2, 5, 5)
        self.assertTrue(rectangle_one.overlap(rectangle_two))
        
        # test 3 - bottom left corner overlap returns True
        rectangle_one = Rectangle(0, 5, 5, 5)
        rectangle_two = Rectangle(2, 3, 5, 5)
        self.assertTrue(rectangle_one.overlap(rectangle_two))
        
        # test 4 - bottom right corner overlap returns True
        rectangle_one = Rectangle(5, 5, 5, 5)
        rectangle_two = Rectangle(3, 3, 5, 5)
        self.assertTrue(rectangle_one.overlap(rectangle_two))

        # test 5 - rectangle 2 completely inside rectangle 1
        # returns True
        rectangle_1 = Rectangle(0, 0, 10, 10)
        rectangle_2 = Rectangle(2, 2, 5, 5)
        self.assertTrue(rectangle_one.overlap(rectangle_two))

        # test 6 matching rectangles returns True
        rectangle_1 = Rectangle(0, 0, 5, 5)
        rectangle_2 = Rectangle(0, 0, 5, 5)
        self.assertTrue(rectangle_one.overlap(rectangle_two))

        # test 7 - no overlap returns False
        rectangle_one = Rectangle(0, 0, 5, 5)
        rectangle_two = Rectangle(7, 0, 5, 5)
        self.assertFalse(rectangle_one.overlap(rectangle_two))
        
        # test 8 - not a rectangle raises ValueError
        rectangle_two = "not a rectangle"
        with self.assertRaises(ValueError):
            rectangle_one = Rectangle(0, 0, 5, 5)
            rectangle_one.overlap(rectangle_two)

    def test_intersect(self):
        '''
        tests the intersect method which computes and
        returns a Rectangle instance that represents
        the area in common with the current instance
        and the other Rectangle passed to it
        '''
        
        # test 1- rectangles intersect
        rectangle_one = Rectangle(0, 0, 5, 5)
        rectangle_two = Rectangle(3, 3, 5, 5)
        intersect_rectangle = rectangle_one.intersect(rectangle_two)
        self.assertEqual(intersect_rectangle.x, 3)
        self.assertEqual(intersect_rectangle.y, 3)
        self.assertEqual(intersect_rectangle.width, 2)
        self.assertEqual(intersect_rectangle.height, 2)
        
        # test 2 - rectangles do not intersect
        rectangle_one = Rectangle(0, 0, 5, 5)
        rectangle_two = Rectangle(6, 6, 5, 5)
        with self.assertRaises(ValueError):
            intersect_rect = rectangle_one.intersect(rectangle_two)
            
        # test 3 - rectangle completely inside another rectangle
        rectangle_one = Rectangle(0, 0, 10, 10)
        rectangle_two = Rectangle(2, 2, 4, 4)
        intersect_rectangle = rectangle_one.intersect(rectangle_two)
        self.assertEqual(intersect_rectangle.x, 2)
        self.assertEqual(intersect_rectangle.y, 2)
        self.assertEqual(intersect_rectangle.width, 4)
        self.assertEqual(intersect_rectangle.height, 4)
    
    def test___str__(self):
        '''
        tests the __str__ method which returns a string
        representation of the current Rectangle instance.
        in the form "(x=a,y=b,width=c,height=d)
        '''
        # test 1 - positive x, y
        rect = Rectangle(1, 1, 5, 10)
        self.assertEqual(str(rect), "(x=1,y=1,width=5,height=10)")

        # test 2 - negative x, positive y
        rect = Rectangle(-1, 1, 5, 10)
        self.assertEqual(str(rect), "(x=-1,y=1,width=5,height=10)")

        # test 3 - postitive x, negative y
        rect = Rectangle(1, -1, 5, 10)
        self.assertEqual(str(rect), "(x=1,y=-1,width=5,height=10)")

        # test 4 - negative x, negative y
        rect = Rectangle(-1, -1, 5, 10)
        self.assertEqual(str(rect), "(x=-1,y=-1,width=5,height=10)")

    def test___eq__(self):
    
        '''
        Tests that the __eq__ method which compares two
        rectangles and returns True both are equivalent,
        otherwise returns False.
        '''
        # test 1- same x, y, width, height returns True
        rectangle_one = Rectangle(1, 1, 5, 10)
        rectangle_two = Rectangle(1, 1, 5, 10)
        self.assertTrue(rectangle_one == rectangle_two)

        # test 2 - different x returns False
        rectangle_three = Rectangle(0, 1, 5, 10)
        self.assertFalse(rectangle_one == rectangle_three)

        # test 3 - different y returns False
        rectangle_four = Rectangle(1, 0, 5, 10)
        self.assertFalse(rectangle_one == rectangle_four)

        # test 4 - different width returns False
        rectangle_five = Rectangle(1, 1, 6, 10)
        self.assertFalse(rectangle_one == rectangle_five)

        # test 5 - different height returns False
        rectangle_six = Rectangle(1, 1, 5, 11)
        self.assertFalse(rectangle_one == rectangle_six)
    
def main():

    unittest.main(verbosity=3)

if __name__ == "__main__":
    main()
