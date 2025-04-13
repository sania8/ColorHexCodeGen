# 🎨 CodeHexGen — From Color Descriptions to Color Codes with AI!

![Hugging Face](https://img.shields.io/badge/HuggingFace-Model-yellow) ![Flask](https://img.shields.io/badge/Backend-Flask-blue) ![Render](https://img.shields.io/badge/Hosted%20on-Render-green) ![Colab](https://img.shields.io/badge/Train%20on-Google%20Colab-red)

> 🚀 Turn simple color descriptions like `"deep ocean blue"` into precise hex codes like `#006994` using a fine-tuned LLM.

---

## 💡 What is CodeHexGen?

**CodeHexGen** is an AI-powered app that converts **textual color descriptions** into **accurate HEX color codes**. It's powered by a fine-tuned version of [TinyLLaMA](https://huggingface.co/TinyLlama) and designed for creators, designers, and developers looking to quickly map creative color ideas to exact color values.

---

## 🤖 Model Details

- **Base Model:** [`TinyLlama`](https://huggingface.co/TinyLlama)
- **Fine-tuning Technique:** LoRA (Low-Rank Adaptation)
- **Dataset:** [`burkelibbey/colors`](https://huggingface.co/datasets/burkelibbey/colors)
- **Hyperparameters:**
  - Learning Rate: `2e-5`
  - Training Steps: `250`
- **Final Model:** [saniaverma/tinyllama-colorist-v0](https://huggingface.co/saniaverma/tinyllama-colorist-v0)

> ✅ The model is deployed on Hugging Face Inference API:  
> 🔗 https://api-inference.huggingface.co/models/saniaverma/tinyllama-colorist-v0

---

## 🖥️ Application Architecture

- **Frontend**: HTML + CSS (minimal)
- **Backend**: Python + Flask
- **Hosting**: Render

> 🌐 Live App: [https://chromaticai.onrender.com/](https://chromaticai.onrender.com/)

---

## 📒 Google Colab Notebook

Explore the full fine-tuning process and model push-to-hub in the Colab notebook:

📓 [Open in Google Colab](https://colab.research.google.com/drive/12-5O6NvMdISOe0KVeHBrLkHMxMFqGp9Y#scrollTo=4Ho3JJDLt6Pa)

---

## 🧪 How It Works

1. 🧠 You describe a color in natural language, e.g. `"faded peach with a soft blush"`.
2. 🚀 The app sends this to the Hugging Face inference API.
3. 🎯 The fine-tuned TinyLLaMA model generates a hex color code.
4. 🌈 The app displays the color preview + hex code.

---

## 📦 Installation (Run Locally)

```bash
git clone https://github.com/yourusername/CodeHexGen.git
cd CodeHexGen
pip install -r requirements.txt
python app.py
