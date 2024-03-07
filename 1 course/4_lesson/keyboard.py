def keyboard(buttons, push):
    for i in push:
        buttons[i - 1] = buttons[i - 1] - 1
    print(buttons)
    for button in buttons:
        print("YES" if button < 0 else "NO")
input()
l1 = list(map(int, input().split()))
input()
l2 = list(map(int, input().split()))
keyboard(l1, l2)