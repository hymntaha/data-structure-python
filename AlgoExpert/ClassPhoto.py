def classPhotos(redShirtHeights, blueShirtHeights):
    redShirtHeights.sort() # 1,3,4,5,8
    blueShirtHeights.sort() # 2,4,5,6,9

    blueInTheBack = False
    guidelinessMatch = False

    if redShirtHeights[0] < blueShirtHeights[0]:
        blueInTheBack = True

    for i in range(len(redShirtHeights)):
        if blueInTheBack:
            if redShirtHeights[i] < blueShirtHeights[i]:
                guidelinessMatch = True
            else:
                return False

        if blueInTheBack == False:
            if redShirtHeights[i] > blueShirtHeights[i]:
                guidelinessMatch = True
            else:
                return False
    return guidelinessMatch


blueShirtHeights = [21, 5, 4, 4, 4, 4, 4, 4, 4]
redShirtHeights = [19, 2, 4, 6, 2, 3, 1, 1, 4]
print(classPhotos(blueShirtHeights,redShirtHeights))
