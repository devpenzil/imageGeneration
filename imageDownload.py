from urllib import request


def imagedownload():
    url = 'https://images.unsplash.com/photo-1573039608965-7c8e38125ef5?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8NXx8d2hpdGUlMjBzcXVhcmV8ZW58MHx8MHx8&auto=format&fit=crop&w=800&q=60'

    res = request.urlopen(url, )
    with open("nature.png", "wb") as f:
        f.write(res.read())
    return None
