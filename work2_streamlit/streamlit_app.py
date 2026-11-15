"""JN Apartment Builder on Streamlit.

Shows index.html, unchanged, across the whole browser window, so it behaves
like the file opened locally. The 3D app itself lives only in index.html.

Needs Streamlit 1.56 or newer (st.iframe). The older st.components.v1.html
was removed from Streamlit in 2026 and is not used here.

Run locally, from inside this folder:
    pip install -r requirements.txt
    streamlit run streamlit_app.py
"""

from pathlib import Path

import streamlit as st

APP_FILE = Path(__file__).parent / "index.html"
FRAME_TITLE = "JN Apartment Builder"

st.set_page_config(page_title=FRAME_TITLE, layout="wide", initial_sidebar_state="collapsed")

if not APP_FILE.exists():
    st.error(f"index.html was not found next to streamlit_app.py ({APP_FILE}).")
    st.stop()

# Let the embedded page cover the whole window and hide Streamlit's own header,
# toolbar and padding. The frame is found by its title, which st.iframe sets from "alt".
st.html(
    f"""
    <style>
      header[data-testid="stHeader"],
      div[data-testid="stToolbar"],
      div[data-testid="stDecoration"],
      footer {{ display: none !important; }}
      .block-container {{ padding: 0 !important; max-width: 100% !important; }}
      iframe[title="{FRAME_TITLE}"] {{
        position: fixed !important;
        inset: 0 !important;
        width: 100vw !important;
        height: 100vh !important;
        height: 100dvh !important;
        border: 0 !important;
        z-index: 1000;
      }}
    </style>
    """
)

# A local .html file given as a Path is embedded as it is, in a frame that runs
# its JavaScript. The pixel height is only a fallback; the CSS above makes it fill the window.
st.iframe(APP_FILE, height=900, alt=FRAME_TITLE)
