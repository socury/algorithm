d = {"A+": 4.5, "A0": 4.0, "B+": 3.5, "B0": 3.0, "C+": 2.5, "C0": 2.0, "D+": 1.5, "D0": 1.0, "F": 0.0}
scoreSum = 0
subSum = 0

for i in range(20):
    a, score, rank = input().split()
    if rank == "P":
        continue
    subScore = float(d[rank])
    score = float(score)

    scoreSum += score
    subSum += score * subScore

answer = subSum/scoreSum
print(round(answer, 6))