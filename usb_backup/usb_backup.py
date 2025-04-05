import os
import shutil
import time
import random
import string
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from pathlib import Path
import win32api
import win32con
import win32file

class USBHandler(FileSystemEventHandler):
    def __init__(self):
        self.backup_dir = os.path.join('C:', 'course_ppt')
        self.supported_extensions = {'.ppt', '.pptx', '.pdf', '.doc', '.docx', '.txt'}
        self.ensure_backup_dir()
    
    def ensure_backup_dir(self):
        """确保备份目录存在"""
        if not os.path.exists(self.backup_dir):
            os.makedirs(self.backup_dir)
            print(f"创建备份目录: {self.backup_dir}")
    
    def get_unique_filename(self, file_path):
        """生成唯一的文件名"""
        base_name = os.path.basename(file_path)
        name, ext = os.path.splitext(base_name)
        
        while True:
            new_path = os.path.join(self.backup_dir, f"{name}{ext}")
            if not os.path.exists(new_path):
                return new_path
            # 如果文件已存在，添加随机字符串
            random_str = ''.join(random.choices(string.ascii_letters + string.digits, k=4))
            name = f"{name}_{random_str}"
    
    def is_supported_file(self, file_path):
        """检查文件是否是需要备份的类型"""
        return os.path.splitext(file_path)[1].lower() in self.supported_extensions
    
    def copy_file(self, src_path):
        """复制文件到备份目录"""
        try:
            dst_path = self.get_unique_filename(src_path)
            shutil.copy2(src_path, dst_path)
            print(f"已备份文件: {src_path} -> {dst_path}")
        except Exception as e:
            print(f"备份文件时出错 {src_path}: {str(e)}")
    
    def scan_directory(self, path):
        """扫描目录中的文件"""
        for root, _, files in os.walk(path):
            for file in files:
                file_path = os.path.join(root, file)
                if self.is_supported_file(file_path):
                    self.copy_file(file_path)
    
    def on_created(self, event):
        """当新文件或目录被创建时调用"""
        if not event.is_directory:
            if self.is_supported_file(event.src_path):
                self.copy_file(event.src_path)
        else:
            self.scan_directory(event.src_path)

def get_usb_drives():
    """获取所有USB驱动器"""
    drives = []
    for drive in win32api.GetLogicalDriveStrings().split('\000')[:-1]:
        if win32file.GetDriveType(drive) == win32file.DRIVE_REMOVABLE:
            drives.append(drive)
    return drives

def main():
    print("开始监控USB设备...")
    event_handler = USBHandler()
    observer = Observer()
    
    while True:
        try:
            # 获取当前USB驱动器
            current_drives = get_usb_drives()
            
            # 监控每个USB驱动器
            for drive in current_drives:
                if not observer.is_alive():
                    observer.schedule(event_handler, drive, recursive=True)
                    observer.start()
                    print(f"开始监控驱动器: {drive}")
            
            # 扫描每个USB驱动器
            for drive in current_drives:
                event_handler.scan_directory(drive)
            
            time.sleep(5)  # 每5秒检查一次
            
        except KeyboardInterrupt:
            print("\n停止监控...")
            observer.stop()
            observer.join()
            break
        except Exception as e:
            print(f"发生错误: {str(e)}")
            time.sleep(5)

if __name__ == "__main__":
    main() 