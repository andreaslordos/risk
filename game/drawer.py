def drawMap(countries,players):
    from PIL import Image,ImageDraw,ImageFont
    from os import chdir

    color_to_rgb={"red":(255,0,0),"blue":(0,0,204),"yellow":(255,255,0),"green":(0,204,0),"black":(0,0,0),"orange":(255,69,0)}
    chdir("C:\\Users\\user\\Desktop\\Python\\risk-ai")
    base=Image.open('RISK map blank.png')
    f=open("coordinates.txt","r")
    a=f.read().split("\n")[:-1]

    for x in range(len(a)):
        a[x]=(int(a[x].split(",")[0]),int(a[x].split(",")[1]))

    txt=Image.new('RGBA',base.size,(255,255,255,0))
    d=ImageDraw.Draw(txt)
    for x in range(len(a)):
        d.text(a[x],str(countries[x].troops),fill=color_to_rgb[countries[x].ownedBy.color]+(255,))
        d.text((a[x][0]-10,a[x][1]+10),countries[x].name,fill=color_to_rgb[countries[x].ownedBy.color]+(100,))
        out=Image.alpha_composite(base,txt)
        
    out.show()
