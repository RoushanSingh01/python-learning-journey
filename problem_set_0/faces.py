def convert(x):
    "converts :) to 🙂 and :( to 🙁."

    y = x.replace(":)" , "🙂").replace(":(", "🙁")
    return y

def main():
    user_input = input("input: ")
    result = convert(user_input)
    print(result)

main()