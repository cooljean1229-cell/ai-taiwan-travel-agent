from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR

ROOT = Path(__file__).resolve().parent
OUT = ROOT / '圖片簡報_旅遊情報員'
OUT.mkdir(exist_ok=True)
W, H = 1600, 900
FONT = r'C:\Windows\Fonts\msjh.ttc'
FONT_B = r'C:\Windows\Fonts\msjhbd.ttc'
INK = '#172B36'; MUTED = '#5D7078'; CREAM = '#F6F3EC'; TEAL = '#167C80';
ORANGE = '#D97948'; GOLD = '#D6AC58'; PALE = '#E7EFEB'; WHITE = '#FFFFFF'; LINE='#D8E0DA'

def rgb(h):
    h=h.lstrip('#'); return tuple(int(h[i:i+2],16) for i in (0,2,4))
def ft(size,bold=False): return ImageFont.truetype(FONT_B if bold else FONT,size)
def rounded(d,box,r,fill,outline=None,width=1): d.rounded_rectangle(box,radius=r,fill=fill,outline=outline,width=width)
def txt(d,xy,s,size,color=INK,bold=False,anchor=None): d.text(xy,s,font=ft(size,bold),fill=color,anchor=anchor,spacing=8)
def base(n,kicker,title,subtitle):
    im=Image.new('RGB',(W,H),CREAM); d=ImageDraw.Draw(im)
    d.rectangle((0,0,W,13),fill=TEAL)
    d.ellipse((1300,-220,1740,220),fill='#E9E4D7'); d.ellipse((1380,-150,1660,130),fill=CREAM)
    txt(d,(100,65),kicker,22,TEAL,True); txt(d,(100,112),title,52,INK,True); txt(d,(100,186),subtitle,24,MUTED)
    d.line((100,820,1500,820),fill=LINE,width=2)
    txt(d,(100,843),'AI 台灣旅遊情報員 × 智慧行程推薦網站',17,MUTED)
    txt(d,(1500,843),f'{n:02d} / 05',17,TEAL,True,anchor='ra')
    return im,d
def pill(d,x,y,label,fill=PALE,color=TEAL,w=150):
    rounded(d,(x,y,x+w,y+42),21,fill); txt(d,(x+w/2,y+21),label,18,color,True,anchor='mm')

slides=[]
# Cover
im,d=base(1,'專案提案｜工作流程總覽','讓旅遊情報，成為下一段旅程的起點','從每週情報出發，依旅客偏好整理合適的台灣旅遊提案。')
rounded(d,(100,280,890,690),28,WHITE)
txt(d,(145,325),'一條清楚、可追溯的內容旅程',29,INK,True)
for i,(lab,col) in enumerate([('旅遊情報',TEAL),('分眾內容',ORANGE),('個人提案',GOLD)]):
    x=150+i*235
    rounded(d,(x,430,x+195,535),22,col)
    txt(d,(x+97,482),lab,26,WHITE,True,anchor='mm')
    if i<2:
        d.line((x+205,483,x+228,483),fill=INK,width=4); d.polygon([(x+228,475),(x+242,483),(x+228,491)],fill=INK)
txt(d,(150,590),'親子　　情侶　　熟齡旅客',22,MUTED)
# decorative illustration
rounded(d,(965,280,1500,690),28,'#DDE9E2')
d.ellipse((1065,365,1405,705),fill='#B6D0C4')
d.polygon([(970,640),(1110,470),(1205,580),(1315,420),(1500,650),(1500,690),(970,690)],fill='#719995')
d.polygon([(970,655),(1130,555),(1240,620),(1370,500),(1500,590),(1500,690),(970,690)],fill='#4C7778')
d.ellipse((1285,335,1345,395),fill=GOLD)
pill(d,1010,310,'研究 × 內容 × 提案',WHITE,TEAL,255)
slides.append(im)

# Roles
im,d=base(2,'角色分工｜六個交付節點','六個角色，接力完成內容','每個角色都有明確的輸入、產出與交接責任。')
roles=[('01','旅遊研究員','蒐集可追溯素材',TEAL),('02','週報編輯','轉為分眾內容',ORANGE),('03','簡報企劃','組織重點與來源',GOLD),('04','影片企劃','腳本與素材需求','#5D8293'),('05','網站工程師','呈現內容與提案','#55796C'),('06','驗收員','檢查、退修、複驗','#7C668B')]
for i,(num,name,desc,col) in enumerate(roles):
    row=i//3; c=i%3; x=100+c*465; y=290+row*230
    rounded(d,(x,y,x+420,y+185),24,WHITE)
    d.ellipse((x+25,y+28,x+90,y+93),fill=col); txt(d,(x+57,y+60),num,19,WHITE,True,anchor='mm')
    txt(d,(x+112,y+33),name,28,INK,True); txt(d,(x+112,y+86),desc,20,MUTED)
    d.line((x+28,y+137,x+390,y+137),fill=LINE,width=2)
    txt(d,(x+28,y+151),'輸入明確｜交接留痕',16,col,True)
slides.append(im)

