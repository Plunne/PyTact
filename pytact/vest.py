# pytact/vest.py

# matrix2Dto1D()
# @matrix : 2D list
# return : 1D list
def matrix2Dto1D(matrix):
    array = []
    for i in matrix:
        for j in i:
            array.append(j)
    
    return array

scale_x = [0.16, 0.5, 0.83]
scale_y = [0.12, 0.35, 0.62, 0.87]
matrix2D =   [[ 31, 32,  1,  2 ],
            [ 33, 34,  3,  4 ],
            [ 35, 36,  5,  6 ],
            [ 37, 38,  7,  8 ],
            [ 39, 40,  9, 10 ]]
matrix1D = matrix2Dto1D(matrix2D)


# valueToRowColumn()
# @scale : scale of the axis
# @value : point axis value
# return : column or row
def valueToRowColumn(scale, value):

    for i in range(len(scale)):
        if value >= scale[i]:
            axis = i + 1
        else:
            axis = i
            break

    return axis

# dotToIndex()
# @index : tact index of a point
# return : vest index of a point
def dotToIndex(index):

    return matrix1D[int(index)]

# axisToIndex()
# @point : a tact point
# return : index of the point
def axisToIndex(point):

    column = valueToRowColumn(scale_x, point.x)
    row = valueToRowColumn(scale_y, point.y)

    return matrix2D[row][column]

# intensityToVest()
# @point : a tact point
# return : intensity of the point in char (for frame)
def intensityToChar(intensity):

    if intensity < 1:
        intensity *= 10
        return str(int(intensity))
    else:
        return 'A'
