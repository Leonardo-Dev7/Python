Pop_A = (80000)
Pop_B = (200000)
Anos = (0)

while True:
    Anos += 1
    Pop_A *= 1 + (3 / 100)
    Pop_B *= 1 + (1.5 / 100)
    if Pop_A >= Pop_B:
        print(
            f"Em {Anos} anos a população A a B."
            f"\nTendo na população A {Pop_A:.0f} habitantes e na B {Pop_B:.0f}."
        )
        break