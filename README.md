#I don t know how to copy paste stuff
#include <iostream>
#include <string>

class RoombaTwo {
public:
    enum State {
        PowerOff,
        RoamingSlow,
        RoamingAverage,
        RoamingFast,
        Rotate
    };

    RoombaTwo() : current_state(PowerOff) {}

    void transition(State next_state) {
        if (next_state != current_state) {
            exit_state();
            enter_state(next_state);
            current_state = next_state;
        }
    }

    State get_current_state() const {
        return current_state;
    }

private:
    State current_state;

    void enter_state(State state) {
        switch (state) {
            case PowerOff:
                std::cout << "\nPower off. Velocity = 0\n";
                break;
            case RoamingSlow:
                std::cout << "\nMoving at a slow speed. Velocity = 4\n";
                break;
            case RoamingAverage:
                std::cout << "\nMoving at an average speed. Velocity = 6\n";
                break;
            case RoamingFast:
                std::cout << "\nMoving at a fast speed. Velocity = 8\n";
                break;
            case Rotate:
                int velocity = 0;
                std::cout << "\nObject detected. Velocity set to " << velocity << ". Rotating 90 degrees.\n";
                std::cout << "\nRotated 90 degrees. Automatically transitioning to RoamingAverage\n";
                bool camera = false;
                double sensor = 1.0;
                if (camera || sensor <= 0.25) {
                    transition(RoamingAverage);
                }
                break;
        }
    }

    void exit_state() {
        // Add any exit logic if needed
    }
};

int main() {
    RoombaTwo roomba;

    while (true) {
        std::cout << "\nCurrent state: " << roomba.get_current_state() << std::endl;
        std::cout << "Enter the state to transition to: PowerOff, RoamingSlow, RoamingAverage, RoamingFast, or to exit the program enter 'exit' (case sensitive!)" << std::endl;

        std::string user_input;
        std::cin >> user_input;

        if (user_input == "exit") {
            break;
        } else if (user_input == "PowerOff") {
            roomba.transition(RoombaTwo::PowerOff);
        } else if (user_input == "RoamingSlow") {
            roomba.transition(RoombaTwo::RoamingSlow);
        } else if (user_input == "RoamingAverage") {
            roomba.transition(RoombaTwo::RoamingAverage);
        } else if (user_input == "RoamingFast") {
            roomba.transition(RoombaTwo::RoamingFast);
        } else {
            std::cout << "Invalid state" << std::endl;
        }
    }

    return 0;
}
