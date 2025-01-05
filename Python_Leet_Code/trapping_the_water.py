class Solution:
    def trap(self, height: list[int]) -> int:
        # bl is bar length
        pos = 0
        start_window_pos = -1
        trapped = 0  # result
        # get the first postion from where the water will start trapping
        while pos < len(height):
            bl = height[pos]
            if bl > 0:
                # start the window
                start_window_pos = pos
                break
            pos = +1

        if start_window_pos == -1 or len(height)==1:
            return trapped
        else:
            # Create a while loop iterating through the whole list and get adhere to listed rules
            while start_window_pos < len(height):
                print(start_window_pos)
                
                pos = start_window_pos
                max_value_window = height[
                    pos
                ]  # this height will be the max value which you can see in a window
                temp_pos = pos

                # go forward if reapting character in starting window (optimization)
                while temp_pos < len(height):
                    if height[start_window_pos] == height[temp_pos] and temp_pos!=start_window_pos:
                        temp_pos += 1
                    else:
                        break

                pos = temp_pos
                height_delta = 0
                while True:
                    if pos >= len(height):
                        # Did not get height >= until very end so we will parse it
                        start_window_pos = temp_pos + 1
                          # just one incremented from before
                        break
                    if height[pos] >= max_value_window and pos!=temp_pos :
                        # stop new window
                        # assign start_window_pos to pos
                        start_window_pos = pos
                        max_value_window = height[pos]
                        trapped += height_delta
                        break
                    else:
                        # As there is a negative difference in heigh account for delta (don't add it into result trapped as you don't know if the ending is there )
                        height_delta += max_value_window -  height[pos]
                        
                    pos += 1
            return trapped


x=Solution()
# print(x.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
# print(x.trap([4,2,0,3,2,5]))
print(x.trap([4,2,3]))