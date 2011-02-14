#!/usr/bin/env python
import sys
import numpy as N
from hogg2k import Cosmos


cosmos1 = Cosmos(1.00, 0.00, 1.)  # Einsten-de Sitter
cosmos2 = Cosmos(0.05, 0.00, 1.)  # low-density
cosmos3 = Cosmos(0.20, 0.80, 1.)  # high lambda


def age_of_universe(z, cosmos):
    return cosmos.t(z) / cosmos.t_H(z)


def angular_diameter_distance(z, cosmos):
    return cosmos.D_A(z) / cosmos.D_H(z)


def comoving_volume_element(z, cosmos):
    return cosmos.dV_C(z) / cosmos.D_H(z)**3


def distance_modulus(z, cosmos):
    return cosmos.DM(z)


def lookback_time(z, cosmos):
    return cosmos.t_L(z) / cosmos.t_H(z)


def luminosity_distance(z, cosmos):
    return cosmos.D_L(z) / cosmos.D_H(z)


def probability_of_intersection(z, cosmos):
    return cosmos.dP(z) / cosmos.D_H(z)


def proper_motion_distance(z, cosmos):
    return cosmos.D_M(z) / cosmos.D_H(z)


def generate_output(func, cosmos_list):
    zlist = N.arange(0., 5., .1)
    for z in zlist:
        fmt = '%.3e'
        tup = (z,)
        for each in cosmos_list:
            fmt = ' '.join([fmt, '%.3e'])
            tup += (func(z, each),)
        print (fmt % tup)


def main(func):
    cosmos_list = [cosmos1, cosmos2, cosmos3]
    generate_output(func, cosmos_list)
    return


if __name__ == '__main__':
    function = eval(sys.argv[1])
    main(function)

