# python version 3.7 
    pip install   PyQt5 
    pip install   transformers


模型选择

    tokenizer = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-en-zh")
    model = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-en-zh")

可以登录 https://huggingface.co/models 选择合适的翻译模型 将翻译模型的名字进行替换
其中 

    Helsinki-NLP/opus-mt-en-zh

就是我选择的 英文——中文 的翻译模型


### 拖拽之后窗口可能有未响应的字样  别急,那是后台正在逐句翻译 这需要时间

### 翻译的结果将会写入到 *D:/result.txt* 中

### 您也可以通过修改  *dragEnterEvent(self, evn)* 函数来修改结果文件的位置