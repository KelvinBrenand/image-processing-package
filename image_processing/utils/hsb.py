def __rgb2hsbConverter(red, green, blue):
    red, green, blue = red/255., green/255., blue/255.
    cmax = max(red, green, blue)
    cmin = min(red, green, blue)
    diff = cmax-cmin

    if cmax == cmin: h = 0
    elif cmax == red: h = (60*((green-blue)/diff)+360)%360
    elif cmax == green: h = (60*((blue-red)/diff)+120)%360
    elif cmax == blue: h = (60*((red-green)/diff)+240)%360
 
    if cmax == 0: s = 0
    else: s = (diff / cmax) * 100
 
    b = cmax * 100

    return [h, s, b]

def __hsb2rgbConverter(h, s, b):
    h = h/360.
    s = s/100
    b = b/100
    if s == 0.0: return [b*255, b*255, b*255]
    
    i = int(h*6.)
    f = (h*6.)-i
    p = b*(1.-s)
    q = b*(1.-s*f)
    t = b*(1.-s*(1.-f))

    return_value = []
    if i == 0: return_value = [b, t, p]
    if i == 1: return_value = [q, b, p]
    if i == 2: return_value = [p, b, t]
    if i == 3: return_value = [p, q, b]
    if i == 4: return_value = [t, p, b]
    if i == 5: return_value = [b, p, q]
    return [round(i*255) for i in return_value]