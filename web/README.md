# PyPO web app

This Svelte and TypeScript frontend uses Vite.

- `npm install` installs frontend dependencies.
- `npm run dev` starts the Vite development server on `127.0.0.1:5173`.
- `npm run check` runs Svelte and TypeScript checks.
- `npm run build` creates the static app in `dist/`.

The PyPO version badge is loaded from the local Python server at
`127.0.0.1:8000`. Start `python3 hello_world_server.py` from the repository
root; for a production-style local page, run `npm run build` first.
