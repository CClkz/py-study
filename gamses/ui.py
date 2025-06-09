import tkinter as tk

# 创建主窗口
root = tk.Tk()
root.title("简单界面")

# 添加标签控件
label = tk.Label(root, text="Hello World!", font=('Arial', 24))
label.pack(padx=20, pady=20)

# 启动主循环
root.mainloop()
