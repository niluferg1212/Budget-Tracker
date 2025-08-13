import csv

USER_FILE = "users.csv"

# Test: Otomatik kullanıcı ekle
def register_test_user():
    with open(USER_FILE, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["testuser", "test123"])

# Giriş fonksiyonu (güçlendirilmiş)
def login(username, password):
    with open(USER_FILE, newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) == 2:
                if row[0].strip() == username.strip() and row[1].strip() == password.strip():
                    return True
    return False

# Kullanıcıyı kayıt et (bir defaya mahsus)
register_test_user()

# Login denemesi
username_input = input("Kullanıcı adı: ")
password_input = input("Şifre: ")

if login(username_input, password_input):
    print("Giriş başarili!")
else:
    print("Giriş başarisiz.")