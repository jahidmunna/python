import numpy as np

def gradient_descent(x,y):
    w0 = w1 = 0
    iterations = 10
    m = len(x)
    alpha = 0.01

    for i in range(iterations):
        y_predicted = w1 * x + w0
        print("y_predicted = ",y_predicted)
        cost = (1/(2*m)) * sum((y-y_predicted)**2)
        # md = -(2/m)*sum(x*(y-y_predicted))
        # bd = -(2/m)*sum(y-y_predicted)
        # m_curr = m_curr - learning_rate * md
        # b_curr = b_curr - learning_rate * bd
        w0 = w0 - alpha*(1/m)*sum(y_predicted-y)
        w1 = w1 - alpha*(1/m)*sum(x*(y_predicted-y))
        print ("w0 {}, w1 {}, cost {} iteration {}".format(w0,w1,cost, i))

# x = np.array([1,2,3,4,5])
# y = np.array([5,7,9,11,13])

x = np.array([1,2,4,3,5])
y = np.array([1,3,3,2,5])

gradient_descent(x,y)