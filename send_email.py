import yagmail



def send_email_end(self):
    sender_email = "benedetta.zattera@gmail.com"
    receiver_email = 'topran.pp@gmail.com'
    subject = "Your lightsheet experiment is complete"
    # TODO: Add the password in the lightsheet computer
    sender_password = "benedetta123"

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
        attachments=None
    )