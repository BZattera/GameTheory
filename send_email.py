import yagmail



sender_email = "felsenberglab@gmail.com"
receiver_email = 'benedetta.zattera@gmail.com'
subject = "Your lightsheet experiment is complete"
# TODO: Add the password in the lightsheet computer
sender_password = "Flytrap.1"

yag = yagmail.SMTP(user=sender_email, password=sender_password)

body = [
    "Hey!",
    "\n",
    "Your lightsheet experiment has completed and was a success! Come pick up your little fish",
    "\n"
    "Always yours,",
    "fishgitbot"
]

yag.send(
    to=receiver_email,
    subject=subject,
    contents=body,
    attachments=r'C:\Users\zattbene\Documents\GitHub\GameTheory\user1.csv'
)

