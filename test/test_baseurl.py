# pytest test_baseurl.py --base-url http://192.168.29.122
def test_base_url(base_url):
    print("基础url：" + base_url)
    assert 3==2

