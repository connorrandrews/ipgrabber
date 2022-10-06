import requests

def detect_public_ip():
    try:
        raw = requests.get('https://api.duckduckgo.com/?q=ip&format=json')
        answer = raw.json()["Answer"].split()[4]

    except Exception as e:
        return 'Error: {0}'.format(e)

    else:
        return answer

public_ip = detect_public_ip()
print(public_ip)


