import asyncio

import aiohttp


async def snap_discord_webhook(webhooker_url):
    async with aiohttp.ClientSession() as session:
        async with session.delete(url=webhooker_url) as response:
            if response.status == 204:
                print("Webhook successfully deleted!")
            elif response.status == 404:
                print("Webhook not found!")
            elif response.status == 429:
                print("You are currently being ratelimited! Try again later")
            else:
                print(f"Failed to send message. Status code: {response.status}")


async def send_discord_webhook(webhook_url, message):
    data = {"content": message}
    async with aiohttp.ClientSession() as session:
        while True:
            async with session.post(url=webhook_url, data=data) as response:
                if response.status == 204:
                    print("Message sent!")
                elif response.status == 404:
                    print("Webhook not found!")
                elif response.status == 429:
                    print("You are currently being ratelimited! Try again later")
                else:
                    print(f"Failed to send message. Status code: {response.status}")


async def main():
    while True:
        print('''
▗▖  ▗▖ ▗▄▖ ▗▄▄▄  ▗▄▄▄▖    ▗▄▄▖▗▖  ▗▖    ▗▄▄▖ ▗▄▄▄▖▗▄▄▄   ▗▄▄▖▗▖   ▗▄▄▄▖▗▖  ▗▖▗▄▄▄▖
▐▛▚▞▜▌▐▌ ▐▌▐▌  █ ▐▌       ▐▌ ▐▌▝▚▞▘     ▐▌ ▐▌▐▌   ▐▌  █ ▐▌   ▐▌     █  ▐▛▚▞▜▌▐▌   
▐▌  ▐▌▐▛▀▜▌▐▌  █ ▐▛▀▀▘    ▐▛▀▚▖ ▐▌      ▐▛▀▚▖▐▛▀▀▘▐▌  █  ▝▀▚▖▐▌     █  ▐▌  ▐▌▐▛▀▀▘
▐▌  ▐▌▐▌ ▐▌▐▙▄▄▀ ▐▙▄▄▖    ▐▙▄▞▘ ▐▌      ▐▌ ▐▌▐▙▄▄▖▐▙▄▄▀ ▗▄▄▞▘▐▙▄▄▖▗▄█▄▖▐▌  ▐▌▐▙▄▄▖
                                                                                  
        ''')
        print("\nDiscord Webhook Trollinator v0.1")
        print("\nMade By TheMrRedSlime!")
        print("\nMenu:")
        print("1. Delete Webhook")
        print("2. Spam Webhook")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("Webhook Deleter!")
            webhooker_url = input("Enter the Discord webhook URL: ")
            await snap_discord_webhook(webhooker_url)

        elif choice == "2":
            print("Webhook Spammer!!!")
            webhook_url = input("Enter the Discord webhook URL: ")
            message = input("Enter the message you want to send: ")
            await send_discord_webhook(webhook_url, message)

        elif choice == "0":
            print("Webhook Troller Exiting")
            print("Thank you for using Webhook Troller v0.1")
            break

        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Webhook Troller Exiting")
        print("Thank you for using Webhook Troller v0.1")

