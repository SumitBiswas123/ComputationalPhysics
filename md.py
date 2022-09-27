#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 09:20:23 2022

First part of the code is to initialize by reading input parameters.
@author: marioborunda
"""

def read_XV(filename):
    n_atoms = None
    xyz_coordinates = []
    vel_coordinates = []
    
    with open(filename, "r") as file:
        for line_number, line in enumerate(file):
            if line_number == 0:
                n_atoms = int(line)
            else :
                x, y, z, vx, vy, vz = line.split()
                xyz_coordinates.append([float(x), float(y), float(z)])
                vel_coordinates.append([float(vx), float(vy), float(vz)])
   
    return n_atoms, xyz_coordinates, vel_coordinates

# read number of particles and their coordinates.
atoms, xyz_coordinates, vel_coordinates = read_XV("input.txt")
print(atoms)
print(xyz_coordinates[0][0])