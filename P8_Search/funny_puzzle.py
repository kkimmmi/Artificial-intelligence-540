import heapq

def get_manhattan_distance(from_state, to_state=[1, 2, 3, 4, 5, 6, 7, 0, 0]):
    """
    TODO: implement this function. This function will not be tested directly by the grader. 

    INPUT: 
        Two states (if second state is omitted then it is assumed that it is the goal state)

    RETURNS:
        A scalar that is the sum of Manhattan distances for all tiles.
    """

    distance = 0

    for i in range(len(from_state)):
        if(from_state[i]==0) : continue
        else:
            x=abs(to_state.index(from_state[i])%3-i%3)
            y=abs(int(to_state.index(from_state[i])/3)-int(i/3))
        distance+= x+y
    return distance




def print_succ(state):
    """
    TODO: This is based on get_succ function below, so should implement that function.

    INPUT: 
        A state (list of length 9)

    WHAT IT DOES:
        Prints the list of all the valid successors in the puzzle. 
    """
    succ_states = get_succ(state)

    for succ_state in succ_states:
        print(succ_state, "h={}".format(get_manhattan_distance(succ_state)))


def get_succ(state):
    """
    TODO: implement this function.

    INPUT: 
        A state (list of length 9)

    RETURNS:
        A list of all the valid successors in the puzzle (don't forget to sort the result as done below). 
    """
   
    succ_states=[]

    #up
    for i in range(len(state)):
        temp_state = state.copy()
        if(i-3>=0 and state[i]!=0 and state[i-3]==0):
            temp_state[i-3]=state[i]
            temp_state[i] = 0
            succ_states.append(temp_state)    
    #down
    for i in range(len(state)):
        temp_state = state.copy()
        #up
        if(i+3<9 and state[i]!=0 and state[i+3]==0):
            temp_state[i+3]=state[i]
            temp_state[i] = 0
            succ_states.append(temp_state)  
    #right
    for i in range(len(state)):
        temp_state = state.copy()
        #up
        if((i%3)<2 and state[i]!=0 and state[i+1]==0):
            temp_state[i+1]=state[i]
            temp_state[i] = 0
            succ_states.append(temp_state)  
    #left
    for i in range(len(state)):
        temp_state = state.copy()
        #up
        if(i%3>0 and state[i]!=0 and state[i-1]==0):
            temp_state[i-1]=state[i]
            temp_state[i] = 0
            succ_states.append(temp_state)  

    return sorted(succ_states)


def solve(state, goal_state=[1, 2, 3, 4, 5, 6, 7, 0, 0]):
    """
    TODO: Implement the A* algorithm here.

    INPUT: 
        An initial state (list of length 9)

    WHAT IT SHOULD DO:
        Prints a path of configurations from initial state to goal state along 
        h values, number of moves, and max queue number in the format specified in the pdf.
    """
    OPEN = []
    CLOSED = []
    max_queue_len = 0
    # initial state
    h = get_manhattan_distance(state)
    g = 0
    heapq.heappush(OPEN, (h+g, state, (g, h, -1)))
    #pt_s=dict()
    visited = []
    pt_s=dict()
    a=-1
    pt_s[a]=state

    while True:
        minhp = heapq.heappop(OPEN)
        heapq.heappush(CLOSED, minhp)
        visited.append(minhp[1])
        pt_s[minhp[2][2]]=minhp[1]
        if minhp[1] == goal_state:
            a=[]
            temp = -1
            h = CLOSED[-1][2][0]
            for i in range(h+1):
                for j in range(len(CLOSED)):
                    if(CLOSED[j][2][2]==temp):
                        a.append(CLOSED[j])
                        temp+=1
                        break
     
            #[4, 3, 0, 5, 1, 6, 7, 2, 0] h=7 moves: 0

            for t in range(0,len(a)):
                print(f'{a[t][1]} h={a[t][2][1]} moves: {t}')
            print(f'Max queue length: {max_queue_len}')
            return



        for succ in get_succ(minhp[1]):
            g = minhp[2][0] + 1
            h = get_manhattan_distance(succ)
            
            if succ in visited:
                continue
            else:
                
                if succ not in CLOSED:
                    heapq.heappush(OPEN, (h+g, succ, (g, h, minhp[2][2]+1)))
                else:
                    if(succ in CLOSED):
                        for j in range(0, len(CLOSED)):
                            if(CLOSED[j][2][0]>g):
                                heapq.heappush(OPEN, (h+g, succ, (g, h,  CLOSED[j][2][2])))
                            break  

            

            if len(OPEN) > max_queue_len:
                max_queue_len = len(OPEN)





if __name__ == "__main__":
    """
    Feel free to write your own test code here to exaime the correctness of your functions. 
    Note that this part will not be graded.
    """
    solve([3, 4, 6, 0, 0, 1, 7, 2, 5])
