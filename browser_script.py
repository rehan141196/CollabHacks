import webbrowser

url = 'http://localhost:3333?name=sdevkota'

# MacOS
chrome_path = 'open -a /Applications/Google\ Chrome.app %s'

webbrowser.get(chrome_path).open(url)

# Can try to run http server from here itself
# REHSHAH-M-L12H:sample-browser-single-party-call rehshah$ httpster
# Starting HTTPster v1.0.4 on port 3333 from /Users/rehshah/Desktop/sample-browser-single-party-call