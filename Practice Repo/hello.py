def main():
    lives = 3
    goals = 0
    print("GAME STARTED!")
    while lives > 0:
        print(f"Lives = {lives}")
        print(f"Goals = {goals}")
        power = int(input("Input a power level from 1 to 10: "))
        target = int(input("Pick one of the 5 positions: "))
        if power < 1 or power > 10:
            print("Invalid power! Skied it out of the stadium. Lose a life.")
            lives -= 1
        # 2. Top-Left or Top-Right (Targets 1 & 2)
        elif target == 1 or target == 2:
            if power >= 7 and power < 10:
                print("GOAL! Absolute rocket into the top bins!")
                goals += 1
            elif power == 10 and power % 2 == 0:
                print("GOAL! Stunner into the top corner off the underside of the bar!")
                goals += 1
            elif power >= 7:
                print("CLANG! Too much power, you hit the structural iron of the crossbar!")
                lives -= 1
            else:
                print("Saved! Too weak, the keeper easily plucks it out of the air.")
                lives -= 1
        # 3. Bottom-Left or Bottom-Right (Targets 3 & 4)
        elif target == 3 or target == 4:
            if 4 <= power <= 8:
                print("GOAL! Tucked neatly into the bottom corner!")
                goals += 1
            elif power > 8:
                print("Wide! You dragged your shot past the post.")
                lives -= 1
            else:
                print("Saved! A weak trundler straight into the keeper's gloves.")
                lives -= 1
        # 4. Down the Middle (Target 5)
        elif target == 5:
            if power == 4 or power == 5:
                print("GOAL! A cheeky Panenka down the middle as the keeper dives!")
                goals += 1
            else:
                print("Saved! The keeper stood their ground and caught it easily.")
                lives -= 1

        # 5. Invalid target number
        else:
            print("Invalid target! You kicked it out for a throw-in.")
            lives -= 1
main()