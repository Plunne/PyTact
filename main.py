# main.py

import asyncio
import sys

from pytact.frame import *
from pytact.modes import *

def main():

    print("\n***** TACT VEST *****\n")

    # Create a list of points
    pointsList = []

    # Get points in ".tact" file
    for arg in sys.argv[1:]:        # Pour chaque arguments en commencant par le 2eme
        tact_file(arg + ".tact", pointsList)

    # Sort point list by earlier
    pointsList.sort(key=lambda x: x.startTime)
    
    # Prepare frames
    timedFrames = preComputeFrames(pointsList)

    # Send Frames
    asyncio.run(playFrames(timedFrames))

if __name__ == "__main__":
    main()

# End of Main