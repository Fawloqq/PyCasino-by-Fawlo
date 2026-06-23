# 🎰 Python Casino Simulator

A lightweight, object-oriented Casino Simulator built with Python. Features a robust user registration and login authentication system, alongside persistent local data storage powered by dynamic JSON routing.

## 🚀 Key Features

- **🔐 User Authentication:** Secure sign-up and login systems handling duplicate names, credentials verification, and unique user tracking.
- **💾 Local JSON Database:** Automated database generation (`users-data.json`) upon the first boot. Built using dynamic absolute pathing to completely eliminate `FileNotFoundError` issues regardless of the terminal's active directory.
- **💰 State Persistence:** Automatically tracks and saves player data, including wallet balance (`balance`), unique `id`, and total `games_played`.

## 🛠️ Roadmap & Game Modules

| Status | Feature / Game | Description |
| :---: | :--- | :--- |
| 🟢 | **Account System** | User sign-up, secure login, and JSON state persistence. |
| 🟢 | **Account Manager** | In-game options to load balance, change passwords, and safely delete accounts. |
| 🟢 | **Slot Machine** | Classical 3-reel slot mechanism with customizable betting and multipliers. |
| 🟢 | **Blackjack** | Dynamic card-dealing logic against a virtual dealer. |
| 🟢 | **Roulette** | Multiple betting options including colors, even/odd, dozens, and specific numbers. |
| 🟢 | **Robust Error Handling** | Crash-proof main loop with seamless input validation and exception catching. |
| 🔴 | **Automated Testing** | Comprehensive unit tests using `unittest` and CI/CD integration via GitHub Actions. |
| 🔴 | **Texas Hold'em Poker** | Advanced multi-round card game with AI opponents. |

*Legend: 🟢 Completed | 🟡 In Progress | 🔴 Planned*

## 📦 Getting Started

### Prerequisites
- GIT
- Python 3.10 or higher installed.
- No external dependencies required (built entirely using Python's native standard libraries like `json` and `os`).

### Installation & Execution

1. ***Clone the repository:***
```bash
git clone https://github.com/Fawloqq/PyCasino-by-Fawlo.git
```
2. ***Navigate to the project directory:***

In terminal:
```bash
cd PyCasino-by-Fawlo/app
```
 3. ***Run file:***

On Mac/Linux in terminal:
```bash
python3 main.py
```
On Windows in terminal:
```bash
python main.py
```