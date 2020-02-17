for schedule in dictSchedule :
    currentSchedule = dictSchedule[schedule]
    currentGames = currentSchedule.find_all("p","game")
    for game_i in currentGames :
        ##  Remove Spring Training Games and Games that Have Not Happened Yet
        if game_i.text.find("(Spring)") > 0:
            loopCurrent += 1
            countSkip += 1
            print("Games "+str(loopCurrent)+" out of "+str(totalGames)+' ('+str(countRecord)
              +' Recorded, '+str(countSkip)+' Skipped)')
            continue
        if game_i.text.find("Preview") > 0:
            loopCurrent += 1
            countSkip += 1
            print("Games "+str(loopCurrent)+" out of "+str(totalGames)+' ('+str(countRecord)
              +' Recorded, '+str(countSkip)+' Skipped)')
            continue
        ### And So On...
