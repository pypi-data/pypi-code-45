import smtplib

def spam(subject,message):
	server = smtplib.SMTP('smtp.gmail.com',587)
	server.login('unknownannei@gmail.com',r'unknownselva')
	server.sendmail('unknownannei@gmail.com','anupamkris13262@gmail.com',
		"Subject : {}\n\n{}".format(subject,message))
	server.quit()
	return "Success"

print("Welcome to UnknownAnnei Span corporation")
print("Use from unknownannei import spam to send spams")
print("Copying of this work or misusing will lead to the feel of machetes on their necks")
print("Visit Saidapet and donate us!")