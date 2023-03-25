def nearly_equal(a,b):
    len1 = len(a)
    len2 = len(b)
    different = 0
    x = y = 0
    while(x<len1 and y < len2):
        if a[x] != b[y]:
            different += 1
            if len1 > len2:
                x += 1

            elif len1 < len2:
                x -= 1

        if different > 1:
            return False
        x += 1
        y += 1
    
    if different < 2:
        return True
    
in1 = input("Enter First:")
in2 = input("Enter Second:")
val = nearly_equal(in1,in2)
print(val)