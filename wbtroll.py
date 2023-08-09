import requests

def snap_discord_webhook(webhooker_url):
    response = requests.delete(webhooker_url)

    if response.status_code == 204:
        print("Webhook deleted successfully!")

def send_discord_webhook(webhook_url, message):
    data = {
        "content": message
    }
    while True:
        response = requests.post(webhook_url, json=data)

        if response.status_code == 204:
            print("Message sent successfully!")
        else:
            print(f"Failed to send message. Status code: {response.status_code}")


def main():
    while True:
        print("\nDiscord Webhook Trollinator vTesT")
        print("\nMade By TheMrRedSlime!")
        print("\nMenu:")
        print("1. Delete Webhook")
        print("2. Spam Webhook")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("Webhook Deleter!")
            webhooker_url = input("Enter the Discord webhook URL: ")
            snap_discord_webhook(webhooker_url)

        elif choice == "2":
            print("Webhook Spammer!!!")
            webhook_url = input("Enter the Discord webhook URL: ")
            message = input("Enter the message you want to send: ")
            send_discord_webhook(webhook_url, message)

        elif choice == "0":
            print("Webhook Troller Exiting")
            print("Thank you for using Webhook Troller vTesT")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
