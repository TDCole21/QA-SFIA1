import urllib3

def test_home():
    http = urllib3.PoolManager()
    r = http.request('GET', 'http://localhost:5000/')
    assert 200 == r.status #200 is successful connection

# def test_nonpage():
#     http = urllib3.PoolManager()
#     r = http.request('GET', 'http://35.242.135.176:5000/sdghsdfjgh')
#     assert 40 == r.status #200 is successful connection    

#make different defs to test each page.
#also test pages that don't exist.