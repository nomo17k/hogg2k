#!/usr/bin/env python2.6
"""
This test script creates a bunch of figures that match those in Hogg
(2000).  Just for checking the computations are reasonable.
"""
import matplotlib.pyplot as plt
import numpy as np
from hogg2k import Cosmos


def age_of_universe(z, cosmos):
    return cosmos.t(z) / cosmos.t_H(z)


def angular_diameter_distance(z, cosmos):
    return cosmos.D_A(z) / cosmos.D_H()


def comoving_volume_element(z, cosmos):
    return cosmos.dV_C(z) / cosmos.D_H()**3


def distance_modulus(z, cosmos):
    return cosmos.DM(z)


def lookback_time(z, cosmos):
    return cosmos.t_L(z) / cosmos.t_H(z)


def luminosity_distance(z, cosmos):
    return cosmos.D_L(z) / cosmos.D_H()


def probability_of_intersection(z, cosmos):
    return cosmos.dP(z) / cosmos.D_H()


def proper_motion_distance(z, cosmos):
    return cosmos.D_M(z) / cosmos.D_H()


def main():

    cosmos1 = ('k-', 'Esinstein-de Sitter', Cosmos(1.00, 0.00, 1.))
    cosmos2 = ('k:', 'Low-density', Cosmos(0.05, 0.00, 1.))
    cosmos3 = ('k--', 'High-lambda', Cosmos(0.20, 0.80, 1.))

    zs = np.arange(0., 5., .1)

    fs = [('Age of Universe', age_of_universe),
          ('Angular Diameter Distance D_A / D_H', angular_diameter_distance),
          ('Comoving Volume Element', comoving_volume_element),
          ('Distance Modulus', distance_modulus),
          ('Lookback Time', lookback_time),
          ('Luminosity Distance', luminosity_distance),
          ('Probability of Intersection', probability_of_intersection),
          ('Proper Motion Distance', proper_motion_distance)]

    for i, (funcname, func) in enumerate(fs):
        plt.figure(i + 1)

        for fmt, label, cosmos in [cosmos1, cosmos2, cosmos3]:

            ys = [func(z, cosmos) for z in zs]

            plt.plot(zs, ys, fmt, label=label)

        plt.ylabel(funcname)
        plt.xlabel('Redshift z')
        plt.legend(loc='best')

    plt.show()


if __name__ == '__main__':
    main()
