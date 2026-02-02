# aadit_portfolio

This repository contains a simple portfolio with a Flask backend and a static frontend.

Deployment plan

- **Backend**: deploy the `backend/` folder to Render (Web Service). Use `requirements.txt` and the `Procfile` added to this folder.
- **Frontend**: deploy the `frontend/` folder to Vercel as a static site. `vercel.json` is included to serve `frontend/main.html` at `/`.

Quick local run

- Backend: from repo root run:

```bash
python -m pip install -r backend/requirements.txt
python backend/main.py
```

- Frontend: open `frontend/main.html` in a browser (it fetches from `http://127.0.0.1:5000/api` by default).

Preparing for deployment

1. Push this repository to GitHub (or ensure it's already on GitHub).

2. Deploy backend on Render

	- In Render dashboard click **New** → **Web Service**.
	- Connect your GitHub repo and select the `backend` subdirectory as the root.
	- Build command: leave blank (Render will run `pip install -r requirements.txt`) or set to:

		```bash
		pip install -r requirements.txt
		```

	- Start command: `gunicorn main:app`
	- Render will provide a public URL (e.g. `https://aadit-backend.onrender.com`).

3. Deploy frontend on Vercel

	- Install the Vercel CLI or use the Vercel dashboard.
	- If using CLI, from repo root run:

		```bash
		npm i -g vercel
		vercel --prod --cwd frontend
		```

	- Or in Vercel dashboard, create a new project from your GitHub repo and set the Framework to "Other" / Static, with the output directory left empty. `vercel.json` in the repo will route `/` to `frontend/main.html`.

4. Configure frontend to use backend URL

	- After Render gives you the backend URL, edit the `<meta name="api-base">` tag in `frontend/main.html` and set its `content` to the Render URL with `/api` appended, for example:

		```html
		<meta name="api-base" content="https://your-backend.onrender.com/api" />
		```

	- Commit that change and re-deploy the frontend on Vercel.

Notes

- CORS is already enabled in `backend/main.py` via `flask_cors.CORS(app)`, so the frontend on Vercel will be able to call the Render backend.
- If you'd like, I can:
	- (A) attempt to deploy automatically using your Render/Vercel credentials (you'd need to provide access), or
	- (B) walk you through each dashboard step while you click along.

Once you deploy both services, send me the Render backend URL and I will update `frontend/main.html` with the correct `api-base` and re-deploy instructions, then prepare a small message you can send to sir with the final URLs.
