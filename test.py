import keyboard

key_press = keyboard.read_key(suppress=True)

keyboard.on_press_key()
def main():
    while True:
        if key_press:
            print("success")

if __name__ == '__main__':
    main()
