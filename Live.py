import Method as md



class Action_Limbo:
	
	
	def __init__(self):
		try:
			super().__init__()
			self.start = md.time.time()
			self.setting = md.get_json("setting")
			self.driver = self.set_browser()
			self.set_action()
			
		except Exception as e:
			md.set_error_log()
		finally:
			def __call__(self): return self.__init__()
			
			
	def __del__(self):
		print("\n")
		print("処理時間：　" + str(md.time.time() - self.start))
		input()
		
		
		#ブラウザセット
	def set_browser(self):
		root = md.join(__file__, "..")

		# webdriverオブジェクトを作る（ブラウザが開く）
		driver_path=md.join(root, "chromedriver.exe")

		# 起動時にオプションをつける。（ポート指定により、起動済みのブラウザのドライバーを取得）
		options = md.webdriver.ChromeOptions()
		options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
		driver = md.webdriver.Chrome(executable_path=driver_path, options=options)
		driver.implicitly_wait(10)
		# ページのタイトルを表示する
		
		print("========== title ========== ")
		print(driver.title)
		return driver
		
		
	def set_action(self):
		
		check_list = []
		init_price = 100
		set_count = 1
		md.set_txt_w("set_count", 1)
		
		while True:
			
			try:
				print("start")
				check_list.clear()
				
				get_elements = self.driver.find_elements(md.By.CLASS_NAME, "recent-item")
				if len(get_elements) > 0:
					i = 0
					for elm in get_elements:
						if "is-lose" in elm.get_attribute("innerHTML"):
							check_list += ["lose"]
						else:
							check_list += ["win"]
						i = i + 1
				
				if "win" in check_list[ len(check_list)-1 ]:
					
					set_count = md.get_txt("set_count")
					set_count = int(set_count) + 1
					if set_count==2:
						set_price = init_price * 3
					elif set_count==3:
						set_price = init_price * 2
					elif set_count==4:
						set_price = init_price * 6
					elif set_count==5:
						set_price = init_price
					#金額入力
					self.set_price_action(set_price)
					self.game_btn_click()
					
					if set_count==5:
						set_count = 1
					md.set_txt_w("set_count", set_count)
					
				else:
					md.set_txt_w("set_count", 1)
					#金額入力
					self.set_price_action(init_price)
					self.game_btn_click()
					
				
			except:
				print("wait")
			
			md.sleep(0.1)
			md.os.system('cls')
		
		
	def set_price_action(self, set_price):
		#金額入力
		price_elm = self.driver.find_element(md.By.XPATH, '//*[@id="Limbo-control-0"]/div[2]/div/div[1]/div[2]/input')
		price_elm.click()
		price_elm.send_keys(md.Keys.CONTROL, "a")
		price_elm.send_keys(set_price)
		md.sleep(0.1)
		
		
	def game_btn_click(self):
		self.driver.find_element(md.By.XPATH, '//*[@id="Limbo-control-0"]/div[2]/div/button/div').click()
		md.sleep(0.1)
		
		
	def set_win_lose(self, filepath, data):
		with open(filepath + ".txt",'w') as f:
			f.writelines([d+"\n" for d in data])
			
			
	def get_win_lose(self, filename):
		get_data = md.get_txt_list(filename)
		new_data_list = []
		for row in get_data:
			if row!="":
				new_data_list.append(row)
				
		return new_data_list
		
		


ad = Action_Limbo()



