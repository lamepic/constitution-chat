import dotenv

from indexing import generate_response

dotenv.load_dotenv()


def main():
    while True:
        prompt = input("Enter question: ")
        answer = generate_response(prompt)
        print(answer)
        print()


if __name__ == "__main__":
    main()
