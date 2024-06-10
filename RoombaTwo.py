from statemachine import StateMachine, State
class RoombaTwo(StateMachine):
    
    PowerOff = State(initial = True)
    RoamingSlow = State()
    RoamingAverage = State()
    RoamingFast = State()
    Rotate = State()
    
    rotatecycle = (
        Rotate.from_(RoamingSlow, RoamingAverage, RoamingFast)
        )
    
    exitrotate = (
        Rotate.to(RoamingAverage)
        )
    
    to_PowerOff = RoamingSlow.to(PowerOff) | RoamingAverage.to(PowerOff) | RoamingFast.to(PowerOff) | Rotate.to(PowerOff)
    to_RoamingSlow = PowerOff.to(RoamingSlow) | RoamingAverage.to(RoamingSlow) | RoamingFast.to(RoamingSlow)
    to_RoamingAverage = PowerOff.to(RoamingAverage) | RoamingSlow.to(RoamingAverage) | RoamingFast.to(RoamingAverage)
    to_RoamingFast = PowerOff.to(RoamingFast) | RoamingSlow.to(RoamingFast) | RoamingAverage.to(RoamingFast)
    
    def on_enter_Rotate(self):
        velocity = 0
        print("\nObject detected. Velocity set to " + str(velocity) + ". Rotating 90 degrees.")
        print("\nRotated 90 degrees. Automatically transitioning to RoamingAverage")
        camera = False
        sensor = 1.0
        if camera == True or sensor <= 0.25:
            sm.send("rotatecycle")
        else:
            sm.send("exitrotate")
            
        
    def on_enter_PowerOff(self):
        velocity = 0
        print("\nPower off. Velocity = " + str(velocity))
    
    def on_enter_RoamingSlow(self):
        velocity = 4
        camera = False
        sensor = 1.0
        print("\nMoving at a slow speed. Velocity = " + str(velocity))
        if camera == True or sensor <= 0.25:
            sm.send("rotatecycle")
            
    def on_enter_RoamingAverage(self):
        velocity = 6
        camera = False
        sensor = 1
        print("\nMoving at an average speed. Velocity = " + str(velocity))
        if camera == True or sensor <= 0.25:
            sm.send("rotatecycle")
            
    def on_enter_RoamingFast(self):
        velocity = 8
        camera = True
        sensor = 4.0
        print("\nMoving at a fast speed. Velocity = " + str(velocity))
        if camera == True or sensor <= 0.25:
            sm.send("rotatecycle")
        
sm = RoombaTwo()

def trigger_transition(state_machine, state_name):
    if state_name == 'PowerOff':
        state_machine.to_PowerOff()
    elif state_name == 'RoamingSlow':
        state_machine.to_RoamingSlow()
    elif state_name == 'RoamingAverage':
        state_machine.to_RoamingAverage()
    elif state_name == 'RoamingFast':
        state_machine.to_RoamingFast()
    else:
        print("Invalid state")
        
        
img_path = "/Users/isabel/.spyder-py3/test4.png"   

sm._graph().write_png(img_path) 

while True:
    print(f"\nCurrent state: {sm.current_state}")
    user_input = input("Enter the state to transition to: PowerOff, RoamingSlow, RoamingAverage, RoamingFast, or to exit the program enter 'exit' (cap sensitive!) \n")
    if user_input == 'exit':
        break
    trigger_transition(sm, user_input)
    