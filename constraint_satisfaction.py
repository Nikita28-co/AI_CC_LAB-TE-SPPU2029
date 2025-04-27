colors=["Red","Blue","Green"]
states=["WA","NT","SA","Q","NSW","V"]
neg={
    "WA":["NT","SA"],
    "NT":["WA","SA","Q"],
    "SA":["WA","NT","Q","NSW","V"],
    "Q":["NT","SA","NSW"],
    "NSW":["Q","SA","V"],
    "V":["SA","NSW"]
}

colors_of_states={}

def promising(state,color):
    for negs in neg.get(state):
        color_of_neg=colors_of_states.get(negs)
        if color_of_neg==color:
            return False
    return True
def backtrack(state_index):
    if state_index==len(states):
        return True
    state=states[state_index]

    for color in colors:
        if promising(state,color):
            colors_of_states[state]=color
            if backtrack(state_index+1):
                return True
            colors_of_states[state]=None
            (backtrack)

    return False
def get_color_for_state(state):
    for color in colors:
        if promising(state,color):
            return color

def main():
    for state in states:
        colors_of_states[state]=get_color_for_state(state)
    print(colors_of_states)

    if backtrack(0):
        print(colors_of_states)
    else:
        print("no solution found")
main()