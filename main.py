import sys
from PyQt5.QtWidgets import *
from transformers import pipeline,AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-en-zh")
model = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-en-zh")
translation = pipeline('translation_zh_to_en',model=model,tokenizer=tokenizer)
# print('加载完成')


def translationPytorch(word):
  res = translation(word)[0]['translation_text']
  return  res


def isnumber(string):
  a = string[:1]
  if a == "0" or a == "1" or a == "2" or a == "3" or a == "4" or a == "5" or a == "6" or a == "7" or a == "8" or a == "9":
    return True
  else:
    return False

def write_txt(path, content):
  '''实现TXT文档的写方法'''
  with open(path, 'a+',encoding='utf-8') as f:
    f.write(content + "\n")


def transtxt(pathfrom,pathto):
  data = []
  file = open(pathfrom, 'r',encoding='utf-8')
  file_data = file.readlines()
  for row in file_data:
    tmp_list = row.split('\n')
    data.append(tmp_list)
  for indexi in data:
    for words in indexi:
      if len(words) > 0:
        if isnumber(words):
          # print(words)
          # write
          write_txt(pathto, words)

        else:
          tran = translationPytorch(words)
          # print(words)
          # print(tran)
          # write tran
          write_txt(pathto, words)
          write_txt(pathto, tran)


class example(QWidget):
    position=''
    def __init__(self):
        super(example, self).__init__()
        # 窗口标题
        self.setWindowTitle('请拖拽进需要执行的文件')
        # 定义窗口大小
        self.resize(500, 400)
        self.QLabl = QLabel(self)
        self.QLabl.setGeometry(2, 200, 4000, 90)
        # 调用Drops方法
        self.setAcceptDrops(True)

    def dragEnterEvent(self, evn):
        self.setWindowTitle('可以松手了 可能响应别急正在翻译中。。。。')
        self.QLabl.setText('已完成：\n' + evn.mimeData().text()+'的翻译\n结果在：D:/result.txt')
        self.position = evn.mimeData().text()
        pathfrom = self.position
        pathfrom = pathfrom[8:]
        pathto = "D:/result.txt"
        transtxt(pathfrom,pathto)
        evn.accept()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    e = example()
    e.show()
    sys.exit(app.exec_())
