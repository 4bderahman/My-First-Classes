class Mobile:
    def __init__(self, company_name, storage, serial_num, name, dual_sim, support_4k):
        self.company_name = company_name
        self.storage = storage
        self.serial_num = serial_num
        self.name = name
        self.dual_sim = dual_sim
        self.support_4k = support_4k

    def call(self, number):
        print(f"Calling {number} from {self.name}.")

    def send_message(self, number, message):
        print(f"Sending message to {number}: '{message}'.")

    def play_media(self, media_name):
        print(f"Playing '{media_name}' on {self.name}.")


mobile1 = Mobile("iPhone", 128, "XXX1234567890", "iPhone 13", False, True)
mobile1.call("06666666")
mobile1.send_message("06666666", "Hello, im abderrahman!")
mobile1.play_media("No roles modelz.mp3")
