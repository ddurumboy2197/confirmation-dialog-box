from tkinter import Tk, messagebox

def confirmation_dialog():
    root = Tk()
    root.withdraw()  # Dialogni ko'rish uchun root ni yashirib qo'yamiz
    response = messagebox.askyesno("Tasdiqlash", "Bu xatolikni tasdiqlaysizmi?", icon='error')
    root.destroy()  # Dialogni yashirib qo'ygan root ni yo'q qilamiz
    return response

print(confirmation_dialog())
