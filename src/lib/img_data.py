###############################################################################
# LABEL IMAGES
###############################################################################
def label_img(img, label_data):
  index = int(img.split('.')[1])
  start = index*8
  end = (index+1)*8

  result = np.array(label_data[start:end,:])

  return result

###############################################################################
# CREATE TRAINING DATA
###############################################################################
def create_training_data():
  X = []
  y = []
  data = csv.reader(open(ROOT_PATH + 'textures/tr_data.csv', "rt"),
                      delimiter=",")
  x = list(data)
  label_data = np.array(x).astype("float32")
  
  for img in tqdm(os.listdir(DATA_DIR)):
    y.append(label_img(img, label_data))
    path = os.path.join(DATA_DIR, img)
    X.append(cv2.imread(path, cv2.IMREAD_GRAYSCALE))
  
  X = np.array(X).reshape(-1, IMG_SIZE, IMG_SIZE, 1)
  y = np.array(y).reshape(-1, 8, 8, 1) #8x8xN

  return X, y

###############################################################################
# LOAD TEST IMG
###############################################################################
def load_test_img(num):
  y = []
  data = csv.reader(open(ROOT_PATH + 'textures/ts_data.csv', "rt"),
                      delimiter=",")
  x = list(data)
  label_data = np.array(x).astype("float32")

  img = TEST_DIR + 'fab.' + str(num) + '.jpg'

  y.append(label_img(img, label_data))
  y = np.array(y).reshape(-1, 8, 8, 1)

  return y
