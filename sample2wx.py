import wx

app = wx.App()

frame = wx.Frame(None, -1, '')
frame.SetToolTip(wx.ToolTip('this is a frame'))
frame.SetCursor(wx.StockCursor(wx.CURSOR_MAGNIFIER))
frame.SetSize(wx.Size(300,250))
frame.SetTitle('simple2.py')
frame.Show()

app.MainLoop()

def main():
    app = wx.App()
    file1 = wx.Menu()
    frame =wx.Frame(None, title='Icon', pos=(300,300))
    frame.SetIcon(wx.Icon('tipi.ico', wx.BITMAP_TYPE_ICO))
    frame.Center()
    frame.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()
