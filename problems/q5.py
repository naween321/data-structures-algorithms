def solution(sequence):
    sequence = sequence.lower()
    qee = sequence.split("qee")
    print(qee)
    zee = sequence.split("zee")
    print(zee)
    if qee.count("qee") == zee.count("zee"):
        return True
    return False


print(solution("QEeabZeeQeeZee"))
