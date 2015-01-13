# GetJams - get some new jams for ya mental
# Released for Github on Oct 21 2014
import musicbrainzngs as jams
import random,sys,os,wx
jams.set_useragent("GetJams","1.0","inhumanundead@gmail.com")
def GetArtist(genre):
	x = jams.search_artists(tag=genre)['artist-list']
	y = []
	y.append(x[random.randint(0,len(x)-1)]['sort-name'])
	y.append(x[random.randint(0,len(x)-1)]['sort-name'])
	y.append(x[random.randint(0,len(x)-1)]['sort-name'])
	y.append(x[random.randint(0,len(x)-1)]['sort-name'])
	y.append(x[random.randint(0,len(x)-1)]['sort-name'])
	return y
def GetSimilar(artist):
	x = jams.search_artists(sortname=artist)['artist-list'][0]['tag-list'][0]['name']
	y = jams.search_artists(tag=x)['artist-list']
	z = []
	for i in range(0,5):
		z.append(y[random.randint(0,len(x)-1)]['sort-name'])
	return z
class GetJamsWindow(wx.Frame):
	def __init__(self,parent,title):
		wx.Frame.__init__(self,parent,title=title,size=(640,300))
		self.SetIcon(wx.Icon("icon.ico", wx.BITMAP_TYPE_ICO))
		self.textbox = wx.TextCtrl(self, size=(126,30), pos=(250,20))
		self.button = wx.Button(self, wx.ID_OK, " Genre ",pos=(250+36,55),size=(48+4,30))
		self.button2 = wx.Button(self,wx.ID_OK, "Artist",pos=(250+42,55+30),size=(42,30))
		self.artist_text = wx.StaticText(self,label="Artists:\n\n",pos=(275,125),size=(640,410),style=wx.ALIGN_CENTER)
		self.CreateStatusBar()
		self.button.Bind(wx.EVT_BUTTON,self.GenreSearch)
		self.button2.Bind(wx.EVT_BUTTON,self.ArtistSearch)
		self.Show(True)
	def ArtistSearch(self,event):
		z = GetSimilar(self.textbox.GetValue())
		self.artist_text.SetLabel("Artists:\n\n"+z[0]+"\n"+z[1]+"\n"+z[2]+"\n"+z[3]+"\n"+z[4])
	def GenreSearch(self,event):
		z = GetArtist(self.textbox.GetValue())
		self.artist_text.SetLabel("Artists:\n\n"+z[0]+"\n"+z[1]+"\n"+z[2]+"\n"+z[3]+"\n"+z[4])
if __name__ == "__main__":
	app = wx.App(False)
	frame = GetJamsWindow(None, "GetJams by Draven Stedman")
	app.MainLoop()
