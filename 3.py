#function that calculates the amount of payment
def payment_amount(d):
    k=len(d)
    sum=0.0
    for i in range(n):
       l2=list(d[i])
       pr=float(l2[0])
       ta=float(l2[1])
       this=pr+pr*ta/100
       sum=sum+this
    p_a=float("{0:.2f}".format(sum))
    print("Payment amount: ",p_a)
       
       
    
n = int(input("Εnter number of purchases :"))
d = {}
for i in range(n):
    keys = input("Give the name of product:") 
    values = input("Give product price and tax rate (for example 4.20,25):").split(",")
    d[keys] = values
l1=list(d.values())
payment_amount(l1)

