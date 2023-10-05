def play_with_asterisk(n):
    ast = '*'
    m = n - 1
    pattern = ""
    for i in range(0, n):
        for j in range(0, m):
            pattern += ' '
        m = m - 1
        for j in range(0, i + 1):
            pattern += ast + ' '
        pattern += "\n"
    return pattern

if __name__ == '__main__':
    print(play_with_asterisk(5))
    """
    *
   * *
  * * *
 * * * *
* * * * *
    """
