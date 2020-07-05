def whichExit(mat):
    my_pos_row = -1
    my_pos_col = -1
    left_score = 0
    right_score = 0
    for i in range(0, len(mat)):
        for j in range(0, len(mat[i])):
            if mat[i][j] == 0:
                my_pos_row = i
                my_pos_col = j

    for j in range(0, my_pos_col):
        if mat[my_pos_row][j] == 1:
            left_score += mat[my_pos_row][j]

    for j in range(my_pos_col, len(mat[i])):
        if mat[my_pos_row][j] == 1:
            right_score += mat[my_pos_row][j]

    if left_score < right_score:
        return "left"
    elif right_score < left_score:
        return "right"
    elif left_score == right_score:
        return "same"