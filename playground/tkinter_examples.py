import tkinter


def main():
    main_window = tkinter.Tk()
    main_window.title('Hello, Tk')
    main_window.geometry('{w}x{h}+{left}+{top}'.format(w=640, h=480, left=100, top=400))
    main_window.mainloop()


if __name__ == '__main__':
    main()
