from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import subprocess
import threading

OUT = Path(__file__).resolve().parent / 'output'
OUT.mkdir(exist_ok=True)
W, H = 1600, 900
FONT = r'C:\Windows\Fonts\msjh.ttc'
FONT_B = r'C:\Windows\Fonts\msjhbd.ttc'
INK='#F8F3E9'; MUTED='#D9DED7'; TEAL='#2E7777'; GOLD='#E3B65E'; CORAL='#D97851'; DEEP='#172D3A'
def f(sz,b=False): return ImageFont.truetype(FONT_B if b else FONT,sz)
def poly(d,pts,fill): d.polygon(pts,fill=fill)
def text(d,xy,s,sz,fill=INK,bold=False,anchor=None): d.text(xy,s,font=f(sz,bold),fill=fill,anchor=anchor,spacing=9)
def base(scene, place, date):
    im=Image.new('RGB',(W,H),DEEP); d=ImageDraw.Draw(im)
    d.rectangle((0,0,W,14),fill=TEAL)
    # cinematic dusk gradient bands
    for y in range(430,900):
        t=(y-430)/470
        col=(int(22+14*t),int(43+19*t),int(58+20*t))
        d.line((0,y,W,y),fill=col)
    d.rounded_rectangle((76,68,1524,832),radius=34,outline='#708382',width=2)
    d.rounded_rectangle((106,95,380,145),radius=24,fill='#193D45')
    text(d,(243,120),'旅遊情境示意畫面',18,'#D9EADF',True,'mm')
    text(d,(110,174),scene,27,GOLD,True)
    text(d,(110,222),place,47,INK,True)
    d.line((110,294,1490,294),fill='#85928C',width=2)
    # date/source overlay
    text(d,(110,756),date,17,MUTED)
    text(d,(110,791),'資料查詢：2026-11-27｜活動日期、場次與開放資訊請出發前重查官方公告',16,MUTED)
    text(d,(1490,791),'AI 台灣旅遊情報員',16,GOLD,True,'ra')
    return im,d

# 1 city festive dusk, generic light bokeh and silhouettes
im,d=base('01｜城市節慶的相遇','城市冬夜・暖色燈火氛圍','新北歡樂耶誕城｜活動日期 2026-11-13 至 2026-12-27')
d.ellipse((1110,340,1260,490),fill='#E7B967')
# abstract skyline
poly(d,[(0,655),(0,550),(145,550),(145,490),(260,490),(260,555),(380,555),(380,470),(510,470),(510,560),(660,560),(660,510),(780,510),(780,620),(930,620),(930,485),(1060,485),(1060,600),(1230,600),(1230,520),(1360,520),(1360,620),(1600,620),(1600,900),(0,900)],'#27424B')
# warm festive lights, intentionally abstract, no event installations
for x,y,r,c in [(150,400,14,GOLD),(255,370,10,CORAL),(380,420,12,GOLD),(520,350,9,'#F3D99B'),(660,415,13,CORAL),(800,365,10,GOLD),(960,410,14,'#F3D99B'),(1300,400,11,CORAL),(1440,360,12,GOLD)]:
    d.ellipse((x-r-16,y-r-16,x+r+16,y+r+16),fill='#35474A'); d.ellipse((x-r,y-r,x+r,y+r),fill=c)
# two companion silhouettes, consistent clothing cues
d.ellipse((670,566,730,626),fill='#1A2630');d.ellipse((770,560,832,622),fill='#1A2630')
d.rounded_rectangle((650,610,748,800),radius=32,fill='#E8E0D1')
d.rounded_rectangle((755,608,855,800),radius=32,fill='#536049')
d.polygon([(700,610),(748,662),(727,726),(683,682)],fill='#A44F3D')
d.polygon([(797,608),(755,658),(780,720),(819,680)],fill='#D3C7AD')
d.rectangle((640,788,754,808),fill='#18222C');d.rectangle((748,788,866,808),fill='#18222C')
d.rounded_rectangle((110,555,1100,710),radius=24,fill='#152A36')
text(d,(150,585),'夜色亮起，和喜歡的人，',33,INK,True)
text(d,(150,635),'把城市走成一段節日記憶。',33,INK,True)
im.save(OUT/'01_城市節慶.png')

