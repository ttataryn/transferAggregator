from flask import *
from tweepy import OAuthHandler
import tweepy
import pandas as pd
import datetime, time
import requests
app = Flask(__name__)

def before_request():
    app.jinja_env.cache = {}

@app.route('/test')
def testPage():
	return render_template('/test.html')

@app.route('/graphs')
def graphs():
	return render_template('/graphs.html')
	
@app.route('/home')
def homepage():

	return render_template('/home.html')

@app.route('/transfer-reliability')
def tReliability():

	
	return render_template('/tReliability.html')
	
@app.route('/statistics')
def stats():
	winterDict = pd.DataFrame([['The Guardian', '5', '7', '71.4%'], ['Daily Telegraph', '3', '6', '50%'], ['Daily Mail', '11', '17', '64.7%'],
	['The Times', '3', '4', '75%'], ['Daily Mirror', '9', '28', '32.14%'], ['Daily Express', '1','9', '11.11%'],
	['Sun Sport', '1', '10', '10%'], ['Daily Star', '2', '10', '20%'], ['Sky Sports', '9', '14', '64.28%']], columns= ['Source', 'Correct', 'Total', 'Accuracy'])
	summerDict = pd.DataFrame([['Independent', '8', '20', '40%'], ['Evening Standard', '5','10','50%'],
	['Daily Telegraph', '24','46','52.17%'], ['The Guardian', '14', '16', '87.5%'], ['Manchester Evening News', '10','16', '62.5%'],
	['Daily Mail', '26','56', '46.42%'], ['Daily Star', '19', '43','44.19%'], ['The Times' ,'5', '8', '62.5%'], ['Daily Mirror', '47', '95', '49.4%'],
	['L\'Equipe', '6','14', '42.86%'], ['BBC Sport' ,'5', '5', '100%'], ['Daily Express', '17', '46','36.96%'], ['Sky Sports', '61','72','84.72%'], ['Sun Sport', '31','77', '40.26%']], columns = ['Source', 'Correct', 'Total', 'Accuracy'])
	sumWint1617Dict = pd.DataFrame([['The Guardian', '9','11','81.81%'], ['Manchester Evening News', '8','12','66.67%'], ['Daily Telegraph','17','24','70.83%'],
		['Daily Mail','30','45','66.67%'], ['Daily Star','15','26','57.69%'],['The Times','8','9','88.89%'], ['Daily Mirror','26','52','50%'], ['Daily Express','13','22','59.09%'],
		['Sky Sports','33','38','86.84%'],['Sun Sport','33','62','53.23%']], columns= ['Source', 'Correct','Total','Accuracy'])
	reporterDict = pd.DataFrame([['Mark Ogden','8','12','66.67%'],['Simon Stone','23','28','82.14%'], ['John Cross','24','38','63.16%'],['David Ornstein', '15','16','93.75%'],
		['John Percy',' 16','17', '94.12%'], ['Duncan Castles','8','20','40%'],['Ed Aarons', '20','29', '68.97%'], ['Lyall Thomas','17','23','73.91'],
		['Paul Joyce','11','13','84.62%'], ['James Ducker','17','20','85%'],['Keith Downie','9','12','75%']], columns =['Source', 'Correct', 'Total', 'Accuracy'])
	combinedDict = pd.DataFrame([['The Guardian','28','34','82.25%'], ['Daily Telegraph', '44','76','57.89%'], ['The Times','16','21','76.19%'],
		['Daily Mail','67','118','56.77%'], ['Daily Mirror','82','175','46.86%'],['Daily Express','31','77','40.26%'],['Sky Sports',
		'103','124','83.06%'],['Manchester Evening News','18','28','64.29%'], ['Daily Star','36','79','45.57%'],
		['Sun Sport','55','149','36.91%']], columns = ['Source','Correct','Total','Accuracy'])
	firstTransfers = pd.DataFrame([['Krychowiak','West Brom','John Percy (Telegraph)'],['Kevin Wimmer','Stoke City','Stoke Sentinel'],
		['Clucas','Swansea','BBC Sport'],['Davinson Sanchez', 'Tottenham','Sky Sports'],['Chris Wood','Burnley','Phil Hay (Yorkshire Post)'],
		['Joselu','Newcastle','Andy Goldstein (talkSPORT)'],['Jese','Stoke City','AS English'],['Gareth Barry','West Brom','Simon Jones (Daily Mail)'],
		['Martins Indi','Stoke City','Rob Dorsett (Sky Sports)'],['Lemina','Southampton','Kaveh Solhekol'],['Choupo-Moting','Stoke City','Darren Lewis (Daily Mirror)'],
		['Merino','Newcastle','Marca'],['Phil Bardsley','Burnley','Alan Nixon (Sun Sport)']], columns = ['Player Name','EPL Team','First to Report'])
	# winterDict['Accuracy'] = winterDict['Accuracy'].apply(lambda x: "<a href='%s'> a </a>" % (x))
	winterDict = winterDict.to_html(escape= False)
	summerDict = summerDict.to_html()
	reporterDict = reporterDict.to_html()
	sumWint1617Dict = sumWint1617Dict.to_html()
	combinedDict = combinedDict.to_html()
	firstTransfers = firstTransfers.to_html()
	return render_template('/stats.html',table = winterDict, table2 = summerDict, table3 = reporterDict, table4 =sumWint1617Dict, table5 = combinedDict,
		table6 = firstTransfers)

