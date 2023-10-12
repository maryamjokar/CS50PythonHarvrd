a = ["42", "forty-two", "forty two"]
q = (
    input(
        "what is  the answer to the Great Question of Life, the Universe and Everything? "
    )
    .strip()
    .lower()
)

if q in a:
    print("Yes")
else:
    print("No")
