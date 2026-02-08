# 🤖 Discord Portfolio Bot
[![Python Version](https://img.shields.io/badge/python-3.13-blue.svg)](https://python.org)
[![Discord.py](https://img.shields.io/badge/library-discord.py-7289DA.svg)](https://discordpy.readthedocs.io/)

A professional, asynchronous Discord bot built to showcase API integration and system monitoring capabilities. This project demonstrates secure credential management and event-driven architecture.

## 🛠 Technologies Used
* **Python 3.13:** Leveraging the latest stable release features.
* **Discord.py:** For high-level interface with the Discord API.
* **Python-Dotenv:** Managing sensitive API keys via environment variables (Security Best Practice).
* **Asynchronous Programming:** Non-blocking event loops for high performance.

## 🚀 Features
* **Real-time Connectivity:** Instant response via Discord Gateway.
* **System Metrics:** Commands to display bot status and uptime.
* **Secure Architecture:** Zero-exposure of API tokens using `.env` configurations.
* 
## ☁️ Cloud Architecture & Deployment
- **Hosting:** Deployed on **Render** as a Web Service.
- **24/7 Uptime:** Implemented a **Flask-based heartbeat** server to prevent service suspension.
- **CI/CD:** Integrated with GitHub for automatic deployments upon every commit to the `main` branch.
- **Global Availability:** Hosted in the **Singapore** region for optimized latency in Southeast Asia.
- 
## ⚙️ Setup & Installation
1. Clone the repository: `git clone https://github.com/King-of-javascript/discord-portfolio-bot.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Create a `.env` file and add your `DISCORD_TOKEN`.
4. Run the bot: `python main.py`
