from src.loop import GameLoop


def main():
    with GameLoop() as loop:
        loop.run()


if __name__ == "__main__":
    main()
