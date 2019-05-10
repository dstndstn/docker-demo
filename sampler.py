import numpy as np
import emcee

def lnprob(x, ivar):
    return -0.5 * np.sum(ivar * x ** 2)


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--mpi', action='store_true', default=False)
    parser.add_argument('--walkers', type=int, default=100)
    parser.add_argument('--steps', type=int, default=1000)
    opt = parser.parse_args()

    pool = None
    if opt.mpi:
        import socket
        import os
        from emcee.utils import MPIPool
        pool = MPIPool()
        print('Running in MPI.  Host', socket.gethostname(), 'pid', os.getpid(),
              'is master?', pool.is_master())
        if not pool.is_master():
            pool.wait()
            return

    ndim, nwalkers = 2, opt.walkers

    ivar = 1. / np.random.rand(ndim)
    p0 = [np.random.rand(ndim) for i in range(nwalkers)]
    sampler = emcee.EnsembleSampler(nwalkers, ndim, lnprob, args=[ivar],
                                    pool=pool)

    import time
    print('Running for', opt.steps, 'steps with', opt.walkers, 'walkers')
    t0 = time.time()
    sampler.run_mcmc(p0, opt.steps)
    print('Finished in', time.time()-t0, 'seconds')

    if pool:
        pool.close()
    
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    plt.figure()
    for i in range(ndim):
        plt.subplot(1,ndim,1+i)
        plt.hist(sampler.flatchain[:,i], 100, color="k", histtype="step")
        plt.title("Dimension {0:d}".format(i))
    plt.savefig('plot.png')
    print('Saved plot')


if __name__ == '__main__':
    main()

