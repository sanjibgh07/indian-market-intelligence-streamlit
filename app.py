from pathlib import Path
import runpy
import shutil
import tempfile
import zipfile

ROOT = Path(tempfile.gettempdir()) / "indian_market_streamlit_bundle"
BUNDLE = Path(__file__).with_name("app_bundle.zip")

if ROOT.exists():
    shutil.rmtree(ROOT)
ROOT.mkdir(parents=True, exist_ok=True)
with zipfile.ZipFile(BUNDLE) as archive:
    archive.extractall(ROOT)

runpy.run_path(str(ROOT / "app.py"), run_name="__main__")
