# 🚀 FounderAI Bot: Agentic Thought Leadership

A fully autonomous AI agent that manages an X (Twitter) presence with the persona of a high-signal Tech Founder. Powered by **Gemini 3 Flash** and **GitHub Actions**, this bot executes a "Blind Authority" strategy to build a brand in the Agentic AI, FinTech, and Future of Work sectors.

---

## 🧠 The Philosophy
Most bots sound like bots. **FounderAI** is designed to sound like a builder. It avoids "AI fluff" and focus on contrarian, execution-heavy insights. 

- **Autonomous:** Runs on a 3-hour pulse via GitHub Actions.
- **Cost-Effective:** Operates 100% on the **Free Tiers** of X API and Google Gemini.
- **Context-Aware:** Uses a hardcoded "Interest Profile" to ensure brand consistency.

---

## 🛠️ Tech Stack
- **LLM:** [Google Gemini 3 Flash](https://ai.google.dev/) (2025 Model)
- **Framework:** [Tweepy](https://www.tweepy.org/) (X API v2)
- **Automation:** GitHub Actions (Cron-based scheduling)
- **Language:** Python 3.11

---

## ⚡ Quick Start

### 1. Prerequisites
- An **X Developer Account** (Free Tier is sufficient).
- A **Google AI Studio API Key**.

### 2. GitHub Secrets Setup
To keep your credentials safe, add the following to your GitHub Repository Secrets (`Settings > Secrets and variables > Actions`):

| Secret Name | Source |
| :--- | :--- |
| `X_API_KEY` | X Dev Portal (Consumer Key) |
| `X_API_SECRET` | X Dev Portal (Consumer Secret) |
| `X_ACCESS_TOKEN` | X Dev Portal (Generated with R/W permissions) |
| `X_ACCESS_TOKEN_SECRET` | X Dev Portal (Generated with R/W permissions) |
| `GEMINI_API_KEY` | Google AI Studio |

### 3. Deployment
1. **Fork this repository.**
2. **Enable Actions:** Go to the `Actions` tab and click "I understand my workflows, go ahead and enable them."
3. **Customize your persona:** Edit the `INTEREST_PROFILE` in `main.py` to match your own niche.

---

## 🤖 Strategy: Blind Authority Mode
Due to X Free Tier restrictions on reading other users' timelines, this bot operates in **Thesis Mode**:
1. **Wake up:** Triggered every 3 hours by a GitHub Cron job.
2. **Brainstorm:** Gemini 3 Flash generates a high-signal founder insight based on your `INTEREST_PROFILE`.
3. **Ship:** The insight is posted to X via the v2 API.
4. **Sleep:** The instance shuts down to save resources.

---

## 🤝 Contributing
Found a way to optimize the prompts? Want to add an RSS news-feed trigger? Contributions are welcome! 

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git checkout origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License
Distributed under the MIT License. See `LICENSE` for more information.

---
**Built with ☕ and Agents by NotShubham1112**
