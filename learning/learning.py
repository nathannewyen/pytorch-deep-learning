import numpy as np

# Create a 3-dimensional array (2x3x4)

array = np.array(
    [[
        [[ 0,  1,  2,  3],
         [ 4,  5,  6,  7],
         [ 8,  9, 10, 11]],

        [[12, 13, 14, 15],
         [16, 17, 18, 19],
         [20, 21, 22, 23]]
    ], [
        [[ 9,  1,  2,  3],
         [ 8,  5,  6,  7],
         [ 3,  9, 10, 11]],

        [[1, 3, 14, 15],
         [16, 2, 18, 19],
         [20, 9, 22, 23]]
    ]]
)

print(array.shape)
selected_elements = array[:, :, 0, 1]
print(selected_elements)
