def process_log(log):
	lines=log.split('\n')
	log=[]
	for line in lines:
		log1={}
		timestamp,sererity,message=line.split('-')
		log1["timestamp"]=timestamp
		log1["sererity"]=sererity
		log1["message"]=message
		log.append(log1)
	return log

log="""5-6-hello
	8-9-goodby"""

print(process_log(log))