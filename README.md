

# 🧠 Getting Started

This guide walks you through installing **Ollama** and setting up the **Qwen2:0.5B** model locally.

---

## ✅ Step 1: Install Ollama

Ollama provides a simple way to run large language models locally.

### 🔧 For macOS

```bash
brew install ollama
```

> ℹ️ Requires macOS 12.6+ and Apple Silicon.

### 🔧 For Linux

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

> Test with `ollama run llama3` to confirm the installation.

### 🔧 For Windows

Download the installer from: [https://ollama.com/download](https://ollama.com/download)

> Requires Windows Subsystem for Linux (WSL 2)

---

## 🚀 Step 2: Start Ollama

Once installed, start the Ollama service (Linux/macOS):

```bash
ollama serve
```

On Windows, this runs automatically when the Ollama app is open.

---

## 📥 Step 3: Pull the Qwen2:0.5B Model

Use the following command to download and install the **Qwen2 0.5B** model:

```bash
ollama pull qwen2:0.5b
```

This will download the model weights and make them available for local inference.

---

## 💬 Step 4: Run the Python files in Lessons folder 


## 📌 Notes

* Qwen2:0.5B is a small, fast model ideal for prototyping and low-resource environments.

