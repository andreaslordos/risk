def generateCountries():
    from country_class import country

    def genCountries():
        alaska=country(1,[2,4,30],"alaska")
        northwest_territory=country(2,[1,4,5],"northwest territory")
        greenland=country(3,[2,5,6,20],"greenland")
        alberta=country(4,[1,2,5,7],"alberta")
        ontario=country(5,[2,3,4,6,7,8],"ontario")
        quebec=country(6,[3,5,8],"quebec")
        western_us=country(7,[4,5,8,9],"western us")
        eastern_us=country(8,[5,6,7,9],"eastern us")
        central_america=country(9,[7,8,10],"central america")

        venezuela=country(10,[9,11,12],"venezuela")
        peru=country(11,[10,12,13],"peru")
        brazil=country(12,[10,11,13,14],"brazil")
        argentina=country(13,[11,12],"argentina")

        north_africa=country(14,[12,25,26,15,16,17],"north africa")
        egypt=country(15,[14,26,36,16],"egypt")
        east_africa=country(16,[15,17,19,18,36],"east africa")
        congo=country(17,[14,16,18],"congo")
        south_africa=country(18,[17,16,19],"south africa")
        madagascar=country(19,[16,18],"madagascar")

        iceland=country(20,[3,21,23],"iceland")
        scandinavia=country(21,[20,22,24,23],"scandinavia")
        russia=country(22,[21,24,26,36,31,27],"russia")
        great_britain=country(23,[20,21,24,25],"great britain")
        northern_europe=country(24,[23,21,22,26,25],"northern europe")
        western_europe=country(25,[23,24,26,14],"western europe")
        southern_europe=country(26,[25,24,22,36,15,14],"southern europe")

        ural=country(27,[22,31,32,28],"ural")
        siberia=country(28,[27,32,33,34,29],"siberia")
        yakutsk=country(29,[28,34,30],"yakutsk")
        kamchatka=country(30,[29,34,33,35],"kamchatka")
        afghanistan=country(31,[22,27,32,37,36],"afghanistan")
        china=country(32,[33,28,27,31,37,38],"china")
        mongolia=country(33,[32,28,34,30,35],"mongolia")
        irkutsk=country(34,[30,29,28,33],"irkutsk")
        japan=country(35,[30,33],"japan")
        middle_east=country(36,[16,15,26,22,31,37],"middle east")
        india=country(37,[36,31,32,38],"india")
        siam=country(38,[37,32,39],"siam")

        indonesia=country(39,[38,40],"indonesia")
        new_guinea=country(40,[39,41,42],"new guinea")
        western_australia=country(41,[40,42],"western australia")
        eastern_australia=country(42,[40,41],"eastern australia")

        return [alaska,northwest_territory,greenland,alberta,ontario,quebec,western_us,eastern_us,central_america,venezuela,peru,brazil,argentina,north_africa,egypt,east_africa,congo,south_africa,madagascar,iceland,scandinavia,russia,great_britain,northern_europe,western_europe,southern_europe,ural,siberia,yakutsk,kamchatka,afghanistan,china,mongolia,irkutsk,japan,middle_east,india,siam,indonesia,new_guinea,western_australia,eastern_australia]

    countries=genCountries()
    id_to_country={}
    for territory in countries:
        id_to_country[territory.idnumb]=territory
    
    for country in countries:
        for x in range(len(country.connectedTo)):
            country.connectedTo[x]=id_to_country[country.connectedTo[x]]


    return countries
