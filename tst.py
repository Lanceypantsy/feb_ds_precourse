from scipy.stats import norm
import numpy as np

data = np.array([ 12.1085187 ,  12.10867427,  11.21137858,  10.01311363,
                  10.79744224,  13.19280269,  12.44086123,  11.88810057,
                  10.70064104,  11.50382741])

def log_likelihood_normal_two_parameters(mu, sigma_sq, data_in):
    """
    Consume the parameters mu (mean) and sigma_sq (variance) of a normal
    distribution, and compute the likelihood of a fixed dataset (data_in).
    """
    normal = norm(mu, np.sqrt(sigma_sq))
    likelihoods = [normal.pdf(datum) for datum in data_in]
    return np.sum(np.log(likelihoods))

from itertools import product

for mu, sigma_sq in product([10, 11, 12], [1.0, 1.1, 1.2]):
    print("Log-Lik of Two Parameter Normal Model With mu={0}, sigma_sq={1}: {2:3.2f}".format(
        mu, sigma_sq, log_likelihood_normal_two_parameters(mu, sigma_sq, data))
    )
