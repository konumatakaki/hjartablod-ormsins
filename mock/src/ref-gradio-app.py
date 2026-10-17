import numpy as np, librosa, librosa.display, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import gradio as gr

sr = 16000
t = np.linspace(0, 4, 4 * sr, endpoint=False)
env = (np.sin(2 * np.pi * 1.3 * t) > -0.2).astype(float)
y = env * (0.4 * np.sin(2 * np.pi * (180 + 40 * np.sin(2 * np.pi * 0.7 * t)) * t)
           + 0.2 * np.sin(2 * np.pi * 900 * t) + 0.05 * np.random.default_rng(0).standard_normal(t.size))
mfcc = librosa.feature.mfcc(y=y, sr=sr)
fig, ax = plt.subplots(figsize=(6, 2))
librosa.display.specshow(mfcc, sr=sr, x_axis="time", ax=ax)
ax.set(title="MFCC  session_002.wav  00:14:28-00:14:32")
fig.tight_layout()
import tempfile, os
mfcc_path = os.path.join(tempfile.gettempdir(), "mfcc.png")
fig.savefig(mfcc_path, dpi=100)

with gr.Blocks(title="phone-recog") as demo:
    gr.Image(mfcc_path, label="MFCC (n_mfcc=20)")
    gr.Textbox("tʰ a ʔ i n ɛ k a l u", label="phones (allosaurus, universal)")
    gr.Button("Submit", variant="primary")
demo.launch(server_name="127.0.0.1", server_port=7860)
