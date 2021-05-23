SIZE = 8
p = 331941721759386740446055265418196301559
MS = MatrixSpace(GF(p), SIZE)

key = Matrix([
    [116401981595413622233973439379928029316, 198484395131713718904460590157431383741,
     210254590341158275155666088591861364763, 63363928577909853981431532626692827712,
     85569529885869484584091358025414174710, 149985744539791485007500878301645174953,
     257210132141810272397357205004383952828, 184416684170101286497942970370929735721],
    [42252147300048722312776731465252376713, 199389697784043521236349156255232274966,
     310381139154247583447362894923363190365, 275829263070032604189578502497555966953,
     292320824376999192958281274988868304895, 324921185626193898653263976562484937554,
     22686717162639254526255826052697393472, 214359781769812072321753087702746129144],
    [211396100900282889480535670184972456058, 210886344415694355400093466459574370742,
     186128182857385981551625460291114850318, 13624871690241067814493032554025486106,
     255739890982289281987567847525614569368, 134368979399364142708704178059411420318,
     277933069920652939075272826105665044075, 61427573037868265485473537350981407215],
    [282725280056297471271813862105110111601, 183133899330619127259299349651040866360,
     275965964963191627114681536924910494932, 290264213613308908413657414549659883232,
     140491946080825343356483570739103790896, 115945320124815235263392576250349309769,
     240154953119196334314982419578825033800, 33183533431462037262108359622963646719],
    [53797381941014407784987148858765520206, 136359308345749561387923094784792612816,
     26225195574024986849888325702082920826, 262047729451988373970843409716956598743,
     170482654414447157611638420335396499834, 270894666257247100850080625998081047879,
     91361079178051929124422796293638533509, 34320536938591553179352522156012709152],
    [266361407811039627958670918210300057324, 40603082064365173791090924799619398850,
     253357188908081828561984991424432114534, 322939245175391203579369607678957356656,
     63315415224740483660852444003806482951, 224451355249970249493628425010262408466,
     80574507596932581147177946123110074284, 135660472191299636620089835364724566497],
    [147031054061160640084051220440591645233, 286143152686211719101923153591621514114,
     330366815640573974797084150543488528130, 144943808947651161283902116225593922999,
     205798118501774672701619077143286382731, 317326656225121941341827388220018201533,
     14319175936916841467976601008623679266, 112709661623759566156255015500851204670],
    [306746575224464214911885995766809188593, 35156534122767743923667417474200538878,
     35608800809152761271316580867239668942, 259728427797578488375863755690441758142,
     29823482469997458858051644485250558639, 137507773879704381525141121774823729991,
     29893063272339035080311541822496817623, 292327683738678589950939775184752636265],
])

enc = Matrix([
    [133156758362160693874249080602263044484, 293052519705504374237314478781574255411,
     72149359944851514746901936133544542235, 56884023532130350649269153560305458687,
     67693140194970657150958369664873936730, 227562364727203645742246559359263307899,
     98490363636066788474326997841084979092, 323336812987530088571937131837711189774],
    [244725074927901230757605861090949184139, 63515536426726760809658259528128105864,
     297175420762447340692787685976316634653, 279269959863745528135624660183844601533,
     203893759503830977666718848163034645395, 163047775389856094351865609811169485260,
     103694284536703795013187648629904551283, 322381436721457334707426033205713602738],
    [17450567396702585206498315474651164931, 105594468721844292976534833206893170749,
     10757192948155933023940228740097574294, 132150825033376621961227714966632294973,
     329990437240515073537637876706291805678, 57236499879418458740541896196911064438,
     265417446675313880790999752931267955356, 73326674854571685938542290353559382428],
    [270340230065315856318168332917483593198, 217815152309418487303753027816544751231,
     55738850736330060752843300854983855505, 236064119692146789532532278818003671413,
     104963107909414684818161043267471013832, 234439803801976616706759524848279829319,
     173296466130000392237506831379251781235, 34841816336429947760241770816424911200],
    [140341979141710030301381984850572416509, 248997512418753861458272855046627447638,
     58382380514192982462591686716543036965, 188097853050327328682574670122723990784,
     125356457137904871005571726686232857387, 55692122688357412528950240580072267902,
     21322427002782861702906398261504812439, 97855599554699774346719832323235463339],
    [298368319184145017709393597751160602769, 311011298046021018241748692366798498529,
     165888963658945943429480232453040964455, 240099237723525827201004876223575456211,
     306939673050020405511805882694537774846, 7035607106089764511604627683661079229,
     198278981512146990284619915272219052007, 255750707476361671578970680702422436637],
    [45315424384273600868106606292238082349, 22526147579041711876519945055798051695,
     15778025992115319312591851693766890019, 318446611756066795522259881812628512448,
     269954638404267367913546070681612869355, 205423708248276366495211174184786418791,
     92563824983279921050396256326760929563, 209843107530597179583072730783030298674],
    [662653811932836620608984350667151180, 304181885849319274230319044357612000272,
     280045476178732891877948766225904840517, 216340293591880460916317821948025035163,
     79726526647684009633247003110463447210, 36010610538790393011235704307570914178,
     284067290617158853279270464803256026349, 45816877317461535723616457939953776625]
])

key_ms = copy(MS.zero())
enc_ms = copy(MS.zero())

for i in range(SIZE):
    for j in range(SIZE):
        key_ms[i, j] = key[i, j]
        enc_ms[i, j] = enc[i, j]

M = key_ms.inverse() * enc_ms * key_ms.inverse()

flag = ''
for i in range(SIZE):
    for j in range(SIZE):
        if M[i, j] < 256:
            flag += chr(M[i, j])
print(flag)
