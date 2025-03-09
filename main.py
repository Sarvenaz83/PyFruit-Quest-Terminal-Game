from src.game import Game

if __name__ == '__main__':
    game = Game()
    game.run()
    print("=== Fruit Loop Terminal Game ===")
    print("Controls: WASD to move | I: Inventory | Q: Quit")

    while True:
        try:
            game.display()
            cmd = input("Command:").strip().upper()

            if cmd in ["Q", "X"]:
                print("Thanks for playing!")
                break
            game.handle_input(cmd)
        except Exception as e:
            print(f"Error: {str(e)}")
            break