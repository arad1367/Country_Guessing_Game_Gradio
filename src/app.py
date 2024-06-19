import random
import gradio as gr

# List of countries
countries = [
    "Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua and Barbuda",
    "Argentina", "Armenia", "Australia", "Austria", "Azerbaijan", "Bahamas", "Bahrain",
    "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin", "Bhutan", "Bolivia",
    "Bosnia and Herzegovina", "Botswana", "Brazil", "Brunei", "Bulgaria", "Burkina Faso",
    "Burundi", "Cabo Verde", "Cambodia", "Cameroon", "Canada", "Central African Republic",
    "Chad", "Chile", "China", "Colombia", "Comoros", "Congo", "Costa Rica", "Croatia",
    "Cuba", "Cyprus", "Czech Republic", "Denmark", "Djibouti", "Dominica", "Dominican Republic",
    "East Timor", "Ecuador", "Egypt", "El Salvador", "Equatorial Guinea", "Eritrea", "Estonia",
    "Eswatini", "Ethiopia", "Fiji", "Finland", "France", "Gabon", "Gambia", "Georgia", "Germany",
    "Ghana", "Greece", "Grenada", "Guatemala", "Guinea", "Guinea-Bissau", "Guyana", "Haiti",
    "Honduras", "Hungary", "Iceland", "India", "Indonesia", "Iran", "Iraq", "Ireland", "Israel",
    "Italy", "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya", "Kiribati", "Korea, North",
    "Korea, South", "Kuwait", "Kyrgyzstan", "Laos", "Latvia", "Lebanon", "Lesotho", "Liberia",
    "Libya", "Liechtenstein", "Lithuania", "Luxembourg", "Madagascar", "Malawi", "Malaysia",
    "Maldives", "Mali", "Malta", "Marshall Islands", "Mauritania", "Mauritius", "Mexico",
    "Micronesia", "Moldova", "Monaco", "Mongolia", "Montenegro", "Morocco", "Mozambique",
    "Myanmar", "Namibia", "Nauru", "Nepal", "Netherlands", "New Zealand", "Nicaragua", "Niger",
    "Nigeria", "North Macedonia", "Norway", "Oman", "Pakistan", "Palau", "Palestine", "Panama",
    "Papua New Guinea", "Paraguay", "Peru", "Philippines", "Poland", "Portugal", "Qatar",
    "Romania", "Russia", "Rwanda", "Saint Kitts and Nevis", "Saint Lucia", "Saint Vincent and the Grenadines",
    "Samoa", "San Marino", "Sao Tome and Principe", "Saudi Arabia", "Senegal", "Serbia",
    "Seychelles", "Sierra Leone", "Singapore", "Slovakia", "Slovenia", "Solomon Islands",
    "Somalia", "South Africa", "South Sudan", "Spain", "Sri Lanka", "Sudan", "Suriname",
    "Sweden", "Switzerland", "Syria", "Taiwan", "Tajikistan", "Tanzania", "Thailand", "Togo",
    "Tonga", "Trinidad and Tobago", "Tunisia", "Turkey", "Turkmenistan", "Tuvalu", "Uganda",
    "Ukraine", "United Arab Emirates", "United Kingdom", "United States", "Uruguay", "Uzbekistan",
    "Vanuatu", "Vatican City", "Venezuela", "Vietnam", "Yemen", "Zambia", "Zimbabwe"
]

# Initialize game variables
selected_country = ""
attempts_left = 0
guessed_letters = []
player_name = ""

def start_game(name):
    global selected_country, attempts_left, guessed_letters, player_name
    player_name = name
    selected_country = random.choice(countries).upper()
    attempts_left = len(selected_country)
    guessed_letters = ["_"] * len(selected_country)
    return update_display()

def update_display():
    return f"Country: {' '.join(guessed_letters)}", f"Guesses left: {attempts_left}", ""

def guess_letter(letter):
    global attempts_left
    if attempts_left == 0:
        return "No more attempts left. Please restart the game.", "", "Try again."

    letter = letter.upper()
    if letter in selected_country:
        for i in range(len(selected_country)):
            if selected_country[i] == letter:
                guessed_letters[i] = letter
    else:
        attempts_left -= 1

    if "_" not in guessed_letters:
        return f"Country: {' '.join(guessed_letters)}", f"Guesses left: {attempts_left}", f"Congratulations {player_name}! You won!"

    if attempts_left == 0:
        return f"Country: {' '.join(guessed_letters)}", f"Guesses left: {attempts_left}", f"Sorry {player_name}, you lost. The country was {selected_country}."

    return update_display()

def restart_game():
    return start_game(player_name)

footer = """
<div style="text-align: center; margin-top: 20px;">
    <a href="https://www.linkedin.com/in/pejman-ebrahimi-4a60151a7/" target="_blank">LinkedIn</a> |
    <a href="https://github.com/arad1367/Visual_QA_MiniCPM-Llama3-V-2_5_GradioApp" target="_blank">GitHub</a> |
    <a href="https://arad1367.pythonanywhere.com/" target="_blank">Live demo of my PhD defense</a>
    <br>
    Made with 💖 by Pejman Ebrahimi
</div>
"""

with gr.Blocks(theme='abidlabs/dracula_revamped') as demo:
    gr.Markdown("### Country Guessing Game")
    with gr.Row():
        name_input = gr.Textbox(label="Enter your name:", placeholder="Name")
        start_button = gr.Button("Start Game")
    country_display = gr.Textbox(label="Country", interactive=False)
    attempts_display = gr.Textbox(label="Guesses left", interactive=False)
    result_display = gr.Textbox(label="Result", interactive=False)
    letter_input = gr.Textbox(label="Enter a letter:", max_lines=1, placeholder="Letter")
    guess_button = gr.Button("Guess")
    restart_button = gr.Button("Restart Game")

    start_button.click(start_game, inputs=name_input, outputs=[country_display, attempts_display, result_display])
    guess_button.click(guess_letter, inputs=letter_input, outputs=[country_display, attempts_display, result_display])
    restart_button.click(restart_game, inputs=None, outputs=[country_display, attempts_display, result_display])

    gr.HTML(footer)

demo.launch()
