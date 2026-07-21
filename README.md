# DNA Nanostar Simulaton Project

Developer: Neha Desigar

PI: Omar Saleh

Important Contributors: Michio Tateno

## Overview:

Consists of a set of Jupyter Notebook files, which each hold code to run a specific simulation relating to the phase separation process of DNA nanostars. 
It contains some files that simulate the phase separation in 1- and 2-D, others that construct binodal diagrams, etc. 
Each file has a clearly defined purpose explained in the file name/first markdown cell.

Nanostar simulations are all based on the Cahn-Hilliard equation using Wertheim free energy as proposed in: 

Marco Cappa, Francesco Sciortino, Lorenzo Rovigatti; A phase-field model for solutions of DNA-made particles. J. Chem. Phys. 21 May 2025; 162 (19): 194901. https://doi.org/10.1063/5.0257265


## File Naming Conventions: 

- 1D/2D-- File is a simulation of a nanostar system in one, two, or three dimensions. 
- AA/AA AB etc-- Describes the nanostar types (identified by sticky end pattern, tetravalent unless specified otherwise) included in the system.  AA = AAAA, BB = BBBB, and AB = AABB or ABBB (crosslinker)
- Sym/Asym-- Indicates that nanostar arms of different sticky end types have different lengths. Implemented by changing the value of B2 (excluded volume) for each pair of nanostars
- CP Test/NP Test-- Identifies code written to test the capabilities of the GRIT HPC system, using both NumPy (on the CPU) and CuPy (on the GPU). For other files, 1D code is written in NumPy and 2D/3D in CuPy
- Sequence-- Indicates that the code accounts for sticky ends of different sequences, where the sequence is specified and strength found using the Santa Lucia NN method
- dG-- Also accounts for sticky end sequences of different strengths, but without specifying the end sequences (chosen values of dH, dS)
