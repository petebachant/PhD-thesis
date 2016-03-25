#!/usr/bin/env bash

# Should be run from project root directory
if [[ "$PWD" == *scripts ]]
then
    cd ..
fi

mkdir -p videos

cp "$HOME/Google Drive/Research/CFT-vectors/videos/cft-animation.mp4" videos/cft-animation.mp4

cp "$HOME/Google Drive/Research/OpenFOAM/turbinesFoam/video/unh-rvat-les-Smagorinsky-7_thresh-30fps-longer-domain.ogv" videos/unh-rvat-alm-les.ogv

cp "$HOME/Google Drive/Research/OpenFOAM/turbinesFoam/video/unh-rvat-near-surface-1.75mps.ogv" videos/unh-rvat-alm-free-surface.ogv

cp "$HOME/Google Drive/Research/OpenFOAM/turbinesFoam/video/NTNU-HAWT-LES-refined-more-Smagorinsky.ogv" videos/aft-alm-les.ogv
