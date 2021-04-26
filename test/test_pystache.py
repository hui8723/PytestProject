import pystache
import chevron

def test_mustache():
    print(pystache.render('Hi,{{person}}!',{'person':'XiaoMing'}))

def test_chevron():
    with open('/Users/aviva.tang/PycharmProjects/PytestProject/data/test.mustache', 'r') as f:
        print(chevron.render(f, {'name': 'LL','mobile': '12345678901'}))