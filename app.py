from flask import Flask, request, render_template

app = Flask(__name__)

# Nutritional Data (name: [calories, carbs, fats, proteins])
food_data = {
    "bread": [265, 49, 4, 9],
    "cereal": [375, 67, 4, 8],
    "pasta": [131, 25, 1, 5],
    "potato": [77, 17, 0.1, 2],
    "noodles": [138, 28, 1, 5],
    "dumplings": [150, 30, 3, 4],
    "cracker": [80, 14, 3, 1],
    "cookie": [200, 30, 9, 2],
    "apple": [52, 14, 0.2, 0.3],
    "banana": [89, 23, 0.3, 1.1],
    "orange": [47, 12, 0.1, 0.9],
    "grape": [69, 18, 0.2, 0.7],
    "strawberry": [32, 7.7, 0.3, 0.7],
    "blueberry": [57, 14, 0.3, 0.7],
    "raspberry": [52, 12, 0.8, 1.5],
    "mango": [60, 15, 0.4, 0.8],
    "avocado": [160, 9, 15, 2],
    "chicken": [239, 0, 14, 27],
    "egg": [155, 1.1, 11, 13],
    "legumes": [127, 22, 0.8, 9],
}

# Route to serve the HTML page
@app.route('/')
def home():
    """Serve the HTML page"""
    return render_template('index.html')

# Route to get food info
@app.route('/calories', methods=['GET'])
def get_food_info():
    """Return calorie and macronutrient information."""
    food_item = request.args.get('food', '').lower()
    if food_item in food_data:
        data = food_data[food_item]
        response = (
            f"{food_item.capitalize()}:\n"
            f"Calories: {data[0]} kcal\n"
            f"Carbs: {data[1]}g\n"
            f"Fats: {data[2]}g\n"
            f"Proteins: {data[3]}g"
        )
        return response
    else:
        return "Food item not found. Please try again."

if __name__ == '__main__':
    app.run(debug=True)
