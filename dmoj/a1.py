for i in range(1, int(input()) + 1):
    char, *text = input().split(" ")

    char = int(char)
    text = " ".join(text)

    print(i, text[: char - 1] + text[char:])
