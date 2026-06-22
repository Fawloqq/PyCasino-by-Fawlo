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
| 🟡 | **Slot Machine** | Classical 3-reel slot mechanism with customizable betting and multipliers. |
| 🔴 | **Blackjack** | Dynamic card-dealing logic against a virtual dealer. |

*Legend: 🟢 Completed | 🟡 In Progress | 🔴 Planned*

## 📦 Getting Started

### Prerequisites
- Python 3.10 or higher installed.
- No external dependencies required (built entirely using Python's native standard libraries like `json` and `os`).

### Installation & Execution

1. **Clone the repository:**
```bash
   https://github.com/Fawloqq/PyCasino-by-Fawlo.git