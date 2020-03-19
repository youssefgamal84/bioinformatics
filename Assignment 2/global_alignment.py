import numpy as np


# Recursive Traceback to generate all possible answers
def traceback(answer, r, c, strand1, strand2, part1, part2, diagonal_arrows, up_arrows, left_arrows):
    if r == 0 and c == 0:
        answer.append((part1, part2))
        return

    if diagonal_arrows[r][c]:
        traceback(answer, r - 1, c - 1, strand1, strand2, strand1[r - 1] + part1, strand2[c - 1] + part2,
                  diagonal_arrows, up_arrows, left_arrows)
    if up_arrows[r][c]:
        traceback(answer, r - 1, c, strand1, strand2, strand1[r - 1] + part1, "-" + part2, diagonal_arrows, up_arrows,
                  left_arrows)
    if left_arrows[r][c]:
        traceback(answer, r, c - 1, strand1, strand2, "-" + part1, strand2[c - 1] + part2, diagonal_arrows, up_arrows,
                  left_arrows)


def global_alignment(strand1, strand2, match, mismatch, gap):
    R = len(strand1) + 1
    C = len(strand2) + 1

    matrix = np.zeros((R, C), dtype=np.int)
    # indicating arrows for traceback
    left_arrows = np.zeros((R, C), dtype=np.bool)
    up_arrows = np.zeros((R, C), dtype=np.bool)
    diagonal_arrows = np.zeros((R, C), dtype=np.bool)

    # fill the matrix

    ## initialization
    for i in range(0, C):
        matrix[0, i] = i * gap
        left_arrows[0, i] = True
    for i in range(0, R):
        matrix[i, 0] = i * gap
        up_arrows[i, 0] = True

    for i in range(1, R):
        for j in range(1, C):
            is_match = (strand1[i - 1] == strand2[j - 1])
            # Determine the highest score
            new_score = max(matrix[i - 1][j - 1] + is_match * match + (not is_match) * mismatch, matrix[i - 1][j] + gap,
                            matrix[i][j - 1] + gap)
            matrix[i][j] = new_score
            # determine what paths made the highest score
            if new_score == matrix[i - 1][j - 1] + is_match * match + (not is_match) * mismatch:
                diagonal_arrows[i][j] = True
            if new_score == matrix[i - 1][j] + gap:
                up_arrows[i][j] = True
            if new_score == matrix[i][j - 1] + gap:
                left_arrows[i][j] = True

    # trace back
    answer = []
    traceback(answer, R - 1, C - 1, strand1, strand2, "", "", diagonal_arrows, up_arrows, left_arrows)
    return answer
