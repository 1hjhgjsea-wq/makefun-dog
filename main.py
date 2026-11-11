import os, shutil

dst_dir = "/output"
os.makedirs(dst_dir, exist_ok=True)

src = os.path.join(os.path.dirname(__file__), "dog.png")
dst = os.path.join(dst_dir, "entry.png")

shutil.copyfile(src, dst)
