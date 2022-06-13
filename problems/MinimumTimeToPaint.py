def paint(A, B, C):
    min_time = 0
    i = 0
    
    while i < len(C):
        avaliable_painters = 0
        j = i
        print (C)
        while avaliable_painters < A and j < len(C):

            if C[j] != 0:
                avaliable_painters += 1
                C[j] -= 1

            j += 1
            
            if avaliable_painters >= (A - 1):
                min_time += B
            elif j < len(C):
                min_time += B
            

    
        if C[i] == 0:
            i += 1


    return min_time


A = 1
B = 10
C = [ 1]

print(paint(A,B,C))
