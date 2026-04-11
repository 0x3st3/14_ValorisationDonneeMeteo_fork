import subprocess
import sys


def run(command: list[str]) -> None:
    print(f"Running: {' '.join(command)}", flush=True)
    subprocess.run(command, check=True)


def main() -> None:
    run(["uv", "run", "python", "manage.py", "migrate", "--noinput"])
    run(["uv", "run", "python", "manage.py", "collectstatic", "--noinput"])
    subprocess.run(sys.argv[1:], check=True)


if __name__ == "__main__":
    main()