# Flow
im,d=base(3,'共同流程｜一份核對素材，多渠道製作','從研究素材包，走到驗收與發布','所有內容分支共用同一份已核對素材，來源更新時同步通知。')
steps=[('研究問題','界定客群與主題'),('研究素材包','事實、觀察、來源'),('週報編輯','保留引用關聯'),('多渠道製作','簡報／影片／網站'),('驗收與複驗','修正後再檢查'),('發布','核准後交付')]
for i,(a,b) in enumerate(steps):
    x=85+i*245; y=390
    rounded(d,(x,y,x+205,y+145),22,TEAL if i in (0,5) else WHITE,outline=None if i in (0,5) else LINE,width=2)
    col=WHITE if i in (0,5) else INK; sub='#DCECE7' if i in (0,5) else MUTED
    txt(d,(x+102,y+47),a,24,col,True,anchor='mm'); txt(d,(x+102,y+98),b,16,sub,anchor='mm')
    if i<5:
        d.line((x+210,y+72,x+230,y+72),fill=ORANGE,width=4); d.polygon([(x+230,y+64),(x+242,y+72),(x+230,y+80)],fill=ORANGE)
rounded(d,(215,600,1385,700),20,'#E9E4D7')
txt(d,(800,638),'研究素材包一路回鏈：週報 → 簡報／影片／網站 → 驗收紀錄',22,INK,True,anchor='mm')
slides.append(im)

# Trust rules
im,d=base(4,'內容規範｜讓資訊可信、讓風險可見','事實可追溯，不確定就標清楚','內容發布前，清楚交代資料來源、狀態與安全邊界。')
rules=[('來源＋日期','外部事實附來源名稱、頁面、網址與查詢日期。',TEAL,'↗'),('待確認','資訊無法確認或來源衝突時，保留待確認與缺口。',ORANGE,'?'),('模擬資料','虛構旅客、價格、評分、成效或案例，顯眼標示。',GOLD,'模'),('憑證保護','密碼與 API Key 不寫入前端或 Git，改用環境變數。','#5D8293','✓')]
for i,(head,body,col,icon) in enumerate(rules):
    x=100+(i%2)*700; y=290+(i//2)*225
    rounded(d,(x,y,x+650,y+185),24,WHITE)
    rounded(d,(x+30,y+30,x+100,y+100),20,col)
    txt(d,(x+65,y+65),icon,21 if len(icon)>1 else 27,WHITE,True,anchor='mm')
    txt(d,(x+128,y+34),head,27,INK,True)
    # wrap Chinese text into two lines
    if len(body)>26: body=body[:26]+'\n'+body[26:]
    txt(d,(x+128,y+86),body,18,MUTED)
    d.line((x+30,y+145,x+610,y+145),fill=LINE,width=2)
txt(d,(100,755),'無法證實的資訊不補猜；時效性資訊標有效期間或待確認。',20,TEAL,True)
slides.append(im)

# Acceptance
im,d=base(5,'驗收員｜問題修正與複驗','發布前，完成驗收與複驗','逐項留下狀態、證據與修正建議，通過後才交付發布。')
checks=[('來源與日期','每個可驗證主張都能回到來源'),('標籤與內容','待確認、模擬資料清楚可見'),('版面與連結','內容一致、主要頁面可用'),('個資與憑證','表單只收必要資料，無密鑰外露')]
for i,(a,b) in enumerate(checks):
    y=290+i*112
    rounded(d,(100,y,890,y+88),18,WHITE)
    d.ellipse((125,y+19,175,y+69),fill=PALE); rounded(d,(140,y+32,160,y+54),3,WHITE,outline=TEAL,width=2)
    txt(d,(200,y+18),a,24,INK,True); txt(d,(440,y+25),b,17,MUTED)
rounded(d,(970,290,1500,700),28,'#E6ECE5')
txt(d,(1020,330),'驗收狀態',21,TEAL,True)
for i,(label,col) in enumerate([('通過',TEAL),('不通過',ORANGE),('待確認',GOLD)]):
    y=390+i*85
    rounded(d,(1020,y,1450,y+58),18,WHITE)
    d.ellipse((1040,y+16,1066,y+42),fill=col); txt(d,(1090,y+29),label,22,INK,True,anchor='lm')
txt(d,(1020,665),'不通過 → 修正 → 複驗 → 核准發布',18,MUTED,True)
rounded(d,(100,755,1500,795),18,'#F2E4D8')
txt(d,(800,775),'目前這份簡報為流程摘要；不代表旅遊研究或發布驗收已完成。',18,'#8B5034',True,anchor='mm')
slides.append(im)

# PNG exports
for i,im in enumerate(slides,1):
    im.save(OUT/f'{i:02d}_投影片.png',quality=95)

# PowerPoint editable deck with each page as full-slide raster for exact visual fidelity
prs=Presentation(); prs.slide_width=Inches(13.3333); prs.slide_height=Inches(7.5)
blank=prs.slide_layouts[6]
for i in range(1,len(slides)+1):
    s=prs.slides.add_slide(blank)
    s.shapes.add_picture(str(OUT/f'{i:02d}_投影片.png'),0,0,width=prs.slide_width,height=prs.slide_height)
prs.core_properties.title='AI 台灣旅遊情報員｜圖片簡報'
prs.core_properties.subject='專案角色分工、交付流程與內容驗收規範'
prs.core_properties.author='OpenAI Codex'
prs.save(OUT/'AI台灣旅遊情報員_圖片簡報.pptx')
print('\n'.join(str(p) for p in sorted(OUT.iterdir())))
