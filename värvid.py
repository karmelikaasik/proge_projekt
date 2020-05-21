hall = [128,128,128]
punane = [255,51,51]
must = [0,0,0]
sinine = [51,122,255]
kollane = [255,255,51]
roheline =[91,255, 51]
valge = [255,255,255]
button = [50, 10, 70]
tumebutton = [40, 0, 60]

def tumedamvärv(värv):
    if värv[0] >= 10 and värv[1] >= 10 and värv[2] >= 10:
        uusvärv = [värv[0] - 10, värv[1] - 10, värv[2] - 10]
        return uusvärv

    # Palju tähenduseta if-e, lihtsalt don't worry
    elif värv[0] >= 10 and värv[1] >= 10:
        uusvärv = [värv[0] - 10, värv[1] - 10, 10]
        return uusvärv
    elif värv[1] >= 10 and värv[2] >= 10:
        uusvärv = [10, värv[1] - 10, värv[2] - 10]
        return uusvärv
    elif värv[0] >= 10 and värv[2] >= 10:
        uusvärv = [värv[0] - 10, 10, värv[2] - 10]
        return uusvärv

    elif värv[0] >= 10:
        uusvärv = [värv[0] - 10, 10, 10]
        return uusvärv
    elif värv[1] >= 10:
        uusvärv = [10, värv[1] - 10, 10]
        return uusvärv
    elif värv[2] >= 10:
        uusvärv = [10, 10, värv[2] - 10]
        return uusvärv
