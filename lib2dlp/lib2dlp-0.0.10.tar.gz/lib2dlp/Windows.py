#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Tkinter import *
from office import office
from edlp import control
import getopt
from faker import Factory
from faker import Faker

class Window:



	def CreateTxtWindow(self):

		root = Tk()
		#设置标题
		root.title("")
		#设置窗口的大小宽x高+偏移量
		root.geometry('440x30+700+500')
		#禁止调整窗口大小
		#root.resizable(0, 0)
		#设置窗口图标
		#root.iconbitmap('img\mainlogo.ico')

		root.overrideredirect(True) #清除所有的tkinters窗口选项
		#root.attributes('-disabled', True) #防止与窗口中的任何用户交互

		root.wm_attributes('-topmost',1) #置顶窗口


		#l1 = Label(root, text="文件行数，不得超过500行:",bg = 'red')
		l1 = Label(root, text="文件行数，不得超过500行:",bg = 'red')
		l1.pack(side=LEFT)
		num1 = StringVar()
		txt1 = Entry(root, width=5,borderwidth=2, textvariable = num1)
		num1.set("50")
		txt1.pack(side=LEFT)


		#l2 = Label(root, text="文件个数，不得超过500个:",bg = 'red')
		l2 = Label(root, text="文件个数，不得超过500个:",bg = 'red')
		l2.pack(side=LEFT)
		num2 = StringVar()
		txt2 = Entry(root, width=5,borderwidth=2, textvariable = num2)
		num2.set("1")
		txt2.pack(side=LEFT)


		def on_click():
			ret = True
			o = office()
			x = num1.get()
			y = num2.get()
			if x is not None:
				s = int(x)
				n = int(y)
				if 0 < s <= 500 and 0 < n <= 500:
				#if 0 < s <= 500 and 0 < n <= 500:
					ret = o.CreateTxtE(s,n)
					if ret:
						print("OK")
					else:
						print("FALSE")
				else:
					print("最大可设置2000")
					#print("最大可设置500")

			root.destroy()
			return True

		Button(root, text="生成文件", command = on_click).pack(side=LEFT)

		root.mainloop()

	def CreateWordWindow(self):

		root = Tk()
		#设置标题
		root.title("")
		#设置窗口的大小宽x高+偏移量
		root.geometry('440x30+700+500')
		#禁止调整窗口大小
		#root.resizable(0, 0)
		#设置窗口图标
		#root.iconbitmap('img\mainlogo.ico')

		root.overrideredirect(True) #清除所有的tkinters窗口选项
		#root.attributes('-disabled', True) #防止与窗口中的任何用户交互

		root.wm_attributes('-topmost',1) #置顶窗口


		l1 = Label(root, text="文件页数，不得超过500页:",bg = 'red')
		l1.pack(side=LEFT)
		num1 = StringVar()
		txt1 = Entry(root, width=5,borderwidth=2, textvariable = num1)
		num1.set("50")
		txt1.pack(side=LEFT)


		l2 = Label(root, text="文件个数，不得超过500个:",bg = 'red')
		l2.pack(side=LEFT)
		num2 = StringVar()
		txt2 = Entry(root, width=5,borderwidth=2, textvariable = num2)
		num2.set("1")
		txt2.pack(side=LEFT)


		def on_click():
			ret = True
			o = office()
			x = num1.get()
			y = num2.get()
			if x is not None:
				s = int(x)
				n = int(y)
				if 0 < s <= 500 and 0 < n <= 500:
					ret = o.CreateWordE(s,n)
					if ret:
						print("OK")
					else:
						print("FALSE")
				else:
					print("最大可设置500")

			root.destroy()
			return True

		Button(root, text="生成文件", command = on_click).pack(side=LEFT)

		root.mainloop()

	def CreateExcelWindow(self):

		root = Tk()
		#设置标题
		root.title("")
		#设置窗口的大小宽x高+偏移量
		root.geometry('240x210+700+500')
		#禁止调整窗口大小
		#root.resizable(0, 0)
		#设置窗口图标
		#root.iconbitmap('img\mainlogo.ico')

		root.overrideredirect(True) #清除所有的tkinters窗口选项
		#root.attributes('-disabled', True) #防止与窗口中的任何用户交互

		root.wm_attributes('-topmost',1) #置顶窗口


		#l1 = Label(root, text="文件sheet数，不得超过500 sheet:",bg = 'red')
		l1 = Label(root, text="文件sheet数，不得超过500 sheet:",bg = 'red')
		#l1.pack(side=LEFT)
		#l1.pack(side=TOP)
		l1.pack(side=TOP,anchor=W,fill='both')
		#l1.grid(row=0, column=0)
		num1 = StringVar()
		txt1 = Entry(root, width=5,borderwidth=2, textvariable = num1)
		num1.set("100")
	
		#txt1.pack(side=LEFT)
		#txt1.pack(side=TOP)
		txt1.pack(side=TOP,anchor=W)
		#txt1.grid(row=0,column=1)


		#l2 = Label(root, text="文件个数，不得超过500个:",bg = 'red')
		l2 = Label(root, text="文件个数，不得超过500个:",bg = 'green')
		l2.pack(side=TOP,anchor=W,fill='both')
		#l2.pack(side=TOP)
		#l2.grid(row=1,column=0)
		num2 = StringVar()
		txt2 = Entry(root, width=5,borderwidth=2, textvariable = num2)
		num2.set("1")
		txt2.pack(side=TOP,anchor=W)
		#txt2.pack(side=TOP)
		#txt2.grid(row=1,column=1)


		#----zhangji------
		#----行数--------
		l3 = Label(root, text="文件行数，不得超过10000行:",bg = 'red')
		l3.pack(side=TOP,anchor=W,fill='both')
		#l3.pack(side=TOP)
		#l3.grid(row=2,column=0)
		num3 = StringVar()
		txt3 = Entry(root, width=5,borderwidth=2, textvariable = num3)
		num3.set("10")
		txt3.pack(side=TOP,anchor=W)
		#txt3.pack(side=TOP)
		#txt3.grid(row=2,column=1)

		#----列数----
		l4 = Label(root, text="文件列数，不得超过255列:",bg = 'green')
		l4.pack(side=TOP,anchor=W,fill='both')
		#l4.pack(side=TOP)
		#l4.grid(row=3,column=0)
		num4 = StringVar()
		txt4 = Entry(root, width=5,borderwidth=2, textvariable = num4)
		num4.set("5")
		txt4.pack(side=TOP,anchor=W)
		#txt4.pack(side=TOP)
		#txt4.grid(row=4,column=1)

		def on_click():
			ret = True
			faker = Faker("zh_CN")
			#text = faker.name()
			text = "我不是关键字,我是来占格子的,%s" % faker.name()
			o = office()
			x = num1.get()    #sheet页
			y = num2.get()    #文件个数
			w = num3.get()    #行数
			q = num4.get()    #列数
			if x is not None:
				s = int(x)
				n = int(y)
				r = int(w)
				c = int(q)
				#if 0 < s <= 500 and 0 < n <= 500:
				if 0 < s <= 500 and 0 < n <= 500 and 0 <r <= 10000 and 0 < c <= 255:
					#ret = o.CreateExcelE(text,s,n)
					ret = o.CreateExcelE(text,s,n,r,c)
					if ret:
						print("OK")
					else:
						print("FALSE")
				else:
					#print("最大可设置500")
					print("最大可设置500")

			root.destroy()
			return True

		Button(root, text="生成文件", command = on_click).pack(side=TOP,anchor=W)

		root.mainloop()
	def CreatePptWindow(self):

		root = Tk()
		#设置标题
		root.title("")
		#设置窗口的大小宽x高+偏移量
		root.geometry('440x30+700+500')
		#禁止调整窗口大小
		#root.resizable(0, 0)
		#设置窗口图标
		#root.iconbitmap('img\mainlogo.ico')

		root.overrideredirect(True) #清除所有的tkinters窗口选项
		#root.attributes('-disabled', True) #防止与窗口中的任何用户交互

		root.wm_attributes('-topmost',1) #置顶窗口


		l1 = Label(root, text="文件页数，不得超过500页:",bg = 'red')
		l1.pack(side=LEFT)
		num1 = StringVar()
		txt1 = Entry(root, width=5,borderwidth=2, textvariable = num1)
		num1.set("50")
		txt1.pack(side=LEFT)


		l2 = Label(root, text="文件个数，不得超过500个:",bg = 'red')
		l2.pack(side=LEFT)
		num2 = StringVar()
		txt2 = Entry(root, width=5,borderwidth=2, textvariable = num2)
		num2.set("1")
		txt2.pack(side=LEFT)


		def on_click():
			ret = True
			o = office()
			x = num1.get()
			y = num2.get()
			if x is not None:
				s = int(x)
				n = int(y)
				if 0 < s <= 500 and 0 < n <= 500:
					ret = o.CreatePptE(s,n)
					if ret:
						print("OK")
					else:
						print("FALSE")
				else:
					print("最大可设置500")

			root.destroy()
			return True

		Button(root, text="生成文件", command = on_click).pack(side=LEFT)

		root.mainloop()

	def CreateImageWindow(self):

		root = Tk()
		#设置标题
		root.title("")
		#设置窗口的大小宽x高+偏移量
		root.geometry('250x30+700+500')
		#禁止调整窗口大小
		#root.resizable(0, 0)
		#设置窗口图标
		#root.iconbitmap('img\mainlogo.ico')

		root.overrideredirect(True) #清除所有的tkinters窗口选项
		#root.attributes('-disabled', True) #防止与窗口中的任何用户交互

		root.wm_attributes('-topmost',1) #置顶窗口

		l2 = Label(root, text="文件个数，不得超过500个:",bg = 'red')
		l2.pack(side=LEFT)
		num2 = StringVar()
		txt2 = Entry(root, width=5,borderwidth=2, textvariable = num2)
		num2.set("1")
		txt2.pack(side=LEFT)


		def on_click():
			ret = True
			o = office()
			y = num2.get()
			if y is not None:
				n = int(y)
				if 0 < n <= 500:
					ret = o.CreateImageE(n)
					if ret:
						print("OK")
					else:
						print("FALSE")
				else:
					print("最大可设置500")

			root.destroy()
			return True

		Button(root, text="生成文件", command = on_click).pack(side=LEFT)

		root.mainloop()


	def CreatePdfWindow(self):

		root = Tk()
		#设置标题
		root.title("")
		#设置窗口的大小宽x高+偏移量
		root.geometry('440x30+700+500')
		#禁止调整窗口大小
		#root.resizable(0, 0)
		#设置窗口图标
		#root.iconbitmap('img\mainlogo.ico')

		root.overrideredirect(True) #清除所有的tkinters窗口选项
		#root.attributes('-disabled', True) #防止与窗口中的任何用户交互

		root.wm_attributes('-topmost',1) #置顶窗口


		l1 = Label(root, text="文件页数，不得超过500页:",bg = 'red')
		l1.pack(side=LEFT)
		num1 = StringVar()
		txt1 = Entry(root, width=5,borderwidth=2, textvariable = num1)
		num1.set("50")
		txt1.pack(side=LEFT)


		l2 = Label(root, text="文件个数，不得超过500个:",bg = 'red')
		l2.pack(side=LEFT)
		num2 = StringVar()
		txt2 = Entry(root, width=5,borderwidth=2, textvariable = num2)
		num2.set("1")
		txt2.pack(side=LEFT)


		def on_click():
			ret = True
			o = office()
			x = num1.get()
			y = num2.get()
			if x is not None:
				s = int(x)
				n = int(y)
				if 0 < s <= 500 and 0 < n <= 500:
					ret = o.CreatePdfE(s,n)
					if ret:
						print("OK")
					else:
						print("FALSE")
				else:
					print("最大可设置500")

			root.destroy()
			return True

		Button(root, text="生成文件", command = on_click).pack(side=RIGHT)

		root.mainloop()


	def CreateGenSizeWindow(self):

		root = Tk()
		#设置标题
		root.title("")
		#设置窗口的大小宽x高+偏移量
		root.geometry('260x30+700+500')
		#禁止调整窗口大小
		#root.resizable(0, 0)
		#设置窗口图标
		#root.iconbitmap('img\mainlogo.ico')

		root.overrideredirect(True) #清除所有的tkinters窗口选项
		#root.attributes('-disabled', True) #防止与窗口中的任何用户交互

		root.wm_attributes('-topmost',1) #置顶窗口

		l2 = Label(root, text="文件大小，不得超过10000M:",bg = 'red')
		l2.pack(side=LEFT)
		num2 = StringVar()
		txt2 = Entry(root, width=5,borderwidth=2, textvariable = num2)
		num2.set("1")
		txt2.pack(side=LEFT)


		def on_click():
			ret = True
			o = office()
			y = num2.get()
			if y is not None:
				n = int(y)
				if 0 < n <= 10000:
					ret = o.GenSizeFile(n)
					if ret:
						print("OK")
					else:
						print("FALSE")
				else:
					print("最大可设置10000")

			root.destroy()
			return True

		Button(root, text="生成文件", command = on_click).pack(side=LEFT)

		root.mainloop()
	def CreateTelnetWindow(self):

		root = Tk()
		#设置标题
		root.title("")
		#设置窗口的大小宽x高+偏移量
		root.geometry('350x30+700+500')
		#禁止调整窗口大小
		#root.resizable(0, 0)
		#设置窗口图标
		#root.iconbitmap('img\mainlogo.ico')

		root.overrideredirect(True) #清除所有的tkinters窗口选项
		#root.attributes('-disabled', True) #防止与窗口中的任何用户交互

		root.wm_attributes('-topmost',1) #置顶窗口


		l1 = Label(root, text="IP地址:",bg = 'red')
		l1.pack(side=LEFT)
		num1 = StringVar()
		txt1 = Entry(root, width=20,borderwidth=2, textvariable = num1)
		num1.set("10.95.41.15")
		txt1.pack(side=LEFT)


		l2 = Label(root, text="端口号:",bg = 'red')
		l2.pack(side=LEFT)
		num2 = StringVar()
		txt2 = Entry(root, width=8,borderwidth=2, textvariable = num2)
		num2.set("8000")
		txt2.pack(side=LEFT)


		def on_click():
			ret = True
			c = control()
			x = num1.get()
			y = num2.get()
			if x is not None:
				n = int(y)
				if 0 < n <= 65536:
					ret = c.PortIsOpen(x,n)
					if ret:
						print("OK")
					else:
						print("FALSE")
				else:
					print("最大可设置65535")

			root.destroy()
			return True

		Button(root, text="TELNET", command = on_click).pack(side=LEFT)

		root.mainloop()
	def CreateCardWindow(self):

		root = Tk()
		#设置标题
		root.title("")
		#设置窗口的大小宽x高+偏移量
		root.geometry('130x30+900+500')
		#禁止调整窗口大小
		#root.resizable(0, 0)
		#设置窗口图标
		#root.iconbitmap('img\mainlogo.ico')

		root.overrideredirect(True) #清除所有的tkinters窗口选项
		#root.attributes('-disabled', True) #防止与窗口中的任何用户交互

		root.wm_attributes('-topmost',1) #置顶窗口

		l2 = Label(root, text="生成数量",bg = 'red')
		l2.pack(side=LEFT)
		num2 = StringVar()
		txt2 = Entry(root, width=5,borderwidth=2, textvariable = num2)
		num2.set("1")
		txt2.pack(side=LEFT)


		def on_click():
			ret = True
			app = control()
			y = num2.get()
			if y is not None:
				n = int(y)
				if 0 < n <= 10000:
					ret = app.genfaker(n)
					if ret:
						print("OK")
					else:
						print("FALSE")
				else:
					print("最大可设置10000")

			root.destroy()
			return True

		Button(root, text="生成", command = on_click).pack(side=LEFT)

		root.mainloop()

	def CreateContentWindow(self):

		root = Tk()
		#设置标题
		root.title("")
		#设置窗口的大小宽x高+偏移量
		root.geometry('440x30+700+500')
		#禁止调整窗口大小
		#root.resizable(0, 0)
		#设置窗口图标
		#root.iconbitmap('img\mainlogo.ico')

		root.overrideredirect(True) #清除所有的tkinters窗口选项
		#root.attributes('-disabled', True) #防止与窗口中的任何用户交互

		root.wm_attributes('-topmost',1) #置顶窗口


		l1 = Label(root, text="文件大小，不得超过100M:",bg = 'red')
		l1.pack(side=LEFT)
		num1 = StringVar()
		txt1 = Entry(root, width=5,borderwidth=2, textvariable = num1)
		num1.set("1")
		txt1.pack(side=LEFT)


		l2 = Label(root, text="文件个数，不得超过500个:",bg = 'red')
		l2.pack(side=LEFT)
		num2 = StringVar()
		txt2 = Entry(root, width=5,borderwidth=2, textvariable = num2)
		num2.set("1")
		txt2.pack(side=LEFT)


		def on_click():
			ret = True
			c = control()
			x = num1.get()
			y = num2.get()
			if x is not None:
				s = int(x)
				n = int(y)
				if 0 < s <= 500 and 0 < n <= 500:
					ret = c.CreateContent(s,n)
					if ret:
						print("OK")
					else:
						print("FALSE")
				else:
					print("最大可设置500")

			root.destroy()
			return True

		Button(root, text="生成文件", command = on_click).pack(side=LEFT)

		root.mainloop()
