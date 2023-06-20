# pytact/tact.py

import json

# Tact File
#
# Base class for ".tact" files from BeHaptic software manipulation
# For the ".tact" files structure, refer to doc/PyTact_TactFilesTree.png diagram
class Tact_File:

    # Tact File Class Constructor
    # @tact_file : the tact file object
    def __init__(self, tact_file):

        print("Opening " + tact_file + "\n")
        with open("tact/" + tact_file) as file:
            self.tact = json.load(file)
    
    ###################
    #     GETTERS     #
    ###################

    ### Tracks ###

    # get_all_tracks()
    # return : all tracks list
    def get_all_tracks(self):
        return self.tact["project"]["tracks"]

    # get_track()
    # @track_idx : index of the track you want to select in the tact file
    # return : track
    def get_track(self, track_idx):
        return self.get_all_tracks()[track_idx]

    ### Effects ###

    # get_all_effects()
    # @track_idx : index of the track you want to select in the tact file
    # return : all effects list
    def get_all_effects(self, track_idx):
        return self.get_track(track_idx)["effects"]

    # get_effect()
    # @track_idx : index of the track you want to select in the tact file
    # @effect_idx : index of the effect you want to select in the track
    # return : effect
    def get_effect(self, track_idx, effect_idx):
        return self.get_all_effects(track_idx)[effect_idx]

    # get_effect_name()
    # @track_idx : index of the track you want to select in the tact file
    # @effect_idx : index of the effect you want to select in the track
    # return : effect name
    def get_effect_name(self, track_idx, effect_idx):
        return self.get_effect(track_idx, effect_idx)["name"]

    # get_effect_startTime()
    # @track_idx : index of the track you want to select in the tact file
    # @effect_idx : index of the effect you want to select in the track
    # return : effect start time
    def get_effect_startTime(self, track_idx, effect_idx):
        return self.get_effect(track_idx, effect_idx)["startTime"]

    # get_effect_offsetTime()
    # @track_idx : index of the track you want to select in the tact file
    # @effect_idx : index of the effect you want to select in the track
    # return : effect offset time
    def get_effect_offsetTime(self, track_idx, effect_idx):
        return self.get_effect(track_idx, effect_idx)["offsetTime"]

    ### Modes ###

    # get_mode_side()
    # @track_idx : index of the track you want to select in the tact file
    # @effect_idx : index of the effect you want to select in the track
    # @mode_side_str : name of the vest side you want to select in the effect
    # return : mode side
    def get_mode_side(self, track_idx, effect_idx, mode_side_str):
        return self.get_effect(track_idx, effect_idx)["modes"][mode_side_str]
    
    # get_mode_type()
    # @track_idx : index of the track you want to select in the tact file
    # @effect_idx : index of the effect you want to select in the track
    # @mode_side_str : name of the vest side you want to select in the effect
    # @mode_type_str : name of the mode you want to select in the effect
    # return : mode type
    def get_mode_type(self, track_idx, effect_idx, mode_side_str, mode_type_str):
        return self.get_mode_side(track_idx, effect_idx, mode_side_str)[mode_type_str]


    ### Feedback ###
    
    # get_all_feedbacks()
    # @track_idx : index of the track you want to select in the tact file
    # @effect_idx : index of the effect you want to select in the track
    # @mode_side_str : name of the vest side you want to select in the effect
    # @mode_type_str : name of the mode you want to select in the effect
    # return : all feedbacks list
    def get_all_feedbacks(self, track_idx, effect_idx, mode_side_str, mode_type_str):
        return self.get_mode_type(track_idx, effect_idx, mode_side_str, mode_type_str)["feedback"]

    # get_mode_feedback()
    # @track_idx : index of the track you want to select in the tact file
    # @effect_idx : index of the effect you want to select in the track
    # @mode_side_str : name of the vest side you want to select in the effect
    # @mode_type_str : name of the mode you want to select in the effect
    # @mode_feedback_idx : index of the feedback you want to select in the mode
    # return : feedback at index
    def get_feedback(self, track_idx, effect_idx, mode_side_str, mode_type_str, mode_feedback_idx):
        return self.get_all_feedbacks(track_idx, effect_idx, mode_side_str, mode_type_str)[mode_feedback_idx]

    # get_feedback_startTime()
    # @mode_feedback_idx : index of the feedback you want to select in the mode
    # return : feedback startTime value
    def get_feedback_startTime(self, track_idx, effect_idx, mode_side_str, mode_type_str, mode_feedback_idx):
        return self.get_feedback(track_idx, effect_idx, mode_side_str, mode_type_str, mode_feedback_idx)["startTime"]

    # get_feedback_endTime()
    # @mode_feedback_idx : index of the feedback you want to select in the mode
    # return : feedback endTime value
    def get_feedback_endTime(self, track_idx, effect_idx, mode_side_str, mode_type_str, mode_feedback_idx):
        return self.get_feedback(track_idx, effect_idx, mode_side_str, mode_type_str, mode_feedback_idx)["endTime"]

    ### Point ###

    # get_pointList()
    # @track_idx : index of the track you want to select in the tact file
    # @effect_idx : index of the effect you want to select in the track
    # @mode_side_str : name of the vest side you want to select in the effect
    # @mode_type_str : name of the mode you want to select in the effect
    # @mode_feedback_idx : index of the feedback you want to select in the mode
    # @point_in_list : index of the point you want to select in the list
    # return : point in list
    def get_pointList(self, track_idx, effect_idx, mode_side_str, mode_type_str, mode_feedback_idx):
        return self.get_feedback(track_idx, effect_idx, mode_side_str, mode_type_str, mode_feedback_idx)["pointList"]

    # get_point_in_list()
    # @track_idx : index of the track you want to select in the tact file
    # @effect_idx : index of the effect you want to select in the track
    # @mode_side_str : name of the vest side you want to select in the effect
    # @mode_type_str : name of the mode you want to select in the effect
    # @mode_feedback_idx : index of the feedback you want to select in the mode
    # @point_in_list : index of the point you want to select in the list
    # return : point in list
    def get_point_in_list(self, track_idx, effect_idx, mode_side_str, mode_type_str, mode_feedback_idx, point_in_list):
        return self.get_pointList(track_idx, effect_idx, mode_side_str, mode_type_str, mode_feedback_idx)[point_in_list]

    # get_point_index()
    # @mode_feedback_idx : index of the feedback you want to select in the mode
    # @point_in_list : index of the point you want to select in the list
    # return : point index value
    def get_point_index(self, track_idx, effect_idx, mode_side_str, mode_type_str, mode_feedback_idx, point_in_list):
        return self.get_point_in_list(track_idx, effect_idx, mode_side_str, mode_type_str, mode_feedback_idx, point_in_list)["index"]

    # get_point_intensity()
    # @mode_feedback_idx : index of the feedback you want to select in the mode
    # @point_in_list : index of the point you want to select in the list
    # return : point intensity value
    def get_point_intensity(self, track_idx, effect_idx, mode_side_str, mode_type_str, mode_feedback_idx, point_in_list):
        return self.get_point_in_list(track_idx, effect_idx, mode_side_str, mode_type_str, mode_feedback_idx, point_in_list)["intensity"]

    # get_point_time()
    # @mode_feedback_idx : index of the feedback you want to select in the mode
    # @point_in_list : index of the point you want to select in the list
    # return : point time value
    def get_point_time(self, track_idx, effect_idx, mode_side_str, mode_type_str, mode_feedback_idx, point_in_list):
        return self.get_point_in_list(track_idx, effect_idx, mode_side_str, mode_type_str, mode_feedback_idx, point_in_list)["time"]

    # get_point_x()
    # @mode_feedback_idx : index of the feedback you want to select in the mode
    # @point_in_list : index of the point you want to select in the list
    # return : point x position value
    def get_point_x(self, track_idx, effect_idx, mode_side_str, mode_type_str, mode_feedback_idx, point_in_list):
        return self.get_point_in_list(track_idx, effect_idx, mode_side_str, mode_type_str, mode_feedback_idx, point_in_list)["x"]

    # get_point_x()
    # @mode_feedback_idx : index of the feedback you want to select in the mode
    # @point_in_list : index of the point you want to select in the list
    # return : point y position value
    def get_point_y(self, track_idx, effect_idx, mode_side_str, mode_type_str, mode_feedback_idx, point_in_list):
        return self.get_point_in_list(track_idx, effect_idx, mode_side_str, mode_type_str, mode_feedback_idx, point_in_list)["y"]
