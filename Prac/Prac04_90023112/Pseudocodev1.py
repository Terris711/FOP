#
# competitionv1.py - scores for competitors from judges 
#
def main():
    numJudges = 7
    numCompetitors = int(input("Enter number of competitors (between 3 and 16 inc)"))

    for comp in range(numCompetitors):
        totalC = 0
        print('Input scores between 0 and 10 for each judge:')
        for j in range(numJudges):
            scoreJ = int(input('Score for judge' + str(j) + ":"))
            totalC = totalC + scoreJ
        scoreC = totalC / numJudges
        print('Score for competitor', comp,' is', scoreC)

if __name__ == "__main__":
    main()

