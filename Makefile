all: server

clean:
	rm -r public

local : dest=$(shell pwd)/public

local : base=$(dest)

local : hugoopts = --ignoreCache --cleanDestinationDir --buildDrafts --buildFuture

local : hugo results

hugo: 
	hugo ${hugoopts} --enableGitInfo --destination ${dest} ${BASE}

results:
	#echo Deployed to ${base} at ${dest}
	open ${base}/index.html 
	wait

server: 
	(sleep 1 ; open http://localhost:1313)&
	hugo server --buildDrafts --baseURL http://localhost/ 

