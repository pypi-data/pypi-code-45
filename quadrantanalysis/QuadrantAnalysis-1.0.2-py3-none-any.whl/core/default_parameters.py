default_filename = "Choose a Set Directory!"

default_arena_shape = 'Auto'

default_ppm = '300'

# rectangular arena defaults
default_rectangle_rows = '3'
default_rectangle_cols = '3'
default_rectangle_length = ''
default_rectangle_width = ''

# circular arena defaults
default_num_inner = '1'
default_num_outer = '4'
default_inner_rad = '0.5'  # 50% of the outer radius
default_circle_radius = ''

default_bin_label_array = {}

# our default 3x3 grid
default_bin_label_array[('Rectangular', 3, 3)] = [[0, 0, 0],
                                                  [0, 1, 0],
                                                  [0, 0, 0]]

'''
# our default 5x5 grid
default_bin_label_array[('Rectangular', 5, 5)] = [[0, 0, 0, 0, 0],
                                                  [0, 2, 2, 2, 0],
                                                  [0, 2, 1, 2, 0],
                                                  [0, 2, 2, 2, 0],
                                                  [0, 0, 0, 0, 0]]
'''

default_bin_label_array[('Circle', 1, 4)] = [[1],
                                             [0, 0, 0, 0]]
