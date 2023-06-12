import Method as md



class set_live_open():
	
	
	def __init__(self):
		try:
			super().__init__()
			self.start = md.time.time()
			self.setting = md.get_json("setting")
			self.driver = self.set_browser()
			self.set_opening()
			
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
		
		
	def set_opening(self):
		
		"""
		#左スライドメニュー閉じる
		left_menu = self.driver.find_element(md.By.XPATH, '//*[@id="page-unfold-sidebar"]/div[1]/div/button')
		print(left_menu)
		if left_menu is not None:
			left_menu.click()
			md.sleep(0.1)
			
			
		#右スライドメニュー閉じる
		right_menu = self.driver.find_elements(md.By.XPATH, '//*[@id="public-chat"]/div[1]/div[2]/button')
		if right_menu is not None:
			right_menu.click()
			md.sleep(0.1)
			
		"""
		
		auto_tab = self.driver.find_element(md.By.XPATH, '//*[@id="Limbo-control-1"]/div[1]/button[2]')
		auto_tab.click()
		md.sleep(0.1)
		auto_tab.send_keys(md.Keys.TAB)
		md.sleep(0.1)
		
		#金額入力
		price_elm = self.driver.find_element(md.By.XPATH, '//*[@id="Limbo-control-1"]/div[2]/div/div[1]/div[2]/input')
		price_elm.send_keys(self.setting["price"])
		md.sleep(0.1)
		
		#勝ちリセット増やす%タブオープン
		self.driver.find_element(md.By.XPATH, '//*[@id="Limbo-control-1"]/div[2]/div/div[3]/div[2]/div[1]').click()
		md.sleep(0.1)
		#勝ちリセット増やす%入力
		"""
		win_reset_elm = self.driver.find_element(md.By.XPATH, '//*[@id="Limbo-control-1"]/div[2]/div/div[3]/div[2]/input')
		win_reset_elm.send_keys(md.Keys.CONTROL, "a")
		win_reset_elm.send_keys(self.setting["win_reset"])
		auto_tab.send_keys(md.Keys.TAB)
		"""
		
		#勝ったら辞める
		price_elm = self.driver.find_element(md.By.XPATH, '//*[@id="Limbo-control-1"]/div[2]/div/div[4]/div[2]/input')
		price_elm.send_keys(md.Keys.CONTROL, "a")
		price_elm.send_keys(self.setting["win_price"])
		md.sleep(1)
		
		#負けリセット増やす%タブオープン
		lose_tab = self.driver.find_element(md.By.XPATH, '//*[@id="Limbo-control-1"]/div[2]/div/div[5]/div[2]/div[1]')
		lose_tab.click()
		md.sleep(0.1)
		#負けリセット増やす%入力
		price_elm = self.driver.find_element(md.By.XPATH, '//*[@id="Limbo-control-1"]/div[2]/div/div[5]/div[2]/input')
		price_elm.send_keys(md.Keys.CONTROL, "a")
		price_elm.send_keys(self.setting["lose_reset"])
		md.sleep(0.1)
		
		#負けたら辞める入力
		price_elm = self.driver.find_element(md.By.XPATH, '//*[@id="Limbo-control-1"]/div[2]/div/div[6]/div[2]/input')
		price_elm.click()
		price_elm.send_keys(md.Keys.CONTROL, "a")
		price_elm.send_keys(self.setting["lose_price"])
		md.sleep(0.1)
		
		#ペイアウト入力
		payout_elm = self.driver.find_element(md.By.XPATH, '//*[@id="game-Limbo"]/div/div[2]/div[2]/div[3]/div[1]/div[2]/input')
		payout_elm.click()
		payout_elm.send_keys(md.Keys.CONTROL, "a")
		payout_elm.send_keys(self.setting["payout"])
		md.sleep(0.1)
		
		#live open
		live_open = self.driver.find_element(md.By.XPATH, '//*[@id="game-Limbo"]/div/div[3]/button[5]')
		live_open.click()
		
		md.subprocess.run(r"python C:\Users\User\OneDrive\デスクトップ\Limbo\Live.py")
		
		
set_live_open = set_live_open()



