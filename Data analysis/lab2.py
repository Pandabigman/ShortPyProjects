import numpy as np
import matplotlib.pyplot as plt
def monte_carlo (n, m):
    '''
    n is the number of simulations
    m is the number of points in one simulation
    we return the average value of pi over the n simulations
    we plot the different values of pi obtained by each simulation
    '''
    pi_mean=0
    pi_values=[]
    for i in range(n):
        value=0
        x=np.random.uniform(0,1,m).tolist()
        y=np.random.uniform(0,1,m).tolist()
        for j in range(m):
            z=np.sqrt(x[j]*x[j]+y[j]*y[j])
            if z<=1:
                value+=1
        pi_value=value*4/m
        pi_values.append(pi_value)
        pi_mean += pi_value
    pi_mean = pi_mean/n
    ind=range(1,n+1)
    plt.plot(ind,pi_values)
    plt.show()
    return(pi_mean)
res = monte_carlo(1000, 10000)
print('The simulated value of pi is: ', res)
print('File Not Found')

