import Method as md


class Action_Limbo:
	
	def __init__(self):
		try:
			super().__init__()
			self.start = md.time.time()
			self.setting = md.get_json("setting")
			self.martin_flg = 'off'
			self.set_action()
#			self.set_values()
			
		except Exception as e:
			md.setErrorLog()
		finally:
			def __call__(self): return self.__init__()
			
			
	def __del__(self):
		print("\n")
		print("処理時間：　" + str(md.time.time() - self.start))
		input()
		
		
	def set_action(self):
		self.set_login()
		update_price, update_payout, update_parcent = self.get_price_payout(self.setting['mode'])
		self.set_parameter(update_price, update_payout, update_parcent)
		self.set_start_stop()
		self.live_open()
		self.set_game()
		
		
	def set_values(self):
		data = {
"normal_price":10,
"normal_payout":1.01,
"normal_parcent":0,
"martin_price":1,
"martin_payout":2.01,
"martin_parcent": 100.01,
"mode":1,
"update": 0,
"profit": 0,
"profit_price_high":100,
"profit_price_low":-50,
"email":"goat6998@gmail.com",
"password":"irei*0103"
}
		data = md.set_json("setting", data)
		print(data)
		
		
	def set_login(self):
		#ctrl+d
		md.pyautogui.hotkey('winleft', 'd')
		md.pyautogui.moveTo(76, 829)
		md.pyautogui.doubleClick()
		md.sleep(2)
		
		
		#ブラウザ拡大
		md.pyautogui.hotkey('alt', 'space')
		md.sleep(2)
		md.pyautogui.press('x')
		md.sleep(1)
		
		
		#limbo
		limbo_url = 'bc.game/ja/game/limbo'
		md.pyperclip.copy(limbo_url)
		md.pyautogui.hotkey('ctrl', 't')
		md.pyautogui.click(555, 79)
		md.pyautogui.hotkey('ctrl', 'V')
		md.pyautogui.press('enter')
		md.sleep(3)
		
		
		#cookie
		md.pyautogui.moveTo(1118, 906)
		md.sleep(1)
		md.pyautogui.click()
		md.sleep(1)
		
		#login
		md.pyautogui.moveTo(1512, 151)
		md.sleep(1)
		md.pyautogui.click()
		md.sleep(1)
		
		#login check
		md.pyautogui.moveTo(713, 74)
		md.sleep(1)
		md.pyautogui.click()
		md.pyautogui.hotkey('ctrl', 'a')
		md.pyautogui.hotkey('ctrl', 'c')
		check_url = md.pyperclip.paste()
		if 'profile' in check_url:
			#profile close
			md.pyautogui.moveTo(1261, 200)
			md.sleep(1)
			md.pyautogui.click()
			md.sleep(1)
			
		else:
			#gmail
			md.pyautogui.moveTo(1068, 904)
			md.sleep(1)
			md.pyautogui.click()
			md.sleep(3)
			
			#account
			md.pyautogui.moveTo(843, 571)
			md.sleep(1)
			md.pyautogui.click()
			md.sleep(4)
			
			
		
	def set_parameter(self, price, payout, parcent):
		
		md.pyautogui.hotkey("ctrl", "home")
		md.sleep(1)
		
		#自動
		md.pyautogui.moveTo(519, 362)
		md.sleep(1)
		md.pyautogui.click()
		md.sleep(1)
		
		#price
		md.pyperclip.copy(price)
		md.pyautogui.moveTo(238, 491)
		md.sleep(1)
		md.pyautogui.click()
		md.pyautogui.hotkey('ctrl', 'a')
		md.pyautogui.hotkey('ctrl', 'V')
		md.sleep(1)
		
		#スクロール
		m_posi_x, m_posi_y = md.pyautogui.position()
		md.pyautogui.scroll(-300,m_posi_x,m_posi_y)
		
		#martin parcent
		if self.martin_flg == 'off' and self.setting['mode']==2:
			md.pyautogui.moveTo(200, 638)
			md.sleep(1)
			md.pyautogui.click()
			md.sleep(1)
			self.martin_flg = 'on'
			
		md.pyperclip.copy(parcent)
		md.pyautogui.moveTo(404, 632)
		md.sleep(1)
		md.pyautogui.click()
		md.pyautogui.hotkey('ctrl', 'a')
		md.pyautogui.hotkey('ctrl', 'V')
		md.sleep(1)
		
		if self.martin_flg == 'on' and self.setting['mode']==1:
			md.pyautogui.moveTo(200, 638)
			md.sleep(1)
			md.pyautogui.click()
			md.sleep(1)
			self.martin_flg = 'off'
			
		
		#payout
		md.pyperclip.copy(payout)
		md.pyautogui.moveTo(755,782)
		md.pyautogui.click()
		md.pyautogui.hotkey('ctrl', 'a')
		md.pyautogui.hotkey('ctrl', 'V')
		
		
	def set_start_stop(self):
		#game start
		md.pyautogui.moveTo(430,997)
		md.pyautogui.click()
		md.sleep(1)
		
		
		#live open
	def live_open(self):
		print("live open")
		md.pyautogui.moveTo(1660, 993)
		md.pyautogui.click()
		md.sleep(1)
		
		
		#live close
	def live_close(self):
#		md.pyautogui.hotkey("ctrl", "home")
#		md.sleep(1)
		md.pyautogui.moveTo(1146, 285)
		md.pyautogui.click()
		md.sleep(1)
		
		
	def get_price_payout(self, mode):
		if mode==1:
			set_price = self.setting['normal_price']
			set_payout = self.setting['normal_payout']
			set_parcent = self.setting['normal_parcent']
		else:
			set_price = self.setting['martin_price']
			set_payout = self.setting['martin_payout']
			set_parcent = self.setting['martin_parcent']
		return set_price, set_payout, set_parcent
		
		
	def set_game(self):
		
		#profit
		md.pyautogui.moveTo(1093, 524)
		
		while True:
			self.setting = md.get_json("setting")
			self.setting['martin_price'] = round(self.setting['martin_price'], 6)
			set_price, set_payout, set_parcent = self.get_price_payout(self.setting['mode'])
			print( "set price:" + str(set_price) + " set payout: " + str(set_payout) )
			if self.setting['mode']==2:
				print("set_parcent:" + str(set_parcent))
			
			md.pyautogui.doubleClick()
			md.pyautogui.hotkey('ctrl', 'c')
			md.pyautogui.hotkey('ctrl', 'V')
			profit = md.pyperclip.paste()
#			profit = float(profit)
			
			
#			profit = self.setting['profit']
			print("profit:" + str(profit))
			
			if profit > self.setting['profit_price_high'] and self.setting['mode']==2:
				self.setting["update"] = 100
				update_price, update_payout, update_parcent = self.get_price_payout(1)
				self.setting['mode'] = 1
#				print( "normal_price:" + str(self.setting["normal_price"]) )
				
			elif profit < self.setting['profit_price_low'] and self.setting['mode']==1:
				self.setting["update"] = 100
				update_price, update_payout, update_parcent = self.get_price_payout(2)
				self.setting['mode'] = 2
#				print( "martin_price:" + str(self.setting["martin_price"]) )
				
			if self.setting["update"] == 100:
				self.set_start_stop()
				self.live_close()
				
				self.set_parameter(update_price, update_payout, update_parcent)
				self.setting["update"] = 0
				md.set_json('setting', self.setting)
				
				self.set_start_stop()
				self.live_open()
				
			
			print( "update:" + str(self.setting["update"]) )
			md.sleep(1)
			md.os.system('cls')
			
			
			
			
			