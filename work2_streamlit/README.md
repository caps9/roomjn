# JN Apartment Builder on Streamlit

A 3D planner for one apartment. The whole app is the single file `index.html`.
`streamlit_app.py` only shows that file across the full browser window.

## Files

| File | What it is |
|---|---|
| `index.html` | The app (build 17). Works on its own when opened in a browser. |
| `streamlit_app.py` | Streamlit wrapper. Entry point for Streamlit. |
| `requirements.txt` | Tells Streamlit which package to install. |
| `.streamlit/config.toml` | Hides the Streamlit toolbar. Optional. |

## Put it online with Streamlit Community Cloud

1. Create a new repository on GitHub.
2. Upload everything in this folder to the top level of the repository, including the `.streamlit` folder.
   The `.streamlit` folder is hidden on a Mac: press Cmd + Shift + . in Finder to see it.
3. Go to https://share.streamlit.io and sign in with GitHub.
4. Choose "Create app", pick the repository and branch, and set the main file path to `streamlit_app.py`.
5. Deploy. The app opens at its own `streamlit.app` address.

## Run it on your own computer

```
pip install -r requirements.txt
streamlit run streamlit_app.py
```

## Good to know

- Needs Streamlit 1.56 or newer. The wrapper uses `st.iframe`; the older `st.components.v1.html` was removed in 2026.
- The app needs internet: it loads its 3D library, fonts and the Photoreal textures, sky and figure from public CDNs.
- Layout, bed size and wall colours are saved in the visitor's own browser, per address. Each visitor has their own; the online app starts fresh compared with the local file.
- Click once inside the 3D view before using the keyboard.
- To change the app, edit `index.html` only. `streamlit_app.py` does not need to change.
