#1
def count_positives_sum_negatives(arr):
    if arr == []:
        return []
    posit = 0
    neg = 0
    for i in arr:
            if i > 0:
                posit += 1
            elif i < 0:
                neg += i
                
    
    return [posit, neg]

#2
def dna_to_rna(dna):
    return dna.replace("T","U")


#3
def zero_fuel(distance_to_pump, mpg, fuel_left):
    if mpg * fuel_left >= distance_to_pump:
        return True
    else:
        return False
    
#4
def bmi(weight, height):
    x = weight / (height*height)
    if x <= 18.5:
        return "Underweight"
    elif x <= 25.0:
        return "Normal"
    elif x <= 30.0:
        return "Overweight"
    else:
        return "Obese"
    

#5
def minimum(arr):
    return min(arr)

def maximum(arr):
    return max(arr)