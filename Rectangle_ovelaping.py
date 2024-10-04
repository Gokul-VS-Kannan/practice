# Given two rectangles, find if the given two rectangles overlap or not.A rectangle is denoted by providing the X and Y coordinates of two points: the left top corner and right bottom corner of the rectangle.Two rectangles sharing a side are considered overlapping.(L1 and R1 are the extreme points of the first rectangle and L2 and R2 are the extreme points of the second rectangle).


# conditons for no over laping is:

# The first rectangle is completely to the left of the second rectangle: R1[0] < L2[0].
# The first rectangle is completely to the right of the second rectangle: L1[0] > R2[0].
# The first rectangle is completely above the second rectangle: R1[1] > L2[1].
# The first rectangle is completely below the second rectangle: L1[1] < R2[1].

def rectangle_overlap(L1,R1,L2,R2):
    # check if one rectangle is completly to the right or left of other
    if (R1[0] < L2[0] or R2[0] < L1[0]):
        return 0

    # check if one rectangle is completly above or below of other
    if (R1[1] > L2[1] or R2[1] > L1[1]):
        return 0
    
    return 1


# top-left corner of first rectangle
a1 = (0,10)
# bottom-right corner of first rectangle
b1 = (10,0)
# top-left corner of second rectangle
a2 = (5,5)
# bottom-right corner of second rectangle
b2 = (15,0)


x = rectangle_overlap(a1,b1,a2,b2)
print(x)
if x== 1:
    print("Rectangles intersect")
else:
    print("Rectangles do not intersect")

