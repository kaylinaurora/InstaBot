<p align="center">
  <img src="https://i.ibb.co/R0pSFvK/Insta-Bot-with-text-transparent.png" width="400" alt="project-logo">
</p>
<p align="center">
    <h1 align="center">kaylinaurora/InstaBot</h1>
</p>
<p align="center">
	<!-- local repository, no metadata badges. -->
<p>
<p align="center">
		<em>A simple Discord bot developed in Python</em>
</p>
<p align="center">
	<img src="https://img.shields.io/badge/Discord-5865F2.svg?style=default&logo=Discord&logoColor=white" alt="Discord">
	<img src="https://img.shields.io/badge/Python-3776AB.svg?style=default&logo=Python&logoColor=white" alt="Python">
</p>

<br><!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary><br>

- [ Overview](#overview)
- [ Features](#features)
- [ Repository Structure](#repository-structure)
- [ Modules](#modules)
- [ Getting Started](#getting-started)
  - [ Installation](#installation)
  - [ Usage](#usage)
- [ Project Roadmap](#project-roadmap)
</details>
<hr>

##  Overview

Hi! 👋 I'm InstaBot! I help combat shitty IG Reel integration by utilizing a service called DDinstagram 📸

---

##  Features

- Send any TikTok video or IG Reel URL as a *server message* to automagically make the video playable within Discord
  - **InstaBot** will replace the domain with `ddinstagram` or `vxtiktok`, accordingly
- If conversion fails, you can retry by reacting to any message from **InstaBot** with a 👎 emoji
  - **InstaBot** will try removing the existing message and re-sending the link (YMMV)

---

##  Repository Structure

```sh
└── ./
    ├── InstaBot.py
    └── requirements.txt
```

---

##  Modules

<details open><summary>Modules</summary>

| Module | Version |
| --- | --- |
| discord.py | <code>2.3.2</code> |
| python-dotenv | <code>1.0.1</code> |

</details>

---

##  Getting Started

**System Requirements:**

* **Python**: `version 3.10.10` (known working, YMMV on other versions)

###  Installation


> 1. Navigate to the repo directory:
>
> ```console
> $ cd /path/to/InstaBot
> ```
>
> 2. Install the requirements:
> ```console
> $ pip install -r requirements.txt
> ```
>
> 3. Create a .env file and add your bot token from the Discord Developer Portal:
> ```console
> $ nvim .env
> ```
> ```console
> DISCORD_BOT_TOKEN={your_token_here}

###  Usage

> Run the bot
> ```console
> $ python InstaBot.py
> ```


---

##  Project Roadmap

- [ ] `Add server logging`
- [ ] `Add capability for local media processing, toggled via config JSON/YAML`
---

[**Return**](#overview)

---
