import firebase_admin
from firebase_admin import credentials, firestore

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


def main():
    print("Listing team codes and progresses:\n")

    questions = database.collection("questions").stream()
    questions_legth = len(list(questions))

    teams = database.collection("teams").stream()

    for document in teams:
        team = document.to_dict()

        print(document.id, "[", end=" ")
        for i, question in enumerate(team["questions"]):
            if i < team["current"]:
                print("#", end=" ")
            elif question["revealed"]:
                print("?", end=" ")
            else:
                print("-", end=" ")

        print("]", " ", "REVEALS", "[", end=" ")
        for i in range(questions_legth):
            if i < team["reveals"]:
                print("#", end=" ")
            else:
                print("-", end=" ")

        print(
            "]",
            " ",
            "MISTAKES",
            " ".join(["#" for _ in range(team["guesses"] - team["current"])]),
            end=" ",
        )
        print()

    print("\nScraping finished successfully!")


if __name__ == "__main__":
    main()
