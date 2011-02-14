reset
set terminal postscript eps enhanced defaultplex butt
set terminal postscript monochrome blacktext
set terminal postscript dashlength 3 linewidth 1
set terminal postscript 'SFRM1000' 24
set fontpath "/usr/share/texmf/fonts/type1/public/cm-super/" "/usr/share/texmf-tetex/fonts/type1/bluesky/cm/"
set terminal postscript fontfile 'sfrm1000.pfb'
#set terminal postscript fontfile 'sfti1000.pfb'
set terminal postscript fontfile 'cmr10.pfb'
#set terminal postscript fontfile 'cmmi10.pfb'
#set terminal postscript fontfile 'cmsy10.pfb'

set encoding iso_8859_1

set output 'fig.comoving_volume_element.eps'

_margin = 1
set tmargin _margin
set bmargin _margin
set lmargin _margin
set rmargin _margin

set size square 1, 1
set origin 0, 0

set xrange [0:5]
set yrange [0.0:1.1]

set xtics 1
set mxtics 5
set ytics 0.2
set mytics 4

set tics scale 2

set xlabel 'redshift z'
set ylabel 'comoving volume element dV_C/dz/d{/CMR10 \255}' offset 1,0

unset key

set style data lines
set style line 1 lt 1 lw 1
set style line 2 lt 0 lw 1
set style line 3 lt 2 lw 1

f1='comoving_volume_element.dat'

plot f1 u 1:2 ls 1,\
     f1 u 1:3 ls 2,\
     f1 u 1:4 ls 3
