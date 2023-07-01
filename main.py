class mywindow(QtWidgets.QMainWindow):
"""docstring for mywindow"""
	def __init__(self):
		super(mywindow, self).__init__()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.ui.road_to_site.clicked.connect(self.road_to_site)
		self.ui.road_to_cms.clicked.connect(self.road_to_cms)
		self.ui.OK.clicked.connect(self.OK)
		self.ui.Cancel.clicked.connect(QCoreApplication.instance().quit)
		# self.ui.Cancel.clicked.connect(self.test)
	def road_to_site(self):
		fname = QFileDialog.getExistingDirectory(self, 'Open file', "C:/")
		self.ui.view_site.setText(fname)

	def road_to_cms(self):
		fname = QFileDialog.getExistingDirectory(self, 'Open file', "C:/")
		self.ui.view_cms.setText(fname)

	def OK(self):
		resourse = self.ui.view_site.text()
		destrib = self.ui.view_cms.text()
		copy = copyrat(resourse, destrib)
		flag = copy.copy()
		if not flag:
		copy.update()
		copy.trees()
		QMessageBox.information(self, "Complete", "the derictory has been moved successfully", 
		QMessageBox.Ok, QMessageBox.Ok)
		else:
		QMessageBox.warning(self, "Error copyrate", "this diectory already exists", QMessageBox.Ok, 
		QMessageBox.Ok)
		app = QtWidgets.QApplication([])
		app.setStyleSheet("""QMainWindow {background-image: url("back1.jpg"); background-repeat: 
		no-repeat; background-position: center;} QPushButton {background-color: #62adcd; fontfamily: "Century Gothic";} QLabel{font-family: "Century Gothic"; font-size: 9pt;} 
		QComboBox{font-family: "Century Gothic"; background-color: #62adcd; }""")
		application = mywindow()
		application.show()


class copyrat(object):
"""docstring for copyrat"""
	def __init__(self, sourse, destination):
		super(copyrat, self).__init__()
		self.sourse = sourse
		arr = sourse.split('/')
		self.destination = destination
		self.destination += '/' + arr[len(arr)-1]
		self.blog = self.destination + "/local/templates/blog"

	def copy(self):
		flag = os.path.exists(self.destination)
		if not flag:
			shutil.copytree(self.sourse, self.destination)
			os.makedirs(self.blog)
			list_dir = os.listdir(self.sourse + "/wp-content")
		for i in list_dir:
			if not os.path.exists(self.blog + '/' + i):
				shutil.copytree(self.sourse + "/wp-content/" + i,self.blog + '/' + i)
		if os.path.exists(self.destination + "/wp-content/"):
			shutil.rmtree(self.destination + "/wp-content/")
			list_dir = os.listdir(self.sourse + "/wp-includes")
			5
		for i in list_dir:
			if not os.path.exists(self.blog + '/' + i):
				shutil.copytree(self.sourse + "/wp-includes/" + i,self.blog+ '/' + i)
		if os.path.exists(self.destination + "/wp-includes"):
			shutil.rmtree(self.destination + "/wp-includes")
			return flag
		else:
			return flag
	def update(self):
		offset = 0
		line = ""
		index_php = self.sourse + '/index.php'
		#---------------------------------header
		file = open(index_php, encoding = "utf-8", errors = "ignore")
		f = open(self.blog + "/header.php", "w")
		while True:
			item = file.readline()
			new_item = item.strip()
			if item.find("wp-content"):
				item = item.replace("wp-content","<?=SITE_TEMPLATE_PATH?>")
			elif item.find("wp-includes"):
				item = item.replace("wp-includes","<?=SITE_TEMPLATE_PATH?>")
			elif item.find("wp-json"):
				item = item.replace("wp-json","<?=SITE_TEMPLATE_PATH?>")

			if new_item != "<style>":
				f.write(item)
			else:
				line = item
				break

		offset = file.tell()
		f.close()
		file.close()
		#-------------------------------/header
		#-------------------------------index.php
		file = open(index_php, "r",encoding = "utf-8", errors = "ignore")
		file.seek(offset+5)
		f = open(self.destination + "/index.php", "w")
		f.write("<? require($_SERVER['DOCUMENT_ROOT'].'/bitrix/header.php'); ?>\n")
		f.write(line)
		count = 0
		while True:
			item = file.readline()
			new_item = item.strip()
			if item.find("wp-content"):
				item = item.replace("wp-content","<?=SITE_TEMPLATE_PATH?>")
			elif item.find("wp-includes"):
				item = item.replace("wp-includes","<?=SITE_TEMPLATE_PATH?>")
			elif item.find("wp-json"):
		6
				item = item.replace("wp-json","<?=SITE_TEMPLATE_PATH?>")
			if new_item != "<div class=\"footer\">":
				f.write(item)
			else:
				line = item
				f.write("<? require($_SERVER['DOCUMENT_ROOT'].'/bitrix/footer.php'); ?>")
				break

		f.close()
		#-------------------------------/index.php
		#-------------------------------footer.php
		f = open(self.blog + "/footer.php", "w")
		f.write(line)
		count = 0
		while True:
			item = file.readline()
			new_item = item.strip()
			if item.find("wp-content"):
				item = item.replace("wp-content","<?=SITE_TEMPLATE_PATH?>")
			elif item.find("wp-includes"):
				item = item.replace("wp-includes","<?=SITE_TEMPLATE_PATH?>")
			elif item.find("wp-json"):
				item = item.replace("wp-json","<?=SITE_TEMPLATE_PATH?>")
			if new_item != "</html>":
				f.write(item)
			else:
				f.write(item)
				break
		f.close()
		file.close()
	def trees(self):
		lis = []
		# for name in sorted(glob.glob(self.destination + '/**/index.php', recursive=True)):
		# lis.append(name)
		for name in sorted(glob.glob(self.destination + '/**/index.html', recursive=True)):
			lis.append(name)
		# lis.pop(0)
		for iname in lis:
			copyrat.change(self,iname)
	def change(self,put):
		are = put.split('\\')
		fname = ""
		are[-1] = "index.php"
		for i in are:
			fname+=i + '/'
			fname = fname[:-1]
			put = put.replace('\\','/')
			file = open(put, "r", encoding = "utf-8", errors = "ignore")
			ofer = 0
			f = open(fname, "w", errors =
			"ignore")
		7
		f.write("<? require($_SERVER['DOCUMENT_ROOT'].'/bitrix/header.php'); ?>")
		count = 0
		while True and count < 2000:
			item = file.readline()
			new_item = item.strip()
			count += 1
			if new_item == "<div class=\"content-wrapper\">":
			f.write(item)
			ofer = file.tell()
			break
		file.seek(ofer)
		count = 0
		while True and count<1000:
			item = file.readline()
			new_item = item.strip()
			count += 1
			if item.find("wp-content"):
				item = item.replace("wp-content","<?=SITE_TEMPLATE_PATH?>")
			elif item.find("wp-includes"):
				item = item.replace("wp-includes","<?=SITE_TEMPLATE_PATH?>")
			elif item.find("wp-json"):
				item = item.replace("wp-json","<?=SITE_TEMPLATE_PATH?>")

			if new_item != "<div class=\"footer\">":
				f.write(item)
			else:
				f.write("<? require($_SERVER['DOCUMENT_ROOT'].'/bitrix/footer.php'); ?>")
				break
		f.close()
		file.close()