import smtplib

def spam(subject,message,email):
	try:
		server = smtplib.SMTP('smtp.gmail.com',587)
		server.ehlo()
		server.starttls()
		server.login('unknownannei@gmail.com',r'unknownselva')
		server.sendmail('unknownannei@gmail.com',email,
			"Subject : {}\n\n{}".format(subject,message))
		server.quit()
		return "Success"
	except:
		raise EnvironmentError("Some error Occured!")
	

print("Welcome to UnknownAnnei Spam corporation")
print("Use \nfrom unknownannei import spam \nto send spams")
print("Copying of this work or misusing will lead to the feel of machetes on their necks")
print("Visit Saidapet and donate us!")
