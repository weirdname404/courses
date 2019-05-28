#python3                                                                      
#where m ≤ n, find the last digit of the sum F m + F m+1 + Fn

def fib_mod_sum(m, n):                                                           
    mod_seq = [0, 1]                                                          
    # mod is 10 -> pisano period is 60                                        
    pp = 60                                                                   
                                                                              
    fib_m = m % pp
    fib_n = n % pp
                                                                              
    for _ in range(1, fib_n):                                                 
        mod_seq.append((mod_seq[-1] + mod_seq[-2]) % 10)                      
                                                                              
    return sum(mod_seq[fib_m:fib_n + 1]) % 10                                      
                                                                              
                                                                              
def main():                                                                   
    m, n = map(int, input().split())                                                          
    print(fib_mod_sum(m, n))                                                     
                                                                              
                                                                              
if __name__ == "__main__":                                                    
    main()                                                                    

