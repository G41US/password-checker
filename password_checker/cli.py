import sys
from .checker import check_strength

def main():
    if len(sys.argv) != 2:
        print("Usage: python -m password_checker.cli <password>")
        sys.exit(1)

    password = sys.argv[1]
    result = check_strength(password)
    print(f"Strength: {result['strength']}")
    if result['feedback']:
        print("Suggestions:")
        for f in result['feedback']:
            print(f" - {f}")

if __name__ == "__main__":
    main()
