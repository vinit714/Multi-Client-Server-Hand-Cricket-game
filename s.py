import socket
import threading
import random
class game(threading.Thread):
	dict = {1:'1',2:'2',3:'3',4:'4',6:'6'}
	valid_input = ['1','2','3','4','6']
	opt = ['BAT','BOWL']
	dict_opt = {1:'BAT',2:'BOWL'}
	error = "invalid input pls try again"
	
	def __init__(self,name,c,addr):
		threading.Thread.__init__(self)
		self.name = name
		self.c = c
		self.addr = addr
		
	def run(self):
		self.user_name = self.c.recv(1024).decode("utf-8")
		print("Game started of user "+self.user_name)
		Stage = 0
		wic = 0
		score = 0
		target = 0
		wiceq = 0


		while (Stage==0):
			user_input = self.c.recv(1024).decode("utf-8")
			if user_input in game.opt:
				if user_input == "BAT":
					result = "BAT FIRST"
					Stage = 1
				else:
					result = "BOWL FIRST"
					Stage = 5
				print("sending to user "+self.user_name+" "+result)
				self.c.send(result.encode("utf-8"))
			else:
				self.c.send("invalid input pls try again".encode("utf-8"))

		while(Stage==1):
			while (wic < 2):
				user_input = self.c.recv(1024).decode("utf-8")
				if user_input in game.valid_input:
					c = random.choice([1,2,3,4,6])
					comp = game.dict[c]
					if user_input == comp:
						result = "Wicket!!  "
						wic = wic + 1
						if(wic==2):
							Stage = 2
							target = score
					else:
						addscore = int(user_input)
						score = score + addscore
						if(addscore==1):
							result = "Single    "
						elif(addscore==2):
							result = "double    "
						elif(addscore==3):
							result = "Triple    "
						elif(addscore==4):
							result = "Four!!    "
						else:
							result = "SIX!!     "
					
					strwic = str(wic)
					strscore = str(score)

					strtosend = result+self.user_name+" "+strscore+"-"+strwic
					strversion = str(strtosend)
					print("sending to user "+self.user_name+" "+result+" "+strscore+"-"+strwic)
					self.c.send(strversion.encode("utf-8"))

				else:
					self.c.send("invalid input pls try again".encode("utf-8"))

		while(Stage==2):

			user_input = self.c.recv(1024).decode("utf-8")
			if user_input in game.valid_input:
				result = "COMPUTER'S TURN TO BAT"
				Stage = 3
				score = 0
				wic = 0
				wiceq = 0
				print("sending to user "+self.user_name+" "+result)
				self.c.send(result.encode("utf-8"))
			else:
				self.c.send("invalid input pls try again".encode("utf-8"))

		while(Stage==3):
			while (score<target):
				while (wiceq < 2):
					user_input = self.c.recv(1024).decode("utf-8")
					if user_input in game.valid_input:
						c = random.choice([1,2,3,4,6])
						comp = game.dict[c]
						if user_input == comp:
							result = "Wicket!!  "
							wic = wic + 1
							wiceq = wiceq + 1
							if(wiceq==2):
								if(score==target):
									result = "DRAW!!"
									Stage = 4
								else:
									result = "YOU WIN!!"
									Stage = 4

						else:
							addscore = int(comp)
							score = score + addscore
							if(score>target):
								result = "COMPUTER WIN!! "
								Stage = 4
								wiceq = 2

							elif(addscore==1):
								result = "Single    "
							elif(addscore==2):
								result = "double    "
							elif(addscore==3):
								result = "Triple    "
							elif(addscore==4):
								result = "Four!!    "
							else:
								result = "SIX!!     "
						
						strwic = str(wic)
						strscore = str(score)

						strtosend = result+" "+strscore+"-"+strwic
						strversion = str(strtosend)
						print("sending to user "+"COMP "+self.user_name+" "+result+" "+strscore+"-"+strwic)
						self.c.send(strversion.encode("utf-8"))

					else:
						self.c.send("invalid input pls try again".encode("utf-8"))
		
		while(Stage==4):
			self.c.recv(1024).decode("utf-8")
			print("Game over with "+self.user_name)
			self.c.send("GAME OVER".encode("utf-8"))

		
		while(Stage==5):
			while (wic < 2):
				user_input = self.c.recv(1024).decode("utf-8")
				if user_input in game.valid_input:
					c = random.choice([1,2,3,4,6])
					comp = game.dict[c]
					if user_input == comp:
						result = "Wicket!!  "
						wic = wic + 1
						if(wic==2):
							Stage = 6
							target = score
					else:
						addscore = int(comp)
						score = score + addscore
						if(addscore==1):
							result = "Single    "
						elif(addscore==2):
							result = "double    "
						elif(addscore==3):
							result = "Triple    "
						elif(addscore==4):
							result = "Four!!    "
						else:
							result = "SIX!!     "
					
					strwic = str(wic)
					strscore = str(score)

					strtosend = result+"COMP"+" "+strscore+"-"+strwic
					strversion = str(strtosend)
					print("sending to user "+"COMP "+self.user_name+" "+result+" "+strscore+"-"+strwic)
					self.c.send(strversion.encode("utf-8"))

				else:
					self.c.send("invalid input pls try again".encode("utf-8"))

		while(Stage==6):

			user_input = self.c.recv(1024).decode("utf-8")
			if user_input in game.valid_input:
				result = "YOUR'S TURN TO BAT"
				Stage = 7
				score = 0
				wic = 0
				wiceq = 0
				print("sending to user "+self.user_name+" "+result)
				self.c.send(result.encode("utf-8"))
			else:
				self.c.send("invalid input pls try again".encode("utf-8"))

		while(Stage==7):
			while (score<target):
				while (wiceq < 2):
					user_input = self.c.recv(1024).decode("utf-8")
					if user_input in game.valid_input:
						c = random.choice([1,2,3,4,6])
						comp = game.dict[c]
						if user_input == comp:
							result = "Wicket!!  "
							wic = wic + 1
							wiceq = wiceq + 1
							if(wiceq==2):
								if(score==target):
									result = "DRAW!!    "
									Stage = 8
								else:
									result = "COMP WIN!! "
									Stage = 8

						else:
							addscore = int(user_input)
							score = score + addscore
							if(score>target):
								result = "YOU WIN"
								Stage = 8
								wiceq = 2

							elif(addscore==1):
								result = "Single    "
							elif(addscore==2):
								result = "double    "
							elif(addscore==3):
								result = "Triple    "
							elif(addscore==4):
								result = "Four!!    "
							else:
								result = "SIX!!     "
						
						strwic = str(wic)
						strscore = str(score)

						strtosend = result+self.user_name+" "+strscore+"-"+strwic
						strversion = str(strtosend)
						print("sending to user "+self.user_name+" "+result+" "+strscore+"-"+strwic)
						self.c.send(strversion.encode("utf-8"))

					else:
						self.c.send("invalid input pls try again".encode("utf-8"))

		while(Stage==8):
			self.c.recv(1024).decode("utf-8")
			print("Game over with "+self.user_name)
			self.c.send("GAME OVER".encode("utf-8"))

			

def Main():
	host = "127.0.0.1"
	port = 1234
	
	s = socket.socket()
	s.bind((host,port))
	
	s.listen(3)
	for i in range(3):
		print(str(i))
		c,addr = s.accept()
		print("connect with "+str(i))
		print("starting Game..... with "+str(i))
		game(str(i),c,addr).start()

if __name__ == "__main__":
	Main()