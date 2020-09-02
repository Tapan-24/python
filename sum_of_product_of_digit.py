x=abs(int(input("Insert Integer values only : ")))
su_m =0
mu_l =1
while x!=0:
    digit = x%10
    su_m += digit
    mu_l *= digit
    x = x//10
print("Sum of Digit is ",su_m)
print("Product of Digit is ",mu_l)