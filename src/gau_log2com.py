#!/usr/bin/env python

from omg.gaussian.gaussian import GaussianLog

if __name__ == "__main__":
    import sys
    log_file = sys.argv[1]
    parser = GaussianLog(log_file)
    atoms = parser.parse()
    for atom in atoms:
        print(atom.symbol, atom.x, atom.y, atom.z)