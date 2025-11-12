import sys
def si(principle,rate,time):
    return(principle*rate*time)

if __name__== "__main__":
    print("++SI++")
    try:
        print("Length: ",len(sys.argv))
        if len(sys.argv) == 4:
            p=float(sys.argv[1])
            r=float(sys.argv[2])
            t=float(sys.argv[3])
        else:
            p=float(input("Enter the Principle amount: "))
            r=float(input("Enter the Rate of interest (%): "))
            t=float(input("Enter the time (in year): "))
        print("===program parameters==")
        print("Principl amount: ",p)
        print("Rate of Interest: ",r)
        print("Time in year: ",t)
        interest=si(p,r,t)
        print(f"\n SIMPLE INTEREST = {interest:.2f}")
    except ValueError:
        print("Invalid input")
