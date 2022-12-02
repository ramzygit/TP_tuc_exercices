'''import methods from scripts'''
from .script import lireligne


def test():
    '''method test lireligne'''
    assert lireligne( 1 , "id" ) == "57RtLWT7IpugV0yi5bsxJk"
    assert lireligne( 1 , "id" ) != "azeza"
    assert lireligne( 2 , "id" ) == "5VyfAfp2Yt3qaeuvq55ll3"
