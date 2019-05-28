#python3                                                                      
# Given an integer n, find the last digit of the sum F 0 + F 1 + · · · + F n .
                                                                              
def fib_mod_sum(n):                                                           
    mod_seq = [0, 1]                                                          
    # mod is 10 -> pisano period is 60                                        
    pp = 60                                                                   
                                                                              
    fib_i = n % pp                                                            
                                                                              
    for _ in range(1, fib_i):                                                 
        mod_seq.append((mod_seq[-1] + mod_seq[-2]) % 10)                      
                                                                              
    return sum(mod_seq[:fib_i + 1]) % 10                                      
                                                                              
                                                                              
def main():                                                                   
    n = int(input())                                                          
    print(fib_mod_sum(n))                                                     
                                                                              
                                                                              
if __name__ == "__main__":                                                    
    main()
                                                                    
