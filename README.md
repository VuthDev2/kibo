# 7th Kibo-RPC - Team INFINITE

Starter repository for Team INFINITE's 7th Kibo-RPC training and development environment checks.

## Team members

| Name | GitHub | Role |
|---|---|---|
| Monyroth Lim | Not provided | Team Lead |
| Kry Saravuth | Not provided | Software Developer |
| Sour Chansokpanha (Lavinha San) | Not provided | Software Developer |
| Puth Poygerry | Not provided | Navigation & Control |
| Khoun Visal | Not provided | Systems Integration |
| Preoung Nyudampanha | Not provided | Testing & QA |

## Contents

- `verify_env.py` — Displays the operating system, platform, architecture, and Python version.
- `test.cpp` — Checks that a C++ compiler can build and run a basic program.
- `watchdog.py` — Demonstrates battery monitoring in a simulated 10-waypoint navigation run; it does not control a robot.
- `.gitignore` — Excludes generated build files and local editor and operating-system files.

## Workflow

Do not commit directly to `main`. Create a feature branch for each change:

```bash
git checkout -b feature/<short-description>
```

Commit your changes on that branch, push it to GitHub, and open a Pull Request for team review before merging.

## How to run

Requirements: Python 3 and `g++`. From the repository directory, run:

```bash
python3 verify_env.py
python3 watchdog.py
g++ test.cpp -o test
./test
```

The watchdog output varies between runs because battery loss is randomized.
