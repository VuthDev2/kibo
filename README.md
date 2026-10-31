# 7th Kibo-RPC - Team [YOUR TEAM NAME]

A starter repository for verifying the development environment and practicing the team's Kibo-RPC workflow.

## Team members

| Name | GitHub | Role |
|---|---|---|
| TODO | TODO | TODO |
| TODO | TODO | TODO |
| TODO | TODO | TODO |

## Contents

- `verify_env.py` — Displays system and Python details to check the environment.
- `test.cpp` — Confirms that the C++ compiler can build and run a basic program.
- `watchdog.py` — Simulates battery monitoring across navigation waypoints.
- `.gitignore` — Excludes generated build files and local editor/OS files.
- `README.md` — Team information, workflow, and run instructions.

## Workflow

Never commit directly to `main`. Create a feature branch for your changes:

```bash
git checkout -b feature/<name>
```

Push your branch and open a Pull Request for review before merging.

## How to run

From the repository directory, run the Python programs and compile/run the C++ program:

```bash
python3 verify_env.py
python3 watchdog.py
g++ test.cpp -o test
./test
```
