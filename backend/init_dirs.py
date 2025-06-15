import os
import sys

def create_if_not_exists(directory):
    """如果目录不存在则创建"""
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"创建目录: {directory}")
    else:
        print(f"目录已存在: {directory}")

def create_empty_file(filepath):
    """如果文件不存在则创建空文件"""
    if not os.path.exists(filepath):
        with open(filepath, 'w', encoding='utf-8') as f:
            pass
        print(f"创建空文件: {filepath}")
    else:
        print(f"文件已存在: {filepath}")

def main():
    """创建必要的目录结构和初始文件"""
    # 创建目录结构
    directories = [
        "app",
        "app/api",
        "app/api/endpoints",
        "app/core",
        "app/models",
        "app/schemas",
        "app/services",
        "app/utils",
        "tests",
    ]
    
    for directory in directories:
        create_if_not_exists(os.path.join("app", directory))
    
    # 创建空文件
    files = [
        "app/__init__.py",
        "app/api/__init__.py",
        "app/api/endpoints/__init__.py",
        "app/core/__init__.py",
        "app/models/__init__.py",
        "app/schemas/__init__.py",
        "app/services/__init__.py",
        "app/utils/__init__.py",
        "tests/__init__.py",
    ]
    
    for file in files:
        create_empty_file(os.path.join(file))
    
    print("初始化目录结构完成！")

if __name__ == "__main__":
    main() 