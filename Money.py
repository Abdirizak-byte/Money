from graphics import *

win = GraphWin("Convertions", 400, 100)
win.setCoords(0,0,500, 500)
win.setBackground("Green")



P1 = Point(75, 300)
USDBox= Entry(P1,7)
USDBox.setSize(20)
USDBox.setFill("White")
USDBox.setTextColor("Black")
USDBox.draw(win)

P2 = Point(425, 300)
EUROBox = Entry(P2, 7)
EUROBox.setSize(20)
EUROBox.setFill("White")
EUROBox.setTextColor("Black")
EUROBox.draw(win)

USDP = Point(80, 450)
USD = Text(USDP, "USD:")
USD.draw(win)

EUROP = Point(435, 450)
EURO = Text(EUROP, "EUROS:")
EURO.draw(win)

Rate = Text(Point(250, 300), "=> 1 USD = .84 Euro =>")
Rate.draw(win)


clicked = win.getMouse()
Amount = eval(USDBox.getText())
cc = (Amount * .84)
EUROBox.setText(cc)
          
win.getMouse()
win.close()
