import time

from coffee.interactions import enter_input

def keep_alive(time_between_actions_in_seconds: int = 300, perform_n_times: int = 99999999):

    for i in range(perform_n_times):
        print("wiggle")
        enter_input("numlock")
        enter_input("numlock")
        time.sleep(time_between_actions_in_seconds)    
    