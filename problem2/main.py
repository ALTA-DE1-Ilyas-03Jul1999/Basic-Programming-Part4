def draw_xyz(N):
    pattern = ""
    for i in range(N):
        for j in range(N):
            # Calculate the index based on row and column.
            index = i * N + j + 1

            # Check if it's a multiple of 3.
            if index % 3 == 0:
                pattern += 'X '
            # Check if it's an odd index.
            elif index % 2 == 1:
                pattern += 'Y '
            # Else it's an even index.
            else:
                pattern += 'Z '

        pattern += '\n'
    return pattern

if __name__ == '__main__':
    print(draw_xyz(3))
    """
    Y Z X 
    Z Y X 
    Y Z X 
    """

    print(draw_xyz(5))
    """
    Y Z X Z Y 
    X Y Z X Z 
    Y X Y Z X 
    Z Y X Y Z 
    X Z Y X Y 
    """
