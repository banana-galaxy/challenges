def solution(path_list):
    north_value = 0
    south_value = 0
    east_value = 0
    west_value = 0
    if len(path_list) >10 :
        return False
    else:
        for item in path_list:
            if item.lower() == 'n':
                north_value += 1
            elif item.lower() == 'w':
                west_value += 1
            elif item.lower() == 'e':
                east_value += 1
            elif item.lower() == 's':
                south_value += 1
        if north_value - south_value == 0 and east_value - west_value == 0:
            return True
        else:
            return False