# CRM_NGO

cd backend
python3 -m venv .venv
source .venv/bin/activate
# Windows: .venv\Scripts\activate | Linux/macOS: source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload --port 8000


cd frontend
npx nuxi@latest init .
npm install
npm run dev