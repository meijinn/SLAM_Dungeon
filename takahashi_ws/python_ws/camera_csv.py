from PIL import Image
import csv

# 画像ファイルを読み込む
img = Image.open(r"c:\Users\s_takahashi\takahashi_workspace\7_gh_ws\SLAM_Dungeon\takahashi_ws\python_ws\target.jpg")
# 画像のピクセルデータを取得
pixels = img.load()
# 画像の幅と高さを取得
width, height = img.size

# RGB値を格納するリストを初期化
#rgb_values = []
# RGB値を列ごと
r_values = []
g_values = []
b_values = []

# 画像の各ピクセルのRGB値をリストに格納
for y in range(height):
    tmp_r = []
    tmp_g = []
    tmp_b = []
    for x in range(width):
        r, g, b = pixels[x, y]
        tmp_r.append(r)
        tmp_g.append(g)
        tmp_b.append(b)
        #rgb_values.append((r, g, b))
    r_values.append(tmp_r)
    g_values.append(tmp_g)
    b_values.append(tmp_b)
# CSVファイルにRGB値を書き込む
with open('image_r.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for item in r_values:
        writer.writerow(item)
with open('image_g.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for item in g_values:
        writer.writerow(item)
with open('image_b.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for item in b_values:
        writer.writerow(item)