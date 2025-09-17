import pdfplumber

def pdf_to_text(pdf_path):
    """
    将PDF文件转换为文本内容
    
    参数:
        pdf_path: PDF文件的路径
        
    返回:
        提取的文本内容字符串，如果出错则返回None
    """
    try:
        # 打开PDF文件
        with pdfplumber.open(pdf_path) as pdf:
            text_content = ""
            # 逐页提取文本
            for page in pdf.pages:
                # 提取当前页文本并添加到结果中
                page_text = page.extract_text()
                if page_text:
                    text_content += page_text + "\n\n"
            return text_content.strip()
    except FileNotFoundError:
        print(f"错误: 找不到文件 '{pdf_path}'")
        return None
    except Exception as e:
        print(f"处理PDF时出错: {str(e)}")
        return None

# 使用示例
if __name__ == "__main__":
    # 替换为你的PDF文件路径
    pdf_file = "1224596794.pdf"
    result = pdf_to_text(pdf_file)
    
    if result:
        print("PDF提取的文本内容:")
        print("-" * 50)
        print(result)
        print("-" * 50)
