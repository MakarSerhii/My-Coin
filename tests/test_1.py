import requests

def test_file1_method1():
	r = requests.get('http://127.0.0.1:5000/')
	assert r.status_code == 200,"test failed"