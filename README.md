# 🎮 Stone Paper Scissors Game

A simple and interactive **Stone Paper Scissors** game built using **Python** and **Streamlit**.

The game allows a user to play against the computer through a clean and user-friendly web interface.

## 🚀 Live Demo

Play the game online:

https://arpan-stone-paper-game.streamlit.app

## ✨ Features

- 🪨 Stone, 📄 Paper and ✂️ Scissors gameplay
- 🤖 Computer randomly selects a move
- 🏆 First player to reach 30 points wins
- ⭐ Each winning round gives 5 points
- 🤝 Draw gives no points
- 🔄 Reset Game option
- 🎨 Clean and responsive Streamlit interface
- 🌐 Available online through Streamlit Community Cloud

## 🎯 Game Rules

| Your Move | Computer Move | Result |
|---|---|---|
| 🪨 Stone | ✂️ Scissors | You win +5 |
| 📄 Paper | 🪨 Stone | You win +5 |
| ✂️ Scissors | 📄 Paper | You win +5 |
| Same Move | Same Move | Draw +0 |
| 🪨 Stone | 📄 Paper | Computer +5 |
| 📄 Paper | ✂️ Scissors | Computer +5 |
| ✂️ Scissors | 🪨 Stone | Computer +5 |

The first player to reach **30 points** wins the game.

## 🛠️ Technologies Used

- Python
- Streamlit
- Random module
- HTML/CSS for UI customization

## 📁 Project Structure

```text
stone-paper-scissors-game/
│
├── app.py
├── game.py
├── requirements.txt
└── README.md
