def matrixSum(matrix):
    #Returns a list of cols instead of rows
    def get_col():
        rt = []
        for c in range(len(matrix[0])):
            ct = []
            for i in range(len(matrix)):
                ct.append(matrix[i][c])
            rt.append(ct)
        return rt
    
    #Check if TWT staff isn't able to move in
    def not_able(idx,c):
        for i, v in enumerate(c):
            if i < idx and v <= 0:
                return True
        return False
                
    col = get_col().copy()
    SUMLIST = []
    
    for col_count, every_col in enumerate(col):
        for num_count, every_num in enumerate(every_col):
            if not_able(num_count,every_col):
                SUMLIST.append(0)
            else:
                SUMLIST.append(every_num)
                    
    return sum(SUMLIST)