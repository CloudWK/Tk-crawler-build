import tkinter as tk
from tkinter import Label, Button, Text, Entry
from scripts.cURL import convert_curl_to_requests
from scripts.timeStamp import get_current_timestamp, convert_timestamp_to_readable_format
# from tkinter import LEFT
from tkinter import messagebox


# print(convert_curl_to_requests("curl -X GET https://example.com"))

class ToolkitApp:
    
    def __init__(self): 
        self.root = tk.Tk()
        self.root.title("Yunr爬虫工具箱v1.0.1")
        self.root.geometry("920x520+350+100")
        self.root.resizable(False, False) # 设置窗口是否可调整大小（width, height）
        # # 让第0行和第0列可以伸缩
        self.root.rowconfigure(0, weight=0)
        self.root.columnconfigure(0, weight=0)

    def create_widgets(self):
        """
        创建里面的组件
        'e'	East（东/右）	组件紧贴单元格右边界
        'w'	West（西/左）	组件紧贴单元格左边界
        'n'	North（北/上）	组件紧贴单元格上边界
        's'	South（南/下）	组件紧贴单元格下边界    
        """
        # 0,0
        label1 = Label(
            self.root, 
            text="粘贴 cURL(bash)", 
            font=("Arial", 11)
        ) # 标签
        label1.grid(row=0, column=0, ipadx=140,ipady=10, sticky="w")
        # 1,0
        text1 = Text(
            self.root, 
            width=45, 
            height=20, 
            font=("Arial", 12)
        ) # 文本框
        text1.grid(row=1, column=0, ipadx=20, ipady=20, sticky="e", padx=(12,0), rowspan=2)
        
        self.add_placeholder(text1, " 请在此粘贴 cURL 命令...")
        # text1.config(wrap="word")  # 设置自动换行
        
        # 2,1
        button1 = Button(
            self.root,
            bg="#8cbf7e",
            fg="white", 
            text="转 换",
            width=5,
            cursor="hand2",                 # 鼠标悬停时显示手型
            font=("微软雅黑", 11), 
            command=lambda: self.convert_curl(text1)
        ) # 按钮
        button1.grid(row=1, column=1, pady=10,padx=(10,0), sticky="s")
        
        button3 = Button(
            self.root, 
            bg="#cc0000",
            fg="white", 
            text="清 空", 
            width=5, 
            cursor="hand2",                 # 鼠标悬停时显示手型
            font=("微软雅黑", 11), 
            command=lambda: self.clear_text(text1)
        ) # 按钮
        button3.grid(row=2, column=1, padx=(10,0),pady=(20,0), sticky="n")
        
        # 创建标签
        label2 = Label(
            self.root,
            text="Python requests（Ctrl+A+C 复制）",
            font=("微软雅黑", 11),
            # bg="#f4f4e1",  # 设置背景颜色
            anchor="center",  # 设置文本对齐方式为左对齐
            width=12
        )
        label2.grid(row=0, column=2,ipadx=130, ipady=10,padx=(50,0), sticky="w")  # 设置标签位置和对齐方式
        # 1,2
        self.text2 = Text(
            self.root, 
            width=45, 
            height=22,
            font=("Arial", 11), 
            state='disabled', 
            bg="#f4f4e1", 
            cursor="spider"
        ) # 文本框
        self.text2.grid(row=1, column=2, ipadx=20, ipady=20, sticky="e", padx=(0,0), rowspan=2)
        
        
        # 时间戳
        label3 = Label(
            self.root,
            text="请 输 入 时 间 戳 ：", 
            font=("微软雅黑", 11)
        )
        label3.grid(row=3, column=0, sticky="w", padx=(40,0), pady=(10,0))
        
        entry = Entry(
            self.root,
            font=("Arial", 12), 
            width=22,
        )
        entry.grid(row=3, column=0, padx=(190,0), pady=(10,0), ipady=2, ipadx=20, sticky="w")
        self.add_placeholder(entry, ' 回车（Enter）转换时间戳', color="green")
        entry.bind("<Return>", lambda _: messagebox.showinfo("转换结果", convert_timestamp_to_readable_format(entry.get())))
        
        # 创建一个 Frame 来容纳“时间戳标签”和“刷新按钮and复制按钮”
        time_frame = tk.Frame(self.root)
        time_frame.grid(row=3, column=2, sticky="w", padx=(10,0), pady=(10,0))

        # 时间戳标签（保存引用以便刷新）
        self.current_timestamp_label = Label(
            time_frame,
            text=f"系 统 当 前 时 间 戳：{get_current_timestamp()}",
            font=("微软雅黑", 11)
        )
        self.current_timestamp_label.pack(side="left", padx=(5, 0))
        
        # 刷新图标按钮（改为扁平样式，只显示图标）
        refresh_btn = Button(
            time_frame,
            text="刷 新",                      
            font=("微软雅黑", 10),
            fg="white",                   # 图标颜色
            bg="#a1c4fd",                     # 背景与窗口一致
            # relief="flat",                  # 去掉边框
            bd=0,                           # 边框宽度为0
            cursor="hand2",                 # 鼠标悬停时显示手型
            activebackground="white",       # 点击时背景不变
            command=self.refresh_timestamp  # 绑定刷新方法
        )
        refresh_btn.pack(side="left", padx=(30, 0))
        
        # 复制图标按钮（改为扁平样式，只显示图标）
        self.copy_btn = Button(
            time_frame,
            text="复 制",                      
            font=("微软雅黑", 10),
            fg="white",                   # 图标颜色
            bg="#a1c4fd",                     # 背景与窗口一致
            # relief="flat",                  # 去掉边框
            bd=0,                           # 边框宽度为0
            cursor="hand2",                 # 鼠标悬停时显示手型
            activebackground="white",       # 点击时背景不变
            command=self.copy_timestamp  # 绑定复制方法
        )
        self.copy_btn.pack(side="left", padx=(20, 0))
    
    def refresh_timestamp(self):
        """刷新当前时间戳显示"""
        if self.current_timestamp_label:
            new_ts = get_current_timestamp()
            self.current_timestamp_label.config(text=f"系 统 当 前 时 间 戳：{new_ts}")
            self.copy_btn.config(text="复 制", bg="#a1c4fd")  # 还原复制按钮样式
        
    def copy_timestamp(self):
        """复制当前时间戳到剪贴板"""
        if self.current_timestamp_label:
            ts_text = self.current_timestamp_label.cget("text").split("：")[-1]
            self.root.clipboard_clear()  # 清空剪贴板
            self.root.clipboard_append(ts_text)  # 复制内容到剪贴板
            # messagebox.showinfo("提示", f"已复制时间戳：{ts_text}")
            self.copy_btn.config(text="已复制", bg="#4CAF50")  # 改变按钮文本和颜色
    # 清空
    def clear_text(self, text):
        text.delete('1.0', 'end')
        self.text2.config(state='normal')
        self.text2.delete('1.0', 'end')
        self.text2.config(state='disabled')
        
    # 转换
    def convert_curl(self, text1):
        content = text1.get('1.0', "end-1c").strip()
        # python字典格式化方法
        def dict_to_lines(d, indent=2):
            # indent: 缩进数量
            pad = " " * indent
            body = ",\n".join(f"{pad}{k!r}: {v!r}" for k, v in d.items())
            return "{\n" + body + ",\n}"
        if content == "" or content == text1._placeholder.strip():
            messagebox.showwarning("警告", "请先输入bash curl 命令")
            return None
        proto_curl = convert_curl_to_requests(content)
        if proto_curl.__len__() == 2 and proto_curl[0] != '':
            # 1. 启用文本框
            self.text2.config(state='normal')
            self.text2.delete('1.0', 'end') # 每次转换前先清空（放置重复点击转换）
            # 2. 插入文字（例如在末尾追加）
            self.text2.insert(
                'end',
                f'import requests\n\nheaders= {dict_to_lines(proto_curl[1])}\n\n'
                f'response = requests.get({repr(proto_curl[0])},headers=headers)'
            )   
            # 3. 恢复禁用状态（如果需要保持只读）
            self.text2.config(state='disabled')
        elif proto_curl.__len__() == 3 and proto_curl[0] != '':
            # 1. 启用文本框
            self.text2.config(state='normal')
            self.text2.delete('1.0', 'end') # 每次转换前先清空（放置重复点击转换）
            # 2. 插入文字（例如在末尾追加）
            self.text2.insert(
                'end',
                f'import requests\n\n\nheaders = {dict_to_lines(proto_curl[1])}\n\n'
                f'cookies = {dict_to_lines(proto_curl[2])}\n\n'
                f'response = requests.get({repr(proto_curl[0])},headers=headers,cookies=cookies)\n\nprint(response.status_code)'
            )   
            # 3. 恢复禁用状态（如果需要保持只读）
            self.text2.config(state='disabled')
        else: messagebox.showerror("警告", "输入bash curl 命令不规范")
            
        
        
    # 提示文字
    def add_placeholder(self, widget, placeholder_text, color="#444444"):
        """为 Text 或 Entry 组件添加占位提示（通用方法）"""
        widget._placeholder = placeholder_text
        widget._placeholder_color = color

        # ---------- 针对 Text 组件的内部函数 ----------
        def text_show_placeholder():
            if not widget.get("1.0", "end-1c"):
                widget.insert("1.0", placeholder_text)
                widget.config(fg=color, font=("微软雅黑", 10))

        def text_clear_placeholder(event=None):
            if widget.get("1.0", "end-1c") == placeholder_text:
                widget.delete("1.0", "end")
                widget.config(fg="black")

        # ---------- 针对 Entry 组件的内部函数 ----------
        def entry_show_placeholder():
            if not widget.get():
                widget.insert(0, placeholder_text)
                widget.config(fg=color, font=("微软雅黑", 10))

        def entry_clear_placeholder(event=None):
            if widget.get() == placeholder_text:
                widget.delete(0, "end")
                widget.config(fg="black")

        # ---------- 根据组件类型选择对应的函数 ----------
        if isinstance(widget, tk.Text):
            show = text_show_placeholder
            clear = text_clear_placeholder
        elif isinstance(widget, tk.Entry):
            show = entry_show_placeholder
            clear = entry_clear_placeholder
        else:
            raise TypeError("Unsupported widget type: only Text and Entry are supported.")
        # ---------- 绑定事件 ----------
        widget.bind("<FocusIn>", clear)
        
        def on_focus_out(event):
            # 判断内容是否为空
            if isinstance(widget, tk.Text):
                is_empty = not widget.get("1.0", "end-1c")
            else:  # Entry
                is_empty = not widget.get()
            if is_empty:
                show()

        widget.bind("<FocusOut>", on_focus_out)
        # 对于 Text，点击时清除；对于 Entry 也一样（但 Entry 的 focus 事件已经覆盖，为保险可以加上）
        widget.bind("<Button-1>", clear)

        # 初始化显示
        show()

if __name__ == "__main__":
    app = ToolkitApp()
    app.create_widgets()
    # 启动
    app.root.mainloop()
