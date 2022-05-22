y={"MyFamily":{"Ayush":"Love","Deepti":"Lover"},"MyLove":{"Ayush":"Boyfriend","Deepti":"Girlfriend"}}
for x in y:
    print(x)
    for z in y[x]:
        print(z,':',y[x][z])