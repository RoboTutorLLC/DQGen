import sendgrid

client = sendgrid.SendGridClient('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')
message = sendgrid.Mail()

message.add_to("huiluo9527@gmail.com")
message.set_from("no-reply@dqgen.com")
message.set_subject("Sending with SendGrid is Fun")
message.set_html("and easy to do anywhere, even with Python")

client.send(message)