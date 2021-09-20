def fibinnachi(numIn):
    if numIn>1:
        return numIn + fibinnachi(numIn-1)
    else:
        return 1
    print(numIn)
fibinnachi(6)

    