if __name__ == "__main__":
	w = Window()
	def usage():
		print(u'\
        	-h or --help：显示帮助信息\n\
        	-1 ：CreateTxtWindow\n\
        	-2 ：CreateWordWindow\n\
        	-3 ：CreateExcelWindow\n\
        	-4 ：CreatePptWindow\n\
        	-5 ：CreateImageWindow\n\
        	-6 ：CreatePdfWindow\n\
        	-7 ：CreateGenSizeWindow\n\
        	-8 : CreateTelnetWindow\n\
        	-9 : CreateCardWindow\n\
        	-a : CreateContentWindow\n\
        	-v or --version：显示版本\
        	')
	if len(sys.argv) == 1:
		usage()
		sys.exit()

	try:
		opts, args = getopt.getopt(sys.argv[1:], "h123456789av", ["help", "version"])
	except getopt.GetoptError:
		usage()        

	for cmd, arg in opts:
		if cmd in ("-h", "--help"):
			usage()
		elif cmd in ("-1", "1"):
			w.CreateTxtWindow()
		elif cmd in ("-2", "1"):
			w.CreateWordWindow()
		elif cmd in ("-3", "1"):
			w.CreateExcelWindow()
		elif cmd in ("-4", "1"):
			w.CreatePptWindow()
		elif cmd in ("-5", "1"):
			w.CreateImageWindow()
		elif cmd in ("-6", "1"):
			w.CreatePdfWindow()
		elif cmd in ("-7", "1"):
			w.CreateGenSizeWindow()
		elif cmd in ("-8", "1"):
			w.CreateTelnetWindow()
		elif cmd in ("-9", "1"):
			w.CreateCardWindow()
		elif cmd in ("-a", "1"):
			w.CreateContentWindow()
		elif cmd in ("-v", "--version"):
			print("version 1.0")