import emoji as emo

s = str(input("input: ").strip())
print(f"output: {emo.emojize(s, language='alias')}")
