import sys
from getpass import getpass
from .checker import check_strength

def main():
    if len(sys.argv) > 2:
        print("Usage: python -m password_checker.cli [password]")
        sys.exit(1)

    # Typing it at the hidden prompt keeps the password out of shell history and the process list.
    password = sys.argv[1] if len(sys.argv) == 2 else getpass("Password to check (hidden): ")
    result = check_strength(password)
    print(f"Strength: {result['strength']}")
    if result['feedback']:
        print("Suggestions:")
        for f in result['feedback']:
            print(f" - {f}")

if __name__ == "__main__":
    main()
