class Tictactoe:

    def __init__(self):
        self.board={1:' ',2:' ',3:' ',
                    4:' ',5:' ',6:' ',
                    7:' ',8:' ',9:' '}
        self.turn='X'

    def __str__(self):
        
            return str((str(self.board[1])+ ' |' +str(self.board[2]) + ' |' +str(self.board[3]) + '\n'
                    +'--------\n'
                    +str(self.board[4])+ ' |' +str(self.board[5]) + ' |' +str(self.board[6]) + '\n'
                    +'--------\n'
                    +str(self.board[7])+ ' |' +str(self.board[8]) + ' |' +str(self.board[9]) 
                    ))
    def checkwin(self):
        if (self.board[1]=='X' and self.board[2]=='X' and self.board[3]=='X'):
            print('X wins')
            return True
        elif (self.board[1]=='X' and self.board[5]=='X' and self.board[9]=='X'):
            print('X wins')
            return True
        elif (self.board[4]=='X' and self.board[5]=='X' and self.board[6]=='X'):
            print('X wins')
            return True
        elif (self.board[7]=='X' and self.board[8]=='X' and self.board[9]=='X'):
            print('X wins')
            return True
        elif (self.board[1]=='X' and self.board[4]=='X' and self.board[7]=='X'):
            print('X wins')
            return True
        elif (self.board[2]=='X' and self.board[5]=='X' and self.board[8]=='X'):
            print('X wins')
            return True
        elif (self.board[3]=='X' and self.board[6]=='X' and self.board[9]=='X'):
            print('X wins')
            return True
        elif (self.board[1]=='O' and self.board[4]=='O' and self.board[7]=='O'):
            print('O wins')
            return True
        elif (self.board[7]=='X' and self.board[5]=='X' and self.board[3]=='X'):
            print('X wins')
            return True
        elif (self.board[2]=='O' and self.board[5]=='O' and self.board[8]=='O'):
            print('O wins')
            return True
        elif (self.board[3]=='O' and self.board[6]=='O' and self.board[9]=='O'):
            print('O wins')
            return True
        elif (self.board[1]=='O' and self.board[2]=='O' and self.board[3]=='O'):
            print('O wins')
            return True
        elif (self.board[1]=='O' and self.board[5]=='O' and self.board[9]=='O'):
            print('O wins')
            return True
        elif (self.board[4]=='O' and self.board[5]=='O' and self.board[6]=='O'):
            print('O wins')
            return True
        elif (self.board[7]=='O' and self.board[8]=='O' and self.board[9]=='O'):
            print('O wins')
            return True
        elif (self.board[7]=='O' and self.board[5]=='O' and self.board[3]=='O'):
            print('O wins')
            return True
        else:
            return False
            
    def turnchanger(self):
        if self.turn=='X':
            self.turn='Y'
        if self.turn=='Y':
            self.turn='X'
            

    def boardupdate(self):
        if self.checkwin() is False:
            valid=[]
            for i in range(1,10):
                if self.board[i]==' ':
                    valid.append(i)
            print('Turn of ' + str(self.turn) + '\n'
                  +'You can move at positions ' + str(valid))
            move=int(input('Enter number to place your marker: '))
            self.board[move]=str(self.turn)
            if self.turn=='O':
                self.turn='X'
            elif self.turn=='X':
                self.turn='O'
            

def main():
    game=Tictactoe()
    print(game)
    while game.checkwin() is False:
        game.boardupdate()
        print(game)
       

if __name__=='__main__':
    main()
    
            
        
        
        
        
        
