from flask import Flask, request, jsonify, render_template
import sqlite3

app = Flask(__name__)


# # Simple Home Route
# @app.route('/')
# def home():
#     return "Hello, Flask! Your API is running."

# Database Connection
def connect_db():
    conn = sqlite3.connect('buses.db')  
    conn.row_factory = sqlite3.Row
    return conn

# Home Route to Render HTML Page
@app.route('/')
def home():
    return render_template('index.html')

# Read Buses (Get all buses and routes)
@app.route('/buses', methods=['GET'])
def get_buses():
    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM buses")
        buses = cursor.fetchall()
        return jsonify([dict(bus) for bus in buses])
    except Exception as e:
        return jsonify({'message': 'Error fetching buses', 'error': str(e)}), 400

# Create a Bus (Post a new bus route)
@app.route('/buses', methods=['POST'])
def add_bus():
    try:

        if not request.is_json:
            return jsonify({'message': 'Invalid Content-Type header, expected application/json'}), 400
        data = request.json
        print("Received JSON:", data)

        # Validate that all necessary fields are present in the request
        if 'bus_number' not in data or 'bus_type' not in data or 'capacity' not in data or 'status' not in data or 'route_id' not in data:
            return jsonify({'message': 'Missing required fields'}), 400
        
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO buses (bus_number, bus_type, capacity, status, route_id, route_name, start_location, end_location) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                       (data['bus_number'], data['bus_type'], data['capacity'], data['status'], data['route_id'], data['route_name'], data['start_location'], data['end_location']))
        conn.commit()
        return jsonify({'message': 'Bus added successfully'}), 201
    except Exception as e:
        print(f"Error: {e}") 
        return jsonify({'message': 'Error adding bus', 'error': str(e)}), 400



# Update a Bus (Update details of a bus route)
@app.route('/buses/<int:bus_id>', methods=['PUT'])
def update_bus(bus_id):
    try:
        data = request.json
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("UPDATE buses SET bus_number=?, bus_type=?, capacity=?, status=?, route_id=?, route_name=?, start_location=?, end_location=? WHERE bus_id=?",
                       (data['bus_number'], data['bus_type'], data['capacity'], data['status'], data['route_id'], data['route_name'], data['start_location'], data['end_location'], bus_id))
        conn.commit()
        return jsonify({'message': 'Bus updated successfully'})
    except Exception as e:
        return jsonify({'message': 'Error updating bus', 'error': str(e)}), 400

# Delete a Bus (Remove a bus route)
@app.route('/buses/<int:bus_id>', methods=['DELETE'])
def delete_bus(bus_id):
    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM buses WHERE bus_id=?", (bus_id,))
        conn.commit()
        return jsonify({'message': 'Bus deleted successfully'})
    except Exception as e:
        return jsonify({'message': 'Error deleting bus', 'error': str(e)}), 400
    
# to fetch all available routes
@app.route('/routes', methods=['GET'])
def get_routes():
    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("""select * from buses;""")
        routes = cursor.fetchall()
        return jsonify([dict(route_id) for route_id in buses])
    except Exception as e:
        return jsonify({'message': 'Error fetching routes', 'error': str(e)}), 400


if __name__ == '__main__':
    app.run(debug=True)
