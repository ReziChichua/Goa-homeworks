# 1) ყვლეა ტიპი გამოიყენება ელემენტების შესანახად, ყველა მათგანი არის iterable და ყველაში შეგვიძლია შევინახოთ ყველა ტიპის მონაცემები
#მაგალითად: int, str, boolean, float
#list da set არის mutable ხოლო tuple არის immutable
#list da tuple ში შეგვიძლია გამოვიყენოთ slicing da indexing, set ში არ შეგვიძლია რადგან ინდექსები არ აქვს

#2
def goals(laLiga, copaDelRey, championsLeague):
    return laLiga + copaDelRey + championsLeague


#3
def double_char(s):
    return "".join([x * 2 for x in s])


#4
def get_age(age):
    return int(age[0])