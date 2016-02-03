
#console.log("\033[0;34mINX\033[3DFO\033[0m\n");
import sys, tty, termios

def main():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)

    player_one = 0
    player_two = 0

    try:
        tty.setraw(sys.stdin.fileno())
        while True:
            ch = sys.stdin.read(1)
            if ch == "q":
                return
            elif ch == "n":
                player_one += 1
            elif ch == "j":
                player_one -= 1
            elif ch == "m":
                player_two += 1
            elif ch == "k":
                player_two -= 1

            draw(player_one, player_two)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

HEIGHT = 25
WIDTH = 80
PADDLE_HEIGHT = 3

def draw(position_one, position_two):
    view = new_view()
    for i in range(PADDLE_HEIGHT):
        view[position_one + i][0] = "x"
        view[position_two + i][WIDTH - 1] = "x"

    sys.stdout.write("".join(["".join(row) + "\r\n" for row in view]))
    sys.stdout.write("\033[" + str(HEIGHT) + "A")

def new_view():
    view = []
    for h in range(HEIGHT):
        row = [" "] * WIDTH
        view.append(row)
    return view

if __name__ == "__main__":
    main()
