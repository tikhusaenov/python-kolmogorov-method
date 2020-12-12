import numpy as np
from scipy.interpolate import interp1d


def _conf_set(F, alpha=0.05):
    nobs = len(F)
    epsilon = np.sqrt(np.log(2.0 / alpha) / (2 * nobs))
    lower = np.clip(F - epsilon, 0, 1)
    upper = np.clip(F + epsilon, 0, 1)
    return lower, upper


class StepFunction:
    def __init__(self, x, y, ival=0.0, sorted=False, side="left"):
        if side.lower() not in ["right", "left"]:
            msg = "side can take the values 'right' or 'left'"
            raise ValueError(msg)
        self.side = side
        _x = np.asarray(x)
        _y = np.asarray(y)
        if _x.shape != _y.shape:
            msg = "x and y do not have the same shape"
            raise ValueError(msg)
        if len(_x.shape) != 1:
            msg = "x and y must be 1-dimensional"
            raise ValueError(msg)
        self.x = np.r_[-np.inf, _x]
        self.y = np.r_[ival, _y]
        if not sorted:
            asort = np.argsort(self.x)
            self.x = np.take(self.x, asort, 0)
            self.y = np.take(self.y, asort, 0)
        self.n = self.x.shape[0]

    def __call__(self, time):
        tind = np.searchsorted(self.x, time, self.side) - 1
        return self.y[tind]


class ECDF(StepFunction):
    def __init__(self, x, side="right"):
        x = np.array(x, copy=True)
        x.sort()
        nobs = len(x)
        y = np.linspace(1.0 / nobs, 1, nobs)
        super(ECDF, self).__init__(x, y, side=side, sorted=True)


def monotone_fn_inverter(fn, x, vectorized=True, **keywords):
    x = np.asarray(x)
    if vectorized:
        y = fn(x, **keywords)
    else:
        y = []
        for _x in x:
            y.append(fn(_x, **keywords))
        y = np.array(y)
    a = np.argsort(y)
    return interp1d(y[a], x[a])


if __name__ == "__main__":
    # TODO: Make sure everything is correctly aligned and make a plotting
    # function
    from urllib.request import urlopen
    import matplotlib.pyplot as plt

    nerve_data = urlopen("http://www.statsci.org/data/general/nerve.txt")
    nerve_data = np.loadtxt(nerve_data)
    x = nerve_data / 50.0  # Was in 1/50 seconds
    cdf = ECDF(x)
    x.sort()
    F = cdf(x)
    plt.step(x, F, where="post")
    lower, upper = _conf_set(F)
    plt.step(x, lower, "r", where="post")
    plt.step(x, upper, "r", where="post")
    plt.xlim(0, 1.5)
    plt.ylim(0, 1.05)
    plt.vlines(x, 0, 0.05)
    plt.show()