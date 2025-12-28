YontenData

本仓库用于存放广韵相关的数据文件与工具代码，主要服务于韵图生成、音系分析以及相关研究用途。

This repository contains data files and tools related to the Guangyun (《广韵》), mainly for rhyme table generation, phonological analysis, and related research purposes.

⸻

文件说明 | File Description

1. superttf.ttf
	•	方正超大字符集字体文件
	•	覆盖极其完整的汉字范围，确保《广韵》中出现的汉字绝大多数都可以被正确显示
	•	适用于韵图绘制、字表展示、PDF / 图片导出等需要高兼容性的场景
	•	Fangzheng ultra-large character set TrueType font
	•	Provides extremely broad CJK coverage, ensuring that the vast majority of characters appearing in Guangyun can be correctly displayed
	•	Suitable for rhyme table rendering, character list display, and PDF / image export scenarios requiring high glyph compatibility

⸻

2. YondoCreator.py
	•	韵图生成器的核心代码文件
	•	负责读取广韵字表与声韵数据，按照设定规则生成韵图结构
	•	可作为研究、二次开发或工具链集成的基础模块
	•	Core source code for the rhyme table generator
	•	Reads the Guangyun character database and initial consonant / final data, then generates rhyme table structures according to predefined rules
	•	Can serve as a base module for research, secondary development, or integration into other toolchains

⸻

3. kuangJyon.sqlite
	•	《广韵》全字表数据库文件（SQLite 格式）
	•	包含广韵收录的完整字项信息
	•	便于通过 SQL 查询进行统计分析、条件筛选和程序化处理
	•	Complete Guangyun character database (SQLite format)
	•	Contains full character entries recorded in Guangyun
	•	Convenient for statistical analysis, conditional filtering, and programmatic processing via SQL queries

⸻

4. Sjiengnjiu.json
	•	韵图的声母初始数据
	•	以 JSON 形式定义韵图所使用的声母系统及其基础属性
	•	作为韵图自动生成过程中的输入数据之一
	•	Initial consonant (shengmu) data for rhyme tables
	•	Defines the consonantal system and its basic attributes in JSON format
	•	Serves as one of the input data sources for automatic rhyme table generation

⸻

5. 韵图的韵母初始数据 | Initial Finals Data
	•	用于定义韵图中各类 韵母（韵部 / 韵类） 的基础结构与分组方式
	•	与声母数据配合，共同决定韵图的整体布局与逻辑结构
	•	Defines the basic structure and grouping of finals (rhyme categories) used in rhyme tables
	•	Works together with initial consonant data to determine the overall layout and logical organization of the rhyme tables

⸻

适用场景 | Use Cases
	•	中古汉语 / 广韵音系研究
	•	韵图的自动生成与可视化
	•	教学演示与学术资料制作
	•	相关工具或系统的底层数据支持
	•	Middle Chinese / Guangyun phonological research
	•	Automatic generation and visualization of rhyme tables
	•	Teaching demonstrations and academic material preparation
	•	Foundational data support for related tools or systems

⸻

如需对数据结构或生成逻辑进行扩展，可直接基于现有文件进行修改或二次开发。

If you wish to extend the data structures or generation logic, you may directly modify the existing files or use them as a basis for further development.
