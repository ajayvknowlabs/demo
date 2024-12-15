from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory data storage
items = []

@app.route('/home', methods=['GET'])
def home():
    return jsonify({"status": True, 'messages':'Successfully project is running.'}), 200

# Route to fetch all items
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items), 200


# Route to fetch a specific item by ID
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    for item in items:
        if item['id'] == item_id:
            return jsonify(item), 200
    return jsonify({'error': 'Item not found'}), 404

# Route to add a new item
@app.route('/items', methods=['POST'])
def add_item():
    new_item = request.get_json()
    if 'id' not in new_item or 'name' not in new_item:
        return jsonify({'error': 'Invalid data'}), 400
    items.append(new_item)
    return jsonify(new_item), 201

# Route to update an existing item by ID
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    updated_item = request.get_json()
    for item in items:
        if item['id'] == item_id:
            item.update(updated_item)
            return jsonify(item), 200
    return jsonify({'error': 'Item not found'}), 404

# Route to delete an item by ID
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global items
    items = [item for item in items if item['id'] != item_id]
    return jsonify({'message': 'Item deleted'}), 200

if __name__ == '__main__':
    app.run(debug=True)
