import webbrowser

sivut = [
    "https://www.youtube.com",
    "https://github.com"
]

chrome = webbrowser.get(using='firefox')

for sivu in sivut:
    chrome.open_new_tab(sivu)
