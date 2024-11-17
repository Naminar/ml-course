import numpy as np

def get_dominant_eigenvalue_and_eigenvector(data, num_steps):
    """
    data: np.ndarray – symmetric diagonalizable real-valued matrix
    num_steps: int – number of power method steps
    
    Returns:
    eigenvalue: float – dominant eigenvalue estimation after `num_steps` steps
    eigenvector: np.ndarray – corresponding eigenvector estimation
    """
    ### YOUR CODE HERE
    r_new = np.random.normal(size=(data.shape[0]))
    r_prev = np.random.normal(size=(data.shape[0]))

    for step in range(num_steps):
        r_new = data @ r_prev
        r_new /= np.sqrt(r_new.T @ r_new)
        r_prev = r_new

    return r_new.T @ data @ r_new / (r_new.T @ r_new), r_new