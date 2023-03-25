import My_code

api_url = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"

def test_getresponse():
    ret = My_code.get_response(api_url)
    assert ret.status_code == 200

def test_sum():
    assert 3 == 3

def test_mul():
    assert 3 * 3
