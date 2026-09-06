import tkinter as tk
from tkinter import Label, Button, Text, Entry
from scripts.cURL import convert_curl_to_requests
from scripts.timeStamp import get_current_timestamp, convert_timestamp_to_readable_format
# from tkinter import LEFT
from tkinter import messagebox


print(convert_curl_to_requests("curl -X GET https://example.com"))

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
            width=40, 
            height=20, 
            font=("Arial", 12)
        ) # 文本框
        text1.grid(row=1, column=0, ipadx=20, ipady=20, sticky="e", padx=(0,0), rowspan=2)
        
        self.add_placeholder(text1, "请在此粘贴 cURL 命令...")
        # text1.config(wrap="word")  # 设置自动换行
        
        # 2,1
        button1 = Button(
            self.root,
            bg="#8cbf7e",
            fg="white", 
            text="转 换",
            width=5,
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
            font=("微软雅黑", 11), 
            command=lambda: self.clear_text(text1)
        ) # 按钮
        button3.grid(row=2, column=1, padx=(10,0),pady=(20,0), sticky="n")
        
        # 创建标签
        label2 = Label(
            self.root,
            text="Python requests",
            font=("Arial", 11)
        )
        label2.grid(row=0, column=2,ipadx=130, ipady=10,padx=(50,0), sticky="w")
        # 1,2
        text2 = Text(
            self.root, 
            width=40, 
            height=21,
            font=("Arial", 12), 
            state='disabled', 
            bg="#f4f4e1", 
            cursor="spider" 
        ) # 文本框
        text2.grid(row=1, column=2, ipadx=20, ipady=20, sticky="e", padx=(10,0), rowspan=2)
        
        # 时间戳
        label3 = Label(
            self.root,
            text="输入时间戳转换：", 
            font=("微软雅黑", 11)
        )
        label3.grid(row=3, column=0, sticky="w", padx=(30,0), pady=(10,0))
        
        entry = Entry(
            self.root,
            font=("Arial", 12), 
            width=20,
        )
        entry.grid(row=3, column=0, padx=(130,0), pady=(10,0), ipady=2, ipadx=20)
        self.add_placeholder(entry, '输入时间戳进行转换（回车确定）')
        entry.bind("<Return>", lambda _: messagebox.showinfo("转换结果", convert_timestamp_to_readable_format(entry.get())))
        
        label4 = Label(
            self.root,
            text="当前时间戳：", 
            font=("微软雅黑", 11)
        )
        label4.grid(row=3, column=2, sticky="w", padx=(10,0), pady=(10,0))
    
    # 清空
    def clear_text(self, text):
        text.delete('1.0', 'end')
        
    # 转换
    def convert_curl(self, text1):
        content = text1.get('1.0', "end-1c").strip()
        if content == "" or content == text1._placeholder:
            messagebox.showwarning("警告", "请先输入 cURL 命令")
            return None
        
        

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
