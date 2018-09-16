from workspace.board import Board

class executive:
    def __init__(self, length, width, bombCnt):
        self.gameBoard=Board()
        self.length=length
        self.width=width
        self.bombCnt=bombCnt

    def checkWinLose(self):
        num_safe_tile=self.length*self.width-self.bombCnt
        num_safe_revealed_tile=0
        num_flagged_tile = 0
        for j in range(self.length):
            for i in range(self.width):
                if(self.gameBoard.board[i][j].isBomb==True and self.gameBoard.board[i][j].isVisible==True):
                    return 2
                elif(self.gameBoard.board[i][j].isVisible==True):
                    num_safe_revealed_tile=num_safe_revealed_tile+1
                # both mines and tiles need to be revealed so that the user cannot guess which tiles are mines without revealing tiles
                if(self.gameBoard.board[i][j].isBomb==True and self.gameBoard.board[i][j].isFlagged == True):
                    num_flagged_tile=num_flagged_tile+1
        if(num_safe_revealed_tile==num_safe_tile and num_flagged_tile==self.bombCnt):
            return 1
        else:
            return 0

    def setUpBoard(self):
        self.gameBoard.make_board(self.width, self.length, self.bombCnt)
        return

    def run(self):
        self.setUpBoard()
        self.gameBoard.place_bomb()
        self.gameBoard.setAdjBomb()
        self.gameBoard.print_board_true()
        """
        self.gameState=0 #gameState 0->unresolved, 1->Win, 2->Loose
        while self.gameState==0:
            self.gameBoard.print_board_true()
            self.gameBoard.print_board()


            #Main Game Loop
            print("Select a spot to reveal")
            print("x pos:")
            x=int(input())
            print("y pos:")
            y=int(input())

            self.gameBoard.reveal_tile(x,y)
            self.gameState=self.checkWinLose()
            continue
       
        self.gameBoard.print_board()
        if(self.gameState==2):
            print("YOU LOSE")
        elif(self.gameState==1):
            print("YOU WIN")
         """
        return