@app.route('/rumor-aggregator')
def rAggregator():

	return render_template('/rAggregator.html')

# @app.route('/results', methods =['POST'])
# def getOtherTweets():
# 	teamName = request.form['teamForm']
# 	print(teamName)
# 	consumer_key = '8cmlVBTRHLbTglTMtyDd0vaNz'
# 	consumer_secret = 'p5HwgFVUv1e1VaBxeKC4vrnvQ6bVlNSKtrGOqvbK5MItrxd6qb'
# 	access_token = '363384668-27HKI7o49IlnYC3LV6T4jNpe82YoZ1f9YqNKVC2I'
# 	access_secret = 'x2YmC8AfzAvZ5r6E7ean7Fve8SHnlGimcyiHcV73k1gFh'
# 	auth = OAuthHandler(consumer_key, consumer_secret)
# 	auth.set_access_token(access_token, access_secret)
# 	api = tweepy.API(auth)
# 	user = api.get_user('ballondebruyne')
# 	if request.method == "POST":
# 		#teamName = t
# 		page = 1
# 		deadend = False 
# 		dfDict = {}
# 		data = {'Username': [], 'Tweet Text': [], 'Time': [], 'URL': [] }
# 		i = 0
# 		while True:
# 			otherSourcesList = ["BBCSport", "SkySportsNews", "TeleFootball", "guardian_sport", "@MattHughesTimes","Independent", "MirrorFootball", "ESPNFC","TheSunFootball",
# 			"garyjacob", "LukeEdwardsTele"]
# 			for reporter in otherSourcesList:
# 				user = reporter
# 				tweets = api.user_timeline(screen_name = user, page = page)
# 				for tweet in tweets:
# 					if (datetime.datetime.now() - tweet.created_at).days < 1:
# 						badText = tweet.text
# 						text = badText.encode("ascii", "ignore")
# 						text = text.decode('utf-8')
# 						print(text)
# 						date = tweet.created_at
# 						userName = tweet.author._json['screen_name']
# 						ID = tweet.id
# 						URL = "https://www.twitter.com/%s/status/%d" % (userName, ID)
# 						tweetTerms = {"Man City": ["City","MCFC""Manchester City", "manchester city", "man city", "@ManCity", "Man City", "mcfc"],
# 						"Tottenham": ["@SpursOfficial", "Spurs", "spurs", "tottenham", "hotspurs", "thfc","THFC"], "Arsenal": ["Arsenal", "gunners","@Arsenal","afc"],
# 						"Chelsea": ["Chelsea","cfc","@ChelseaFC"], "Liverpool": ["Liverpool", "lfc", "LFC"], "Man United": ["Man United", "Manchester United",
# 						"united","mufc", "@ManUtd","United","MUFC"], "Everton": ["Everton", "EFC","efc"], "Southampton": ["@SouthamptonFC", "Southampton", "SaintsFC"], "Leicester City": 
# 						["lcfc", "leicester", "leicester city"], "Watford": ["WatfordFC", "Watford", "watfordfc"], "Brighton": ["OfficialBHAFC", "BHAFC", "Brighton"],
# 						"West Ham": ["West Ham United", "West Ham FC", "West Ham", "@WestHamUtd", "whufc"], "West Brom": ["West Bromwich Albion", "West Brom", "@WBA", "wba"],
# 						"Newcastle United": ["Newcastle", "nufc", "Newcastle United"], "Stoke City": ["Stoke", "Stoke City", "stokecity","scfc"], "Crystal Palace": [
# 						"Crystal Palace", "cpfc"], "Swansea": ["Swansea","swansea city", "SwansOfficial", "swans"], "Burnley": ["Burnley","BurnleyOfficial"],
# 						"Huddersfield Town": ["Huddersfield","huddersfield town", "htafcdotcom","htafc"]}
# 						whichTeam = tweetTerms[teamName]
						
