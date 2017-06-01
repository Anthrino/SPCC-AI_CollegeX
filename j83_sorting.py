class 8puzz:

    def __init__(self, init_state, bcr, bcc, goal_state, bfr, bfc, move, level):
        self.config = init_state
        self.move = move
        self.level = level
        self.heu_val = self.eval_fn() 
        self.blank = blanki
        self.branches = []
        new_state = init_state
        
        if goal_state != init_state and level <= 5:

            if self.bcc > 0 and self.move != 'R':
                temp = new_state[bcr][bcc-1]
                new_state[bcr][bcc-1] = -1
                new_state[bcr][bcc] = temp
                self.branches.append(8puzz(new_state, bcr, bcc-1, goal_state, bfr, bfc, 'L', self.level + 1):

            if self.bcc < 2 and self.move != 'L':
                temp = new_state[bcr][bcc+1]
                new_state[bcr][bcc+1] = -1
                new_state[bcr][bcc] = temp
                self.branches.append(8puzz(new_state, bcr, bcc+1, goal_state, bfr, bfc, 'R', self.level + 1):
                
            if self.bcr > 0 and self.move != 'D':
                temp = new_state[bcr-1][bcc]
                new_state[bcr-1][bcc] = -1
                new_state[bcr][bcc] = temp
                self.branches.append(8puzz(new_state, bcr-1, bcc, goal_state, bfr, bfc, 'U', self.level + 1):
                
            if self.bcr < 2 and self.move != 'U':
                temp = new_state[bcr+1][bcc]
                new_state[bcr+1][bcc] = -1
                new_state[bcr][bcc] = temp
                self.branches.append(8puzz(new_state, bcr+1, bcc, goal_state, bfr, bfc, 'D', self.level + 1):
           
           
        
    def eval_fn



start_state = [[]]
