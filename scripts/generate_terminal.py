import os
import sys

sys.path.insert(0, "/tmp/gifos-env/lib/python3.14/site-packages")
os.environ["GIFOS_GENERAL_COLOR_SCHEME"] = "catppuccin-mocha"
os.environ["GIFOS_FILES_OUTPUT_GIF_NAME"] = "terminal"

import gifos

t = gifos.Terminal(width=800, height=360, xpad=20, ypad=20)
t.set_fps(15)
t.toggle_show_cursor(True)

# Prompt
t.gen_typing_text(
    text="\x1b[0;92m$\x1b[0m whoami",
    row_num=1,
    speed=2,
)
t.clone_frame(20)

# whoami output
t.gen_typing_text(
    text="\x1b[0;96m> Software Engineer focused on frontend, mobile, and developer tooling.\x1b[0m",
    row_num=2,
    speed=1,
)
t.clone_frame(15)

# blank line + next command
t.gen_typing_text(
    text="\x1b[0;92m$\x1b[0m cat interests.txt",
    row_num=4,
    speed=2,
)
t.clone_frame(20)

# interests output
t.gen_typing_text(
    text="\x1b[0;96m> Building with the React ecosystem, Expo, and modern TypeScript tooling.\x1b[0m",
    row_num=5,
    speed=1,
)
t.gen_typing_text(
    text="\x1b[0;96m> Writing CLI tools in Rust and shipping MCP servers.\x1b[0m",
    row_num=6,
    speed=1,
)
t.gen_typing_text(
    text="\x1b[0;96m> Obsessed with clean architecture and great DX.\x1b[0m",
    row_num=7,
    speed=1,
)
t.clone_frame(30)

# cursor blink at end
t.gen_text(
    text="\x1b[0;92m$\x1b[0m",
    row_num=9,
)
t.toggle_blink_cursor(True)
t.clone_frame(40)

t.gen_gif()
