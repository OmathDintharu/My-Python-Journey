import time

def activate_project():
    user_name = "Omath"
    project_name = "Mission 2034"
    
    print(f"--- [ {project_name} SYSTEM INITIALIZING ] ---")
    time.sleep(1)
    
    print(f"System: Checking Operator Identity...")
    time.sleep(1)
    
    if user_name == "Omath":
        print(f"System: Identity Confirmed. Welcome, Creator {user_name}.")
        print("System: Syncing with Quantum Frequency...")
        
        # Loading progress bar logic
        for i in range(1, 6):
            print(f"Syncing... {i*20}%")
            time.sleep(0.5)
            
        print(f"\n[ SUCCESS ] {project_name} is now ACTIVE.")
        print("Remember Omath: 'The world doesn't know about us.' Keep it secret.")
    else:
        print("Access Denied: Unknown Operator.")

activate_project()
