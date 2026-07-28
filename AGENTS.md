# Agent Guide

## Project Overview

This repository is a Jupyter notebook demo for insurance claims image similarity search. It uses TorchVision to embed vehicle damage images, stores those embeddings in MongoDB Atlas, and queries similar images with MongoDB Vector Search.

## Key Files

- `README.md`: User-facing overview with tech stack tags and badges, capabilities, MongoDB value proposition, architecture, prerequisites, quickstart, search index setup, and data model summary.
- `image_similarity.ipynb`: Main runnable demo.
- `EDD.md`: MongoDB schema, index, and query contract.
- `requirements.txt`: Python dependencies for local notebook execution.
- `requirements-dev.txt`: Python dependencies for validation and notebook tests.
- `.github/workflows/validate.yml`: CI smoke check for docs and notebook integrity.
- `tests/test_notebook.py`: Notebook contract tests and optional Atlas-backed integration test.
- `test.jpg` and `top_5.png`: README example images.

## Build and Validation Commands

Create an environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Validate notebook JSON:

```bash
python -m json.tool image_similarity.ipynb > /tmp/image_similarity.validated.json
```

Run default tests:

```bash
python -m pip install -r requirements-dev.txt
pytest -m "not integration"
```

Run the end-to-end notebook integration test:

```bash
export MONGODB_URI="mongodb+srv://<username>:<password>@<cluster-name>/?retryWrites=true&w=majority"
export NOTEBOOK_MAX_DATASET_IMAGES=5
export NOTEBOOK_CLEAR_COLLECTION=true
python -m pip install -r requirements.txt -r requirements-dev.txt
pytest -m integration
```

Run the notebook manually:

```bash
jupyter notebook image_similarity.ipynb
```

## Environment Variables

- `MONGODB_URI`: Required for running the notebook against MongoDB Atlas.
- `NOTEBOOK_MAX_DATASET_IMAGES`: Optional test helper that limits the number of dataset images written and inserted.
- `NOTEBOOK_CLEAR_COLLECTION`: Optional test helper. Set to `true` only when the test can clear `claim_resolution.car_damage_photos`.

Example:

```bash
export MONGODB_URI="mongodb+srv://<username>:<password>@<cluster-name>/?retryWrites=true&w=majority"
```

## README Maintenance

When editing `README.md`, preserve the top-level structure used for search and agent crawlability:

- First-level title.
- First-section text tags and logo badges for the technology stack.
- `Capabilities`, `Where MongoDB Shines`, `Tech Stack`, `Architecture Overview`, `Prerequisites`, `Quick Start`, `Creating Search Index`, and `Data Model` sections.

Keep repository name, description, and topic recommendations in `REPOSITORY_METADATA.md`, not in `README.md`.

## MongoDB Skills

Use the official MongoDB agent skills from https://github.com/mongodb/agent-skills whenever a MongoDB-specific task matches an available skill.

## When To Use EDD.md

Use [EDD.md](./EDD.md) as the source of truth for the MongoDB data model in this repository.

Consult [EDD.md](./EDD.md) before making changes that touch:

- MongoDB collections, document structure, or field names.
- MongoDB Vector Search index names, paths, dimensions, or similarity settings.
- Notebook cells that read or write database records.
- Validation, API payloads, or UI that depend on persisted data.
- Schema documentation, Mermaid diagrams, or entity modeling discussions.

## Guardrails

- Do not commit real MongoDB credentials or customer data.
- Do not change the repository license unless a maintainer explicitly requests it.
- Keep generated datasets such as `car_damage/` out of git.
- Keep README setup commands copy-pasteable from a clean environment.