# 2 mountain forest art-like abstract light; generic not real installation
im,d=base('02｜山林藝術的光','山林夜色・抽象光影氛圍','龍崎光節空山祭｜活動日期 2026-12-19 至 2027-02-14')
# tree trunks / layered slopes
poly(d,[(0,650),(130,510),(280,570),(430,420),(600,555),(800,430),(980,560),(1160,445),(1370,570),(1600,450),(1600,900),(0,900)],'#24464B')
poly(d,[(0,700),(240,600),(450,670),(700,550),(900,690),(1130,570),(1350,675),(1600,570),(1600,900),(0,900)],'#1A383F')
for x,h in [(140,370),(300,300),(500,410),(1090,360),(1260,420),(1480,320)]:
    d.polygon([(x-45,590),(x,590-h),(x+44,590)],fill='#142D34')
    d.rectangle((x-5,590-h//2,x+5,600),fill='#142D34')
# restrained abstract light forms, explicitly conceptual mood only
for x,y,r,c in [(700,470,33,'#E6B75E'),(790,390,24,'#72A9A1'),(900,490,40,'#D97951'),(1010,370,20,'#E6B75E')]:
    d.ellipse((x-r-28,y-r-28,x+r+28,y+r+28),fill='#293E43'); d.ellipse((x-r,y-r,x+r,y+r),fill=c)
# companion backs
d.ellipse((685,593,739,647),fill='#17242B');d.rounded_rectangle((668,638,755,795),radius=27,fill='#E8E0D1');d.polygon([(708,640),(752,680),(733,733),(692,692)],fill='#A44F3D')
d.ellipse((768,590,824,646),fill='#17242B');d.rounded_rectangle((753,636,842,795),radius=27,fill='#536049');d.polygon([(793,638),(754,679),(775,735),(816,693)],fill='#D3C7AD')
d.rounded_rectangle((110,555,1110,710),radius=24,fill='#152A36')
text(d,(150,585),'走進山林，讓一束光，',33,INK,True)
text(d,(150,635),'照見旅程裡新的想像。',33,INK,True)
im.save(OUT/'02_山林光影.png')

# 3 coast sunset, generic shoreline with picnic/music mood
im,d=base('03｜海岸暖冬與旅程邀請','海岸暮色・音樂野餐氛圍','大鵬灣暖冬派對｜活動日期 2026-12-12、13、19、20')
# sea/sunset
d.ellipse((1160,345,1300,485),fill='#E5B45B')
d.rectangle((0,460,W,650),fill='#496E72')
for y in range(485,645,24): d.line((0,y,W,y+10),fill='#719093',width=3)
poly(d,[(0,650),(280,620),(540,665),(790,630),(1050,660),(1310,610),(1600,650),(1600,900),(0,900)],'#233F45')
# simple picnic mat and string lights, no named stage/site details
d.polygon([(270,710),(620,675),(740,738),(390,780)],fill='#B95F43')
d.line((280,340,680,305,1030,340,1450,300),fill='#B5A477',width=3)
for x,y in [(330,336),(500,321),(680,305),(870,322),(1030,340),(1235,319),(1410,304)]:
    d.ellipse((x-9,y-9,x+9,y+9),fill=GOLD)
# companion silhouettes looking seaward
d.ellipse((865,540,925,600),fill='#17242B');d.rounded_rectangle((846,588,940,790),radius=30,fill='#E8E0D1');d.polygon([(887,590),(936,635),(914,699),(871,648)],fill='#A44F3D')
d.ellipse((960,535,1024,599),fill='#17242B');d.rounded_rectangle((944,584,1042,790),radius=30,fill='#536049');d.polygon([(986,587),(945,631),(968,700),(1013,650)],fill='#D3C7AD')
d.rounded_rectangle((110,555,1140,710),radius=24,fill='#152A36')
text(d,(150,581),'從城市燈火到海岸樂聲，',31,INK,True)
text(d,(150,630),'下一段台灣旅程，照你的喜歡出發。',29,INK,True)
d.rounded_rectangle((1190,610,1488,702),radius=20,fill='#1D3B44')
text(d,(1339,640),'提供偏好',18,GOLD,True,'mm'); text(d,(1339,675),'洽詢旅遊提案',19,INK,True,'mm')
im.save(OUT/'03_海岸邀請.png')
print('完成三張示意場景卡')

# Encode a 30-second silent MP4 through stdin so FFmpeg never has to
# interpret the workspace's non-ASCII filesystem path.
ffmpeg = r'C:\Users\user\AppData\Local\CapCut\Apps\9.2.0.3931\ffmpeg.exe'
cmd = [ffmpeg, '-y', '-f', 'rawvideo', '-pixel_format', 'rgb24', '-video_size', f'{W}x{H}',
       '-framerate', '30', '-i', '-', '-an', '-c:v', 'h264_mf', '-b:v', '5M',
       '-pix_fmt', 'yuv420p', '-f', 'mp4', '-movflags', 'empty_moov+frag_keyframe+default_base_moof', '-t', '30', 'pipe:1']
proc = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
chunks = []
def read_output():
    while True:
        part = proc.stdout.read(1024 * 1024)
        if not part:
            break
        chunks.append(part)
reader = threading.Thread(target=read_output, daemon=True)
reader.start()
for filename in ['01_城市節慶.png', '02_山林光影.png', '03_海岸邀請.png']:
    frame = Image.open(OUT / filename).convert('RGB')
    raw = frame.tobytes()
    for _ in range(10 * 30):
        try:
            proc.stdin.write(raw)
        except (BrokenPipeError, OSError):
            break
    if proc.poll() is not None:
        break
proc.stdin.close()
reader.join()
video_bytes = b''.join(chunks)
code = proc.wait()
if code:
    raise RuntimeError(f'FFmpeg exit code {code}')
(OUT / '30秒旅遊宣傳影片.mp4').write_bytes(video_bytes)
print(f'影片輸出完成：{len(video_bytes)} bytes')
