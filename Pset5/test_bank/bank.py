b = input("Greeting: ").strip().lower()

if b.startswith("hello"):
    a = 0
elif b.startswith("h"):
    a = 20
else:
    a = 100

print(f"${a}")