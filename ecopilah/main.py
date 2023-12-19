from flask import Flask, request, jsonify
from PIL import Image
import numpy as np
from tensorflow.keras.models import load_model
import os
from google.cloud import storage

app = Flask(__name__)

# Load model
model = load_model('model.h5')  # Ganti 'model_path' dengan path model Anda

# inisialisasi dengan google cloud
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'ch2-pr636-credentials.json'
client = storage.Client()
bucket_name = 'waste-classifi-bucket'
bucket = client.get_bucket(bucket_name)

# Fungsi untuk memproses gambar dan melakukan klasifikasi
def predict_image(img_path):
    img = Image.open(img_path)
    img = img.resize((256, 256))  # Sesuaikan dengan ukuran input model Anda
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    predictions = model.predict(img_array)
    predicted_class = np.argmax(predictions[0])
    return predicted_class

# Endpoint untuk melakukan klasifikasi
@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify({'error': 'No image file provided'})

    image = request.files['image']
    
    # Simpan gambar sementara
    temp_path = 'temp.jpg'
    image.save(temp_path)
    
    # Upload gambar ke Google Cloud Storage
    blob = bucket.blob('predict/' + image.filename)  # Ganti dengan path yang sesuai di bucket Anda
    blob.upload_from_filename(temp_path)
    blob.make_public()

    # Lakukan klasifikasi
    predicted_class = predict_image(temp_path)

    # Hapus gambar sementara
    os.remove(temp_path)
    
    image_url_gcs = blob.public_url

    # Gantilah dengan label klasifikasi sesuai dengan model Anda
    labels = ['Organik', 'Non-Organik']
    result = {'class': labels[predicted_class], 'image_url_gcs' : image_url_gcs }

    return jsonify(result)

# Endpoint untuk memberikan respons "OK" saat GET dan menunjukkan koneksi ke bucket GCS
@app.route('/check', methods=['GET'])
def check_connection():
    try:
        # Coba mendapatkan daftar objek di bucket (dapat diubah sesuai kebutuhan Anda)
        blobs = list(bucket.list_blobs(max_results=1))
        return 'OK'
    except Exception as e:
        return f'Error: {str(e)}', 500

if __name__ == '__main__':
    app.run(debug=True)
