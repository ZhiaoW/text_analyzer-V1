# Text Analyzer V1

## 简介

这是一个用 Python 编写的英文文本分析小项目。

程序可以读取用户输入的英文文本，或者读取 `.txt` 文件中的内容，然后统计词频，并输出分析结果。

这是我的第一个 Python 小项目，主要用于帮我 
* 1.复习并练习python基础函数,String, List, Dict等等
* 2.将大任务分为多个小模块，培养计算机思维
* 3.练习github，学习项目结构，写readme


---

## 功能

* 清除常见英文标点符号
* 统计总词数
* 统计不同单词的数量
* 找出出现次数最多的前 N 个单词
* 支持读取 `.txt` 文件，或英文句子
* 将完整词频结果保存为 CSV 文件

---

## 项目结构

```text
text_analyzer-V1/
│
├── README.md
├── text_analyzer_v1.py
├── sample.txt
├── sample_output.csv
└── .gitignore
```


---

## 运行方式

在终端进入项目文件夹后，打开python并运行：

text_analyzer_v1.py


---

## 使用方法

运行程序后，会出现提示：

Type 1 to enter text, or 2 to read a .txt file:

输入 `1`：手动输入英文文本。

输入 `2`：读取一个 `.txt` 文件，例如：

sample.txt

之后程序会询问：

How many top words do you want to see?

输入一个数字，例如 `5`，程序就会输出出现次数最多的前 5 个单词。

---

## 示例输入

Python is fun. Python is powerful.
Text analyzer is a simple Python project.

---

## 示例输出

TEXT ANALYSIS REPORT

Total words: 11
Unique words: 8

Top 3 most common words:
1. python          3 times
2. is              2 times
3. fun             2 times

Frequency of words saved to: Text_Analyzer.csv

---

## CSV 输出

程序运行结束后，会生成一个 CSV 文件：

Text Analyzer.csv

里面保存所有单词的出现次数。

示例：

| word   | count |
| ------ | ----- |
| python | 3     |
| is     | 2     |
| fun    | 1     |

---

## 我学到了什么

通过这个项目，我练习了：

* Python 函数
* 字符串处理
* 字典统计
* for 循环
* 文件读取
* 简单项目结构

---

## 未来可以改进的地方

之后可以继续改进：

* 支持 PDF 文件
* 支持中文分词
* 加入词频可视化
* 加入测试文件

---

## 作者

Created by ZhiaoW.
