from urllib import request

csv_file = 'http://insight.dev.schoolwires.com/HelpAssets/C2Assets/C2Files/C2ImportCalEventSample.csv'

def download_csv_file(url):
    response = request.urlopen(url)
    csv = response.read()
    csv_str = str(csv)
    lines = csv_str.split("\\n")
    desk_url = r'goog.csv'

    fr = open(desk_url, "w")
    for line in lines:
        fr.write(line + "\n")
    fr.close()

download_csv_file(csv_file)