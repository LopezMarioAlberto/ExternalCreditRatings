import  ExternalCreditRatings

p1 = ExternalCreditRatings.probability_default(4, 'AAA')
p2 = ExternalCreditRatings.probability_default(3, 'B', 'during')
p3 = ExternalCreditRatings.probability_default(5, 'B', 'during')
p4 = ExternalCreditRatings.probability_default(3, 'BBB', 'during', 'no')
p5 = ExternalCreditRatings.probability_default(4, 'AAA', 'during', 'no')

print(p1)
print(p2)
print(p3)
print(p4)
print(p5)