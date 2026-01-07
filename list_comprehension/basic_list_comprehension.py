texts = ["ai", "machine", "ml", "gsoc", "python"]
cleared=[x.upper() for x in texts if len(x)>2 and x!="machine"]
print(cleared)