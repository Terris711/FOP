#
# competitionv1.py - scores for competitors from Judges 
#
def main():
    numJudges = 7
    numCompetitors = int(input("Enter number of competitors (between 3 and 16 inc):"))

    while numCompetitors < 3 or  numCompetitors > 16:
        print("Error - Re-enter number of competitiors (between 3 and 16 inc)")
        numCompetitors = int(input("Enter number of competitors (between 3 and 16 inc):"))

    for comp in range(numCompetitors):
        totalC = 0
        print('input scores between 0 and 10 for each judge')
        for j in range(numJudges):
             scoreJ = int(input('Score for judge (0-10)' + str(j) + ":"))
            
             while scoreJ < 0 or  scoreJ > 10:
                print("Error - Re-enter score (0-10)")
                scoreJ = int(input("Score for judges (0-10)" + str(j) + ":"))
                print()
                totalC = totalC + scoreJ
        scoreC = totalC / numJudges
        print('Score for competitor', comp,' is', scoreC)

if __name__ == "__main__":
    main()
