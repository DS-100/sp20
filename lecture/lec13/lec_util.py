import numpy as np

def load_data():
    np.random.seed(42)
    n = 50
    x = np.sort(np.random.rand(n)*2.5 *  np.pi)
    x = x - x.mean()/x.std()
    y = np.sin(2.2 * x + 1.8) + 0.2 * np.random.randn(n)
    return (x,y)

