import pyautogui as ag
import cv2

ag.PAUSE = .5
screenWidth, screenHeight = ag.size() # Get the size of the primary monitor.
currentMouseX, currentMouseY = ag.position() # Get the XY position of the mouse.
ag.sleep(1.5) # to allow me to change tabs to fusion360

# To pan, click and hold the mouse wheel button, and move your mouse from side-to-side.
# or can right click, then click on pan, then drag mouse, then hit return
# TODO: won't work if dragging over non-background area, though that might not be a problem if user can position "mouse"
def begin_pan(distance):
    ag.rightClick()
    x, y = ag.locateCenterOnScreen('pan.png', confidence=.5) #arbitrary confidence threshold
    ag.leftClick(x, y)
    ag.drag(distance, 0, duration=.5)
    ag.drag(-distance, 0, duration=.5)

def end_pan():
    ag.hotkey("return")

begin_pan(300)
end_pan()


# To zoom, spin your mouse wheel forward or backward,
# and while doing so, pay attention to where your cursor is (that’s where the zoom center is)!
# Also, note that you can access your preferences to reverse the default zoom direction
# def zoom_in(clicks):
#     ag.scroll(clicks)
# def zoom_out(clicks):
#     ag.scroll(-clicks)
#
# zoom_in(100)
# zoom_out(100)

# To orbit, click and hold the orbit shortcut ( SHIFT key) on your keyboard.
# At the same time, you hold the mouse wheel button, then move the mouse.
# Pay attention to whether you’re using ‘constrained orbit’ or ‘free.’

# ag.keyDown("shift")
#
# ag.keyUp("shift")

