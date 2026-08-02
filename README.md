# 🎮 Rock · Paper · Scissors — Battle Arena

<div align="center">

**A neon-drenched, streak-chasing take on the classic hand game — built entirely in Streamlit.**

![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-4ade80?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-7873f5?style=for-the-badge)

### 🔴 [**Play the Live Demo →**](https://usmani-rps.streamlit.app/)

Crafted with ♥ by **Mohd Faizan Umani**

</div>

---

## ✨ Overview

Forget the boring terminal version — this is Rock · Paper · Scissors reimagined as a **glassy, gradient-lit mini arcade** that lives right in your browser. Best of 3 wins the match, streaks get called out with a 🔥 badge, and every round animates in with its own win/lose/tie banner.

## 🚀 Features

| | |
|---|---|
| 🎨 **Modern dark UI** | Gradient title, glassmorphism score cards, and a deep-space background |
| ⚡ **Instant feedback** | Animated win / lose / tie banners after every round |
| 🔥 **Win streak tracking** | A glowing streak badge appears once you're 2+ rounds deep |
| 🏆 **Best-of-3 matches** | First to 3 wins takes the match, with a dedicated match-over screen |
| 🕓 **Round history** | See your last 8 rounds at a glance with color-coded outcomes |
| 📱 **Fully responsive** | Compact and tidy on mobile, roomy and bold on desktop |
| 🎈 **Victory celebration** | Balloons on a match win, because why not |

## 🖥️ Tech Stack

- **[Streamlit](https://streamlit.io/)** — UI framework & app runtime
- **Python 3.9+** — game logic and state management
- **Custom CSS** — gradients, glassmorphism, responsive grid layout, and animations, all hand-tuned on top of Streamlit's defaults

## 📦 Installation

```bash
# Clone or download this repo, then install the one dependency:
pip install streamlit
```

## ▶️ Running the Game

### Option 1 — Play instantly (no install needed)

👉 **[usmani-rps.streamlit.app](https://usmani-rps.streamlit.app/)**

### Option 2 — Run it locally

```bash
streamlit run rps_game.py
```

Streamlit will open the game automatically in your default browser at `http://localhost:8501`. If it doesn't, just click the link printed in your terminal.

## 🕹️ How to Play

1. Hit **🪨 Rock**, **📄 Paper**, or **✂️ Scissors** to lock in your move.
2. The computer picks at random — the result appears instantly with an animated banner.
3. Win **3 rounds** before the computer does to take the match.
4. Chain wins together to trigger the **🔥 win streak badge**.
5. Hit **Play Again** to start a fresh match, or **Reset Match** anytime mid-game.

## 🗂️ Project Structure

```
.
├── rps_game.py     # The entire game — UI, styling, and logic in one file
└── README.md       # You're reading it
```

## 🎯 Roadmap Ideas

- [ ] Sound effects on win/lose
- [ ] Global leaderboard via persistent storage
- [ ] Multiplayer mode (challenge a friend)
- [ ] Light theme toggle
- [ ] Rock-Paper-Scissors-Lizard-Spock variant

## 📄 License

Released under the **MIT License** — free to use, modify, and share.

---

<div align="center">

Made with ♥ by **Mohd Faizan Umani** · *Fi-Amanillah*

</div>
