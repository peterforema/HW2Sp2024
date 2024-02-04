import math

def Probability (PDF, args, c, GT=True):
    μ, σ = args

    def Simpsons_Rule(func, ll, ul, n):
        '''function will perform numerical integration of simpsons 1/3 rule
                ll = lower limit, ul = upper limit'''
        st =  (ul-ll) / n   #step size, n = number of subintervals used in integration
        x = ll
        result = func(x)  #looking at function starting point
        for i in range(1,n,2): #for odd intervals
            x += st
            result += 4 * func(x) #adding to the final result
            x = ll + 2 * st
        for i in range(2, n - 1, 2):  #for even intervals
            x += st
            result += 2 * func(x)
        return result * st / 3  #creating the 1/3 in Sir Simpsons rule


    def callback_fcn(x):
        return PDF((x, μ, σ))
    if GT:
        result = Simpsons_Rule(callback_fcn, μ - 5 * σ, c, 1000)
    else:
        result = 1 - Simpsons_Rule(callback_fcn, μ - 5 * σ, c, 1000)
    return round (result,2)  #rounds final result to 2 decimal places

def main():
    def PDF(args):
        x, μ, σ = args
        exp = -((x-μ) **2)/ (2 * σ ** 2)
        return (1 / (σ * math.sqrt(2 * math.pi))) * math.exp(exp)

    # Find P(x<105|N(100,12.5))
    prob1 = Probability(PDF, (100, 12.5), 105, GT=False)  #finding probability that x<105 with  μ=100 and σ=12.5
    print(f'P(x<105|N(100,12.5))={prob1:.2f}')

    # Find P(x>μ+2σ|N(100, 3))
    prob2 = Probability(PDF, (100, 3), 100 + 2 * 3, GT=True)  #finding probability that x>μ+2σ with  μ=100 and σ=3
    print(f'P(x>{100 + 2 * 3:.2f}|N(100,3))={prob2:.2f}')


if __name__ == "__main__":     # I still don't fully understand this but I think I'm using it right
    main()
main()

#some math code from ChatGTP
#some arrangments from Prof. Smays examples