vertical_position = 0


def setup():
    size(250,500)
    
def draw():

    global vertical_position
    
    background(map(second(), 0, 59, 0, 255))
    noStroke()
    fill(map(second(), 0, 59, 255, 0))
    
    ellipse (width / 2, vertical_position, 10, 10)
    
    fill (90,150,160)
    ellipse (50,90,60,70)
    ellipse (30,110,90,80)
    ellipse (73,115,70,75)
    
    ellipse (250,250,60,70)
    ellipse (225,270,90,80)
    ellipse (200,282,90,40)
    
    ellipse (0,490,170,160)
    ellipse (70,495,90,100)
    
    if vertical_position > height:
        vertical_position = 0
        
    else:
        vertical_position = map(second(), 0, 59, 0, height)
        
