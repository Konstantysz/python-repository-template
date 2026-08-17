import re
import sys


def main():
    # Copier exposes answers as top-level variables in globals()
    package_name = globals().get("package_name", "")
    if not re.match(r"^[a-z_][a-z0-9_]*$", package_name):
        print("Package name must be snake_case (lowercase letters, digits, and underscores).")
        sys.exit(1)


if __name__ == "__main__":
    main()
