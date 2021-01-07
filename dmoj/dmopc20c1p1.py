for _ in range(int(input())):
    quiz = input()

    math = "M" in quiz
    comp = "C" in quiz

    if math and comp:
        print("NEGATIVE MARKS")
    elif math or comp:
        print("FAIL")
    else:
        print("PASS")
