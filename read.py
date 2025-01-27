import curses

def text_editor(stdscr, initial_text):
    # Initialize curses settings
    curses.curs_set(1)  # Show the cursor
    stdscr.keypad(True)  # Enable special keys
    stdscr.clear()

    # Split the initial text into lines
    lines = initial_text.split('\n')
    max_y, max_x = stdscr.getmaxyx()
    cursor_y, cursor_x = 0, 0

    while True:
        stdscr.clear()
        for idx, line in enumerate(lines):
            stdscr.addstr(idx, 0, line)
        stdscr.move(cursor_y, cursor_x)
        stdscr.refresh()

        key = stdscr.getch()

        if key == curses.KEY_UP:
            if cursor_y > 0:
                cursor_y -= 1
                cursor_x = min(cursor_x, len(lines[cursor_y]))
        elif key == curses.KEY_DOWN:
            if cursor_y < len(lines) - 1:
                cursor_y += 1
                cursor_x = min(cursor_x, len(lines[cursor_y]))
        elif key == curses.KEY_LEFT:
            if cursor_x > 0:
                cursor_x -= 1
            elif cursor_y > 0:
                cursor_y -= 1
                cursor_x = len(lines[cursor_y])
        elif key == curses.KEY_RIGHT:
            if cursor_x < len(lines[cursor_y]):
                cursor_x += 1
            elif cursor_y < len(lines) - 1:
                cursor_y += 1
                cursor_x = 0
        elif key == curses.KEY_BACKSPACE or key == 127:
            if cursor_x > 0:
                lines[cursor_y] = lines[cursor_y][:cursor_x - 1] + lines[cursor_y][cursor_x:]
                cursor_x -= 1
            elif cursor_y > 0:
                cursor_x = len(lines[cursor_y - 1])
                lines[cursor_y - 1] += lines[cursor_y]
                del lines[cursor_y]
                cursor_y -= 1
        elif key == curses.KEY_ENTER or key == 10:
            new_line = lines[cursor_y][cursor_x:]
            lines[cursor_y] = lines[cursor_y][:cursor_x]
            lines.insert(cursor_y + 1, new_line)
            cursor_y += 1
            cursor_x = 0
        elif key == 27:  # ESC key to exit
            break
        else:
            lines[cursor_y] = lines[cursor_y][:cursor_x] + chr(key) + lines[cursor_y][cursor_x:]
            cursor_x += 1

    return '\n'.join(lines)

def main():
    initial_text = """This is the original text.
You can edit it across multiple lines.
Feel free to make changes."""
    edited_text = curses.wrapper(text_editor, initial_text)
    print("\nEdited Text:")
    print(edited_text)

if __name__ == "__main__":
    main()
