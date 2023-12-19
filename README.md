1. CLone repository ke komputer anda
2. download model h5 disini https://drive.google.com/file/d/14i4fYDo_Sa6_ZU6gU86kyEiy_HPcddo7/view?usp=sharing
3. kodingan ini menggunakan Google cloud Storage , jadi kalian harus mempunyai gcs bucket sendiri dengan nama "waste-classifi-bucket", buat folder di bucket tersebut namanya "predict". dan kalian juga harus mempunyai credentials file , ubah nama file tersebut menjadi "ch2-pr636-credentials.json"
4. setelah itu kalian install semua dependencies dengan cara buka terminal lalu ketikan pip install -r requirements.txt
5. jika sudah , run aplikasi dengan ketik python main.py
6. secara default , server akan berjalan di localhost dengan port 5000 , lalu open di browser http://localhost:5000/ , untuk tampilan awal
7. http://localhost:5000/check , untuk mengecek bucket , jika berhasil akan muncul OK
8. http://localhost:5000/predict , untuk mengupload gambar sammpah.
