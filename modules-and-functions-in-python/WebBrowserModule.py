import webbrowser

# WebBrowser module

webbrowser.open("https://www.python.org", new=1, autoraise=True)

help(webbrowser)

chrome = webbrowser.get(using="windows-default")    # TODO: solve the problem of locating the runnable of other than default browser
chrome.open_new("https://www.google.com")

