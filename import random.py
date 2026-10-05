"""
Number guessing game I made over the weekend for fun
There isn't much else to say lol

PS: There isn't much comments, dont use this code please.
"""
import os
import random
import time
from sys import exit
from pick import pick

# Colors (I used ai to generate the variables so I could use them without having to search through everything)
CLR_RED = "\033[31m"
CLR_GREEN = "\033[32m"
CLR_YELLOW = "\033[33m"
CLR_BLUE = "\033[34m"
CLR_MAGENTA = "\033[35m"
CLR_CYAN = "\033[36m"
CLR_WHITE = "\033[37m"
CLR_ORANGE = "\033[38;5;208m"
CLR_PINK = "\033[38;5;205m"
CLR_GRAY = "\033[90m"
CLR_RESET = "\033[0m"
 
num = 0 # The range of which the number will be generated from 0
guess_limit = 5 # The default limit of guesses
hint = True # whether to show a hint by default or not

# === Stats ===
matches_played = 0
won = 0
lost = 0

# == Menu Logo ==
ascii_m = f"""{CLR_CYAN}
 .S_sSSs     .S S.     sSSSSs   .S       S.     sSSs    sSSs    sSSs  
.SS~YS%%b   .SS SS.   d%%%%SP  .SS       SS.   d%%SP   d%%SP   d%%SP  
S%S   `S%b  S%S S%S  d%S'      S%S       S%S  d%S'    d%S'    d%S'    
S%S    S%S  S%S S%S  S%S       S%S       S%S  S%S     S%|     S%|     
S%S    d*S  S%S S%S  S&S       S&S       S&S  S&S     S&S     S&S     
S&S   .S*S   SS SS   S&S       S&S       S&S  S&S_Ss  Y&Ss    Y&Ss    
S&S_sdSSS     S S    S&S       S&S       S&S  S&S~SP  `S&&S   `S&&S   
S&S~YSSY      SSS    S&S sSSs  S&S       S&S  S&S       `S*S    `S*S  
S*S           S*S    S*b `S%%  S*b       d*S  S*b        l*S     l*S  
S*S           S*S    S*S   S%  S*S.     .S*S  S*S.      .S*P    .S*P  
S*S           S*S     SS_sSSS   SSSbs_sdSSS    SSSbs  sSS*S   sSS*S   
S*S           S*S      Y~YSSY    YSSP~YSSY      YSSP  YSS'    YSS'    
SP            SP                                                      
Y             Y                                                       
{CLR_RESET}"""

print(ascii_m, f"{CLR_MAGENTA}By: Devnix{CLR_RESET}")
time.sleep(3)

