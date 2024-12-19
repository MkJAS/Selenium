import pytest
from youtubeTest import YoutubePlayer


class TestYoutubePlayer:
    
    youtubePlayer = YoutubePlayer()    
    channelName = "Northernlion"
    
    #def __init__(self):
     #   self.youtubePlayer = YoutubePlayer()
        
    
    def test_searchYoutube(self):
        title = self.youtubePlayer.searchYoutube("youtube")
        expectedTitle = "YouTube"

        assert title.lower() == expectedTitle.lower()
        
        
    def test_searchChannel(self):
        
        expectedChannelUrl = "youtube.com/@" + self.channelName
        
        assert expectedChannelUrl in self.youtubePlayer.searchChannel(self.channelName)
        
    def test_playVideo(self):
        
        assert "/watch" in self.youtubePlayer.playVideo()
        
        

# def test_search():
    
#     player = YoutubePlayer()
       
        
#     assert player.searchYoutube("youtube").lower() == "youtube"
    
#     channelUrl = "youtube.com/@Northernlion"
    
#     assert channelUrl in player.searchChannel("Northernlion") 
    
#     assert "/watch" in player.playVideo() 
    
    
    
    
# def test_searchChannel():
    
#     channelUrl = "youtube.com/@Nothernlion"
    
#     assert player.searchChannel("Northernlion") == channelUrl
    
    
# def test_playVideo():
    
#     assert "/watch" in player.playVideo() 
    
    
    

