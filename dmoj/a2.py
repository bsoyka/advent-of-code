print("Ready")

while True:
    text = input()

    if text == "  ":
        break

    if text in {"bd", "db", "pq", "qp"}:
        print("Mirrored pair")
    else:
        print("Ordinary pair")
