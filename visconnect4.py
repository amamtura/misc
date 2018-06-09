#!/usr/bin/env python

import os
from itertools import cycle


ROW_COUNT = 6
COLUMN_COUNT = 7

PLAYER_1_DISC_COLOR = '\033[91mRed\033[0m'
PLAYER_2_DISC_COLOR = '\033[93mYel\033[0m'
UNUSED_DISC_SLOT = '   '

WIN_CONTINUOUS_COUNT = 4

PLAYER_MOVE_QUESTION = '\nWhich column (1-%s) would player %s like to drop disc into ? '
BAD_CHOICE_MESSAGE = 'Sorry, bad choice, please try again ...'

PLAYER_WON_MESSAGE = '\nPlayer %s Won!\n'
GAME_DRAW_MESSAGE = 'Draw !!\n'


"""
:returns board: list containing COLUMN_COUNT number of lists, where each sub-list
                 contains ROW_COUNT number of (disc element) positions
"""
def getInitializedBoard(rowCount=ROW_COUNT, columnCount=COLUMN_COUNT):
    board = []
    for i in xrange(columnCount):
        column = [None] * rowCount
        board.append(column)
    return board


"""
prints out the board positions

:returns: None
"""
def displayBoard(board):
    os.system('clear')
    for row in xrange(ROW_COUNT):
        print ''
        for col in board:
            discValue = col[row]
            if discValue is None:
                disc = UNUSED_DISC_SLOT
            else:
                disc = PLAYER_1_DISC_COLOR if discValue == 1 else PLAYER_2_DISC_COLOR
            print '[ %s ]' % disc,
    print '\n'


"""
gets playerChosenColumn after prompting user, sometimes displaying "additionalMessageForPlayer"
alongside the main 'player move question' if needed

:param player: int values 1 or 2 corresponding to the player
:param additionalMessageForPlayer: additional string message for player
:returns: playerChosenColumn (valid range, 1 to COLUMN_COUNT)
"""
def getPlayerMove(player, additionalMessageForPlayer = ''):
    if additionalMessageForPlayer:
        print '\n' + additionalMessageForPlayer

    rawInput = raw_input(PLAYER_MOVE_QUESTION % (COLUMN_COUNT, player))
    try:
        playerChosenColumn = int(rawInput)
    except ValueError:
        playerChosenColumn = -1

    return playerChosenColumn


"""
:param board: See parameter ``board`` in :func:`getInitializedBoard`
:param player: int values 1 or 2 corresponding to the player
:returns: didUpdateBoard (Boolean), lastSlotFilledCoords (Tuple or None)
"""
def updateBoard(board, player, playerChosenColumn):
    if playerChosenColumn < 1 or playerChosenColumn > COLUMN_COUNT:
        return False, None

    discColor = PLAYER_1_DISC_COLOR if player == 1 else PLAYER_2_DISC_COLOR

    chosenColumnIndex = playerChosenColumn - 1
    targetColumn = board[chosenColumnIndex]

    usedSlotsInColumn = len(filter(None, targetColumn))

    if usedSlotsInColumn == ROW_COUNT:
        return False, None

    lowestOpenRowIndex = ROW_COUNT - usedSlotsInColumn - 1
    board[chosenColumnIndex][lowestOpenRowIndex] = player
    return True, (chosenColumnIndex, lowestOpenRowIndex)


"""
:param sequence: list representing disc values in a row/column or a diagonal of the board
:returns winningPlayer: int values 1 or 2 corresponding to player else None
"""
def getWinningPlayerIfAny(sequence):
    discValue = None
    prevDiscValue = None
    continuousCount = 0

    for discValue in sequence:
        if discValue is None:
            continuousCount = 0
            continue
        if prevDiscValue is None or prevDiscValue != discValue:
            continuousCount = 1
            prevDiscValue = discValue
            continue
        continuousCount += 1
        if continuousCount == WIN_CONTINUOUS_COUNT:
            return discValue

"""
:param board: See parameter ``board`` in :func:`getInitializedBoard`
:param lastSlotFilledCoords:
:returns winningPlayer: int values 1 or 2 corresponding to player else None
"""
def checkGameWinStatus(board, lastSlotFilledCoords):

    x = lastSlotFilledCoords[0]
    y = lastSlotFilledCoords[1]
    lastSlotFilledDiscValue = board[x][y]

    column = board[x]
    winningPlayer = getWinningPlayerIfAny(column)
    if winningPlayer:
        return winningPlayer

    row = []
    for col in board:
        row.append(col[y])
    winningPlayer = getWinningPlayerIfAny(row)
    if winningPlayer:
        return winningPlayer

    backwardSlashDiagonal = [lastSlotFilledDiscValue]
    forwardSlashDiagonal = [lastSlotFilledDiscValue]

    # L = last(most recent, valid game move) piece played

    # * * * * * *
    # * * x * * *
    # * * * L * *
    # i.e. top portion of backward slash pattern
    i = x
    j = y
    while True:
        i = i - 1
        j = j - 1
        if i < 0 or j < 0:
            break
        backwardSlashDiagonal.insert(0, board[i][j])

    # * * L * * *
    # * * * x * *
    # * * * * x *
    # i.e. bottom portion of backward slash pattern
    i = x
    j = y
    while True:
        i = i + 1
        j = j + 1
        if i >= COLUMN_COUNT or j >= ROW_COUNT:
            break
        backwardSlashDiagonal.append(board[i][j])

    winningPlayer = getWinningPlayerIfAny(backwardSlashDiagonal)
    if winningPlayer:
        return winningPlayer

    # * * * * L * *
    # * * * x * * *
    # * * x * * * *
    # i.e. bottom portion of forward slash pattern
    i = x
    j = y
    while True:
        i = i - 1
        j = j + 1
        if i < 0 or j >= ROW_COUNT:
            break
        forwardSlashDiagonal.insert(0, board[i][j])

    # * * * * * *
    # * * * * x *
    # * * * L * *
    # i.e. top portion of forward slash pattern
    i = x
    j = y
    while True:
        i = i + 1
        j = j - 1
        if i >= COLUMN_COUNT or j < 0:
            break
        forwardSlashDiagonal.append(board[i][j])

    winningPlayer = getWinningPlayerIfAny(forwardSlashDiagonal)
    if winningPlayer:
        return winningPlayer

    return None


def main():

    playGame = True
    discsPlayed = 0
    additionalMessageForPlayer = ''

    board = getInitializedBoard()
    displayBoard(board)

    playerIterator = cycle(range(1,3))

    while playGame:
        player = playerIterator.next()
        playerChosenColumn = getPlayerMove(player, additionalMessageForPlayer)
        additionalMessageForPlayer = ''

        didUpdateBoard, lastSlotFilledCoords = updateBoard(board, player, playerChosenColumn)

        if not didUpdateBoard:
            additionalMessageForPlayer = BAD_CHOICE_MESSAGE
            playerIterator.next()
            continue

        discsPlayed += 1

        displayBoard(board)
        winningPlayer = checkGameWinStatus(board, lastSlotFilledCoords)

        if winningPlayer:
            print PLAYER_WON_MESSAGE % (PLAYER_1_DISC_COLOR if winningPlayer == 1 
                                                            else PLAYER_2_DISC_COLOR)
            playGame = False
            continue

        if discsPlayed == ROW_COUNT * COLUMN_COUNT:
            print GAME_DRAW_MESSAGE
            playGame = False
            continue

if __name__ == "__main__":
    main()

