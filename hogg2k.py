#!/usr/bin/env python
"""
David Hogg's distance measures in cosmology

This module implements the functions from D. Hogg's very useful
cosmography reference (astro-ph/9905116v4).

REQUIREMENTS

SciPy and NumPy

HISTORY

August 3, 2007 (ver 0.2)
  -- Make the whole thing into a class for better organization.

March 23, 2006 (ver 0.1)
  -- Implements most essential functions.  The results are checked
     against the figures in Hogg.
"""
__version__ = '0.2 (August 3, 2007)'
__credits__ = '''The code is written by Taro Sato (nomo17k@gmail.com)'''

import numpy as N
from scipy import integrate

# frequently used constants
H0 = 100.         # Hubble constant in km/s/Mpc
c = 2.99792458e5  # speed of light in km/s


def E(z, om, ol):
    return N.sqrt(om * (1. + z)**3 + (1. - om - ol) * (1. + z)**2 + ol)


class Cosmos(object):
    """
    Cosmology for which distance measures will be computed

    INPUT

      Omega_matter, Omega_lambda, h_100
        -- defaults to (0.3, 0.7, 0.7)
    """

    def __init__(self, omega_matter=0.3, omega_lambda=0.7, h_100=0.7):
        self.cosmos = (omega_matter, omega_lambda, h_100)

    def D_H(self, z):
        """
        Computes the Hubble distance in Mpc

        REFERENCE

          Eq. (4) of astro-ph/9905116

        INPUT

          z -- redshift
        """
        return c / H0 / self.cosmos[2]

    def D_C(self, z):
        """
        Computes line-of-sight comoving distance in Mpc

        REFERENCE

          Eq. (15) of astro-ph/9905116

        INPUT

          z -- redshift
        """
        def integrand(z, om, ol):
            return 1. / N.sqrt(om * (1. + z)**3
                               + (1. - om - ol) * (1. + z)**2 + ol)
        om, ol, h = self.cosmos
        res = integrate.quad(lambda x: integrand(x, om, ol), 0., z)
        return self.D_H(z) * res[0]

    def D_M(self, z):
        """
        Computes transverse comoving distance in Mpc

        REFERENCE

          Eq. (16) of astro-ph/9905116

        INPUT

          z -- redshift
        """
        om, ol, h = self.cosmos
        _D_C = self.D_C(z)
        _D_H = self.D_H(z)
        ok = 1. - om - ol
        if ok > 0.:
            _D_M = (_D_H / N.sqrt(ok)) * N.sinh(N.sqrt(ok) * _D_C / _D_H)
        elif ok == 0.:
            _D_M = _D_C
        else:
            _D_M = (_D_H / N.sqrt(abs(ok))) * N.sin(N.sqrt(abs(ok))
                                                    * _D_C / _D_H)
        return _D_M

    def D_A(self, z):
        """
        Computes angular diameter distance in Mpc

        REFERENCE

          Eq. (18) of astro-ph/9905116

        INPUT

          z -- redshift
        """
        return self.D_M(z) / (1. + z)

    def D_L(self, z):
        """
        Computes luminosity distance in Mpc

        REFERENCE

          Eq. (21) of astro-ph/9905116

        INPUT

          z -- redshift
        """
        return (1. + z) * self.D_M(z)

    def DM(self, z):
        """
        Computes distance modulus

        REFERENCE

          Eq. (25) of astro-ph/9905116

        INPUT

          z -- redshift
        """
        return 5. * N.log10(self.D_L(z) * 1e6 / 10.)

    def dV_C(self, z):
        """
        Computes the comoving volume element

        This function actually computes the comoving volume element per
        unit solid angle dOmega per unit redshift dz, i.e.,

          dV_C / dOmega / dz

        REFERENCE

          Eq. (28) of astro-ph/9905116

        INPUT

          z -- redshift
        """
        om, ol, h = self.cosmos
        ok = 1. - om - ol
        _D_H = self.D_H(z)
        _D_A = self.D_A(z)
        return _D_H * (1. + z)**2 * _D_A**2 / E(z, om, ol)


    def V_C(self, z):
        """
        Computes the total comoving volume out to the specified redshift

        REFERENCE

          Eq. (29) of astro-ph/9905116

        INPUT

          z -- redshift
        """
        om, ol, h = self.cosmos
        ok = 1. - om - ol
        _D_M = self.D_M(z)
        if ok == 0.: _V_C = 4. * N.pi * _D_M**3 / 3.
        else:
            _D_H = self.D_H(z)
            mh = _D_M / _D_H
            if ok > 0.:
                _V_C = ((2. * N.pi * _D_H**3 / ok)
                        * (mh * N.sqrt(1. + ok * mh**2)
                           - N.arcsinh(mh * N.sqrt(abs(ok)))
                           / N.sqrt(abs(ok))))
            else:
                _V_C = ((2. * N.pi * _D_H**3 / ok)
                        * (mh * N.sqrt(1. + ok * mh**2)
                           - N.arcsin(mh * N.sqrt(abs(ok)))
                           / N.sqrt(abs(ok))))
        return _V_C

    def t_H(self, z):
        """
        Computes the Hubble time in Gyr

        REFERENCE

          Eq. (3) of astro-ph/9905116

        INPUT

          z -- redshift
        """
        _t_H = 1. / H0 / self.cosmos[2]
        _t_H *= 1e-3 * 1e6 * 3.0856776e16  # -> s
        _t_H *= (1 / (365.25 * 24 * 3600)) * 1e-9  # s -> Gyr
        return _t_H

    def t_L(self, z):
        """
        Computes lookback time in Gyr

        REFERENCE

          Eq. (30) of astro-ph/9905116

        INPUT

          z -- redshift
        """
        def integrand(z, om, ol):
            return 1. / (1. + z) / N.sqrt(om * (1. + z)**3
                                          + (1. - om - ol) * (1. + z)**2
                                          + ol)
        om, ol, h = self.cosmos
        res = integrate.quad(lambda x: integrand(x, om, ol), 0., z)
        return self.t_H(z) * res[0]

    def t(self, z):
        """
        Computes the age of universe in Gyr at the specified redshift

        REFERENCE

          Eq. (30) of astro-ph/9905116 but the range of integration is
          (z, +infty)

        INPUT

          z -- redshift
        """
        def integrand(z, om, ol):
            return 1. / (1. + z) / N.sqrt(om * (1. + z)**3
                                          + (1. - om - ol) * (1. + z)**2
                                          + ol)
        om, ol, h = self.cosmos
        res = integrate.quad(lambda x: integrand(x, om, ol), z, +N.inf)
        return self.t_H(z) * res[0]

    def dP(self, z):
        """
        Computes the probability of intersection objects

        This function actually computes 

          dP / dz / n(z) / sigma(z)

        where n(z) is the comoving number density and sigma(z) is the
        cross section.

        REFERENCE

          Eq. (31) of astro-ph/9905116

        INPUT

          z -- redshift
        """
        om, ol, h = self.cosmos
        return self.D_H(z) * (1. + z)**2 / E(z, om, ol)


if __name__ == '__main__':
    """test code"""
    z = 0.4

    cosmos = Cosmos()

    cd1 = cosmos.DM(0.025)
    cd2 = cosmos.DM(0.4)

    D1 = cd1
    D2 = cd2

    print D1, D2


