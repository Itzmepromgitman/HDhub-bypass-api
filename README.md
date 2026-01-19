<blockquote>

# 🎬 HDHub Bypass API ⚡

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white"/>
  <img src="https://img.shields.io/badge/Vercel-000000?style=for-the-badge&logo=vercel&logoColor=white"/>
</p>

<p align="center">
  <b>🔥 Automated link bypass & direct download extraction for HDHub 🔥</b>
</p>

<p align="center">
  <i>No more clicking through annoying redirects and countdown timers! 😈</i>
</p>

---

## 💫 What Is This?

A **blazingly fast** REST API that:

- 🎯 **Scrapes** movie/series download pages from HDHub
- 🔓 **Bypasses** pesky gadgetsweb & hubcloud redirects
- ⚡ **Extracts** direct download links automatically
- 🚀 **Cloudflare-resistant** with curl_cffi fallback

> *"Why waste 30 seconds clicking buttons when code can do it in 3 seconds?"* 😏

---

## 🛠️ Features

| Feature | Description |
|---------|-------------|
| 🎬 **Movie Support** | Scrape single movie pages |
| 📺 **Series Support** | Handle batch packs + individual episodes |
| 🔐 **Token Decryption** | Reverse-engineered JS bypass (Rot13, Base64, etc.) |
| 🛡️ **Cloudflare Bypass** | Auto-fallback to curl_cffi when blocked |
| 🌐 **REST API** | Clean FastAPI endpoints |
| ☁️ **Vercel Ready** | Deploy in one click |

---

## 🚀 Quick Start

### 📦 Installation

```bash
# Clone it
git clone https://github.com/itzmepromgitman/hdhub-bypass.git
cd hdhub-bypass

# Install deps
pip install -r requirements.txt
```

### ⚡ Run Locally

```bash
uvicorn api.index:app --reload --port 8000
```

---

## 📡 API Endpoints

### 🏠 Root
```http
GET /
```
Returns API info & available endpoints.

---

### 🎬 Scrape Page
```http
POST /scrape
Content-Type: application/json

{
  "url": "https://4khdhub.dad/some-movie-page/"
}
```

**Response:**
```json
{
  "title": "Movie Name",
  "type": "movie",
  "batch": [...],
  "singles": [...]
}
```

---

### 🔓 Bypass Single Link
```http
POST /bypass
Content-Type: application/json

{
  "url": "https://gadgetsweb.xyz/?id=..."
}
```

**Response:**
```json
{
  "original_url": "...",
  "final_url": "https://direct-download-link.com/file.mkv",
  "filename": "Movie.2024.1080p.mkv"
}
```

---

### ⚡ Bypass All Links
```http
POST /bypass_all
Content-Type: application/json

{
  "url": "https://4khdhub.dad/some-movie/"
}
```

Scrapes the page **AND** bypasses all found links in one call! 🔥

---

## ☁️ Deploy to Vercel

1. Fork this repo
2. Connect to Vercel
3. **Done!** Your API is live 🎉

The `vercel.json` config handles all the routing magic ✨

---

## 🧠 How It Works

<details>
<summary><b>🔍 Click to see the bypass magic...</b></summary>

```
📥 Input: HDHub Movie/Series Page
         ↓
🔎 Scrape: Extract all gadgetsweb URLs
         ↓
🔐 Decrypt: Token → B64 → B64 → Rot13 → B64 → JSON
         ↓
🌐 Navigate: HubCloud → Download Button → Final Link
         ↓
📤 Output: Direct Download URLs
```

> The site sends encrypted tokens + decryption logic client-side.
> We just replicate that logic 😈

</details>

---

## 📁 Project Structure

```
hdhub/
├── api/
│   └── index.py      # FastAPI app + all endpoints
├── bypass.py         # Standalone bypass script
├── requirements.txt  # Python dependencies
├── vercel.json       # Vercel deployment config
└── README.md         # You are here! 📍
```

---

## ⚠️ Disclaimer

<blockquote>
⚠️ <b>Educational purposes only!</b><br>
This project demonstrates web scraping & link bypass techniques.
Use responsibly. Respect website Terms of Service.
The author is not responsible for misuse. 🙃
</blockquote>

---

## 👨‍💻 Author

<table>
  <tr>
    <td align="center">
      <b>🔥 HetArgon 🔥</b><br>
      <a href="https://t.me/heyargon">📱 Telegram</a> •
      <a href="https://github.com/itzmepromgitman">🐙 GitHub</a>
    </td>
  </tr>
</table>

---

<p align="center">
  <b>⭐ Star this repo if it saved your clicks! ⭐</b>
</p>

<p align="center">
  <img src="https://img.shields.io/github/stars/itzmepromgitman/HDhub-bypass-api?style=social"/>
</p>

</blockquote>

