# README

# Team MORAGS
* Adithya
* Rohith
* Mayank
* Gayathri
* Sooraj
* Juse (aka Anil)

# Concept of the Project  
We know that Scheduling is a NP-hard problem. Our aim is to convert the scheduling problem into a SAT problem to use the Z3 SMT solver. We have to find out a way to set up a query language which a client can use to define their problem which should be converted to a SAT problem.

# INSTALLING Z3

If you want to build on lab account contact me, else follow this if you have sudo rights

step 1: `mkdir -p ~\mayank_is_great; cd ~\mayank_is_great`
step 2: `git clone https://github.com/Z3Prover/z3.git`
step 3: `cd z3`
step 4: ``` python scripts/mk_make.py
            cd build
            make
            sudo make install```
