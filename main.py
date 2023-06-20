# main.py

import asyncio

from pytact.frame import *
from pytact.modes import *

if __name__ == "__main__":

    print("\n***** TACT VEST *****\n")

    # Create a list of points
    pointsList = []

    # Get points in ".tact" file
    # tact_file("tactdroite.tact", pointsList)
    tact_file("tactcircle.tact", pointsList)

    # Sort point list by earlier
    pointsList.sort(key=lambda x: x.startTime)
    
    # Send Frames
    timedFrames = preComputeFrames(pointsList)
    asyncio.run(playFrames(timedFrames))

# End of Main