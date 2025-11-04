def solution(participant, completion):
    parti_ = {}
    for p in participant:
        if p in parti_:
            parti_[p] += 1
        else:
            parti_[p] = 1

    for c in completion:
        parti_[c] -= 1
            
    for key in parti_.keys():
        if parti_[key] > 0:
            return key
    