# 						if any(word in text for word in whichTeam):
# 							data['URL'].append(URL)
# 							data['Time'].append(date)
# 							data['Tweet Text'].append(text)
# 							data['Username'].append(userName)

# 							dfDict[i]= pd.DataFrame(data)
# 					else: #tweets are done now
# 						deadend = True
# 				if not deadend:
# 					page+=1
# 					time.sleep(5)
# 			if( not dfDict):
# 				print("nothing here")
# 				frame = "Sorry there are no tweets for your team available right now"
# 				#frame = frame.to_html(escape = False, classes="nothingHere")
# 				return render_template('/results.html', nothingHere=frame)
# 			else:
# 				frame = dfDict[0]
# 				#frame['URL'] = frame['URL'].apply(lambda x: "<a href='%s'> a </a>" % (x) )
# 				frame = frame.to_html(escape = False, classes="nothingHere")
# 				return render_template('/results.html', table = frame, teamName = teamName)


@app.route('/results', methods=['POST'])
def getTweets():
	print("getTWeets")
	consumer_key = '8cmlVBTRHLbTglTMtyDd0vaNz'
	consumer_secret = 'p5HwgFVUv1e1VaBxeKC4vrnvQ6bVlNSKtrGOqvbK5MItrxd6qb'
	access_token = '363384668-27HKI7o49IlnYC3LV6T4jNpe82YoZ1f9YqNKVC2I'
	access_secret = 'x2YmC8AfzAvZ5r6E7ean7Fve8SHnlGimcyiHcV73k1gFh'
	auth = OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_secret)
	api = tweepy.API(auth)
	user = api.get_user('ballondebruyne')
	print("hello")

	if request.method == "POST":
		teamName = request.form['teamForm']
		page = 1
        deadend = False 
        dfDict = {}
        data = {'Username': [], 'Tweet Text': [], 'Time': [], 'URL': [] }
        i = 0
        x=0
        while True:
			teamDict = {"Tottenham": ["DeadlineDayLive","BenPearceSpurs", "Dan_KP", "SkySportsLyall", "ed_aarons", "bbcsport_david"], "Man United": ["DeadlineDayLive","CraigNorwood", "TelegraphDucker", "DuncanCastles", "MarkOgden_","SimonPeach", "sistoney67"],
			"Man City": ["DeadlineDayLive","TelegraphDucker", "Sammy_Goal", "SunMartinB", "MullockSMirror", "MarkOgden_", "sistoney67"], "Liverpool": ["DeadlineDayLive","LivEchoLFC","_pauljoyce", "JamesPearceEcho", "_ChrisBascombe", "MelissaReddy_"],
			"Everton": ["DeadlineDayLive", "_pauljoyce", "_ChrisBascombe"], "Newcastle United": ["SkySports_Keith", "CaulkinTheTimes", "CraigHope_DM", "Lee_Ryder"], "Chelsea": ["DeadlineDayLive","Matt_Law_DT", "johncrossmirror", "bbcsport_david", "TelegraphDucker"],
			"Arsenal": ["DeadlineDayLive","bbcsport_david", "TelegraphDucker", "amylawrence71"], "Watford": ["DeadlineDayLive", "AdamLeventhal"]}
			if( not teamDict[teamName]):
				frame = "Sorry there are no tweets for your team available right now"
				break
			else:
				whichUsers = teamDict[teamName]
			for reporter in whichUsers:
				user = reporter
				print(user)
				tweets = api.user_timeline(screen_name = user, page = page)
				for tweet in tweets:
					if (datetime.datetime.now() - tweet.created_at).days < 1:
						badText = tweet.text
						text = badText.encode("ascii", "ignore")
						text = text.decode('utf-8')
						#print("first", text)
						date = tweet.created_at
						userName = tweet.author._json['screen_name']
						#print(userName)
						ID = tweet.id
						URL = "https://www.twitter.com/%s/status/%d" % (userName, ID)
						tweetTerms = {"Man City": ["City", "MCFC","Manchester City", "manchester city", "man city", "@ManCity", "Man City", "mcfc"],
						"Tottenham": ["@SpursOfficial", "Spurs", "spurs", "tottenham", "hotspurs", "thfc"], "Arsenal": ["Arsenal", "gunners","@Arsenal","afc"],
						"Chelsea": ["Chelsea","cfc","@ChelseaFC"], "Liverpool": ["Liverpool", "lfc", "LFC"], "Man United": ["United", "MUFC","Man United", "Manchester United",
						"united","mufc", "@ManUtd"], "Everton": ["Everton", "EFC", "efc","Toffees"], "Southampton": ["@SouthamptonFC", "Southampton", "SaintsFC"], "Leicester City": 
						["LCFC", "leicester", "leicester city","Leicester"], "Watford": ["WatfordFC", "Watford", "watfordfc"], "Brighton": ["OfficialBHAFC", "BHAFC", "Brighton"],
						"West Ham": ["West Ham United", "West Ham FC", "West Ham", "@WestHamUtd", "WHUFC","whufc"], "West Brom": ["West Bromwich Albion", "West Brom", "@WBA", "wba"],
						"Newcastle United": ["Newcastle", "NUFC", "Newcastle United", "nufc"], "Stoke City": ["Stoke", "Stoke City", "stokecity","scfc"], "Crystal Palace": [
						"Crystal Palace", "cpfc"], "Swansea": ["Swansea","swansea city", "SwansOfficial", "swans"], "Burnley": ["Burnley","BurnleyOfficial"],
						"Huddersfield Town": ["Huddersfield","huddersfield town", "htafcdotcom","htafc"]}
						whichTeam = tweetTerms[teamName]
						
						if any(word in text for word in whichTeam):
							data['URL'].append(URL)
							data['Time'].append(date)
							data['Tweet Text'].append(text)
							data['Username'].append(userName)
							i+=1
							dfDict[x]= pd.DataFrame(data)
							print("Yes!", text)
					else: #tweets are done now
						deadend = True
				if not deadend:
					page+=1
					time.sleep(5)
			if i <10:
				while True:
					otherSourcesList = ["BBCSport", "SkySportsNews", "TeleFootball", "guardian_sport","TheSunFootball"]
					for reporter in otherSourcesList:
						user = reporter
						tweets = api.user_timeline(screen_name = user, page = page)
						for tweet in tweets:
							if (datetime.datetime.now() - tweet.created_at).days < 1:
								badText = tweet.text
								text = badText.encode("ascii", "ignore")
								text = text.decode('utf-8')
								#print(text)
								date = tweet.created_at
								userName = tweet.author._json['screen_name']
								#print(userName)
								ID = tweet.id
								URL = "https://www.twitter.com/%s/status/%d" % (userName, ID)
								tweetTerms = {"Man City": ["Manchester City", "manchester city", "man city", "@ManCity", "Man City", "mcfc"],
								"Tottenham": ["@SpursOfficial", "Spurs", "spurs", "tottenham", "hotspurs", "thfc"], "Arsenal": ["Arsenal", "gunners","@Arsenal","afc"],
								"Chelsea": ["Chelsea","cfc","@ChelseaFC"], "Liverpool": ["Liverpool", "lfc", "LFC"], "Man United": ["Man United", "Manchester United",
								"united","mufc", "@ManUtd"], "Everton": ["Everton", "efc"], "Southampton": ["@SouthamptonFC", "Southampton", "SaintsFC"], "Leicester City": 
								["lcfc", "leicester", "leicester city"], "Watford": ["WatfordFC", "Watford", "watfordfc"], "Brighton": ["OfficialBHAFC", "BHAFC", "Brighton"],
								"West Ham": ["West Ham United", "West Ham FC", "West Ham", "@WestHamUtd", "whufc"], "West Brom": ["West Bromwich Albion", "West Brom", "@WBA", "wba"],
								"Newcastle United": ["Newcastle", "nufc", "Newcastle United"], "Stoke City": ["Stoke", "Stoke City", "stokecity","scfc"], "Crystal Palace": [
								"Crystal Palace", "cpfc"], "Swansea": ["Swansea","swansea city", "SwansOfficial", "swans"], "Burnley": ["Burnley","BurnleyOfficial"],
								"Huddersfield Town": ["Huddersfield","huddersfield town", "htafcdotcom","htafc"]}
								whichTeam = tweetTerms[teamName]
								if any(word in text for word in whichTeam):
									i+=1
									data['URL'].append(URL)
									data['Time'].append(date)
									data['Tweet Text'].append(text)
									data['Username'].append(userName)
									dfDict[x]= pd.DataFrame(data)
							else: #tweets are done now
								deadend = True
						if not deadend:
							page+=1
							time.sleep(5)
					break
			#dfDict[0]['URL'] = dfDict[0]['URL'].apply(lambda x: "<a href='%s'> a </a>" % (x) )
			frame = dfDict[0]
			if(frame.empty):
				frame = "Sorry there are no tweets for your team available right now"
				return render_template('/results.html', nothingHere = frame, teamName = teamName)
			else:
				frame = frame.to_html(escape = False, classes = "nothingHere")
				#frame.set_option('display.max_colwidth', -1)
				return render_template('/results.html', table = frame, teamName = teamName)



if __name__ == '__main__':
	app.before_request(before_request)
	
	app.run()