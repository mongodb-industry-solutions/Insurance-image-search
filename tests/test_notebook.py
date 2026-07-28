import os
import shutil
from pathlib import Path

import nbformat
import pytest
from nbclient import NotebookClient


REPO_ROOT = Path(__file__).resolve().parents[1]
NOTEBOOK_PATH = REPO_ROOT / "image_similarity.ipynb"


def read_notebook():
    return nbformat.read(NOTEBOOK_PATH, as_version=4)


def test_notebook_is_valid_and_has_code_cells():
    notebook = read_notebook()

    assert notebook.nbformat >= 4
    assert any(cell.get("cell_type") == "code" for cell in notebook.cells)


def test_notebook_has_no_committed_outputs():
    notebook = read_notebook()

    for index, cell in enumerate(notebook.cells):
        assert cell.get("outputs", []) == [], f"Cell {index} has committed outputs"


@pytest.mark.integration
def test_image_similarity_notebook_runs_end_to_end(tmp_path, monkeypatch):
    if not os.environ.get("MONGODB_URI"):
        pytest.skip("Set MONGODB_URI to run the Atlas-backed notebook integration test.")

    workdir = tmp_path / "notebook-run"
    workdir.mkdir()

    shutil.copy2(NOTEBOOK_PATH, workdir / NOTEBOOK_PATH.name)

    monkeypatch.setenv("NOTEBOOK_MAX_DATASET_IMAGES", os.environ.get("NOTEBOOK_MAX_DATASET_IMAGES", "5"))
    monkeypatch.setenv("NOTEBOOK_CLEAR_COLLECTION", os.environ.get("NOTEBOOK_CLEAR_COLLECTION", "true"))

    notebook = nbformat.read(workdir / NOTEBOOK_PATH.name, as_version=4)
    client = NotebookClient(
        notebook,
        timeout=int(os.environ.get("NOTEBOOK_EXECUTION_TIMEOUT", "1800")),
        kernel_name="python3",
        resources={"metadata": {"path": str(workdir)}},
    )

    client.execute()

    image_dir = workdir / "car_damage"
    assert image_dir.exists()
    assert any(image_dir.glob("*.jpg"))
