import os
from datetime import datetime
from app.connectors.s3 import upload_file_to_s3
from app.db_handler import read_database, write_database

def handle_uploaded_image(image, animal_name):
    """
    Processes the uploaded image and returns a S3 URL.
    """
    upload_date = datetime.now().strftime("%Y-%m-%d")
    unique_filename = f"{animal_name}_{upload_date}_{image.filename}"
    
    success = upload_file_to_s3(image, unique_filename)
    
    if not success:
        return None, None
    
    s3_url = f"https://{os.getenv('BUCKET_NAME')}.s3.amazonaws.com/{unique_filename}"
    return s3_url

def add_xray_data_to_database(xray_data, s3_url):
    """
    Adds the new xray data to the database and returns the updated data.
    """
    xrays = read_database()
    
    new_id = 1 if not xrays else max(animal['id'] for animal in xrays) + 1
    xray_data['id'] = new_id
    
    if 'xray_image_urls' not in xray_data:
        xray_data['xray_image_urls'] = []
    xray_data['xray_image_urls'].append(s3_url)
    
    xrays.append(xray_data)
    write_database(xrays)
    
    return xray_data


def get_xray_by_id(xray_id):
    xrays = read_database()
    
    xray = next((xray for xray in xrays if xray['id'] == xray_id), None)
    
    return xray


def update_xray_data(xray_id, xrays_data):
    xrays = read_database()
    for xray in xrays:
        if xray['id'] == xray_id:
            xray.update(xrays_data)
            write_database(xrays)
            return True, xray
    return False, None


def delete_xray_by_id(xray_id):
    xrays = read_database()
    xray_exists = any(xray['id'] == xray_id for xray in xrays)
    
    if not xray_exists:
        return False

    updated_xrays = [xray for xray in xrays if xray['id'] != xray_id]
    write_database(updated_xrays)

    return True

def get_xrays():
    xrays = read_database()
    return xrays