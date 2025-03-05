from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def mad_libs():
    story = ""
    if request.method == "POST":
        noun = request.form["noun"]
        adjective = request.form["adjective"]
        verb = request.form["verb"]
        adverb = request.form["adverb"]
        story = f"One day, a {adjective} {noun} decided to {verb} {adverb}. It was a sight to see!"

    return f'''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Mad Libs Game</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    background: linear-gradient(to right, #ff7e5f, #feb47b);
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                }}
                .container {{
                    background: white;
                    padding: 20px;
                    border-radius: 10px;
                    box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
                    text-align: center;
                    max-width: 400px;
                    width: 100%;
                }}
                input[type="text"] {{
                    width: 90%;
                    padding: 10px;
                    margin: 5px 0;
                    border: 1px solid #ccc;
                    border-radius: 5px;
                }}
                input[type="submit"] {{
                    background: #ff7e5f;
                    color: white;
                    padding: 10px;
                    border: none;
                    border-radius: 5px;
                    cursor: pointer;
                    width: 100%;
                }}
                input[type="submit"]:hover {{
                    background: #feb47b;
                }}
                h2 {{
                    color: #333;
                    margin-top: 20px;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Mad Libs Game</h1>
                <form method="POST">
                    <input type="text" name="noun" placeholder="Enter a noun" required><br>
                    <input type="text" name="adjective" placeholder="Enter an adjective" required><br>
                    <input type="text" name="verb" placeholder="Enter a verb" required><br>
                    <input type="text" name="adverb" placeholder="Enter an adverb" required><br>
                    <input type="submit" value="Generate Story">
                </form>
                <h2>{story}</h2>
            </div>
        </body>
        </html>
    '''

if __name__ == "__main__":
    app.run(debug=True)
