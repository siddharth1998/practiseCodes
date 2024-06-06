
def maxArea(heights: list[int]) -> int:
    length=len(heights)
    max_record=0
    for l,lheight in enumerate(heights):
        r=l+1
        while(r<length):
            total_area=abs(l-r)*min(lheight,heights[r])
            if total_area > max_record:
                max_record=total_area
            r+=1
    return max_record

print(maxArea([2,2,2]))