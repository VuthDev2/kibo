"""Print basic system details for a Kibo-RPC environment check."""

import platform
import sys


TEAM_NAME = "[YOUR TEAM NAME]"


def main():
    print("=== Kibo-RPC Environment Check ===")
    print(f"Team: {TEAM_NAME}")
    print(f"Operating system: {platform.system()} {platform.release()}")
    print(f"Platform: {platform.platform()}")
    print(f"Machine architecture: {platform.machine()}")
    print(f"Python version: {sys.version}")
    print("Environment OK!")


if __name__ == "__main__":
    main()
