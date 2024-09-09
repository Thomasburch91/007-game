print('''
   ,a8888a,       ,a8888a,  888888888888  
 ,8P"'  `"Y8,   ,8P"'  `"Y8,        ,8P'  
,8P        Y8, ,8P        Y8,      d8"    
88          88 88          88    ,8P'     
88          88 88          88   d8"       
`8b        d8' `8b        d8' ,8P'        
 `8ba,  ,ad8'   `8ba,  ,ad8' d8"          
   "Y8888P"       "Y8888P"  8P'           
   ''')

print("Mission: Stop the Villain's Plan")
print("You are Agent 007, tasked with stopping a global villain from launching a doomsday weapon. \nYour mission is to infiltrate the villain's island fortress and disable the weapon.")
print("Do you use stealth and sneak through the jungle or charge in by boat?")

#first choice
choice = input("Do you use stealth and sneak through the jungle or charge in by boat? (Type 'jungle' or 'boat'): ").lower()

if choice == 'jungle':
    print("\nSneak Through the Jungle:")
    print("You move through the thick underbrush, dodging patrols. \n You come across a guard’s watchtower.")
#1 tower choice
    tower_choice = input("Do you take him out silently or bypass the tower? (Type 'silent' or 'bypass'): ").lower()
    if tower_choice == 'silent':
        print("\nYou silently neutralize the guard and move forward, gaining across to a hidden entrance into the base. Mission continues!")
        print("\nInside the Enemy Base:")
        print("You’ve infiltrated the enemy base. You see two paths: one leading to the security control room and the other to the power generator.")
#2 Enemy base choice
        enemy_base_choice = input("Do you sabotage the security system or disable the power grid? (Type 'sabotage' or 'disable'): ").lower()
        if enemy_base_choice == 'sabotage':
            print("\nYou disable the cameras and guards' alarms, giving you an advantage. You head toward the weapons launch room.")
            print("\nReaching the Weapons Room:")
            print("You reach the weapons control room where the villain's countdown to launch is in progress.")
#3 Weapon choice
            weapons_room_choice = input("Do you attempt to hack the computer system or plant explosives on the machinery? (Type 'hack' or 'plant'): ").lower()
            if weapons_room_choice == 'plant':
                print("\nYou plant the explosives successfully and make your way to the villain's lair.")
                print("\nConfronting the Villain:")
                print("You enter the villain's headquarters, where the mastermind is waiting. He’s guarded by two henchmen.")
#4 Confronting choice
                confronting_choice = input("Do you engage in a shootout or try to negotiate? (Type 'shootout' or 'negotiate'): ").lower()
                if confronting_choice == 'shootout':
                    print("\nYou take down the henchmen, but the villain escapes to the launch room. Continue.")
                    print("\nFinal Confrontation:")
                    print("The villain, realizing his plan is foiled, tries to flee.")
#5 Final Confrontation
                    final_confrontation = input("Do you chase him on foot or set a trap to catch him? (Type 'chase' or 'trap'): ").lower()
                    if final_confrontation == 'chase':
                        print("\nYou chase the villain through the base and capture him just as he's about to escape. Mission Success.")
# End of game

                        print("\nAgent 007, you have successfully foiled the villain's plans and saved the world from disaster.")
                        print("\nMISSION COMPLETE!")
                    elif final_confrontation == 'trap':
                        print("\nThe villain falls into your cleverly set trap and is captured by your team. Mission Success.")
                        print("\nAgent 007, you have successfully foiled the villain's plans and saved the world from disaster.")
                        print("\nMISSION COMPLETE!")
                elif confronting_choice == 'negotiate':
                    print("\nYou stall the villain just long enough to trigger your explosives remotely, sabotaging his plan. Mission Success.")
            elif weapons_room_choice == 'hack':
                print("\nYou attempt to hack the countdown but trigger a fail-safe. Game Over.")
        elif enemy_base_choice == 'disable':
            print("\nYou cut the power, but the emergency backup system kicks in. You're detected by the guards. Game Over.")
    elif tower_choice == 'bypass':
        print("\nYou attempted to sneak past but you were spotted by another guard. Game Over.")
    else:
        print("Invalid choice. Mission failed.")
elif choice == 'boat':
    print("\nCharging in by Boat")
    print("You decide to charge the fortress by boat, creating a diversion.\n As you approach, you see a patrol boat headed your way.")
    boat_choice = input("Do you hide underwater or engage in a chase? (Type 'hide' or 'engage'): ").lower()
#1 Boat choice
    if boat_choice == 'hide':
        print("\nYou dive into the water just before the patrol arrives, using your mini-oxygen tank to avoid detection. You sneak into the base from the dock.")
        print("\nInside the Enemy Base:")
        print("You’ve infiltrated the enemy base. You see two paths: one leading to the security control room and the other to the power generator.")
#2 Enemy base choice
        enemy_base_choice = input("Do you sabotage the security system or disable the power grid? (Type 'sabotage' or 'disable'): ").lower()
        if enemy_base_choice == 'sabotage':
            print("\nYou disable the cameras and guards' alarms, giving you an advantage. You head toward the weapons launch room.")
            print("\nReaching the Weapons Room:")
            print("You reach the weapons control room where the villain's countdown to launch is in progress.")
#3 Weapon choice
            weapons_room_choice = input("Do you attempt to hack the computer system or plant explosives on the machinery? (Type 'hack' or 'plant'): ").lower()
            if weapons_room_choice == 'plant':
                print("\nYou plant the explosives successfully and make your way to the villain's lair.")
                print("\nConfronting the Villain:")
                print("You enter the villain's headquarters, where the mastermind is waiting. He’s guarded by two henchmen.")
#4 Confronting choice
                confronting_choice = input("Do you engage in a shootout or try to negotiate? (Type 'shootout' or 'negotiate'): ").lower()
                if confronting_choice == 'shootout':
                    print("\nYou take down the henchmen, but the villain escapes to the launch room. Continue.")
                    print("\nFinal Confrontation:")
                    print("The villain, realizing his plan is foiled, tries to flee.")
#5 Final Confrontation
                    final_confrontation = input("Do you chase him on foot or set a trap to catch him? (Type 'chase' or 'trap'): ").lower()
                    if final_confrontation == 'chase':
                        print("\nYou chase the villain through the base and capture him just as he's about to escape. Mission Success.")
# End of game
                        print("\nAgent 007, you have successfully foiled the villain's plans and saved the world from disaster.")
                        print("\nMISSION COMPLETE!")
                    elif final_confrontation == 'trap':
                        print("\nThe villain falls into your cleverly set trap and is captured by your team. Mission Success.")
                        print("\nAgent 007, you have successfully foiled the villain's plans and saved the world from disaster.")
                        print("\nMISSION COMPLETE!")
                elif confronting_choice == 'negotiate':
                    print("\nYou stall the villain just long enough to trigger your explosives remotely, sabotaging his plan. Mission Success.")
            elif weapons_room_choice == 'hack':
                print("\nYou attempt to hack the countdown but trigger a fail-safe. Game Over.")
    elif boat_choice == 'engage':
        print("\nYou speed away, but the patrols boat is faster. You're captured. GAME OVER.")
    else:
        print("Invalid choice. Mission failed.")



