from dotenv import load_dotenv
from pathlib import Path
import os
from src.presentation.app import create_app

load_dotenv(dotenv_path=Path(__file__).parent / ".env", override=True)
app = create_app()

if __name__ == "__main__":
    host = os.getenv("HOST","0.0.0.0")
    port = int(os.getenv("PORT",5000))
    debug = os.getenv("FLASK_DEBUG","False").lower() == "true"
    print(f"DEBUG waarde: {debug}")   # ← tijdelijk

    app.run(host=host, port=port, debug=debug)


