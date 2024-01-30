import firebase_admin, qrcode, random, json, re, os, math
from firebase_admin import credentials, firestore

NUMBER_OF_TEAMS = 5
FILES = ["./questions-one.json", "./questions-two.json"]


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
        "project_id": "kutdiak-74f58",
        "private_key_id": "53e3d639dcd818eeccda0d72e5fda28c4a6da348",
        "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQCrGzhN4XVceqzm\nWtutwmGKT5HquD/eeNTwJvsJdpUH2QvYS5r6qzJv1Fd2Lt2jQoUujC149SeHQt/X\nnQpyGJQjV6kd3JVBnARrag4+2+Uy5O+BRLPLDK0FNYmIvY92cgpig14YELDPBcKl\nZ6H9jk2FDKH8b18ra+NGr3xwkhbQWovQgPP3CEJ2NtfR+nOsyMWv8ORt8Wgoq6of\nPPgvpW5qGclXSIbnFKwwpSfUc4ML4falRt3uvuRrEfHWUb2fGJPg9BNOSqOKqGMV\nxi5ka3WN8uOR2R6jpSHNeok4AOUhSvX3E4ErdQtrFpDveEIJQ8DA/8172rkHQoi8\nhFk9qsVPAgMBAAECggEASOxZ679KAHb8F1TjyUNNxN+ypaGO/ubqgctrNBZI38Ze\nKPnX/DtYTJboC6NfrIPeNP9jJej9xsT2l3MDj6rv/7wNhH+NUSAINitGFP4syasO\ndD5ujfxCBTVS/2cirG1gBapNQN5kLGcdFNd9D45FdY3zv51Lpzrc6zRBSczJUlSB\nYAfEC8bYJOVKaautKzs0SGZcJVxS16i5mEbsfsN2PwocNq8QPKZ1PAGs6caGJrcy\npBJWbSbxlRZhApwtrLuxl9zjcl3Qy9+y1orupDnNpPSu1ni+efx7rnBNXz+Vjc18\ncdQYAftPdwZEXcXj2+oLsD+SqnPAC1WmPjRRrJJFIQKBgQDoX6qml0wd1uB19cYn\niyFgFUXXq0WgaylcxtxtWQu7QBAMDsNR40EQrRTLrhN6lrCFH5Ji/cx4t2UsTPwd\nC2AlrgYN2gdj/UouFneFGMqdTzViamIjFgz+07KA97H7M1Pi1eDpfhHqEk8qgkuO\nhS7ppoEprJh+kMEegRwravzTnwKBgQC8gNtlxHR6q4OqeBuPszBE12IiPNU5eXNL\nxMyv/3N/ijLYFb3CM7pd7VMlCwouVhwjwpwMvZbvBieymcs8USqxbCB7wAyhP+D5\nGVIm0upTRA/3x/SdJHCEeCCNxwppv02x77oPKp71S2sLpsufzYi9rQUuIl38ZyWl\nL37yc0IwUQKBgAeQHYjAgdyywql0L1fYImTzLEvBqkl3U2hOnJv+evBEPIF39Ylz\nwQle6L9cUgv6XZJnnacVJZOEPIm9k7MKTL3NNSs8PmNVuhVX69nsHaQTEOS8G6eS\nryeYEkY6SZOobwGB/oj67nBU2jjC9tyTnxxBrBCEKo5r/a0VfKo5GDN3AoGAR/zd\nzKuN4BsIGV3tCJ/h2yh17aVVuLFM+q6ZjMz9isN4T1VeNoASuDQeAJOKu89ex7lW\nZvcwYO/00RwypUJKD5+/eAMLz7jZbcfhu7noiwv/HR1bqXd1EOHfbMWKkH/iaAWp\nBIm+UucOZlC4irqvceBVjhzJz86EbeUJkgW6TUECgYAvpXeKCIvEpDaGV0QSLmoS\nsvlImTpwWEdcmIrCDUDWzuQK++rKYJcsSmu8PQqaKH0JheZHBcoRd4GiHdKxmD80\nbJJZn5aY4q+4JgMNpqr/wzhJo/HYHlYCBKfPOpey48ogdXySWPCHTEYvukMRA8FZ\npp3fP8jTSm4l4oMIoq8UNw==\n-----END PRIVATE KEY-----\n",
        "client_email": "firebase-adminsdk-slsw5@kutdiak-74f58.iam.gserviceaccount.com",
        "client_id": "112850582291090960359",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-slsw5%40kutdiak-74f58.iam.gserviceaccount.com",
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

    for questions_file in FILES:
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

        for _ in range(math.ceil(NUMBER_OF_TEAMS / len(FILES))):
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
            print("FILE", questions_file, "-", team_id, "-", questions[0]["id"])

    print("\nData feeded successfully!")


if __name__ == "__main__":
    main()
