# pytact/point.py

# Tact Point
#
# Base class for ".tact" from BeHaptic software points manipulation
# For the ".tact" files structure, refer to doc/PyTact_TactFilesTree.png diagram
class Tact_Point:

    # Tact File Class Constructor
    # @point_x : x value
    # @point_y : y value
    # @point_intensity : intensity value
    # @point_time : time value
    def __init__(self):
        pass
    
    ###################
    #     GETTERS     #
    ###################

    # get_startTime()
    # return : chronologic start time of the point
    def get_startTime(self):
        return self.startTime

    # get_endTime()
    # return : chronologic end time of the point
    def get_endTime(self):
        return self.endTime

    # get_index()
    # return : index of the point
    def get_index(self):
        return self.index

    # get_x()
    # return : x value of the point
    def get_x(self):
        return self.x

    # get_y()
    # return : y value of the point
    def get_y(self):
        return self.y

    # get_intensity()
    # return : intensity of the point
    def get_intensity(self):
        return self.intensity

    ###################
    #     SETTERS     #
    ###################

    # set_startTime()
    # @point_startTime : chronologic start time of the point
    def set_startTime(self, point_startTime):
        self.startTime = point_startTime

    # set_endTime()
    # @point_endTime : chronologic end time of the point
    def set_endTime(self, point_endTime):
        self.endTime = point_endTime

    # set_index()
    # @point_index : index of the point
    def set_index(self, point_index):
        self.index = point_index

    # set_x()
    # @point_x : value of the x key
    def set_x(self, point_x):
        self.x = point_x

    # set_y()
    # @point_y : value of the y key
    def set_y(self, point_y):
        self.y = point_y

    # set_intensity()
    # @point_intensity : value of the intensity key
    def set_intensity(self, point_intensity):
        self.intensity = point_intensity
