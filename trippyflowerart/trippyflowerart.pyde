def setup():
    size(1000, 1000)
    # frameRate(10)
    # fullScreen()
    
x = 1
def draw():
    global x

    
    cv1 = ((abs(sin(x*10)) + 1) / 2) * 255
    cv2 = ((abs(sin(x*15)) + 1) / 2) * 255
    cv3 = ((abs(sin(x*25)) + 1) / 2) * 255
    background(20)
    
    textSize(20)
    text("Code by Isaac Morrow, 2019.", 2, height-30)
    textSize(20)
    text("x(t) = t^2/150*sin(t^x), y(t) = t^2/150*cos(t^x)", 2, height-5)
    textSize(20)
    text("Time: " + str(x)[:-1], 2, height-55) 
    
    translate(width/2, height/2)
    noFill()
    stroke(cv1, cv2, cv3)
    strokeWeight(3)
    
    beginShape()
    for i in range(295): 
        curveVertex(pow(i,2)/150*sin(i*x), pow(i, 2) / 150*cos(i*x))
    
    endShape()
    
    
    
    # if x >= 0:
    #     x -= 0.0005
        
    # if x <= 2*PI:
    #     x += 0.0005
    
    x += 0.0005 * sin(x/2)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
