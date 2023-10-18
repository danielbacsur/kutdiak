from firebase_admin import credentials, firestore
import firebase_admin
import qrcode
import random
import uuid
import json
import re
import os


def delete_all_files(directory):
    files = [
        f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))
    ]
    for file in files:
        os.remove(os.path.join(directory, file))


def generate_qr(url, file_name):
    qr = qrcode.QRCode(
        version=1,  # controls the size of the QR Code
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # controls the error correction used for the QR Code
        box_size=10,  # controls how many pixels each “box” of the QR code is
        border=4,  # controls how many boxes thick the border should be
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    img.save(file_name)


cred = credentials.Certificate(
    {
        "type": "service_account",
        "project_id": "kutdiak-69420",
        "private_key_id": "9e56c6daedef04427776b7c8b46bcf69af8d4ed6",
        "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC+bdgXcpkB8Of6\n3jdqrATV7xJkkhkEoObrr0JJBCIlBT3NKXS3H3gxQu8fkjKD1Inyg7k2SW5DrE1w\n3Z2C6kCO6ru0LWzUTGtojUI0BZAQNMCgsI/zQ+DnmHHyJamxbo1u7djc4DYEse8d\nsJHmSYqe98JdWRtf6RgGRVrw7uM58I4pOMRqYNqspI0yvTG7xdx5IaQaLzh4W/nY\nKz+raSa8YSZDavLCWC5PpBhnOPqo6/y6PgxJ2+UO2PGtOKSAVbNiaBt0UdwHYyiH\n/XS/9MCm0/xjPOM5pPywPYmQ+7u3lm8tvLfRxrcDv54GSAbdF1Nbn5ceyC/0CZn6\nog2JVqexAgMBAAECggEAGtb2jw9621guCiDJ5MIMCG8iw4QH/KwFABD6obnwahFc\nDY+bQLgxw5ewhl2fuw74xnKkZy9gWC9v1smVir8jjEEvZYzFewKuXNUUEKr8DByz\nTbK1B0944ouM+9ktGrH/QzRIzZDYbD77+c5KMhAJdrBq96c4gYMj/LZHxA+XfTHY\noc4/ZQvcqAn3mVL+wWmUGddIOtedZ1QdgljjyD8fh98wHdwpFvtwC5F/MGwdjtTU\ngUB050GqG9yRjZ1brYZYcd25BpsYnX0IyiZ1BDF1WWzozaoD5QW4L1DHt5HvDq+6\nTl9LwPN1/n4yHMwJXeUXJTiZtFg7ZLfQF9cfJP63NQKBgQD/UTP1BUVJbBIcKtGi\ngFG4ceQZXj6Vw5d1hAp3MaYkLjHtqFb/tU/eAyqdLdnSs4Rg2cQHq1CNjHj2Wiul\nSI1EMRaba9LuPHLYlMsthU1eEmYxHy1cFKVtJGb+vt4kfaSNCArPNwkZh42mNsdb\n4bDibNQPD5XEfRsKDqvQKIUcvwKBgQC+8DeM0PdE+/0gCmz8Dmh8gmvZ4jfa9+fi\noPEjWR3WRH/CmHcO7Yi2+zNCWx6jEYY5Z48MlNQVJViK78Bw6BM1kW2T+oY2MeFr\n/fh1/k5SrMFRzfIpomPTla1++hb6LZcQEU7aYUhF4WdbePkxu4FZ1n8RouPUD5sl\ner3eXoWnjwKBgQCmf1v0oxVGBjXhLIM9B5VDRPJNIMqLe9ufhRYWGMiRu5ZPt4HU\ni3aj/0ig66+q2eqwBhLyNWP4iuyvKqpfxOpq1+A4Rp5tQfpbBt1guBd2C2WdDwnT\njJs8i4qnAe13un++gMoby3YhseZLyFlFr+5cGkBH+g/e7P7fFiYxPttfnQKBgGql\nh5F6gjIgwVAtIpRig8/PlOfc56/BOd6mYCmLNBQirG2HdTB8UhlKE2ZjuKgCOMNF\naWvwkMjC1EK+CPHHXjtUYC0ACAirMap871MQWLTq0wubCUBh+HoMpxw+Galg33hV\nAoMNRS3q6Sz5U86IWYZRPSYfojsnAFQdy4ExsFtXAoGATC+b18qzr+SO7KePWkQ7\niyjoOOQYxBRHXDEfmngaBXepqy5/+XjpmZEk2LzcvBUjf1cDEuRrxH76IfQNQkJM\nsxwfu93Lm/NkT8rqPhEK41IrZALwz+ZZE83cV4WS0nllUgCzOSPmZHfXVUJ+tqe3\nzwSuXE/q+/CGQV97ZWxLjKo=\n-----END PRIVATE KEY-----\n",
        "client_email": "firebase-adminsdk-j78dj@kutdiak-69420.iam.gserviceaccount.com",
        "client_id": "113198440879925115349",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-j78dj%40kutdiak-69420.iam.gserviceaccount.com",
        "universe_domain": "googleapis.com",
    }
)
firebase_admin.initialize_app(cred)

db = firestore.client()

teams_docs = db.collection("teams").stream()
for doc in teams_docs:
    doc.reference.delete()

questions_docs = db.collection("questions").stream()
for doc in questions_docs:
    doc.reference.delete()

script_dir = os.path.dirname(os.path.abspath(__file__))

relative_path = "./questions.json"
full_path = os.path.join(script_dir, relative_path)

delete_all_files(script_dir + "/images/")


with open(full_path, "r") as file:
    data = json.load(file)

questions_data = data["questions"]

for question in questions_data:
    question["id"] = str(uuid.uuid4())
    question["revealed"] = False
    db.collection("questions").document(question["id"]).set(question)

n = 40
for i in range(n):
    team_code = str(random.randint(100000, 999999))
    random.shuffle(questions_data)
    db.collection("teams").document(team_code).set(
        {"questions": questions_data, "current": 0, "name": "", "id": team_code}
    )

print("Data filled successfully!")


for question in questions_data:
    generate_qr(
        "https://kutdiak.danielbacsur.dev/question/" + question["id"],
        script_dir
        + "/images/"
        + re.compile(r'[\/:*?"<>|]').sub("", (question["question"].strip() + ".png")),
    )
