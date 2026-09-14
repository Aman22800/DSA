class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        xl1 = rec1[0]
        xr1 = rec1[2]
        yb1 = rec1[1]
        yu1 = rec1[3]

        xl2 = rec2[0]
        xr2 = rec2[2]
        yb2 = rec2[1]
        yu2 = rec2[3]

        yrange = False
        xrange = False

        # X-axis overlap
        if (xl2 < xr1 and xr2 > xl1):
            xrange = True

        # Y-axis overlap
        if (yb2 < yu1 and yu2 > yb1):
            yrange = True

        return xrange and yrange