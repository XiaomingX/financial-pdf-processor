# financial-pdf-processor

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python](https://img.shields.io/badge/Python-3.8%2B-brightgreen.svg)](https://www.python.org/)

一个轻量、高效的**财务类PDF文本提取工具**，专注于将年报、投资者问答记录等财务文档转化为结构化文本，为后续LLM（大语言模型）应用（如财务问答、文档摘要）和数据分析（如指标提取、趋势分析）提供高质量输入。


## 项目简介

财务报告PDF往往包含大量关键信息，但原生格式难以直接用于AI建模或数据挖掘。本项目基于`pdfplumber`实现精准的文本提取，解决财务PDF“可看不可用”的问题，打通“PDF文档 → 机器可读文本”的核心链路，适配各类财务场景的下游需求。

> 核心目标：让财务数据从静态PDF中“解放”出来，成为LLM和数据分析工具的“可用原料”。


## 核心功能

- ✅ **精准文本提取**：逐页解析PDF，保留文本逻辑结构，适配财务文档的多段落、多章节格式。
- ✅ **错误处理机制**：内置文件不存在、解析异常等错误捕获，输出清晰提示，提升稳定性。
- ✅ **轻量无依赖**：仅依赖`pdfplumber`，安装简单，可快速集成到现有财务分析工作流。
- ✅ **下游兼容**：提取的文本可直接输入LLM（如GPT、Llama）或数据分析工具（如Pandas、NLTK）。


## 快速开始

### 1. 环境要求
- Python 3.8 及以上版本

### 2. 安装步骤

```bash
# 克隆仓库
git clone https://github.com/XiaomingX/financial-pdf-processor.git
cd financial-pdf-processor

# 安装依赖（推荐使用虚拟环境）
pip install -r requirements.txt
```

> 若仓库未包含`requirements.txt`，可手动创建并添加内容：`pdfplumber>=0.10.0`

### 3. 基础使用

#### 方式1：直接运行脚本
修改`main.py`中的PDF路径，执行脚本即可输出提取结果：
```bash
python main.py
```

#### 方式2：作为模块集成
在你的Python项目中导入核心函数：
```python
from pdf_processor import pdf_to_text

# 提取财务年报文本
financial_report_text = pdf_to_text("1224596794.pdf")

if financial_report_text:
    # 1. 用于LLM摘要（示例：调用OpenAI API）
    # import openai
    # response = openai.ChatCompletion.create(
    #     model="gpt-3.5-turbo",
    #     messages=[{"role": "user", "content": f"总结以下年报核心财务数据：{financial_report_text[:2000]}"}]
    # )
    
    # 2. 用于数据分析（示例：统计关键词频次）
    # from collections import Counter
    # keywords = ["营收", "净利润", "毛利率"]
    # count = Counter(financial_report_text.split())
    # print({kw: count.get(kw, 0) for kw in keywords})
```


## 项目结构

```
financial-pdf-processor/
├── pdf_processor.py      # 核心模块：PDF文本提取逻辑
├── README.md             # 项目说明文档（当前文件）
├── LICENSE               # Apache-2.0 许可证
├── .gitignore            # Git忽略文件配置
└── requirements.txt      # 项目依赖清单
```


## 下一步改进方向（TODO）

### 1. 功能增强
- [ ] 支持**财务表格提取**：针对年报中的资产负债表、利润表，输出结构化DataFrame（依赖`pdfplumber`表格解析能力）。
- [ ] 开发**OCR适配**：兼容扫描版PDF（集成`pytesseract`，解决图片类PDF无法提取文本的问题）。
- [ ] 实现**批量处理**：支持文件夹级别的多PDF并行提取，输出按文件名分类的文本文件。

### 2. LLM集成优化
- [ ] 对接主流LLM框架：集成LangChain/LlamaIndex，直接将提取的文本构建为财务知识库。
- [ ] 财务问答模板：内置Prompt模板，支持“自动提取净利润增长率”“总结投资者关心的核心问题”等场景化需求。

### 3. 数据分析适配
- [ ] 文本清洗模块：去除财务文档中的冗余信息（如页眉页脚、免责声明），提纯核心数据。
- [ ] 指标自动识别：基于正则表达式或小模型，自动识别并提取“营收”“净利润”“资产负债率”等关键财务指标。

### 4. 工程化优化
- [ ] 开发CLI工具：支持通过命令行指定输入路径、输出格式（TXT/JSON）、页码范围等参数。
- [ ] 增加单元测试：覆盖核心函数的正常/异常场景（如空PDF、加密PDF）。
- [ ] 完善日志系统：替换`print`为`logging`，支持日志输出到文件，便于问题排查。


## 许可证

本项目基于 **Apache License 2.0** 开源，详见[LICENSE](LICENSE)文件。


## 贡献指南

欢迎通过以下方式参与项目改进：
1. 提交Issue：反馈Bug、提出新功能建议（如支持特定类型的财务PDF）。
2. 发起PR：
   - 代码需遵循PEP 8规范。
   - 新增功能需附带对应的测试用例。
   - 提交信息格式：`[类型] 描述`（如`[Feature] 新增表格提取功能`）。


## 联系作者

- GitHub：[XiaomingX](https://github.com/XiaomingX)
- 如有问题，可直接在仓库提交Issue交流。