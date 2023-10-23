import firebase_admin, qrcode, random, json, re, os
from firebase_admin import credentials, firestore

NUMBER_OF_TEAMS = 10

def remove_files(directory: str) -> None:
    files = [
        f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))
    ]
    for file in files:
        os.remove(os.path.join(directory, file))


def remove_documents(collection: str) -> None:
    documents = database.collection(collection).stream()
    for document in documents:
        document.reference.delete()


def generate_qr(url, file_name):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(file_name)


credentials = credentials.Certificate(
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
firebase_admin.initialize_app(credentials)
database = firestore.client()

absolute_path = os.path.dirname(os.path.abspath(__file__))




def main():
    # Remove every document and generated images
    remove_documents("teams")
    remove_documents("questions")
    remove_files(absolute_path + "/images/")

    print("Listing team codes and task ids:\n")

    for questions_file in ["./questions-one.json", "./questions-two.json"]:
        questions_path = os.path.join(absolute_path, questions_file)

        # Open questions.json file
        with open(questions_path, "r", encoding="utf-8") as file:
            questions = json.load(file)["questions"]

        # Upload questions to firestore
        for question in questions:
            database.collection("questions").document(question["id"]).set(question)

        # Generate QR codes
        for question in questions:
            generate_qr(
                "https://kutdiak.danielbacsur.dev/question/" + question["id"],
                absolute_path
                + "/images/"
                + re.compile(r'[\/:*?"<>|]').sub(
                    "", (question["image"].replace("images/", "").strip())
                ),
            )


        for i in range(2):
            team_id = str(random.randint(100000, 999999))
            team_name = ""
            team_current = 0
            team_reveals = 0
            team_guesses = 0
            team_document = {
                "id": team_id,
                "name": team_name,
                "current": team_current,
                "questions": questions,
                "reveals": team_reveals,
                "guesses": team_guesses,
            }

            database.collection("teams").document(team_id).set(team_document)
            print(team_id, "-", questions[0]["id"])

    print("\nData feeded successfully!")


if __name__ == "__main__":
    main()
