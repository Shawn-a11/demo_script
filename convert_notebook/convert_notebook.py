import sys
import os
from nbconvert import PythonExporter
from glob import glob

# 定义输入输出目录
INPUT_DIR = os.path.join(os.path.dirname(__file__), 'input')
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), 'output')

def convert_notebook_to_python(notebook_path):
    """
    Convert specified .ipynb file to .py file
    """
    try:
        exporter = PythonExporter()
        output, _ = exporter.from_filename(notebook_path)
        
        # 修改输出路径到 output 文件夹
        filename = os.path.basename(notebook_path)
        py_filename = os.path.splitext(filename)[0] + '.py'
        py_file = os.path.join(OUTPUT_DIR, py_filename)
        
        with open(py_file, 'w', encoding='utf-8') as f:
            f.write(output)
            
        print(f"Conversion successful: {notebook_path} -> {py_file}")
        
    except Exception as e:
        print(f"Conversion failed: {str(e)}")

def main():
    # 获取input文件夹中所有的.ipynb文件
    notebook_files = glob(os.path.join(INPUT_DIR, "*.ipynb"))
    
    if not notebook_files:
        print(f"Error: No .ipynb files found in '{INPUT_DIR}'")
        return
        
    for notebook in notebook_files:
        convert_notebook_to_python(notebook)

if __name__ == '__main__':
    main()