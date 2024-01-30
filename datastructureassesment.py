set1 = {1,2,4,2,5,63,2}
set2 = {32,2,4,2,1,45,3,23,5}
#we gonna use the inbuilt functions 
intersection = set1.intersection(set2)
union = set1.union(set2)
symmetricdifference = set1.symmetric_difference(set2)
difference = set1.difference(set2)
print("the union is {} , intersectin is {}, the difference is {}, and the symmetric difference is {}".format(union,intersection,difference,symmetricdifference))