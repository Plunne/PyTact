# pytact/frame.py

import time

from bleak import BleakClient

ble_vest_mac = "FA:28:91:E3:0F:3D"
ble_vest_char = "6E400002-B5A3-F393-E0A9-E50E24DCCA9E"

# preComputeFrames()
# Pre compute the list of frames to send to the BLE with their respective timing
# @points : List of points
def preComputeFrames(points):

    # Establish the first list of all unique eventtime and sort them
    timing_set = set([0])

    # For each point in points
    for pt in points:
        
        timing_set.add(pt.get_startTime())
        timing_set.add(pt.get_endTime())
    
    timing_list = list(timing_set)
    timing_list.sort()

    # Now at each eventtime, calculate the frame by checking all points
    timed_frame = []
    for ts in timing_list:
        frame = list("0000000000000000000000000000000000000000")
        for pt in points:
            if pt.get_startTime() <= ts and pt.get_endTime() > ts:
                frame[pt.get_index() - 1] = frame[pt.get_index() - 1] if frame[pt.get_index() - 1] > pt.get_intensity() else pt.get_intensity()
        frame = "".join(frame)
        timed_frame.append((ts,frame))
    return timed_frame


# playFrames()
# Play the frames in timing to BLE
# @timed_frame : List of timed_frame
async def playFrames(timed_frames):

    nb_tf = len(timed_frames)

    #  Connect to BLE Client at @MAC 
    async with BleakClient(ble_vest_mac) as client:

        # If connected successfuly
        if client.is_connected:

            # Print connected BLE Client @MAC
            print(client.address)

            # For each timed frame in timed_frames
            for i_tf in range(nb_tf):
                
                # Send the frame then wait till the next frame
                await client.write_gatt_char(ble_vest_char, bytearray.fromhex(timed_frames[i_tf][1]), True)
                print(f'{ "UUID (" }{ ble_vest_char }{ ") : " }{ timed_frames[i_tf][1] }')
                
                # If it's last frame leave the function
                if i_tf == nb_tf-1:
                    break

                # Time sleep
                time.sleep((timed_frames[i_tf+1][0] - timed_frames[i_tf][0]) / 1000)
