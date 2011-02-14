#!/bin/bash

./make_data.py angular_diameter_distance > angular_diameter_distance.dat
./make_data.py comoving_volume_element > comoving_volume_element.dat
./make_data.py distance_modulus > distance_modulus.dat
./make_data.py lookback_time > lookback_time.dat
./make_data.py age_of_universe > age_of_universe.dat
./make_data.py luminosity_distance > luminosity_distance.dat
./make_data.py probability_of_intersection > probability_of_intersection.dat
./make_data.py proper_motion_distance > proper_motion_distance.dat

gnuplot fig.*.gp ; fixbb fig.*.eps

