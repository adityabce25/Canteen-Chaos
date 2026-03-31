import os
import subprocess
import sys

# --- SMART PATH LOGIC ---
# This finds the directory where main.py is actually located (the Project Root)
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
# If main.py is inside /scripts, we need to go up one level to find the root
if os.path.basename(PROJECT_ROOT) == "scripts":
    PROJECT_ROOT = os.path.dirname(PROJECT_ROOT)

SCRIPTS_DIR = os.path.join(PROJECT_ROOT, "scripts")
# ------------------------

def run_script(script_name):
    """Helper to run scripts using absolute paths to avoid 'double folder' errors."""
    script_path = os.path.join(SCRIPTS_DIR, script_name)
    
    if not os.path.exists(script_path):
        print(f"❌ Error: Cannot find {script_name} at {script_path}")
        return False

    print(f"🚀 Running {script_name}...")
    # We use sys.executable to ensure we use the same Python version
    result = subprocess.run([sys.executable, script_path], capture_output=False)
    return result.returncode == 0

def main():
    print("========================================")
    print("   CAMPUS CANTEEN CHAOS - MASTER CLI   ")
    print("========================================\n")

    # Check for Knowledge Base and Model
    data_file = os.path.join(PROJECT_ROOT, "data", "canteen_data.csv")
    model_file = os.path.join(PROJECT_ROOT, "models", "canteen_model.pkl")

    # 1. Check Data (CO3)
    if not os.path.exists(data_file):
        print("⚠️ Data not found in /data folder!")
        if not run_script("data_generator.py"):
            print("❌ Failed to generate data.")
            return

    # 2. Check Model (CO4)
    if not os.path.exists(model_file):
        print("⚠️ Trained model not found in /models folder!")
        if not run_script("model_trainer.py"):
            print("❌ Failed to train model.")
            return

    # 3. Launch App (CO1)
    print("✅ All systems go. Launching Predictor...")
    run_script("canteen_app.py")

if __name__ == "__main__":
    main()