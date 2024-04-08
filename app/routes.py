from datetime import datetime
from flask import Blueprint, request, jsonify
from app.services import add_xray_data_to_database, delete_xray_by_id, get_xray_by_id, get_xrays, handle_uploaded_image, update_xray_data

main = Blueprint('main', __name__)

@main.route('/xrays', methods=['GET'])
def get_all_xrays():
    xrays = get_xrays()
    return jsonify(xrays), 200

@main.route('/upload-xray', methods=['POST'])
def upload_xray():
    if 'image' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    image = request.files['image']
    if image.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    animal_data = request.form.to_dict()
    animal_name = animal_data.get('name', 'unknown')
    
    s3_url = handle_uploaded_image(image, animal_name)
    
    if not s3_url: 
        return jsonify({'error': 'Failed to upload file to S3'}), 500
    
    updated_animal_data = add_xray_data_to_database(animal_data, s3_url)
    
    return jsonify(updated_animal_data), 201

@main.route('/xray/<int:xray_id>', methods=['GET'])
def get_xray(xray_id):
    xray = get_xray_by_id(xray_id)
    if xray is None:
        return jsonify({'error': 'Xray not found'}), 404
    
    return jsonify(xray), 200

@main.route('/xray/<int:xray_id>', methods=['PUT'])
def update_xray(xray_id):
    is_success, xray = update_xray_data(xray_id, request.form)
    if is_success:
        return jsonify(xray), 200
    return "X-Ray not found.", 404

@main.route('/xray/<int:xray_id>', methods=['DELETE'])
def delete_xray(xray_id):
    is_success = delete_xray_by_id(xray_id)
    if is_success:
        return '', 204 
    return jsonify({'error': 'X-ray not found'}), 404
