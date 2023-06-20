# pytact/modes.py

from pytact.tact import *
from pytact.point import *
from pytact.vest import *

# print_pointValue()
# @point_id : index of the point in the feedback
# @key : key of the point
# @value : value of the key
def print_pointValue(point_id, key, value):
    print(f'{ "    - Point " }{ point_id }{ " (" } { key } { ") : " }{ value }')

# tact_points()
# @tact_obj : Tact() object
# @point_container : list of points objects
# @track_idx : index of the track
# @effect_idx : index of the effect
# @vest_side : side of the vest for the point list
def tact_points(tact_obj, point_container, track_idx, effect_idx, vest_side):

    # Side of the vest
    print(vest_side)

    # Get Modes
    tact_mode_dot(tact_obj, point_container, track_idx, effect_idx, vest_side)
    tact_mode_path(tact_obj, point_container, track_idx, effect_idx, vest_side)

# tact_file()
# @tact_file_str : ".tact" filename
# @point_container : list of points objects
def tact_file(tact_file_str, point_container):

    tact = Tact_File(tact_file_str)

    ### Track ###
    for i in range(len(tact.get_all_tracks())):        
        # Tracks
        ### Effect ###
        for j in range(len(tact.get_all_effects(i))):
            # Effect
            print(tact.get_effect_name(i, j))
            print(f'{ " - Effect startTime (" }{ tact.get_effect_name(i, j) }{") : "}{ tact.get_effect_startTime(i, j) }')
            print(f'{ " - Effect offsetTime (" }{ tact.get_effect_name(i, j) }{") : "}{ tact.get_effect_offsetTime(i, j) }')
            
            ### Vest Sides ###
            tact_points(tact, point_container, i, j, "VestFront")
            tact_points(tact, point_container, i, j, "VestBack")
            
            print("\n")

# tact_mode_dot()
# @tact_obj : Tact() object
# @point_container : list of points objects
# @track_idx : index of the track
# @effect_idx : index of the effect
# @vest_side : side of the vest for the point list
def tact_mode_dot(tact_obj, point_container, track_idx, effect_idx, vest_side):

    # Dot Mode
    for k in range(len(tact_obj.get_all_feedbacks(track_idx, effect_idx, vest_side, "dotMode"))):

        # Dot pointList
        dot_size = len(tact_obj.get_pointList(track_idx, effect_idx, vest_side, "dotMode", k))

        # If there is a Dot Mode
        if dot_size != False:

            # Dot Points
            for l in range(dot_size):

                # Create a tact point
                Point_Dot = Tact_Point()
                
                # Set Start time
                Point_Dot.set_startTime(tact_obj.get_feedback_startTime(track_idx, effect_idx, vest_side, "dotMode", k) + tact_obj.get_effect_startTime(track_idx, effect_idx))
                
                # Set End time from feedback end time
                Point_Dot.set_endTime(tact_obj.get_feedback_endTime(track_idx, effect_idx, vest_side, "dotMode", k) + tact_obj.get_effect_startTime(track_idx, effect_idx))
                
                # Set Index
                Point_Dot.set_index(dotToIndex(tact_obj.get_point_index(track_idx, effect_idx, vest_side, "dotMode", k, l)))
                
                # Set Intensity
                Point_Dot.set_intensity(intensityToChar(tact_obj.get_point_intensity(track_idx, effect_idx, vest_side, "dotMode", k, l)))

                # Debug point
                print_pointValue(l, "startTime", Point_Dot.get_startTime())
                print_pointValue(l, "endTime", Point_Dot.get_endTime())
                print_pointValue(l, "index", Point_Dot.get_index())
                print_pointValue(l, "intensity", Point_Dot.get_intensity())

                # Add point to the container
                point_container.append(Point_Dot)

# tact_mode_path()
# @tact_obj : Tact() object
# @point_container : list of points objects
# @track_idx : index of the track
# @effect_idx : index of the effect
# @vest_side : side of the vest for the point list
def tact_mode_path(tact_obj, point_container, track_idx, effect_idx, vest_side):
    
    # Path Mode
    for k in range(len(tact_obj.get_all_feedbacks(track_idx, effect_idx, vest_side, "pathMode"))):
        
        # Path pointList
        path_size = len(tact_obj.get_pointList(track_idx, effect_idx, vest_side, "pathMode", k))
        
        # If there is a Path Mode
        if path_size != False:
            
            # Path Points
            for l in range(path_size):
                
                # Create a tact point
                Point_Path = Tact_Point()
                
                # Set Start time
                Point_Path.set_startTime(tact_obj.get_point_time(track_idx, effect_idx, vest_side, "pathMode", k, l) + tact_obj.get_effect_startTime(track_idx, effect_idx))
                
                # Set End time from next point start time
                if l < (path_size - 1):
                    Point_Path.set_endTime(tact_obj.get_point_time(track_idx, effect_idx, vest_side, "pathMode", k, l+1) + tact_obj.get_effect_startTime(track_idx, effect_idx))
                else:
                    Point_Path.set_endTime(tact_obj.get_effect_offsetTime(track_idx, effect_idx))

                # Set Axis                
                Point_Path.set_x(tact_obj.get_point_x(track_idx, effect_idx, vest_side, "pathMode", k, l))
                Point_Path.set_y(tact_obj.get_point_y(track_idx, effect_idx, vest_side, "pathMode", k, l))

                # Set Index from axis values
                Point_Path.set_index(axisToIndex(Point_Path))

                # Set Intensity
                Point_Path.set_intensity(intensityToChar(tact_obj.get_point_intensity(track_idx, effect_idx, vest_side, "pathMode", k, l)))

                # Debug point
                print_pointValue(l, "startTime", Point_Path.get_startTime())
                print_pointValue(l, "endTime", Point_Path.get_endTime())
                print_pointValue(l, "index", Point_Path.get_index())
                print_pointValue(l, "x", Point_Path.get_x())
                print_pointValue(l, "y", Point_Path.get_y())
                print_pointValue(l, "intensity", Point_Path.get_intensity())

                # Add point to the container
                point_container.append(Point_Path)
