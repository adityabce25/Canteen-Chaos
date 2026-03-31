import joblib
import os
import pandas as pd
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

# 1. Path Setup (Loading from the /models folder)
MODEL_DIR = os.path.join('..', 'models')

def load_assets():
    try:
        model = joblib.load(os.path.join(MODEL_DIR, 'canteen_model.pkl'))
        le_day = joblib.load(os.path.join(MODEL_DIR, 'le_day.pkl'))
        le_weather = joblib.load(os.path.join(MODEL_DIR, 'le_weather.pkl'))
        return model, le_day, le_weather
    except FileNotFoundError:
        console.print("[bold red]❌ Error: Model files not found in /models folder![/bold red]")
        console.print("[yellow]Please run 'model_trainer.py' first.[/yellow]")
        exit()

# 2. Rational Agent Logic (CO1 & CO2)
def get_rational_advice(wait_time, hunger, time_until_class):
    # Utility Function: Balancing hunger benefit vs. lateness penalty
    # We use a threshold logic to simulate a "Rational Agent"
    buffer_time = 10  # 10 minutes to actually eat the food
    total_needed = wait_time + buffer_time
    
    if total_needed > time_until_class:
        if hunger >= 9: # Extreme hunger might justify being a bit late
            return "[bold yellow]⚠️ ADVICE: RISKY GO.[/bold yellow] You'll likely be late, but you're starving."
        else:
            return "[bold red]❌ ADVICE: STAY.[/bold red] You don't have enough time to eat and make it to class."
    else:
        return "[bold green]✅ ADVICE: GO.[/bold green] You have plenty of time. Enjoy your meal!"

# 3. Terminal Interface
def main():
    model, le_day, le_weather = load_assets()
    
    console.print(Panel.fit(
        "[bold yellow]🏛️ CAMPUS CANTEEN CHAOS PREDICTOR 🏛️[/bold yellow]\n"
        "[italic]Syllabus-Aligned Capstone Project[/italic]",
        border_style="cyan"
    ))

    while True:
        console.print("\n[bold]Main Menu:[/bold]")
        console.print("1. [cyan]Predict Wait Time & Get Advice[/cyan]")
        console.print("2. [cyan]Exit[/cyan]")
        
        choice = console.input("\n[bold]Select an option (1-2): [/bold]")

        if choice == '1':
            try:
                # Inputs for Prediction
                day = console.input("Enter Day (Mon-Fri): ").capitalize()[:3]
                hour = int(console.input("Enter Hour (8-17): "))
                weather = console.input("Weather (Sunny/Rainy/Cloudy): ").capitalize()
                is_exam = int(console.input("Exam Week? (1 for Yes, 0 for No): "))

                # Encoding inputs (Feature Learning - CO3)
                day_enc = le_day.transform([day])[0]
                weather_enc = le_weather.transform([weather])[0]

                # Prediction (CO4)
                prediction = model.predict([[day_enc, hour, is_exam, weather_enc]])[0]
                
                console.print(Panel(
                    f"Predicted Wait: [bold magenta]{prediction:.1f} minutes[/bold magenta]",
                    title="AI Prediction"
                ))

                # Agent Logic Inputs
                hunger = int(console.input("Your Hunger Level (1-10): "))
                minutes_left = int(console.input("Minutes until your next class: "))
                
                # Output Advice (CO1)
                advice = get_rational_advice(prediction, hunger, minutes_left)
                console.print(f"\n{advice}\n")

            except Exception as e:
                console.print(f"[red]Input Error: {e}. Please try again.[/red]")

        elif choice == '2':
            console.print("[italic]Exiting... Good luck with your classes![/italic]")
            break

if __name__ == "__main__":
    main()