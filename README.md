![PyPO logo](logo/pypo-logo.png)

[![DOI](https://zenodo.org/badge/490758642.svg)](https://zenodo.org/badge/latestdoi/490758642)
[![DOI](https://joss.theoj.org/papers/10.21105/joss.05478/status.svg)](https://doi.org/10.21105/joss.05478)

# Welcome to the Python Physical Optics (PyPO) package!

Version 1.2.1

For full documentation and instructions on how to install and use PyPO, we kindly refer to the [documentation page](https://pypo-dev.github.io/PyPO/).

## Local Svelte web app

The Svelte frontend lives in `web/`. To build and serve it locally, install the
frontend dependencies and build the app:

```sh
npm --prefix web install
npm --prefix web run build
python3 hello_world_server.py
```

After installing PyPO, open [http://127.0.0.1:8000](http://127.0.0.1:8000).
The server listens only on your local machine; press `Ctrl+C` to stop it.
For frontend development, run `npm --prefix web run dev` and
`python3 hello_world_server.py` in separate terminals; the Vite app is available
at [http://127.0.0.1:5173](http://127.0.0.1:5173).
