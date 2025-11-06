---
title: Img2img Turbo
emoji: 👁
colorFrom: indigo
colorTo: gray
sdk: gradio
sdk_version: 5.49.0
app_file: app.py
pinned: false
license: mit
---

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference

🎨 Sketch to Image Generator (pix2pix-Turbo + Gradio)

“Turning imagination into reality — one sketch at a time.”

This project implements a Sketch-to-Image translation system using pix2pix-turbo, a one-step diffusion-based model proposed by CMU and Adobe researchers.
It can instantly convert hand-drawn sketches into realistic color images with remarkable quality and speed, all through a Gradio interface.

🧠 Project Summary

Goal:
To build an AI application that takes a user’s sketch and generates a detailed, realistic image using the img2img-turbo architecture — a fast, adversarially trained one-step diffusion model.

Framework:

pix2pix-turbo → for paired translation (sketch → photo)

CycleGAN-turbo → for unpaired translation (day ↔ night, clear ↔ rainy, etc.)

Gradio → for an interactive local demo

⚙️ Features

✅ Convert sketches to high-quality, realistic images
✅ One-step image translation (fast inference — 0.1s on A100 GPU)
✅ Control output with text prompts for style & diversity
✅ Launch interactive Gradio demo locally
✅ Extendable to other tasks like edge-to-image or day-to-night translation

🧩 Model Overview

Paper: One-Step Image Translation with Text-to-Image Models (arXiv:2403.12036)

Authors: Gaurav Parmar, Taesung Park, Srinivasa Narasimhan, Jun-Yan Zhu (CMU + Adobe Research)

Core Idea:
Integrate multiple modules of latent diffusion models into a single, end-to-end network using lightweight LoRA adapters and adversarial training — enabling fast, high-fidelity, one-step image translation.

🏗️ Architecture Diagram
[Input Sketch] → [pix2pix-turbo Generator (1-step)] → [Realistic Image Output]
                   ↑
          Text prompt for style control

🚀 How to Run Locally
1️⃣ Clone Repository
git clone https://github.com/jayraj-patil/sketch-to-image-turbo.git
cd sketch-to-image-turbo

2️⃣ Environment Setup
# Option 1: Conda
conda env create -f environment.yaml
conda activate img2img-turbo

# Option 2: Virtualenv
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

3️⃣ Run the Gradio Demo
# Launch Sketch → Image demo
gradio gradio_sketch2image.py


or

# Launch Canny Edge → Image demo
gradio gradio_canny2image.py


Then open the Gradio link in your browser to interact with the model.

4️⃣ Example Inference via CLI
python src/inference_paired.py \
--model_name "sketch_to_image_stochastic" \
--input_image "assets/examples/sketch_input.png" \
--gamma 0.4 \
--prompt "a futuristic sci-fi city, cinematic lighting, ultra-realistic" \
--output_dir "outputs"

🧠 Sample Results
Input Sketch	Generated Image
🐱 Cat outline	🐈 Realistic colored cat
🐟 Fish sketch	🐠 Lifelike underwater fish
🏔️ Mountain outline	🌄 Beautiful scenic landscape
🧰 Tech Stack
Category	Tools / Libraries
Language	Python
Model	pix2pix-turbo / CycleGAN-turbo
Framework	PyTorch
Interface	Gradio
Utils	OpenCV, NumPy, PIL
🧑‍💻 Author

Jayraj Patil
🎓 Final Year AIML Student
💡 Passionate about Generative AI, Vision Models & Applied Deep Learning
🔗 LinkedIn

📧 [Your Email]

🌟 Future Work

Add custom sketch upload + style prompt input

Integrate background enhancement / lighting control

Train on custom paired datasets

Deploy using Hugging Face Spaces

⭐ “From lines to life — AI turns sketches into imagination realized.”

🧩 Optional Files to Include

requirements.txt

torch
torchvision
torchaudio
gradio
opencv-python
Pillow
numpy
tqdm


.gitignore

__pycache__/
venv/
outputs/
*.pth
*.pt
*.ckpt
*.log

