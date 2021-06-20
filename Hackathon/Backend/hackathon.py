import email
import getpass, imaplib
import os
import sys
import sqlite3
import datetime
import creds
from PIL import Image
import pytesseract
import argparse
import cv2
import os

def imageDownloader():
	files = []
	detach_dir = '.'
	if 'attachments' not in os.listdir(detach_dir):
		os.mkdir('attachments')

	userName = creds.username
	passwd = creds.emailpass

	imapSession = imaplib.IMAP4_SSL('imap.gmail.com')
	typ, accountDetails = imapSession.login(userName, passwd)
	if typ != 'OK':
		print('Not able to sign in!')
		raise

	imapSession.select('Hackathon')

	typ, data = imapSession.search(None, 'ALL')
	if typ != 'OK':
		print('Error searching Inbox.')
		raise

	# Iterating over all emails
	for msgId in data[0].split():
		typ, messageParts = imapSession.fetch(msgId, '(RFC822)')
		if typ != 'OK':
			print('Error fetching mail.')
			raise

		emailBody = messageParts[0][1]
		mail = email.message_from_bytes(emailBody)
		for part in mail.walk():
			if part.get_content_maintype() == 'multipart':
				# print part.as_string()
				continue
			if part.get('Content-Disposition') is None:
				# print part.as_string()
				continue
			fileName = part.get_filename()

			if bool(fileName):
				filePath = os.path.join(detach_dir, 'attachments', fileName)
				if not os.path.isfile(filePath) :
					print(fileName)
					files.append(fileName)
					fp = open(filePath, 'wb')
					fp.write(part.get_payload(decode=True))
					fp.close()
	imapSession.close()
	imapSession.logout()
	return files


def picToText(files):
	conn = sqlite3.connect("test.db")
	c = conn.cursor()
	now = datetime.datetime.now()
	mdy = str(now.month) + "/" + str(now.day) + "/" + str(now.year)

	for x in files:
		path = os.getcwd() + "/attachments/" + x
		print(path)
		img = cv2.imread(path)
		img = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
		#image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		img = cv2.blur(img,(5,5))
		cv2.threshold(img,127,255,cv2.THRESH_BINARY)
		#edges = cv2.Canny(img,100,200)
		img_new = Image.fromarray(img)
		#filename = "{}.png".format(os.getpid())
		#cv2.imwrite(x, img)
		text = pytesseract.image_to_string(img_new, lang="eng")
		#os.remove(x)
		print(text)
		print("-------------------")
		transformText = text.replace('\n', ' ').replace('\r', ' ').split(" ")
		prices = []
		for y in transformText:
			try:
				float(y)
				prices.append(float(y))
			except:
				pass
		halfway = int(len(prices)/2)
		prices = prices[halfway:]
		price = max(prices)
		c.execute('''INSERT INTO receipts VALUES(?,?,?) ''', (mdy,x,price))
	conn.commit()

if __name__ == "__main__":
	files = imageDownloader()
	picToText(files)








