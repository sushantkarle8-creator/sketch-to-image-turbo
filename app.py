import os
import sys
import shutil
import subprocess
import uuid
from pathlib import Path
from PIL import Image
import gradio as gr

BASE = Path(__file__).parent.resolve()
SRC_SCRIPT = BASE / "src" / "inference_paired.py"
OUTPUTS = BASE / "outputs"
TMP_INPUTS = BASE / "tmp_inputs"

TMP_INPUTS.mkdir(parents=True, exist_ok=True)
OUTPUTS.mkdir(parents=True, exist_ok=True)

def run_inference(model_name: str, input_image_path: str, prompt: str, gamma: float):
    if OUTPUTS.exists():
        shutil.rmtree(OUTPUTS)
    OUTPUTS.mkdir(parents=True, exist_ok=True)

    args = [
        sys.executable, str(SRC_SCRIPT),
        "--model_name", model_name,
        "--input_image", str(input_image_path),
        "--prompt", prompt,
        "--output_dir", str(OUTPUTS)
    ]
    if gamma is not None:
        args += ["--gamma", str(gamma)]

    proc = subprocess.run(args, capture_output=True, text=True)
    if proc.returncode != 0:
        return None, f"❌ Error:\n{proc.stderr}\n{proc.stdout}"

    files = sorted(OUTPUTS.glob("*"), key=lambda p: p.stat().st_mtime)
    if not files:
        return None, "⚠️ No output image found."

    return str(files[-1]), f"✅ Success:\n{proc.stdout}"

def generate(input_image, prompt, model_name, gamma):
    if input_image is None:
        return None, "Please upload an input image."

    ext = Path(input_image).suffix or ".png"
    tmp_path = TMP_INPUTS / f"{uuid.uuid4().hex}{ext}"
    shutil.copy(input_image, tmp_path)

    out_path, logs = run_inference(model_name, tmp_path, prompt, gamma)
    return out_path, logs

with gr.Blocks() as demo:
    gr.Markdown("# 🖌️ Img2Img-Turbo\nConvert sketches or edges to realistic images using Turbo diffusion models.")
    with gr.Row():
        with gr.Column():
            input_img = gr.Image(type="filepath", label="Input sketch / edge map")
            prompt = gr.Textbox(label="Prompt", placeholder="a realistic painting of a dog sitting on grass")
            model_name = gr.Radio(choices=["edge_to_image", "sketch_to_image_stochastic"],
                                  value="sketch_to_image_stochastic", label="Model")
            gamma = gr.Slider(0.0, 1.0, value=0.4, label="Gamma")
            btn = gr.Button("Generate")
        with gr.Column():
            output_img = gr.Image(label="Generated Output")
            logs = gr.Textbox(label="Logs", lines=12)

    btn.click(generate, inputs=[input_img, prompt, model_name, gamma], outputs=[output_img, logs])

if __name__ == "__main__":
    demo.launch()
