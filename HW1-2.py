from simpleai.search import SearchProblem, breadth_first


class IbrahimProblem(SearchProblem):

    #These lines of cod will determine the number of sheep and wolfs in both B and A
    def actions(self,state):
        numberOfWolfsInA  = sum([1 for i in range(len(state.split("-"))) if state.split("-")[i] == "wa"])
        numberOfSheepsInA = sum([1 for i in range(len(state.split("-"))) if state.split("-")[i] == "sa"])
        numberOfWolfsInB= 3-numberOfWolfsInA
        numberOfSheepsInB= 3-numberOfSheepsInA

        #If the sheep are eaten there is no reason to continue
        if ((numberOfWolfsInA>numberOfSheepsInA and numberOfSheepsInA!=0) or(numberOfWolfsInB>numberOfSheepsInB and numberOfSheepsInB!=0)):

            return []

        #If the boat is in reign A then the next action has to be to region b
        elif state[0]=="a":
            # These are all of the possible actions to region B but some of them will be excluded
            # depending on the conditions
            actions=["b","b-w","b-w-w","b-s","b-s-s","b-w-s"]
            if numberOfWolfsInA<=1:
                actions.remove("b-w-w")
            if numberOfWolfsInA==0:
                actions.remove("b-w")
                try:
                    actions.remove("b-w-s")
                except Exception:
                    pass
            if numberOfSheepsInA<=1:
                actions.remove("b-s-s")

            if numberOfSheepsInA==0:
                actions.remove("b-s")
                try:
                    actions.remove("b-w-s")
                except Exception:
                    pass
            return actions

        #Same logic as the previous elif
        else:
            actions=["a","a-w","a-w-w","a-s","a-s-s","a-w-s"]

            if numberOfWolfsInB<=1:
                actions.remove("a-w-w")

            if numberOfWolfsInB==0:
                actions.remove("a-w")
                try:
                    actions.remove("a-w-s")
                except Exception:
                    pass

            if numberOfSheepsInB<=1:
                actions.remove("a-s-s")

            if numberOfSheepsInB==0:
                actions.remove("a-s")
                try:
                    actions.remove("a-w-s")
                except Exception:
                    pass
            return actions


    def result(self,state,action):

        state=state.split("-")
        wolfs = sum([1 for i in range(len(action.split("-"))) if action.split("-")[i] == "w"])
        sheeps =sum([1 for i in range(len(action.split("-"))) if action.split("-")[i] == "s"])

        if action[0]=="a":
            state[0]="a"
            for i in range(wolfs):
                state.insert(1+i,"wa")
                state.remove("wb")

            for i in range(sheeps):
                state.insert(len(state),"sa")
                state.remove("sb")

        else:
            state[0]="b"
            for i in range(wolfs):
                state.insert(1+i,"wb")
                state.remove("wa")

            for i in range(sheeps):
                state.insert(len(state),"sb")
                state.remove("sa")
        return "-".join(state)

    def is_goal(self, state):
        if state=="b-wb-wb-wb-sb-sb-sb":
            return True
        else:
            return False


test=IbrahimProblem(initial_state="a-wa-wa-wa-sa-sa-sa")
result = breadth_first(test)

print(result.state)  # the goal state
print(result.path())
