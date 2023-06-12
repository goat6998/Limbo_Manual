import sys, subprocess, cmd, os, traceback, math, re, json, time, pandas as pd, codecs, glob, numpy as np, itertools
from datetime import datetime, timezone, timedelta
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from os.path import join


def get_histogram(image1, image2):
	
	screenshot1 = cv2.imread(image1)
	screenshot2 = cv2.imread(image2)
	
	img_size = (100, 100)
	image1 = cv2.resize(screenshot1, img_size)
	image2 = cv2.resize(screenshot2, img_size)
	
	image1_hist = cv2.calcHist([image1], [0], None, [256], [0, 256])
	image2_hist = cv2.calcHist([image2], [0], None, [256], [0, 256])
	
	hist_check = str(cv2.compareHist(image1_hist, image2_hist, 0))
	return hist_check
	
	
def get_webdriver():
	root = md.join(__file__, "..")

	# webdriverオブジェクトを作る（ブラウザが開く）
	driver_path=md.join(root, "chromedriver.exe")

	# 起動時にオプションをつける。（ポート指定により、起動済みのブラウザのドライバーを取得）
	options = md.webdriver.ChromeOptions()
	options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
	driver = md.webdriver.Chrome(executable_path=driver_path, options=options)

	# ページのタイトルを表示する
	print(driver.title)
	print("========== source ========== ")
	print(driver.page_source)


def set_webdriver(url):
	
#	options = webdriver.ChromeOptions()
#	options.add_argument('--headless')
#	options.add_experimental_option('excludeSwitches', ['enable-logging'])
#	options.use_chromium = True
#	driver = webdriver.Chrome(options=options)
	path_to_driver = "C:/Users/User/OneDrive/デスクトップ/Limbo/chromedriver.exe"
	driver = webdriver.Chrome()
	
#	path_to_driver = r"C:/Users/Goat6/Desktop/Limbo/msedgedriver.exe"
#	driver = webdriver.Edge(executable_path=path_to_driver)
	
#	path_to_driver = "./geckodriver.exe"
#	driver = webdriver.Firefox()
	
	driver.maximize_window()
	driver.get(url)
	print(driver.title)
	return driver
    
    
    
def cls():
	os.system('cls' if os.name=='nt' else 'clear')
	
	
def set_txt_w(filename, data):
	filename = filename+".txt"
	with open(filename, 'w') as file:
		file.write(str(data))
		
		
def set_txt_a(filename, data):
	filename = filename+".txt"
	if os.path.isfile(filename):
		with open(filename, 'a') as file:
			file.write('\n'+str(data))
			
			
def set_txt_O(filename, data):
	filename = filename+".txt"
	if os.path.isfile(filename):
		with open(filename, 'w') as file:
			file.write('\n'.join(data))
			
			
def get_txt(filename):
	filename = filename+".txt"
	if os.path.isfile(filename):
		with open(filename, 'r') as file:
			data = str(file.read())
			return data
	else:
		return None
		
		
def get_txt_list(filename):
	filename = filename+".txt"
	if os.path.isfile(filename):
		with open(filename, 'r') as file:
			data = file.read().split('\n')
			return data
	else:
		return None
		
		
def get_dir(dir):
	if dir is not None:
		path = os.path.dirname(os.path.abspath(__file__)).replace("\\","/")+"/"+str(dir)+"/"
	else:
		path = os.path.dirname(os.path.abspath(__file__)).replace("\\","/")+"/"
		
	if os.path.isdir(path)==False:
		os.mkdir(path)
		if os.path.isdir(path)==True:
			return path
	else:
		return path
		
		
def set_error_log():
	error = u'エラー情報\n' + traceback.format_exc()
	set_txt_w("error", error)
	
	
class JSONDateTimeEncoder(json.JSONEncoder):
    def default(obj):
        if isinstance(obj, (datetime.date, datetime.datetime)):
            return obj.isoformat()
        else:
            return json.JSONEncoder.default(obj)
            
            
def dumps(obj):
    return json.dumps(obj, indent=2, ensure_ascii=False, cls=JSONDateTimeEncoder)
    
    
def set_default(obj):
    if isinstance(obj, set):
        return list(obj)
    raise TypeError
    
    
def get_json(filename):
	filename = filename+'.json'
	if os.path.isfile(filename):
		with open(filename, 'r', encoding='UTF-8') as f:
			data = json.load(f)
			if data is not None:
				data = set_json_decode(data)
				return data
	else:
		return None
		
		
def set_json_decode(results):
	notint = 0
	for data in results:
		if type(data) is str and str(data)=="0":
			notint = 100
	if int(notint)==100:
		results = {int(k):v for k, v in results.items()}
		return results
	else:
		return results
		
		
def set_json(filename, data):
	filename = filename+'.json'
	with open(filename, 'w', encoding='UTF-8') as f:
		return f.write(dumps(data))
		
		
def set_json_row(key, value):
	data = get_json(filename)
	data[key] = value
	set_json(filename,data)
	
	
def set_json_array(filename, array):
	data = get_json(filename)
	for key in array:
		data[key] = array[key]
	set_json(filename,data)
	
	
def set_frame(title, size):
	frame = tkinter.Tk()
	frame.title(title)
	if size is not None:
		frame.geometry(size)
		
	return frame
	
	
def set_frame_center(frame):
	frame.update_idletasks()
	w = frame.winfo_screenwidth()
	h = frame.winfo_screenheight()
	size = tuple(int(_) for _ in frame.geometry().split('+')[0].split('x'))
	x = w/2 - size[0]/2
	y = h/2 - size[1]/1.5
	frame.geometry('%dx%d+%d+%d' % (size + (x, y)))
	
	
#要素待機　clickモード
def get_mode(mode):
	if mode==1:
		set_by = By.XPATH
	elif mode==2:
		set_by = By.CLASS_NAME
	elif mode==3:
		set_by = By.CSS_SELECTOR
	elif mode==4:
		set_by = By.ID
	
	return set_by
	

def wait_click(driver, element):
	WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, element)))
	elm = driver.find_element(By.XPATH, element).click()
	return elm
	
	
def setClick(driver, element):
	actions = ActionChains(driver)
	actions.move_to_element(element)
	actions.click(element)
	actions.perform()
	return True
	
	
#要素待機入力　モード
def wait_sendkey(driver, element, sendkey):
	WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, element)))
	elm = driver.find_element(By.XPATH, element).clear()
	elm.send_keys(sendkey)
	
	
#要素　存在確認クリック
def checkExtClick(driver, mode, element):
	get_elements = getElms(driver, mode, element)
	if len(get_elements) > 0:
		get_element = getElm(driver, mode, element)
		scriptClick(driver, get_element)
		
		
#スクリプトクリック
def scriptClick(driver, element):
	driver.execute_script("arguments[0].click();", element)
	
	
	
