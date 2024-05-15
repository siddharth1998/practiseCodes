def count_numbers_without_repeating_digits(n, m):
     def has_repeating_digits(number):
  4         num_str = str(number)
  5         return len(set(num_str)) != len(num_str)
  6         
  7     count = 0
  8     for number in range(n, m + 1):
  9         if not has_repeating_digits(number):
 10             count += 1
 11             
 12     return count
    def has_repeating_digits(number):
        num_str = str(number)
        return len(set(num_str)) != len(num_str)
    
    count = 0
    for number in range(n, m + 1):
        if not has_repeating_digits(number):
            count += 1
            
    return count