# PS: The box was made with ai (I'm not going to spend an hour designing boxes)

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    guesses_tracked = 0
    feedback_message = ""

    title = (
        "┌────────────────────────┐\n"
        "│       MAIN MENU        │\n"
        "└────────────────────────┘\n"
        " Use arrow keys to select:"
    )
    options = ["  ▶  Play Game", "  📊 View Stats", "  ❌ Exit"]

    option, index = pick(
        options, 
        title, 
        indicator=" ➜ ", 
    )

    if index == 1:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"{CLR_CYAN}┌──────────────────────────────────────┐{CLR_RESET}")
        print(f"{CLR_CYAN}│             PLAYER STATS             │{CLR_RESET}")
        print(f"{CLR_CYAN}├──────────────────────────────────────┤{CLR_RESET}")
        print(f"{CLR_CYAN}│{CLR_RESET}  Matches Played  : {CLR_WHITE}{matches_played:<18}{CLR_RESET}{CLR_CYAN}│{CLR_RESET}")
        print(f"{CLR_CYAN}│{CLR_RESET}  Matches Won     : {CLR_GREEN}{won:<18}{CLR_RESET}{CLR_CYAN}│{CLR_RESET}")
        print(f"{CLR_CYAN}│{CLR_RESET}  Matches Lost    : {CLR_RED}{lost:<18}{CLR_RESET}{CLR_CYAN}│{CLR_RESET}")
        print(f"{CLR_CYAN}└──────────────────────────────────────┘{CLR_RESET}")
        print(f"\n{CLR_GRAY}Returning to main menu in 5 seconds...{CLR_RESET}")
        time.sleep(5)
        continue
    elif index == 2:
        print(f"\n{CLR_RED}Exiting program... Good bye!{CLR_RESET}")
        time.sleep(1)
        exit()
    elif index == 0:
        hint = True
        guess_limit = 5
        
        title = (
            "┌────────────────────────┐\n"
            "│   SELECT DIFFICULTY    │\n"
            "└────────────────────────┘"
        )
        options = ["🟢 Easy (0-10)", "🟡 Normal (0-20)", "🟠 Hard (0-50, No Hints)", "🔴 Impossible (0-100, 3 Guesses)"]

        option, index = pick(
            options, 
            title, 
            indicator=" ➜ ", 
            default_index=1
        )

        print(f"\nSelected: {CLR_YELLOW}{option}{CLR_RESET}...")
        time.sleep(1)

        if index == 0:
            num = 10
        elif index == 1:
            num = 20
        elif index == 2:
            num = 50
            hint = False
        elif index == 3:
            num = 100
            hint = False
            guess_limit = 3

        random_num = random.randint(0, num)
        feedback_message = f"{CLR_CYAN}Guess a number between 0 and {num}!{CLR_RESET}"

        while True:
            try:
                os.system('cls' if os.name == 'nt' else 'clear')
                
                print(f"{feedback_message}\n{CLR_GRAY}{'=' * 50}{CLR_RESET}")
                
                if guesses_tracked >= guess_limit:
                    print(f"{CLR_RED} GAME OVER! You've reached your limit of guesses.{CLR_RESET}")
                    print(f"The correct number was: {CLR_GREEN}{random_num}{CLR_RESET}\n")
                    lost += 1
                    matches_played += 1
                    random_num = random.randint(0, num)
                    guesses_tracked = 0
                    print(f"{CLR_YELLOW}Generating a new number...{CLR_RESET}")
                    time.sleep(4)
                    continue
                attempts_left = guess_limit - guesses_tracked
                print(f"{CLR_GRAY}[Attempts Remaining: {attempts_left}]{CLR_RESET}\n")
                guess = input(f"{CLR_YELLOW}What's your guess? ('r' to return):{CLR_RESET} ")
                
                if guess.strip().lower() == "r":
                    print(f"\n{CLR_RED}Returning to main menu...{CLR_RESET}")
                    time.sleep(1.5)
                    break

                else:
                    guess = int(guess)
                    hint_ans = ""
                    if 0 <= guess <= num:
                        if guess == random_num:
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print(f"{CLR_GREEN} CORRECT! The number was {random_num}!{CLR_RESET}\n")
                            won += 1
                            matches_played += 1
                            random_num = random.randint(0, num)
                            guesses_tracked = 0
                            print(f"{CLR_YELLOW}Generating a new number...{CLR_RESET}")
                            time.sleep(3)
                        else:
                            guesses_tracked += 1
                            if hint:
                                if guess > random_num:
                                    hint_ans = f"{CLR_RED}Too high!{CLR_RESET}"
                                else:
                                    hint_ans = f"{CLR_BLUE}Too low!{CLR_RESET}"

                            feedback_message = f"{CLR_RED}Incorrect guess!{CLR_RESET} ({hint_ans})"
                    else:
                        feedback_message = f"{CLR_RED}Out of bounds!{CLR_RESET} Must be between 0 and {num}."

            except ValueError:
                feedback_message = f"{CLR_RED}Invalid input!{CLR_RESET} Please enter a whole number."

            except KeyboardInterrupt:
                print(f"\n{CLR_RED}Ending program...{CLR_RESET}")
                exit()
