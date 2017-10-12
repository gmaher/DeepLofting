#!/bin/bash

#Note must be executed from withing directory
#Args:
#1: output directory


echo "Input arguments: $1"

SV="/home/marsdenlab/projects/JSV/sv_build/mysim"
TCL="/home/marsdenlab/projects/DeepLofting/gen_models/run_models.tcl"
OUT="/home/marsdenlab/projects/DeepLofting/python/vtp"
GRPSDIR="/home/marsdenlab/projects/DeepLofting/python/pred_groups"

cd $OUT
rm $OUT/*

for g in ${GRPSDIR}/*; do
  echo "$g"
  $SV $TCL $g -tcl
  sleep 100
done
